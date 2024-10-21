from flask import Flask
from utils import calculate_discount

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/discount/<int:price>/<int:percent>')
def discount(price, percent):
    try:
        discounted_price = calculate_discount(price, percent)
        return f"Discounted price: {discounted_price}"
    except ValueError as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)