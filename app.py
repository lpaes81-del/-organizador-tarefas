import streamlit as st

st.title("Organizador de Tarefas")

st.write("Minha aplicação está funcionando!")

nome = st.text_input("Digite seu nome:")

if st.button("Enviar"):
    st.success(f"Olá, {nome}!")
