#run direct from VSCODE environ, weird error where yfinance isn't detected


from flask import Flask, url_for, redirect, render_template_string, render_template, request
from plot.plt import graph
import yfinance as yf
import time
import os
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
            
            #<meta http-equiv="refresh" content="2">

            header = """

            <style>

    .roboto-light {
        font-family: "Roboto", sans-serif;
        font-weight: 300;
        font-style: normal;
    }
    
        footer{
            
            color: white;
            font-family: sans-serif;
            background-color: #36454f;
            margin:0;


            

            
            
        }
        


        h1{
            font-family: sans-serif;
            background-color: #36454f;
            margin:0;

            
            
            color: white;
        }
        h2{
            font-family: sans-serif;

            color: white;
            background-color: #36454f;
            margin:0;

            
        body{
            
            background-color: #36454f;
;
            
            
        }
        
        p{
            
            background-color: #36454f;
            margin:0;

            
        }
        br{
            color: #36454f;
    
            background-color: #36454f;
            margin:0;

        }
        
        
        }
        div{

        margin: 0%;
    }


    </style>
    
    <style type="text/css">
body { margin-top: 0px;
margin-right: 0px;
margin-bottom: 0px;
margin-left: 0px
}
</style>



<div></div>

<div id="no-background"></div>

<h1>QuantSpec</h1>


<div></div>







            
            """
            
            footer = '''
            <center>
            <footer>
                <div class="row justify-content-center">
                    <div class="col-md-7 text-center">
            Copyright Matthew Anto / QuantSpec &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved </a>
                    </div>

                </footer>
                </center>
                
            '''
            
                
            return render_template_string(header+graph(stock)+footer)

                
                
            

        except IndexError:
            return render_template("stock_not_found.html")
        
@app.route('/about')
def about():
    return render_template("about.html")
if __name__ == "__main__":
    
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))