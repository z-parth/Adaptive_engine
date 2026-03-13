from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_study_plan(ability_score: float, topics_missed: list, correct: int, total: int) -> str:
    #Generate a personalized 3-step study plan using OpenAI
    
    topics_str = ", ".join(topics_missed) if topics_missed else "No specific topics missed"
    
    prompt = f"""
    A student just completed a GRE adaptive test. Here are their results:
    - Final ability score: {ability_score} (scale 0.1 to 1.0)
    - Correct answers: {correct} out of {total}
    - Topics where they struggled: {topics_str}

    Based on this performance, generate a concise 3-step personalized study plan to help them improve.
    Each step should be specific, actionable, and tailored to their weak topics.
    Format it as:
    Step 1: ...
    Step 2: ...
    Step 3: ...
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert GRE tutor who creates personalized study plans."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    
    return response.choices[0].message.content