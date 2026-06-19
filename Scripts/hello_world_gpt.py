from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

#Iniciar modelo LLM
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

pregunta = "¿En qué año llegó el ser humano a la Luna por primera vez?"
respuesta = llm.invoke(pregunta)

print("Pregunta: ", pregunta)
print("Respuesta del modelo: ", respuesta.content)