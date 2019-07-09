from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome100!"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = False)
