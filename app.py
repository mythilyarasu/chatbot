from flask import Flask, request, jsonify, render_template
import json
import importlib.metadata  # or import importlib_metadata for older Python versions

# Print Flask version
flask_version = importlib.metadata.version("flask")  # or importlib_metadata.version("flask") for older Python versions
print(f"Flask version: {flask_version}")

app = Flask(__name__)

# Load corpus
with open('corpus.json') as f:
    corpus = json.load(f)

def get_response(message):
    # Check if the message is in the corpus
    for item in corpus:
        if item["question"].lower() in message.lower():
            return item["answer"]
    return "For more information, please contact us directly."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
