from fastapi import FastAPI
from routes.session import router as session_router
from routes.questions import router as questions_router
from database import questions_collection, sessions_collection
from services.ai_insights import generate_study_plan

app = FastAPI(
    title="Adaptive Diagnostic Engine",
    description="A 1D Adaptive Testing System using IRT and AI-powered study plans",
    version="1.0.0"
)

# Register routes
app.include_router(session_router)
app.include_router(questions_router)

@app.get("/")
def root():
    return {"message": "Adaptive Diagnostic Engine is running!"}

@app.get("/session/report/{session_id}")
def get_report(session_id: str):
    """Get AI-generated study plan after test completion"""
    
    session = sessions_collection.find_one({"session_id": session_id})
    
    if not session:
        return {"error": "Session not found"}
    
    if not session["completed"]:
        return {"error": "Test not completed yet"}
    
    correct = sum(session["answers"])
    total = len(session["answers"])
    
    study_plan = generate_study_plan(
        ability_score=session["ability_score"],
        topics_missed=session["topics_missed"],
        correct=correct,
        total=total
    )
    
    return {
        "session_id": session_id,
        "final_ability_score": session["ability_score"],
        "correct_answers": correct,
        "total_questions": total,
        "topics_missed": session["topics_missed"],
        "study_plan": study_plan
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "database": "connected",
        "version": "1.0.0"
    }