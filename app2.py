#realizzare un serverweb che visualizzi l'ora attuale e colori lo sfondo in base all'orario:colore per la mattina uno per il pome uno per la sera e uno per la notte

from flask import Flask,render_template
app = Flask(__name__)
import datetime 

@app.route('/')
def hello_world():
  minuti=datetime.datetime.now().minute
  if minuti%2 == 0:
    col='green'
  else:
    col='red'
  return render_template('risposta.html',colore=col,min=minuti)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)