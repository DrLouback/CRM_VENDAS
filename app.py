import streamlit as st
from datetime import time
import contrato

def main():
    
    st.title('Sistema de CRM')
    email = st.text_input('E-mail do vendedor')
    data = st.date_input('Data da venda')
    hora = st.time_input('Horário da venda')
    valor = st.number_input('Valor da venda', min_value=0.0, format="%0.2f")
    quantidade = st.number_input('Quantidade de produtos')
    produto = st.selectbox('Produto vendido',['ZapFlow com Gemini','ZapFlow com Lhama','ZapFlow com ChatGPT'])
    if st.button('Salvar'):
        st.write('Salvo no banco de dados')


if __name__ == '__main__':
    main()