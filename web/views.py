import os
import subprocess
from django.shortcuts import render
from django.conf import settings

TEMP_HTML_DIR = os.path.join(settings.BASE_DIR, "temp_html")

def index(request):
    folder = request.GET.get("folder")
    notebook = request.GET.get("notebook")

    notebooks = []
    html_file = None

    # Si el usuario escribió una carpeta
    if folder and os.path.exists(folder):
        for file in os.listdir(folder):
            if file.endswith(".ipynb"):
                notebooks.append(file)

    # Si seleccionó un notebook
    if folder and notebook:
        ipynb_path = os.path.join(folder, notebook)

        # Convertir a HTML
        subprocess.run([
            "jupyter", "nbconvert",
            ipynb_path,
            "--to", "html",
            "--execute",
            "--output-dir", TEMP_HTML_DIR,
            "--TemplateExporter.exclude_input=True"
        ])

        html_name = notebook.replace(".ipynb", ".html")
        html_file = f"/html/{html_name}"

    return render(request, "index.html", {
        "notebooks": notebooks,
        "folder": folder,
        "selected_html": html_file
    })


