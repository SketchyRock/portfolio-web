# Personal Portfolio & Blog - Enzo Hins

This repository contains the source code for my personal portfolio website. Built with **Python** and **Flask**, this application serves as a central hub to showcase my work in Computer Science and Cyber Security, as well as a platform for my technical writing.

## Overview

Unlike a static HTML site, this project uses a lightweight dynamic backend to manage content efficiently. It features a custom-built file-based CMS (Content Management System) that allows me to write blog posts in Markdown and update projects via JSON without altering the codebase.

### Key Features
* **Dynamic Project Loading:** Project cards on the homepage are rendered dynamically from a `projects.json` file, making it easy to scale the portfolio.
* **Markdown Blog Engine:** A custom implementation that parses local `.md` files into HTML, allowing for seamless article publishing.
* **Responsive Design:** Custom CSS using CSS variables (`:root`) for easy theming and mobile responsiveness.
* **Jinja2 Templating:** Modular HTML structure using class inheritance (`base.html`).

## Tech Stack

* **Backend:** Python 3, Flask
* **Server:** Gunicorn (for production)
* **Frontend:** HTML5, CSS3, Jinja2
* **Utilities:** Python-Markdown (for text parsing)

## Project Structure

```text
├── app.py                # Main Flask application logic and routing
├── data/
│   ├── blogs/            # Markdown files (.md) for blog posts
│   └── projects.json     # Data source for the projects section
├── static/
│   ├── css/              # Custom stylesheets
│   └── img/              # Assets and icons
├── templates/            # Jinja2 HTML templates (base, index, blog, etc.)
└── requirements.txt      # Python dependencies
```

## Local Development

To run this project locally on your machine:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/SketchyRock/portfolio-web.git](https://github.com/SketchyRock/portfolio-web.git)
    cd portfolio-web
    ```

2.  **Create a Virtual Environment (Optional but recommended)**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application**
    ```bash
    python app.py
    ```
    The site will be available at `http://127.0.0.1:5000`.

## Content Management

### Adding a New Project
To add a project to the homepage, navigate to `data/projects.json` and append a new object:
```json
{
    "name": "Project Name",
    "description": "Brief description...",
    "icon": "icon-name.svg", # If not no icon or words will appear
    "learned": ["Skill 1", "Skill 2"],
    "repo": "[https://github.com/](https://github.com/)..." # where ever you wish the project to take the user to
}
```

## Publishing a Blog Post
Simply drop a **.md** file into the **data/blogs/** folder. The file name will be automatically parsed into the title (e.g., my-new-post.md becomes "My New Post").
(Preferably include data before name "1-30-2020").

---

# TODO:
* implement github api pull for autmatic blog posts
* add more blog posts and potentially fix the spacing on blog page
