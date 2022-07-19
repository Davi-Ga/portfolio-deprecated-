# Further config access https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications

from flask import Flask, render_template, jsonify, make_response,redirect
import os

app = Flask(__name__,static_url_path='',static_folder='static', template_folder='templates')

if __name__ == '__main__':
    port=int(os.environ.get('PORT', 8080))
    app.run(debug=True,host='0.0.0.0',port=port)

@app.route("/",methods=['GET'])
def index_get():
    return render_template("index.html")


