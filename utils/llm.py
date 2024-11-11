from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()


def get_model():
    model = ChatGroq(
        model_name=os.getenv("MODEL_NAME"),
        temperature=os.getenv("TEMPERATURE"),
        groq_api_key=os.getenv("GROQ_API_KEY"),
    )
    return model
