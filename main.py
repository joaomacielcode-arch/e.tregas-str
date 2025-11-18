import streamlit as st
import pandas as pd
import time
import numpy as np
import folium
from folium import plugins
from streamlit_folium import folium_static
from streamlit_folium import st_folium
import streamlit_book as stb


# Você Precisa usar esse session_state para que o botão mantenha os dados ativos -8.29974422830506, -35.978159133460615

# df = pd.DataFrame(np.random.randn(1000,2)/[50,50]+[38,-130],columns=['lat','lon'])

st.set_page_config(page_title="E.Tregas", page_icon=":material/rocket_launch:",initial_sidebar_state='collapsed')

if "circulos" not in st.session_state:
    st.session_state["circulos"] = []

data = {'Cidade':['Petrópolis','Boa Vista','Agamenon Magalhães','Indianópolis','Nova Caruaru','Alto do Moura','Salgado','Cidade Alta','Universitário','Maurício de Nassau'],'LAT':[-8.29974422830506,-8.256630,-8.304608,-8.288957,-8.256177,-8.288583,-8.272877,-8.309479967330306,-8.261844380967561,-8.28139],'LON':[-35.978159133460615,-36.011242,-35.996777,-35.954713,-35.979288,-36.010921,-35.956912,-35.97822366233255,-35.956908443388876,-35.9735],'INFO':['R. São Cristóvão','R. Quitéria Batista de Souza','Estr. Açude Cipó','R. Manoel Nunes Filho','Av. Transcontinental','Av. Leão Dourado','R. Marílio Pederneira','R. Córdoba','Av.Brasil','Rua Frei Caneca']}
df = pd.DataFrame(data)

mapa = folium.Map(location=[-8.28139,-35.9735],zoom_start=13)
for index,row in df.iterrows():
    popup_content=folium.Popup(f"""<b> {row['Cidade']} </b> <br> 
    <p> {row['INFO']} </p>""",max_width=510)
    folium.Marker(location=[row['LAT'],row['LON']],popup=popup_content,icon=folium.Icon(color='red',icon='info-sign')).add_to(mapa)

fg = folium.FeatureGroup(name="Circulos")

for circulo in st.session_state["circulos"]:
    fg.add_child(circulo)

folium.Circle(location=[-8.294011375684411,-35.953620106475775],radius=200,color='blue',fill=True,fill_color='blue',fill_opacity=0.3,tooltip='Estamos Aqui :)').add_to(mapa)

marker_cluster=plugins.MarkerCluster().add_to(mapa)

#folium.Marker(location=[-8.294011375684411,-35.953620106475775]).add_to(marker_cluster)

if 'escl' not in st.session_state:
    st.session_state.escl = False

def bt_click():
    st.session_state.escl = True

if 'escl2' not in st.session_state:
    st.session_state.escl2 = False

def bt_click2():
    st.session_state.escl2 = True

if 'crtlg' not in st.session_state:
    st.session_state.crtlg={'Drone1':False,'Drone2':False,'Drone3':False}


def alt_controlg(botao):
    for drones in st.session_state.crtlg:
        if drones == botao:
            st.session_state.crtlg[drones]=True
        else:
            st.session_state.crtlg[drones]=False

def ad_circl():
    lant = data['LAT'][indxs]
    lont = data['LON'][indxs]
    if ct < 1:
        new_circl = folium.Circle(location=[lant,lont],radius=200,color='red',fill=True,fill_color='red',fill_opacity=0.3,tooltip='Arredores')
        st.session_state["circulos"].append(new_circl)
    else:
        st.session_state["circulos"].pop(0)
        new_circl = folium.Circle(location=[lant,lont],radius=200,color='red',fill=True,fill_color='red',fill_opacity=0.3,tooltip='Arredores')
        st.session_state["circulos"].append(new_circl)
        
freddy = 0

#def on_change_callback():
    #indxs = city_list.index(opcao4)
    #lant = data['LAT'][indxs]
    #lont = data['LON'][indxs]
    #new_circle = folium.Circle(location=[lant,lont],radius=100,color='red',fill=True,fill_color='red',fill_opacity=0.3,tooltip='Arredores').add_to(mapa)
    #st.session_state["circles"].append(new_circle)

# Testando como fazer uma logo (Ficou pequeno, talvez aumentar)
#st.logo("etregaslogo1.png", size='large')

# Fazendo O Título
st.set_page_config(layout="centered")
st.markdown("""
<style>
.E-Tregas{
    font-size:100px !important;
    text-align:center;
    color:#00FF00;}</style> 
""", unsafe_allow_html=True)
st.markdown('<p class="E-Tregas">E.Tregas</p>', unsafe_allow_html=True)
st.markdown('<center>Extra Prático, Extremamente útil, seu site de outro mundo!</center>', unsafe_allow_html=True)

#if st.button('Botão'):
#    st.write('Apertado')

# idade = st.slider('Selecione sua idade.', 0, 100, 0)
# st.write(f'Idade selecionada: {idade}')

st.divider()

st.write('Selecione um drone.')

dron1, dron2, dron3 = st.columns(3)

with dron1:
    st.button('Drone 1', on_click=alt_controlg, args=('Drone1',))
    if st.session_state.crtlg['Drone1']:
        st.badge("Indisponível", icon = ":material/close:", color = "red")
        #opcao1 = st.selectbox(
        #'Escolha um tipo de entrega',
        #['Comida', 'Eletrônicos', 'Brinquedos'],
        #index=None,
        #key = 'um'
        #)
        #st.write(f'Selecionar: {opcao1}?') 
        #st.button('Sim', on_click=bt_click)

with dron2:
    st.button('Drone 2', on_click=alt_controlg, args=('Drone2',))
    if st.session_state.crtlg['Drone2']:
        st.badge("Disponível", icon = ":material/check:", color = "green")
        opcao2 = st.selectbox(
        'Escolha um tipo de entrega',
        ['Comida', 'Eletrônicos', 'Brinquedos'],
        index=None,
        key = 'dois'
        )
        st.write(f'Selecionar: {opcao2}?') 
        st.button('Sim', on_click=bt_click)

with dron3:
    st.button('Drone 3', on_click=alt_controlg, args=('Drone3',))
    if st.session_state.crtlg['Drone3']:
        st.badge("Disponível", icon = ":material/check:", color = "green")
        opcao3 = st.selectbox(
        'Escolha um tipo de entrega',
        ['Comida', 'Eletrônicos', 'Brinquedos'],
        index=None,
        key = 'tres'
        )
        st.write(f'Selecionar: {opcao3}?') 
        st.button('Sim', on_click=bt_click)

st.divider()

if st.session_state.escl:
    # Acessando o dicionário "data" e a key 'Cidade'
    city_list = data['Cidade']
    opcao4 = st.selectbox(
        'Escolha um local',
        city_list,
        key="bairros",
    )
    ct = len(st.session_state["circulos"])
    st.button("Selecionar", on_click=ad_circl)
    indxs = city_list.index(opcao4)
    
    st_folium(
        mapa,
        center=[-8.28139,-35.9735],
        zoom=13,
        key="novo",
        feature_group_to_add=fg,
        height=500,
        width=700
    )
    st.write(f'Tem certeza de sua escolha?')
    st.button('Sim', on_click=bt_click2, key = 'dos')

if st.session_state.escl2:
    match indxs:
        case 0:
            st.session_state.escl2 = False
            st.switch_page("pages/página0.py")
        case 1:
            st.session_state.escl2 = False
            st.switch_page("pages/página1.py")
        case 2:
            st.session_state.escl2 = False
            st.switch_page("pages/página2.py")
        case 3:
            st.session_state.escl2 = False
            st.switch_page("pages/página3.py")
        case 4:
            st.session_state.escl2 = False
            st.switch_page("pages/página4.py")
        case 5:
            st.session_state.escl2 = False
            st.switch_page("pages/página5.py")
        case 6:
            st.session_state.escl2 = False
            st.switch_page("pages/página6.py")
        case 7:
            st.session_state.escl2 = False
            st.switch_page("pages/página7.py")
        case 8:
            st.session_state.escl2 = False
            st.switch_page("pages/página8.py")
        case 9:
            st.session_state.escl2 = False
            st.switch_page("pages/página9.py")
