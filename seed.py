from dotenv import load_dotenv
load_dotenv()

from database import questions_collection
import uuid

questions = [
    {
        "question_id": str(uuid.uuid4()),
        "text": "What is the value of x if 2x + 5 = 15?",
        "options": ["3", "4", "5", "6"],
        "correct_answer": "5",
        "difficulty": 0.2,
        "topic": "Algebra",
        "tags": ["linear equations", "basic math"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "Which word is most similar in meaning to 'BENEVOLENT'?",
        "options": ["Cruel", "Kind", "Angry", "Lazy"],
        "correct_answer": "Kind",
        "difficulty": 0.2,
        "topic": "Vocabulary",
        "tags": ["synonyms", "easy"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "If a triangle has angles 60°, 60°, and 60°, what type of triangle is it?",
        "options": ["Scalene", "Isosceles", "Equilateral", "Right"],
        "correct_answer": "Equilateral",
        "difficulty": 0.3,
        "topic": "Geometry",
        "tags": ["triangles", "angles"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "What is 15% of 200?",
        "options": ["20", "25", "30", "35"],
        "correct_answer": "30",
        "difficulty": 0.3,
        "topic": "Arithmetic",
        "tags": ["percentages", "basic math"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "Which word is most opposite in meaning to 'VERBOSE'?",
        "options": ["Talkative", "Concise", "Loud", "Wordy"],
        "correct_answer": "Concise",
        "difficulty": 0.4,
        "topic": "Vocabulary",
        "tags": ["antonyms", "medium"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "If f(x) = 3x² - 2x + 1, what is f(2)?",
        "options": ["9", "10", "11", "12"],
        "correct_answer": "9",
        "difficulty": 0.4,
        "topic": "Algebra",
        "tags": ["functions", "quadratic"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "A train travels 120 miles in 2 hours. What is its average speed?",
        "options": ["50 mph", "60 mph", "70 mph", "80 mph"],
        "correct_answer": "60 mph",
        "difficulty": 0.4,
        "topic": "Arithmetic",
        "tags": ["speed", "word problems"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "What is the area of a circle with radius 7? (Use π = 3.14)",
        "options": ["143.07", "153.86", "163.54", "173.21"],
        "correct_answer": "153.86",
        "difficulty": 0.5,
        "topic": "Geometry",
        "tags": ["circles", "area"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "Which word best completes the sentence: 'The professor's lecture was so _____ that students struggled to stay awake.'",
        "options": ["Engaging", "Provocative", "Soporific", "Stimulating"],
        "correct_answer": "Soporific",
        "difficulty": 0.5,
        "topic": "Vocabulary",
        "tags": ["sentence completion", "medium"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "If 3x - 7 = 2x + 5, what is x?",
        "options": ["10", "11", "12", "13"],
        "correct_answer": "12",
        "difficulty": 0.5,
        "topic": "Algebra",
        "tags": ["linear equations", "medium"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "What is the probability of rolling an even number on a standard die?",
        "options": ["1/6", "1/3", "1/2", "2/3"],
        "correct_answer": "1/2",
        "difficulty": 0.5,
        "topic": "Probability",
        "tags": ["basic probability", "dice"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "If the ratio of boys to girls in a class is 3:5 and there are 24 boys, how many girls are there?",
        "options": ["35", "38", "40", "45"],
        "correct_answer": "40",
        "difficulty": 0.6,
        "topic": "Arithmetic",
        "tags": ["ratios", "word problems"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "What is the slope of the line passing through points (2, 3) and (6, 11)?",
        "options": ["1", "2", "3", "4"],
        "correct_answer": "2",
        "difficulty": 0.6,
        "topic": "Algebra",
        "tags": ["coordinate geometry", "slope"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "Which word is most similar in meaning to 'PERFIDIOUS'?",
        "options": ["Loyal", "Treacherous", "Honest", "Brave"],
        "correct_answer": "Treacherous",
        "difficulty": 0.6,
        "topic": "Vocabulary",
        "tags": ["synonyms", "hard"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "A cylinder has radius 3 and height 10. What is its volume? (Use π = 3.14)",
        "options": ["254.34", "262.14", "282.60", "300.14"],
        "correct_answer": "282.60",
        "difficulty": 0.7,
        "topic": "Geometry",
        "tags": ["cylinders", "volume"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "If log₂(x) = 5, what is x?",
        "options": ["16", "25", "32", "64"],
        "correct_answer": "32",
        "difficulty": 0.7,
        "topic": "Algebra",
        "tags": ["logarithms", "hard"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "In how many ways can 5 books be arranged on a shelf?",
        "options": ["60", "100", "120", "150"],
        "correct_answer": "120",
        "difficulty": 0.7,
        "topic": "Probability",
        "tags": ["permutations", "combinatorics"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "Which word best describes someone who 'secretly undermines a cause they appear to support'?",
        "options": ["Sycophant", "Zealot", "Saboteur", "Philanthropist"],
        "correct_answer": "Saboteur",
        "difficulty": 0.8,
        "topic": "Vocabulary",
        "tags": ["definitions", "hard"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "If x² - 5x + 6 = 0, what are the values of x?",
        "options": ["1 and 6", "2 and 3", "2 and 4", "3 and 4"],
        "correct_answer": "2 and 3",
        "difficulty": 0.8,
        "topic": "Algebra",
        "tags": ["quadratic equations", "hard"]
    },
    {
        "question_id": str(uuid.uuid4()),
        "text": "A bag contains 4 red, 3 blue, and 5 green balls. What is the probability of picking 2 red balls without replacement?",
        "options": ["1/11", "2/11", "3/11", "4/11"],
        "correct_answer": "1/11",
        "difficulty": 0.9,
        "topic": "Probability",
        "tags": ["combinatorics", "hard"]
    }
]

if __name__ == "__main__":
    questions_collection.drop()
    questions_collection.insert_many(questions)
    print(f"Seeded {len(questions)} questions successfully!")