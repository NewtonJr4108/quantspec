import mplfinance as mpf
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.io as theme
import plotly.express as px 
import time


def graph(stock):
    yf.pdr_override()
    
    stock_data = yf.Ticker(stock)
    
    data = stock_data.history()
    last_quote = '%.2f'%float(data['Close'].iloc[-1])

    
    name = stock_data.info['longName']

    #stock=input("Enter a stock symbol: ")
    #button is web dictates period
    
    df = yf.download(tickers=stock,period='1d',interval='1m')
    
    #print(df)


    fig=go.Figure()    
    fig.layout._initialize_layout_template = "plotly_dark"
    plotly_template = theme.templates["plotly_dark"]
    theme.templates["plotly_dark_custom"] = theme.templates["plotly_dark"]

    

    fig.add_trace(go.Candlestick(x=df.index,
                    
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'], name = 'market data')),
    
    #may not work
    
    
    

    fig.update_layout(
        
        
        title= name +"\n"+str(last_quote),
        font=dict(family='Arial',
                size=18, color='white'),

        #yaxis_title='Stock Price (USD per Share)',
        #xaxis_rangeselector_activecolor='black',
        xaxis_rangeselector_font_color='black',


        plot_bgcolor='rgb(19, 46, 64)',
        paper_bgcolor ='rgb(54, 69, 79)'),

        
        
    

    #plot_bgcolor='#000000'
    
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1440, label="1 Day", step="minute", stepmode="backward"),
                dict(count=7, label="1 Week", step="day", stepmode="backward"),
                dict(count=31, label="1 Month", step="day", stepmode="backward"),
                dict(count=1, label="1Y", step="year", stepmode="backward"),
                dict(count=5, label="5Y", step="year", stepmode="backward"),
                dict(label = "max", step="all")
            ])
        )
    
    )
    #fig._config("{displaylogo: false}")
    fig.update_layout(modebar_remove=[
    'autoScale2d', 'autoscale', 'editInChartStudio', 'editinchartstudio', 'hoverCompareCartesian', 
    'hovercompare', 'lasso', 'lasso2d', 'orbitRotation', 'orbitrotation', 'pan', 'pan2d', 'pan3d', 
    'reset', 'resetCameraDefault3d', 'resetCameraLastSave3d', 'resetGeo', 'resetSankeyGroup', 
    'resetScale2d', 'resetViewMapbox', 'resetViews', 'resetcameradefault', 'resetcameralastsave', 
    'resetsankeygroup', 'resetscale', 'resetview', 'resetviews', 'select', 'select2d', 
    'sendDataToCloud', 'senddatatocloud', 'tableRotation', 'tablerotation', 'toImage', 'toggleHover', 
    'toggleSpikelines', 'togglehover', 'togglespikelines', 'toimage', 'zoom', 'zoom2d', 'zoom3d', 
    'zoomIn2d', 'zoomInGeo', 'zoomInMapbox', 'zoomOut2d', 'zoomOutGeo', 'zoomOutMapbox', 
    'zoomin', 'zoomout'
])
    
    theme.templates['custom'] = go.layout.Template(
    layout_paper_bgcolor='rgba(0,0,0,0)',
    layout_plot_bgcolor='rgba(0,0,0,0)'
    )
    theme.templates.default = ('plotly+custom')

    
    

    config = {'displayModeBar': False}
    
    


    
    

    #print(fig.to_html())
    return fig.to_html(config = config)
    
#print(graph("tsla"))