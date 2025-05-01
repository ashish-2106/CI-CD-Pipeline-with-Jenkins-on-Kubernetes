from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"""
    <html>
        <head><title>CI/CD Pipeline</title></head>
        <body style="font-family: Arial; background-color: #f0f0f0; padding: 20px;">
            <h1 style="color: green;">🚀 CI/CD Pipeline Deployment Successful!</h1>
            <p>App deployed via Jenkins Pipeline.</p>
            <p><strong>Current Server Time:</strong> {current_time}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
