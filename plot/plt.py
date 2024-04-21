import mplfinance as mpf
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.io as theme
import plotly.express as px 



def graph(stock):
    yf.pdr_override()
    
    stock_data = yf.Ticker(stock)
    
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
                    close=df['Close'], name = 'market data'))
                    
    
    

    fig.update_layout(
        
        title= name +" Current Share Price:",
        font=dict(family='Arial',
                size=18, color='white'),

        yaxis_title='Stock Price (USD per Share)',
        plot_bgcolor='rgb(54, 69, 79)',
        paper_bgcolor ='rgb(54, 69, 79)'),

        
        
    

    #plot_bgcolor='#000000'
    
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=3, label="3h", step="hour", stepmode="backward"),
                dict(step="all")
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