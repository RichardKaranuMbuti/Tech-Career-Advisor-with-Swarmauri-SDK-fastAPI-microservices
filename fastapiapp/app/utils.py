from swarmauri.standard.llms.concrete.GroqModel import GroqModel
from swarmauri.standard.messages.concrete.SystemMessage import SystemMessage
from swarmauri.standard.agents.concrete.SimpleConversationAgent import SimpleConversationAgent
from swarmauri.standard.conversations.concrete.MaxSystemContextConversation import MaxSystemContextConversation
from .config import API_KEY

def load_model(selected_model):
    return GroqModel(api_key=API_KEY, name=selected_model)

def get_allowed_models():
    llm = GroqModel(api_key=API_KEY)
    return llm.allowed_models

def converse(input_text, system_context, model_name):
    llm = load_model(model_name)
    conversation = MaxSystemContextConversation()
    agent = SimpleConversationAgent(llm=llm, conversation=conversation)
    agent.conversation.system_context = SystemMessage(content=system_context)
    
    result = agent.exec(input_text)
    return str(result)