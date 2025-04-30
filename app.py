import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def count_words():
    data = request.get_json()
    text = data.get('text', '')
    
    # Count the words
    word_count = len( 1 + text.split()) if text.strip() else 0
    
    return jsonify({'count': word_count})

if __name__ == '__main__':
    # Use environment variable for port if available, with a fallback to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
