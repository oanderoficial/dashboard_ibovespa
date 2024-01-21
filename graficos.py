from data import df_reversed
import plotly.express as px

#Grafico de relação do dia / Volume
data = (df_reversed)
df = data.groupby('Date')[['Volume']].sum()
grafico_de_linha = px.line(
data, 
x= 'Date', 
y ='Volume', 
labels ={'Date': 'Dia/Mês', 'Volume': 'Volume'},
title='Gráfico Relação do Dia/Volume')

#Grafico do fechamento ajustado da bolsa 
fechamento = (df_reversed)
df_fechamento = fechamento.groupby(['Date', 'Adj Close']).first()  # Use 'first()' para obter os preços de abertura e fechamento ajustado do dia
grafico_de_fechamento = px.histogram(
fechamento, 
color_discrete_sequence=['purple'],
x='Date', 
y='Adj Close',
labels={'Date': 'Data/Mês', 'Adj Close': 'Fechamento Ajustado'},
title='Gráfico Relação do fechamento ajustado por mês')

