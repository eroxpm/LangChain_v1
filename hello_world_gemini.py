from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

#Iniciar modelo LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

pregunta = "¿En qué año llegó el ser humano a la Luna por primera vez?"
respuesta = llm.invoke(pregunta)

print("Pregunta: ", pregunta)
print("Respuesta del modelo: ", respuesta.content)