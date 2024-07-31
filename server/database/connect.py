import mysql.connector
import pandas as pd
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="estacao"
)
'''
def maxm():
    query = """SELECT * FROM temp_data;""" 
    result_dataFrame = pd.read_sql(query,mydb)
    df = pd.DataFrame(result_dataFrame)
    df_filtrado = df[df['data'].dt.date == date.today()]

    temperatura_maxima = df['temp'].max()

maxm()
'''
def send_data(query): 
    mycursor = mydb.cursor()
    mycursor.execute(query)
    mydb.commit()

def view_data(query):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    mycursor.fetchall()
  

x = view_data("SELECT temp FROM estacao.temp_data ORDER BY id desc LIMIT 1")
