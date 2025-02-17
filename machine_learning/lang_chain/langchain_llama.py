import os


from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

prompt = f"Crie um roteiro de viagem de {numero_de_dias} dias, para uma família com {numero_de_criancas} crianças, que gostam de {atividade}."
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3")

ai_msg = model.invoke(prompt)
print(ai_msg)

