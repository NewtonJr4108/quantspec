#run direct from VSCODE environ, weird error where yfinance isn't detected


from flask import Flask, url_for, redirect, render_template_string, render_template, request
from plot.plt import graph
import yfinance as yf
import time
import os
from news.scrape import parse_source
app = Flask(__name__)
link = (parse_source()[1])

@app.route('/')
def homepage():
    #use source parsing module to organize data feed on homepage of website
    
    
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
            
            <meta name="theme-color" content="#000000">




            <style>
            mix-blend-mode: multiply;


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

    form{

        background-color: #36454f;
        color: #ffffff;
        font-family: sans-serif;
        border-color: #36454f;


    }

</style>





<div></div>

<div id="no-background"></div>

<h1>QuantSpec</h1>

<form action="/index" method="post" autocomplete="on">

        <label for="stock">Enter valid symbol</label>

        <input type="ticker" name="stock_index" placeholder="ex: AMZN"> 

        <input type="submit">



<div></div>









            
            """
            
            footer = '''
            
                    <center>
            <h1>Recent News:</h1>
            <p>{{link}}</p>
        </center>

            
            
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