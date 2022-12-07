import matplotlib.pyplot as plt
import pandas as pd
import pydeck as pdk
import numpy as np
import streamlit as st


st.set_page_config(
  page_icon=":thumbs_up:",
  layout="wide"
  )

@st.cache
def carga_data():
  return pd.read_excel("carga-bip.xlsx", header=9)

bip = carga_data()

##### Graficar las 5 comunas con más puntos: Pie y Barras
st.header("Desarrollo Desafío Clase 5")
st.info("Top 5 Comunas con más Puntos de Carga Bip")

Ptos_comuna = bip.groupby(by=["MAIPU"]).size()
Ptos_comuna.sort_values(axis="index", ascending=False, inplace=True)
Top5_Com = Ptos_comuna[0:5]

col_pie, col_barra, col_3 = st.columns(3, gap= "medium")

with col_pie:
  pie = plt.figure()
  Top5_Com.plot.pie(
    title="Cantidad de Puntos de Carga por Comuna",
    y="index",
    legend=None
  ).plot()
  st.pyplot(pie)

with col_barra:
  barra = plt.figure()
  Top5_Com.plot.bar(
    title="Cantidad de Puntos de Carga por Comuna",
    xlabel="Comunas",
    ylabel="Cantidad Puntos de Carga",
    color="black",
    grid=True
  ).plot()
  st.pyplot(barra)

with col_3:
  line = plt.figure()
  Top5_Com.plot.line(
    title="Cantidad de Puntos de Carga por Comuna",
    xlabel="Comunas",
    ylabel="Cantidad Puntos de Carga",
    color="red",
    grid=True
  ).plot()
  st.pyplot(line)

##### Crear un multiselector de “Comunas por Puntos de Carga” 
##### con las opciones: menos de 20 puntos, 21 a 60 puntos, más de 60 puntos
##### Reflejar en un mapa


