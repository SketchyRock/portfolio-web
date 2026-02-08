from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open("data/projects.json", "r") as f:
        project_data = json.load(f)
    return render_template('index.html', projects=project_data)

if __name__ == '__main__':
    app.run(debug=True)
