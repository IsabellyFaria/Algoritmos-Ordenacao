from flask import Flask, render_template, request, jsonify, send_from_directory, abort
import os
from app.processar import *

app = Flask(__name__,template_folder='../template', static_folder="../static")
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), "uploads")
app.config['DOWNLOAD_FOLDER'] = os.path.join(os.getcwd(), "static", "files")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/receber",methods=["POST"])
def receber():
    ordenacao = request.form['ordenacao']
    indice =  int(request.form['indice'])
    arquivo = request.files['arquivo']
    
    if arquivo:
        filename = arquivo.filename
        
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file_path = os.path.join(app.config['DOWNLOAD_FOLDER'], filename)
        arquivo.save(save_path)
        processar(save_path, ordenacao,indice, file_path)
    
        return jsonify({
            "path": "/download/" + filename,
            "message": "Deu certo",
            "status": True
        }), 200
        
    return jsonify({
        "message": "Deu ruim",
        "status": False
    }), 400
        
@app.route('/download/<path:filename>')
def download_file(filename):
    try:
        return send_from_directory(app.config['DOWNLOAD_FOLDER'],
                                   filename,
                                   as_attachment=True)
    except FileNotFoundError:
        abort(404)
