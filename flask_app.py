from flask import Flask, request, jsonify, Response, render_template
import json
import ast

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def convertJson():
    if request.method == "POST":

        j = ast.literal_eval(request.form['dictionaryString'].replace("null","'null'"))

        return Response(
            json.dumps(j),
            mimetype='application/json'
        )
    else:
        return render_template('./json.html') 
