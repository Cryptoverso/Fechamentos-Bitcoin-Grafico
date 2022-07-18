import numpy as np 
import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as Dash


based = pd.read_excel('Dados_Bitcoin.xlsx')
based_filter = based.head(10) # filtra certa quantidade de linhas desejadas 
print(based_filter)

# setar o indice: 
 
based.set_index('Data', inplace =True) # dá mais uma variável para o gráfico, nome da variável. 

# grafico de linha 

graf1 =px.line(based, y ='Fechamento') # banco de dados e seu eixo 


Media_Movel = based['Fechamento'].rolling(5).mean()
Media_Tendencia = based['Fechamento'].rolling(30).mean()

# criando um dashboard

Figure = Dash.Figure()
Figure.add_trace( 
    Dash.Scatter(
        x = based.index,
        y = based.Fechamento,
        mode = 'lines',
        name = 'Fechamento',
        marker_color = '#0000CD',
        opacity = 0.5,
    )
)
# adicionando a media 
Figure.add_trace( 
    Dash.Scatter(
        x = based.index,
        y = Media_Movel,
        mode = 'lines',
        name = 'Média Móvel',
        marker_color = '#00FA9A',
        opacity = 0.5,
    )
)
Figure.add_trace( 
    Dash.Scatter(
        x = based.index,
        y = Media_Tendencia,
        mode = 'lines',
        name = 'Média Tendencia',
        marker_color = '#A020F0',
        opacity = 0.5,
    )
)

# ajustes no layout 

Figure.update_layout(
    title = "Análise do Fechamento do Bitcoin",
    titlefont_size=20,
    xaxis = dict(  # info lateral ,x é o eixo 
        title="Período Histórico ",
        titlefont_size= 14,
        tickfont_size = 9, # fonte das datas 
    ),
    yaxis = dict(  # info lateral ,x é o eixo 
        title="Preço do Fechamento ($) ",
        titlefont_size= 14,
        tickfont_size = 9,
    )
)

Figure.show()

