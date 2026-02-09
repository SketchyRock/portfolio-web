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

# TODO: implement github api pull for autmatic blog posts
# TODO: add more blog posts and potentially fix the spacing on blog page
