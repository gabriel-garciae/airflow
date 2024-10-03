import streamlit as st
import pandas as pd
import subprocess

#Função para carregar os dados do arquivo CSV
def load_data()
    df = pd.read_csv("execution_logs.log")
    return df

#Função para executar o script python
def run_python_script()
    subprocess.run("poetry run python pipelint/pipeline.py")

#Layout do aplicativo streamlit
def main():
    st.title("Visualização de Logs e execução de scripts")
    st.image("pics/AirflowLogo.png")
