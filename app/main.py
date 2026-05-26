from flask import Flask, jsonify, request
from app.calculator import add, subtract, multiply, divide

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({
        "message": "Calculator API is running!",
        "endpoints": [
            "/add?a=1&b=2",
            "/subtract?a=5&b=3",
            "/multiply?a=4&b=3",
            "/divide?a=10&b=2",
            "/power?a=2&b=8"
        ]
    })


@app.route('/add')
def route_add():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({"result": add(a, b)})
    
    
@app.route('/power')
def route_power():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({"result": a ** b})


if __name__ == '__main__':
    app.run()