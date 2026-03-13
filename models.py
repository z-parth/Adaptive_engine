from pydantic import BaseModel
from typing import List
from datetime import datetime

class Question(BaseModel):
    question_id: str
    text: str
    options: List[str]
    correct_answer: str
    difficulty: float
    topic: str
    tags: List[str]

class UserSession(BaseModel):
    session_id: str
    ability_score: float = 0.5
    questions_asked: List[str] = []
    answers: List[bool] = []
    topics_missed: List[str] = []
    created_at: datetime = datetime.now()
    completed: bool = False