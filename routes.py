from flask import Flask, render_template, url_for, request
import os 
import dash
import  url_override
import fertilizer_pred as fp 

# from fertilizer import pred_fert_reco 

server = Flask(__name__, static_url_path='/static')

# dash_app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/')

# app.layout = html.Div(id="dash-cointainer")

@server.route("/")
def index():
	return render_template("index.html")

@server.route("/dashboard")
def dashboard():
	return render_template("dashboard.html")

@server.route("/crop")
def crop_pred():
    return render_template('crop.html')

@server.route("/fertilizer")
def fertilizer():
    return render_template("fertilizer.html")

@server.route("/fertilizer_process", methods=["POST", "GET"])
def fertilizer_process():
    
    if request.method == "POST":
        Crop = str(request.form['crop-value'])
        N = int(request.form["n-value"]) #10
        P = int(request.form['p-value']) #20
        K = int(request.form['k-value']) #40
        pH = float(request.form['pH-value'])
        # obj1 = pred_fert_reco()
        # dict_of_values = obj1.compute_values()
        rec = fp.
    return render_template("fertilizer_result.html", context=context)

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


if __name__ == "__main__":
	server.run(debug=True)