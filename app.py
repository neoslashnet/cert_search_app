from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data (Replace this with real data later)
certifications = [
    {"name": "CISSP", "domain": "Security", "level": "Advanced"},
    {"name": "CCSP", "domain": "Cloud Security", "level": "Intermediate"},
    {"name": "CEH", "domain": "Ethical Hacking", "level": "Beginner"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    results = [cert for cert in certifications if query in cert['name'].lower()]
    
    if not results:  # Check if results list is empty
        print("Sorry, that is not in our database of certifications.")
        return jsonify({"message": "Sorry, that is not in our database of certifications."})
    
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
