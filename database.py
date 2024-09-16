
from dotenv import load_dotenv
from psycopg2 import sql
import psycopg2
from contrato import Vendas
import streamlit as st
import os
from pydantic import ValidationError

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD  = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')

def salvar_no_postgres(dados: Vendas):
    try:
            conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
            cursor = conn.cursor()
            cursor = conn.cursor()

            
            insert_query= sql.SQL('INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (%s,%s,%s,%s,%s)')
            cursor.execute(insert_query, (
                    dados.email,
                    dados.data,
                    dados.valor,
                    dados.quantidade,
                    dados.produto

            )
            )
            conn.commit() 

                  
    except ValidationError as e:
            st.error(f'Deu erro {e}')