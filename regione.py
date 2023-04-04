from flask import Flask, render_template, request
import geopandas as gpd
import io
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
import matplotlib.pyplot as plt
import folium
app = Flask(__name__)
comuni = gpd.read_file("/workspace/Flask_Pandas/Limiti01012023_g/Com01012023_g/Com01012023_g_WGS84.shp")
prov = gpd.read_file("/workspace/Flask_Pandas/Limiti01012023_g/ProvCM01012023_g/ProvCM01012023_g_WGS84.shp")
reg = gpd.read_file("/workspace/Flask_Pandas/Limiti01012023_g/Reg01012023_g/Reg01012023_g_WGS84.shp")
@app.route('/')
def home():
    
    return render_template('regioni.html', list=comuni[comuni["COMUNE"]=="Milano"].to_html())



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)