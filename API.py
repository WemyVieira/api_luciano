# Import Bibliotecas
import joblib
import pandas as pd
import numpy as np
import os
from flask import Flask, request, render_template, make_response
import sys

#File name
joblib_file = "ML_IdentificarPublico_74f1.pkl"

# Open Model
joblib_model = joblib.load(joblib_file)

app = Flask(__name__)

@app.route('/predict',methods=['POST'])
def predict():

    #base autenticação
    login = ['lucianopedroso15@gmail.com']
    senha = ['Confianca'] 

    # recebendo texto para prever
    texto = request.get_json()
    # Criando data set
    df = pd.DataFrame(texto, index=[0])
    # autenticacao
    if df['Login'][0] in login and df['Password'][0] in senha:
        # inputs
        dados = df[['Renda','Genero','Idade','EstadoCivil_Casado','EstadoCivil_Outros','EstadoCivil_Solteiro']]
        # prevendo probabilidade do texto
        b = joblib_model.predict(dados)
        df['Previsao'] = b
        # Return
        return df['Previsao'].to_json(orient='records')
    else:
        df['Previsao'] = 'Erro Authentication'
        # Return
        return df['Previsao'].to_json(orient='records')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='5000')