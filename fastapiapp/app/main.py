from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .models import ConversationRequest, ConversationResponse, ModelsResponse, QuestionsResponse
from .utils import converse, get_allowed_models
from .config import QUESTIONS, SYSTEM_PROMPT

app = FastAPI()



system_context = SYSTEM_PROMPT

app.mount("/static", StaticFiles(directory="fastapiapp/static"), name="static")
# Ensure that the path provided here is correct
templates = Jinja2Templates(directory="fastapiapp/templates")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/models", response_model=ModelsResponse)
async def get_models():
    return {"models": get_allowed_models()}

@app.get("/questions", response_model=QuestionsResponse)
async def get_questions():
    return {"questions": QUESTIONS}

@app.post("/converse", response_model=ConversationResponse)
async def conversation(request: ConversationRequest):
    response = converse(request.input_text, system_context, request.model_name)
    print(response)
    return {"response": response}

@app.post("/general/converse", response_model=ConversationResponse)
async def conversation(request: ConversationRequest):
    response = converse(request.input_text, request.system_context, request.model_name)
    print(response)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)