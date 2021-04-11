from flask import Flask, render_template, url_for, request
import os 
import dash
import  url_override
import fertilizer_pred as fp 
from markupsafe import Markup
from dash_demo import *
# from fertilizer import pred_fert_reco 

server = Flask(__name__, static_url_path='/static')
 
@server.route("/")
def index():
	return render_template("index.html")

@server.route("/dashboard")
def dashboard():
    graph = district_wise_prod()
	return render_template("dashboard.html", graph=graph)

@server.route("/crop")
def crop_pred():
    return render_template('crop_pred.html')

@server.route("/fertilizer")
def fertilizer():
    return render_template("fertilizer.html")

@server.route("/fertilizer_process", methods=["POST", "GET"])
def fertilizer_process():
    
    if request.method == "POST":
        Crop = str(request.form['crop-value']).lower()
        N = int(request.form["n-value"])
        P = int(request.form['p-value']) 
        K = int(request.form['k-value']) 
        pH = float(request.form['pH-value'])
 
        values = [Crop, N, P, K, pH]

        rec = fp.compute_values(values)
        dict2 = {'nrec':Markup(rec[0]), 'prec':Markup(rec[1]), 'krec':Markup(rec[2]), 'pHrec':Markup(rec[3])}

    return render_template("fertilizer_result.html", context=dict2)

@server.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(server.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


# if __name__ == "__main__":
# 	server.run(debug=True)