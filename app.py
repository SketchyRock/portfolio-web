from flask import Flask, abort, render_template
import json
import markdown
import os

app = Flask(__name__)

@app.route("/")
def home():
    with open("data/projects.json", "r") as f:
        project_data = json.load(f)
    return render_template("index.html", projects=project_data)


@app.route("/blog")
def blog():
    files = sorted(
        [f for f in os.listdir("data/blogs") if f.endswith(".md")], reverse=True
    )
    posts = []
    for f in files:
        display_title = f.replace(".md", "").replace("-", " ").title()
        posts.append({"filename": f, "title": display_title})

    return render_template("blog_list.html", posts=posts)


@app.route("/blog/<filename>")
def blog_post(filename):
    path = os.path.join("data/blogs", filename)
    if not os.path.exists(path):
        abort(404)

    with open(path, "r", encoding="UTF-8") as f:
        content = f.read()
        html_content = markdown.markdown(content)

    return render_template("blog_post.html", content=html_content)


if __name__ == "__main__":
    app.run()
