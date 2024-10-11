from pydantic import BaseModel, ConfigDict
from typing import List

class ConversationRequest(BaseModel):
    input_text: str
    system_context: str
    model_name: str

    model_config = ConfigDict(protected_namespaces=())

class ConversationResponse(BaseModel):
    response: str

class ModelsResponse(BaseModel):
    models: List[str]

class QuestionsResponse(BaseModel):
    questions: List[str]