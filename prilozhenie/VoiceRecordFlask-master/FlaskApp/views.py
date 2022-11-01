python3 runserver.py"""
Routes and views for the flask application.
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime
from flask import render_template, request, redirect, url_for
from FlaskApp import app
from werkzeug.utils import secure_filename

@app.route('/')
def input():
    """Отображает форму ввода аудио"""
    return render_template(
        'index.html',
        title='Запись аудио'
    )

@app.route('/upload_voice', methods=['POST'])
def upload():
    """Загрузка файла"""
    if request.method == 'POST':
        # check if the post request has the file part
        if 'voice' not in request.files:
            return "Upload failed"

        file = request.files['voice']
        filename = secure_filename(file.filename)
        file.save(os.path.join("d:\\Dev\\VisualStudioCode\\upload\\", filename))
        return f"Upload OK filename={filename}, type={type(file)}"


   

