from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        return f"Thanks for reaching out, {name}! Message received."
    return render_template('contact.html')

# Dynamic route example
@app.route('/user/<username>')
def show_user(username):
    return f"Hello, {username}!"

# Custom 404 error page
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 Not Found</h1><p>The page you're looking for doesn't exist.</p>", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
