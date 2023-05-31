from flask import Flask, request

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    name = data.get('name', '')
    message = f'Hello {name}'
    return {'message': message}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)