import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configurar la página de la app
st.set_page_config(page_title="Chatbot Básico", page_icon="🤖")
st.title("🤖 Chatbot Básico con LangChain")
st.markdown("Este es un *chatbot de ejemplo* construido con LangChain + Streamlit. ¡Escribe tu mensaje abajo para comenzar!")

#Instanciamos el modelo
chat_model = ChatOpenAI(model="gpt-4o-mini",temperature=0.5)

# Inicializar el historial de mensajes  
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar los mensajes del historial  
for mensaje in st.session_state.messages:
    if isinstance(mensaje,SystemMessage):
        continue   

    # Asignamos rol, si es un mensaje de la IA rol asistant si no es un mensaje del usuario
    role = "assistant" if isinstance(mensaje,AIMessage) else "user"

    #Mostrar mensaje del historial
    with st.chat_message(role):
        st.markdown(mensaje.content)
        
#Cuadro de entrada de texto de usuario
pregunta = st.chat_input("Escribe tu mensaje: ")

#Si existe una pregunta
if pregunta: 
    #Mostrar inmediatamente el mensaje del usuario en la interfaz
    with st.chat_message("user"):
        st.markdown(pregunta)

    #Almacenamos el mensaje del usuario
    st.session_state.messages.append(HumanMessage(content=pregunta))

    #Generar respuesta usando el modelo de lenguaje
    respuesta = chat_model.invoke(st.session_state.messages) # aqui le metemos todo el historial de mensajes, hay una manera mejor de hacerlo con la plantilla de promtps

    #Mostrar la respuesta en la interfaz
    with st.chat_message("assistant"):
        st.markdown(respuesta.content)

    #Almacenamos la respuesta del modelo
    st.session_state.messages.append(AIMessage(content=respuesta.content))