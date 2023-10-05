import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
from PIL import Image

st.title("Test gpd")

df = gpd.read_file('https://raw.githubusercontent.com/unisalledatos/big_data/main/datos/countries.geo.json')

fig, ax = plt.subplots(1, 1)
df.plot(ax=ax)

st.pyplot(fig)

image = Image.open('https://raw.githubusercontent.com/unisalledatos/app_geopd/main/test.jpg')
st.image(image)
