import math

def get_probability(ability: float, difficulty: float) -> float:
    
    return 1 / (1 + math.exp(-(ability - difficulty)))

def update_ability(ability: float, difficulty: float, correct: bool) -> float:
   
    probability = get_probability(ability, difficulty)
    
    if correct:
        ability += 0.1 * (1 - probability)  # less gain if question was easy
    else:
        ability -= 0.1 * probability  # less loss if question was hard
    
    # Keep ability within bounds 0.1 to 1.0
    ability = max(0.1, min(1.0, ability))
    return round(ability, 4)

def select_next_question(ability: float, asked_ids: list, questions: list) -> dict:
    """Pick question closest in difficulty to current ability"""
    available = [q for q in questions if q["question_id"] not in asked_ids]
    
    if not available:
        return None
    
    # Find question whose difficulty is closest to current ability
    best = min(available, key=lambda q: abs(q["difficulty"] - ability))
    return best