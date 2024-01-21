import streamlit as st
from data import df_reversed
from graficos import grafico_de_linha
from graficos import grafico_de_fechamento

st.set_page_config(layout='wide')

st.title('Dashboard: Dados históricos da IBOVESPA ')

dataset, volume, fechamento  = st.tabs(['Dataset', 'Volume', 'Fechamento Mensal'])
with dataset:
    st.dataframe(df_reversed, height=1000)

with volume:
    st.plotly_chart(grafico_de_linha, use_container_width=True)

with fechamento:
    st.plotly_chart(grafico_de_fechamento, use_container_width=True)


st.markdown(
    """
    <style>
        footer {
            position: relative;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
        }
    </style>
    <footer>
        <p>Aplicação desenvolvida por Anderson Bezerra Silva.</p>
        <p>© 2024 @oanderoficial</p>
    </footer>
    """,
    unsafe_allow_html=True
)
