from flask import Flask

# Create a Flask app instance
app = Flask(__name__)
# decorator is a fundamental building block in Flask for defining routes and mapping URLs to functions.
# It's widely used for creating homepages, health checks, and API entry points.
@app.route('/')
def Hello():
    return "hello world"
app.run('0.0.0.0')