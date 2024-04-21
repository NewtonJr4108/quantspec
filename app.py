#run direct from VSCODE environ, weird error where yfinance isn't detected


from flask import Flask, url_for, redirect, render_template_string, render_template, request
from plot.plt import graph
import yfinance as yf

from news.scrape import parse_source
app = Flask(__name__)

@app.route('/')
def homepage():
    #use source parsing module to organize data feed on homepage of website
    print(parse_source())
    
    
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
            
            #formats so as to allow same CSS style in index
            #also prevents white border error
            header = """
            <style>

    .roboto-light {
        font-family: "Roboto", sans-serif;
        font-weight: 300;
        font-style: normal;
    }
        


        h1{
            font-family: sans-serif;
            
            
            color: black;
        }
        h2{
            font-family: sans-serif;

            color: white;
            
        body{
            
            background-color: #36454f;
;
            
            
        }
        }


    </style>
    
    <style type="text/css">
body { margin-top: 0px;
margin-right: 0px;
margin-bottom: 0px;
margin-left: 0px
}
</style>

            
            """
            return render_template_string(header+graph(stock)+
                                    "\n<br><h1>hello</h1>")
        except IndexError:
            return render_template("stock_not_found.html")
        
@app.route('/about')
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(debug=True)