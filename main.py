#titulo
import streamlit as st
from openai import OpenAI

modelo_ia =OpenAI()

st.write("# Chatbot com Ia") #markdown

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []


texto_usuario = st.chat_input("Digite sua mensagem")

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario={"role":"user","content":texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)
    
    
    
    resposta_ia= modelo_ia.chat.completions.create(
         messages=st.session_state["lista_mensagens"],
         model="gpt-4o"
    )
   
    texto_resposta_ia=resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia ={"role":"assistant","content":texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)

    print(st.session_state["lista_mensagens"])