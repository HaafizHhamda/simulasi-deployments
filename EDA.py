import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run():
    # Title
    st.title("FIFA Data Exploration")

    #
    st.image('unnamed.jpg')
    # header
    st.header('Latar belakang')

    # Markdone
    st.markdown('Project kali ini bertujuan untuk memprediksi rating pemain FIFA 2022 sehingga semua pemain sepak bola profesional dapat diketahui ratingnya dan tidak menutup kemungkinan untuk lahirnya talenta/wonderkid baru.')

    st.header('Dataset')
    st.markdown(' dabsdaskmadasd,a')
    # load daata
    data = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/refs/heads/v2.3/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    data.rename(columns={'ValueEUR': 'Price', 'Overall': 'Rating'}, inplace=True)
    st.dataframe(data)

    # EDA
    st.header('Exploration data')

    st.subheader('dsajda')

    fig = plt.figure(figsize=(16, 5))
    sns.histplot(data['Rating'], kde=True, bins=30)
    plt.title('Histogram of Rating')

    st.pyplot(fig)

    st.markdown('''dsdasadnas das  Project kali ini bertujuan untuk memprediksi rating pemain FIFA 2022 sehingga semua
                pemain sepak bola profesional dapat diketahui ratingnya dan tidak menutup 
                kemungkinan untuk lahirnya talenta/wonderkid baru. dadadbasjadkajbkjabdb a kadbajda''')

    # subheader 
    st.subheader('dashad')

    # visualisasi
    fig = px.scatter(data, x='Weight', y='Height', hover_name='Name')
    st.plotly_chart(fig)

    # subheader
    st.subheader('dsadasd player')

    # nama kolom yang ada total
    nama_kolom =  data.columns
    total_cols = [col for col in nama_kolom if 'Total' in col]
    
    # user input
    pilihan = st.selectbox('pilih kolom untuk divisualisasikan',
                options = total_cols)
    st.write('pilihan:',pilihan)

    # visualisasi
    fig = plt.figure(figsize=(16, 5))
    sns.histplot(data[pilihan], kde=True, bins=30)
    plt.title('Histogram of Rating')

    st.pyplot(fig)
if __name__=='__main__':
    run()
