#ollama_app.py

from pydantic import BaseModel, Field
import base64
from ollama import chat


class QABase(BaseModel):
    question: str = Field(...")
    answer: str = Field(..., description="Resspuesta en español latino")

class QAAnalytics(QABase):
    thoughts: str = Field(..., description="Proceso de reflexion de la respuesta.")
    topic: str = Field(..., description="La palabra que mejor describe el tema.")


def encode_image_to_base64() -> str:
    with open("image_path", "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
        

def ollama_llm_response(question:str, encode_image:str):
    response = chat(
        model="gemma3:latest",
        messages=[
            {"role":"system", "content":"Eres un asistente de IA que responde preguntas sobre imágenes."},
            {
                "role": "user",
                "content": f"Responde la siguiente pregunta en español latino. "
                           f"Pregunta: {question} "
                           f"Imagen: {encode_image}"
            }
        ],
        model="gemma3:latest",
        format=QAAnalytics.model_json_schema(),    )
    return response["message"]["content"]

