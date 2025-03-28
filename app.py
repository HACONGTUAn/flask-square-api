from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask Square API! Use POST /square to calculate."
    
@app.route('/square', methods=['POST'])
def calculate_square():
    data = request.get_json()
    number = data.get("number", 0)
    result = number ** 2
    return jsonify({"number": number, "square": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


