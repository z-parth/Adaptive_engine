from fastapi import APIRouter, HTTPException
from database import questions_collection

router = APIRouter()

@router.get("/questions")
def get_all_questions():
    """Get all questions in the database"""
    questions = list(questions_collection.find({}, {"_id": 0}))
    return {"total": len(questions), "questions": questions}

@router.get("/questions/{question_id}")
def get_question(question_id: str):
    """Get a single question by ID"""
    question = questions_collection.find_one({"question_id": question_id}, {"_id": 0})
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@router.get("/questions/topic/{topic}")
def get_questions_by_topic(topic: str):
    """Get all questions for a specific topic"""
    questions = list(questions_collection.find({"topic": topic}, {"_id": 0}))
    if not questions:
        raise HTTPException(status_code=404, detail=f"No questions found for topic: {topic}")
    return {"topic": topic, "total": len(questions), "questions": questions}