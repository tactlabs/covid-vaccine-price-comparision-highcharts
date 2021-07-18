
from flask import Flask,  render_template, jsonify,request
import random
import json
import business


app  = Flask(__name__)
PORT = 3000

@app.route("/", methods=["GET","POST"])
def startpy():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    # return jsonify(result)
    return render_template("index.html") 

'''
http://0.0.0.0:3000/api/data
'''

@app.route("/api/data", methods=["GET"])
def api_get_data():

    result = business.get_data()
    print(result)

   
    return jsonify(result)



if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)