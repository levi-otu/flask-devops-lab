from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# In-memory storage for demonstration
storage = []


@app.route('/')
def hello():
    return 'Hello, DevOps World!'


@app.route('/echo', methods=['POST'])
def echo():
    """Echo back the JSON payload sent in the request."""
    data = request.get_json(force=True)
    return jsonify(data), 201


@app.route('/reverse', methods=['PUT'])
def reverse():
    """Reverse a string sent in the JSON payload."""
    data = request.get_json(force=True)
    if 'text' not in data:
        return jsonify({'error': 'Missing "text" field'}), 400

    reversed_text = data['text'][::-1]
    return jsonify({'original': data['text'], 'reversed': reversed_text}), 200


@app.route('/jokes', methods=['GET'])
def get_jokes():
    """Return a random programming joke."""
    jokes = [
        "Why do programmers prefer dark mode? "
        "Because light attracts bugs!",
        "How many programmers does it take to change a light bulb? "
        "None, that's a hardware problem.",
        "Why do Java developers wear glasses? Because they don't C#!",
        "What's a programmer's favorite place? Foo Bar!",
        "Why did the developer go broke? "
        "Because he used up all his cache!",
    ]
    return jsonify({'joke': random.choice(jokes)}), 200


@app.route('/storage', methods=['GET'])
def get_storage():
    """Get all items from storage."""
    return jsonify({'items': storage, 'count': len(storage)}), 200


@app.route('/storage', methods=['POST'])
def add_to_storage():
    """Add an item to storage."""
    data = request.get_json(force=True)
    if 'item' not in data:
        return jsonify({'error': 'Missing "item" field'}), 400

    storage.append(data['item'])
    return jsonify({'message': 'Item added', 'item': data['item']}), 201


@app.route('/storage', methods=['DELETE'])
def clear_storage():
    """Clear all items from storage."""
    count = len(storage)
    storage.clear()
    return jsonify({'message': f'Cleared {count} items', 'count': count}), 200


if __name__ == '__main__':
    app.run()
