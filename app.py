import streamlit as st
st.title('UrbanRide - Aluguel de Carro')
st.subheader('Melhor Loja de Aluguel')
st.sidebar.title('Escolha um Modelo')
st.sidebar.image('Logo.png')


carros = ["Fiat_Mobi","HB20","Corolla","Civic","Compass","Jetta_GLI","BMW_X5","Audi_A5","Camaro","Mustang","Porsche_911","Huracán"]
opcao = st.sidebar.selectbox("Escolha o carro que foi alugado", carros)



st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown("---")

