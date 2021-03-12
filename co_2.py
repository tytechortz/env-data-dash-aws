import pandas as pd
from datetime import datetime
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import numpy as np
app = dash.Dash(__name__)
app.config['suppress_callback_exceptions']=True