from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def home():
     return render_template('es.html')

@app.route('/it', methods=['GET'])
def ciao_mondo():
    return ('<h1>meteo</h1>')

@app.route('/r', methods=['GET'])
def libro():
    return ('<h1>libro</h1>')

@app.route('/c', methods=['GET'])
def calendario():
    return ('<h1>calendario</h1>')
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)