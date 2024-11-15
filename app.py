from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load certifications data from JSON file
with open('certifications.json') as f:
    certifications = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    # Filter certifications based on the query
    results = [cert for cert in certifications if query in cert['name'].lower()]

    if not results:
        return jsonify(f{"message": "Sorry, that is not in our database of certifications."})
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
