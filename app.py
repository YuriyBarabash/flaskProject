from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    message = {'message': f'Hello, {name}!'}
    return jsonify(message)


if __name__ == '__main__':
    app.run()
