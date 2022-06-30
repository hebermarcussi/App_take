from ctypes import alignment
from datetime import datetime
from operator import contains
from tkinter import CENTER
from pyparsing import col
import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import MetaTrader5 as mt5

def get_data():
    arquivo = r'SourceData.xlsx'
    return pd.read_excel(arquivo)



def Robo_python():

  
    col1, col2, col3 = st.columns([2,2,1])

    with col2:
        st.image('take2.png', width=100,)
    st.markdown('---')
    st.markdown("<h2 style='text-align: center; color: black;'>Robôs em Python</h2>", unsafe_allow_html=True)
    st.markdown('---')
    with st.form(key= 'form2'):
        servidor = ["XPMT5-DEMO","XPMT5-PRD","Pepperstone-Demo"]
        col1, col2 = st.columns(2)
        with col1:
            nome_cliente = st.text_input('Primeiro Nome:')
            servidor_conta = st.selectbox('Selecione o Servidor', servidor)
        with col2:    
            Numero_Conta = st.text_input('Numero da Conta:')
            password_conta = st.text_input("Senha", type="password")
        
        Caminho = st.text_input('Caminho Metatrader:', value= "C:\\Program Files\\MetaTrader 5\\terminal64.exe")
        col1, col2, col3 = st.columns([1.7,2,1])
        with col2:
            Conectar = st.form_submit_button('Conectar Metatrader 5')

    if Conectar == True:
        
        if(mt5.initialize(path=Caminho, login=int(Numero_Conta), server=servidor_conta, password=password_conta)):
            st.markdown('Ok conexão estabelecida!')
        else:
         
            st.write('Tivemos problemas na conexão, código do problema = ', mt5.last_error() )
            mt5.shutdown()




def AnaliseRobo():
    col1, col2, col3 = st.columns([2,2,1])
   
    with col2:
        st.image('take2.png', width=100,)
    st.markdown('---')
    st.markdown("<h2 style='text-align: center; color: black;'>Analise Robôs</h2>", unsafe_allow_html=True)
    st.markdown('---')
    st.markdown("<h5 style='text-align: center; color: blue;'>Filtro de Data Grafico</h5>", unsafe_allow_html=True)
    
    with st.form(key= 'form1'):
        col1, col2 = st.columns(2)
        with col1:
            data_incio = st.date_input('Data de incio') 
        with col2:
            data_Fim = st.date_input('Data de Fim')    
        Robos = ['StaloM2','StaloM4','StaloM6','StaloM10','StaloH2', 'StaloM3', 'OnePunch', 'Panzer','Razor','OnePunch_F']
        selecao = st.selectbox('Selecione o Robo', Robos)
        Botao_filtrar = st.form_submit_button('Filtrar')
    if Botao_filtrar == True:
        df = get_data()
        df = df.drop(columns=['Perc. Acerto','Perc. Rebaixamento','maxima negativa'])
        filtro_robo = df[df.robo.str.contains(selecao)]
        data_incio = pd.to_datetime(data_incio)
        data_Fim = pd.to_datetime(data_Fim)
        filtro_data = filtro_robo[filtro_robo['inicio real'].between(data_incio,data_Fim)]
        filtro_data['Robô'] = filtro_data['Pontos'].cumsum()
        fig = px.line(filtro_data, x='inicio real', y=['Robô'], title='Grafico do Robô', labels={'value' : 'Pontos', 'inicio real': ''})
        st.plotly_chart(fig, width = 600)
    


def MontarCarteira():
    col1, col2, col3 = st.columns([2,2,1])
   
    with col2:
        st.image('take2.png', width=100,)
    st.markdown('---')
    st.markdown("<h2 style='text-align: center; color: black;'>Montar Carteira</h2>", unsafe_allow_html=True)
    st.markdown('---')

def Moedor_de_Carne():
    col1, col2, col3 = st.columns([2,2,1])
   
    with col2:
        st.image('take2.png', width=100,)
    st.markdown('---')
    st.markdown("<h2 style='text-align: center; color: black;'>Moedor de Carne</h2>", unsafe_allow_html=True)
    st.markdown('---')

def Prova_de_fogo():
    col1, col2, col3 = st.columns([2,2,1])
   
    with col2:
        st.image('take2.png', width=100,)
    st.markdown('---')
    st.markdown("<h2 style='text-align: center; color: black;'>Prova de Fogo</h2>", unsafe_allow_html=True)
    st.markdown('---')


def main():
    st.sidebar.image('take2.png', width=200,)
    st.sidebar.title('Menu Take Robótica')
    Pagina = st.sidebar.radio('',['Robôs Python', 'Analise Robôs', 'Montar Carteira', 'Moedor de Carne','Prova de Fogo'])

    if Pagina == 'Robôs Python':
        Robo_python()
    if Pagina == 'Analise Robôs':
        AnaliseRobo()
    if Pagina == 'Montar Carteira':
        MontarCarteira()
    if Pagina == 'Moedor de Carne':
        Moedor_de_Carne()
    if Pagina == 'Prova de Fogo':
        Prova_de_fogo()


main()