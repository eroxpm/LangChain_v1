from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

#Iniciar modelo LLM
chat = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

plantilla = PromptTemplate(
    input_variables=["nombre"], #variable dinamica
    template="Saluda al usuario con su nombre. \n Nombre del usuario: {nombre} \n Asistente: ",
)

# Crear la cadena utilizando LCEL (LangChain Expression Language)
chain = plantilla | chat

# Ejecutar la cadena con invoke
resultado = chain.invoke({"nombre": "Eros"})

print(resultado.content)