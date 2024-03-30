#run direct from VSCODE environ, weird error where yfinance isn't detected


from flask import Flask, url_for, redirect, render_template_string, render_template, request
from plot.plt import graph
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/index', methods = ['POST', 'GET'])
def index():
    #return render_template_string("H")
    
    if request.method=='POST':
        try:
            stock = request.form['stock_index']
            
            #quote = yf.Ticker(stock)
            
            
            ticker_yahoo = yf.Ticker(stock)
            data = ticker_yahoo.history()
            last_quote = str(data['Close'].iloc[-1])
            
            #print(data)
            #return render_template_string(last_quote)
            return render_template_string(graph(stock))
        except IndexError:
            return render_template("stock_not_found.html")
        
@app.route('/about')
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(debug=True)