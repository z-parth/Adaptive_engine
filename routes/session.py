from fastapi import APIRouter, HTTPException
from database import questions_collection, sessions_collection
from services.adaptive import update_ability, select_next_question
import uuid
from pydantic import BaseModel

router = APIRouter()

@router.post("/session/start")
def start_session():
    """Start a new test session"""
    session_id = str(uuid.uuid4())
    
    # Get all questions
    questions = list(questions_collection.find({}, {"_id": 0}))
    
    # Start at baseline ability 0.5
    ability = 0.5
    
    # Select first question closest to 0.5 difficulty
    first_question = select_next_question(ability, [], questions)
    
    # Create session in DB
    session = {
        "session_id": session_id,
        "ability_score": ability,
        "questions_asked": [first_question["question_id"]],
        "answers": [],
        "topics_missed": [],
        "completed": False
    }
    sessions_collection.insert_one(session)
    
    return {
        "session_id": session_id,
        "question": first_question,
        "question_number": 1
    }


class AnswerRequest(BaseModel):
    session_id: str
    question_id: str
    answer: str

@router.post("/session/answer")
def submit_answer(request: AnswerRequest):
    if not request.answer.strip():
        raise HTTPException(status_code=400, detail="Answer cannot be empty")
    session_id = request.session_id
    question_id = request.question_id
    answer = request.answer
    
    # Get session
    session = sessions_collection.find_one({"session_id": session_id})
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    if session["completed"]:
        raise HTTPException(status_code=400, detail="Session already completed")
    
    # Get the question
    question = questions_collection.find_one({"question_id": question_id}, {"_id": 0})
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    # Check answer
    correct = answer.strip().lower() == question["correct_answer"].strip().lower()
    
    # Track missed topics
    topics_missed = session["topics_missed"]
    if not correct and question["topic"] not in topics_missed:
        topics_missed.append(question["topic"])
    
    # Update ability using IRT
    new_ability = update_ability(session["ability_score"], question["difficulty"], correct)
    
    # Check if test is complete (10 questions)
    answers = session["answers"] + [correct]
    questions_asked = session["questions_asked"]
    
    if len(answers) >= 10:
        sessions_collection.update_one(
            {"session_id": session_id},
            {"$set": {
                "ability_score": new_ability,
                "answers": answers,
                "topics_missed": topics_missed,
                "completed": True
            }}
        )
        return {
            "message": "Test completed!",
            "final_ability_score": new_ability,
            "correct_answers": sum(answers),
            "total_questions": 10,
            "topics_missed": topics_missed,
            "session_id": session_id
        }
    
    # Get next question
    all_questions = list(questions_collection.find({}, {"_id": 0}))
    next_question = select_next_question(new_ability, questions_asked, all_questions)
    
    # Update session
    sessions_collection.update_one(
        {"session_id": session_id},
        {"$set": {
            "ability_score": new_ability,
            "answers": answers,
            "topics_missed": topics_missed,
            "questions_asked": questions_asked + [next_question["question_id"]]
        }}
    )
    
    return {
        "correct": correct,
        "current_ability": new_ability,
        "question": next_question,
        "question_number": len(answers) + 1
    }