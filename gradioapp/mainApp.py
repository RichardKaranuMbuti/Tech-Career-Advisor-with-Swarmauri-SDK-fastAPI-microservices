from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .models import ConversationApp
import os
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the static directory for serving CSS, JS, etc.
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Define the template folder
templates = Jinja2Templates(directory="app/templates")

# Initialize the conversation app
conversation_app = ConversationApp()

# Static system context (no need for input in the template)
system_prompt = """
You are a career advisor chatbot designed to help non-tech users transition into tech careers.
Your goal is to ask the user a series of questions to understand their background, interests, and preferences. 
Based on their responses, you will suggest a suitable tech career path and provide a personalized learning roadmap 
with an estimated timeline for achieving their career goals.
"""

# Predefined list of questions
questions = [
    "What is your current level of education? (High School, Associate's Degree, Bachelor's Degree, Master's Degree, Other)",
    "What are your interests or hobbies? (e.g., Creative writing, problem-solving, designing, data analysis, etc.)",
    "Have you ever worked on a technical project or used any tech tools? (Yes, No, Not sure)",
    "What type of work environment do you prefer? (Remote, In-office, Hybrid)",
    "How much time can you commit to learning new skills each week? (Less than 5 hours, 5-10 hours, 10-20 hours, More than 20 hours)",
    "What aspect of tech interests you the most? (Programming, Design, Data Science, IT Support, Cybersecurity, Project Management)",
    "Do you have any prior experience in teamwork or leadership roles? (Yes, No, Some experience)"
]

# Route to display the template with the first question
@app.get("/", response_class=HTMLResponse)
async def get_questions(request: Request):
    # First question to display initially
    current_question = questions[0]
    return templates.TemplateResponse("index.html", {
        "request": request,
        "current_question": current_question,
        "question_index": 0,  # Start from the first question
        "models": conversation_app.allowed_models
    })


# Endpoint to handle the submission of answers
@app.post("/submit/", response_class=HTMLResponse)
async def submit_answers(request: Request, answer: str = Form(...), question_index: int = Form(...), answers: str = Form(...), selected_model: str = Form(...)):
    # Convert answers to dictionary and append the new answer
    answer_dict = {} if not answers else eval(answers)  # safely convert string back to dict
    answer_dict[questions[question_index]] = answer  # Save the answer

    # If not the last question, show the next question
    if question_index + 1 < len(questions):
        next_question = questions[question_index + 1]
        return templates.TemplateResponse("index.html", {
            "request": request,
            "current_question": next_question,
            "question_index": question_index + 1,
            "answers": str(answer_dict),
            "models": conversation_app.allowed_models,
            "selected_model": selected_model
        })
    
    # Once all questions are answered, submit to the converse API
    input_text = str(answer_dict)  # Convert the dictionary to string
    response = conversation_app.converse(input_text, {}, system_prompt, selected_model)
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "bot_response": response,
        "models": conversation_app.allowed_models,
        "answers": str(answer_dict),
        "completed": True,  # Indicate that the conversation is done
        "selected_model": selected_model
    })
