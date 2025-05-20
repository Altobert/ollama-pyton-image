from fastapi import FastAPI
from uvicorn import run
from ollama import chat
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import JSONResponse
# from fastapi.encoders import jsonable_encoder

response = chat(
    model = "gemma3:latest",
    messages=[
        {
            "role":"user", "content":"Que es la Inteligencia Artificial?"
        }
    ]
)

print(response["message"]["content"])

"""

app = FastAPI()

@app.get("/")

def read_root():
    return {"Hola": "Terricolas"}

if __name__ == "__main__":    
    run(app, host="0.0.0.0", port=8000, reload=True, workers=4)
# This code creates a simple FastAPI application that returns a JSON response with "Hello": "World" when accessed at the root URL ("/").
# To run the FastAPI application, use the command:  
# uvicorn main:app --reload
# To test the API, you can use a tool like Postman or curl:
# curl http://localhost:8000/
# This will return a JSON response: {"Hello": "World"}

"""

