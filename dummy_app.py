import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Titolo
st.title("📊 Dashboard Interattiva")

# Sidebar
with st.sidebar:
    st.header("Impostazioni")
    num_points = st.slider("Numero di punti", 10, 500, 100)
    noise = st.slider("Rumore", 0.0, 1.0, 0.2)

# Contenitore per descrizione iniziale
with st.container():
    st.subheader("Benvenuto!")
    st.write("Questa è una semplice app Streamlit per mostrare come gestire il layout. "
             "Puoi usare la sidebar per modificare i parametri del grafico.")

# Simulazione di dati
x = np.linspace(0, 10, num_points)
y = np.sin(x) + np.random.normal(0, noise, size=x.shape)

df = pd.DataFrame({'x': x, 'y': y})

# Layout con colonne
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Grafico")
    fig, ax = plt.subplots()
    ax.plot(df['x'], df['y'], label='Seno + rumore')
    ax.set_title("Seno disturbato")
    st.pyplot(fig)

with col2:
    st.subheader("🧮 Statistiche")
    st.write("**Media y:**", round(df['y'].mean(), 2))
    st.write("**Deviazione standard:**", round(df['y'].std(), 2))
    st.dataframe(df.head())

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")

