import streamlit as st
from datetime import time,datetime
from contrato import Vendas
import sys

def main():
    
    st.title('Sistema de CRM')
    email = st.text_input('E-mail do vendedor')
    data = st.date_input('Data da venda',value = 'default_value_today')
    hora = st.time_input('Horário da venda', time(9,0))
    valor = st.number_input('Valor da venda', min_value=0.0, format="%0.2f")
    quantidade = st.number_input('Quantidade de produtos', min_value= 0, step= 1 )
    produto = st.selectbox('Produto vendido',['ZapFlow com Gemini','ZapFlow com Lhama','ZapFlow com ChatGPT'])

    if st.button('Salvar'):
        data_hora = datetime.combine(date= data, time= hora) #type: ignore 
        venda = Vendas(
            email= email,
            data= data_hora,
            valor= valor,
            quantidade= quantidade,
            produto= produto
        )
        st.write('Salvo no banco de dados')


if __name__ == '__main__':
    main()

    
    
