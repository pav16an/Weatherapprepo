from flask import Flask,request,render_template
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/Weatherapp',methods=['GET','POST'])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather?q=london&units=metric&appid=2de9a5b19532b8965ad59e2e7d305691"
    
    param={
        'q':request.form.get('city'),
        'appid' :request.form.get('appid'),
        'units' :request.form.get('units')
        }
    response = requests.get(url,params=param)
    data = response.json()
    return f"data : {data}"
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
