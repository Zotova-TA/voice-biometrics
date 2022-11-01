"""
The flask application package.
"""

#pragma execution_character_set("utf-8")


from flask import Flask
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Здесь загружаем модели

import FlaskApp.views