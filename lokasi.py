from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lokasi", methods=["POST"])
def lokasi():
    data = request.json
    lat = data.get("latitude")
    lon = data.get("longitude")
    
    with open("lokasi_diterima.txt", "a") as f:
        f.write(f"Latitude: {lat}, Longitude: {lon}\n")
    
    return "Lokasi diterima!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
