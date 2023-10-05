import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt

st.title("Test gpd")

df = gpd.read_file('https://raw.githubusercontent.com/unisalledatos/big_data/main/datos/countries.geo.json')

fig, ax = plt.subplots(1, 1)
df.plot(ax=ax)

st.pyplot(fig)
