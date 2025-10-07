import streamlit as st
import pandas as pd
import pickle
import json
import numpy as np

# Load all files

with open('model_file/model_lin_reg.pkl', 'rb') as file_1:
  model_lin_reg = pickle.load(file_1)

with open('model_file/model_scaler.pkl', 'rb') as file_2:
  model_scaler = pickle.load(file_2)

with open('model_file/model_encoder.pkl','rb') as file_3:
  model_encoder = pickle.load(file_3)

with open('model_file/list_num_cols.txt', 'r') as file_4:
  list_num_cols = json.load(file_4)

with open('model_file/list_cat_cols.txt', 'r') as file_5:
  list_cat_cols = json.load(file_5)
  
def run():
# User input
    with st.form(key= 'player'):
        nama = st.text_input('Masukan nama',
                            placeholder = 'messi')
        age= st.number_input('Masukan Umur',
                            placeholder = '36',
                            min_value = 0,max_value = 99)
        height= st.number_input('Masukan tinggi',
                            placeholder = '36',
                            min_value = 0,max_value = 300)
        weight= st.number_input('Masukan berat',
                            placeholder = '36',
                            min_value = 0,max_value = 99)
        harga= st.number_input('Masukan harga',
                            placeholder = '36',
                            help = 'harga dalam usd'
                            )
        st.write('__')
        attacking_wr = st.selectbox('dsadasda',['Low','Medium','High'])
        defending_wr = st.selectbox('saddasda',['Low','Medium','High'])
        st.write('__')

        pace = st.slider('pace total:',min_value =0,max_value=100)
        shoting = st.slider('shoting total:',min_value =0,max_value=100)
        defening = st.slider('defen total:',min_value =0,max_value=100)
        pasing = st.slider('pasing total:',min_value =0,max_value=100)
        dribling = st.slider('dribli total:',min_value =0,max_value=100)
        picikal = st.slider('picikal total:',min_value =0,max_value=100)
        submit = st.form_submit_button('predict')

        if submit:
            data_inf = {
                'Name': nama,
                'Age': age,
                'Height': height,
                'Weight': weight,
                'Price': harga,
                'AttackingWorkRate': attacking_wr,
                'DefensiveWorkRate': defending_wr,
                'PaceTotal': pace,
                'ShootingTotal': shoting,
                'PassingTotal': pasing,
                'DribblingTotal': dribling,
                'DefendingTotal': defening,
                'PhysicalityTotal':picikal
            }

            data_inf = pd.DataFrame([data_inf])
            st.dataframe(data_inf)

            data_inf_num = data_inf[list_num_cols]
            data_inf_cat = data_inf[list_cat_cols]

            data_inf_num_scaled = model_scaler.transform(data_inf_num)

            ## Feature Encoding
            data_inf_cat_encoded = model_encoder.transform(data_inf_cat)

            ## Concate
            data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded], axis=1)

            y_pred_inf = model_lin_reg.predict(data_inf_final)
            st.write('Prediction', round(y_pred_inf[0],1))

if __name__=='__main__':
    run()
