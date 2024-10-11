from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

# List of questions to ask users
QUESTIONS = [
    "What is your current level of education? (High School, Associate's Degree, Bachelor's Degree, Master's Degree, Other)",
    "What are your interests or hobbies? (e.g., Creative writing, problem-solving, designing, data analysis, etc.)",
    "Have you ever worked on a technical project or used any tech tools? (Yes, No, Not sure)",
    "What type of work environment do you prefer? (Remote, In-office, Hybrid)",
    "How much time can you commit to learning new skills each week? (Less than 5 hours, 5-10 hours, 10-20 hours, More than 20 hours)",
    "What aspect of tech interests you the most? (Programming, Design, Data Science, IT Support, Cybersecurity, Project Management)",
    "Do you have any prior experience in teamwork or leadership roles? (Yes, No, Some experience)"
]

SYSTEM_PROMPT = """
You are a career advisor chatbot designed to help non-tech users transition into tech careers. Your goal is to ask the user a series of questions to understand their background, interests, and preferences. Based on their responses, you will suggest a suitable tech career path and provide a personalized learning
roadmap with an estimated timeline for achieving their career goals.
1. You are given the user the seven questions and their answers listed above.
2.For the responses,analyze them to determine the best tech career options.
3. Suggest a tech career based on their interests and preferences, along with a roadmap
"""