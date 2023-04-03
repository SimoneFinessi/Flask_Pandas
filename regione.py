from flask import Flask, render_template, request
import geopandas as pd
"app = Flask(__name__)"
comuni = pd.read_file("{{ url_for('Limiti01012023_g', filename='Com01012023_g/Com01012023_g_WGS84.shp') }}")
print(comuni)
"""@app.route('/')
def home():
    comuni = dati_regioni.drop_duplicates(subset=['denominazione_regione'])
    return render_template('html.html', list= list(nomi_regioni['denominazione_regione']))

@app.route('/search', methods = ['GET'])
def search():
    regione = request.args['regione']
    risultato = dati_regioni[dati_regioni['denominazione_regione']==regione.capitalize()]
    if len(risultato) == 0:
        table = 'Regione non trovata'
    else:
        table = risultato.to_html()
    return render_template('table.html', tabella = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)"""