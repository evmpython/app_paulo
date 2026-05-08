
# importando o GEE e Geemap
import ee
import geemap
import streamlit as st

# inicializando GEE
geemap.ee_initialize(project='testepaulo-495717')

st.markdown('# Testando o Streamlit by Enriqueddddd2222')

# cria o mapa com centro nas coordenadas [latitude, longitude] e zoom inicial
Map = geemap.Map(center=[-14, -55], zoom=4)

# adicionando basemap
Map.add_basemap('SATELLITE')

# exibe na tela
Map
