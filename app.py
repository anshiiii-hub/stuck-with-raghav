from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    """
    Serves the main cinematic SPA (Single Page Application).
    Flask automatically looks for 'index.html' inside the 'templates' folder.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
