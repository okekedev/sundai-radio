import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import numpy as np
from datetime import datetime, timedelta
import threading
import time

# Import custom components
from components.category_grid import create_category_grid
from components.sleep_timer import create_sleep_timer
from utils.theme import RetroTheme
from utils.music_categories import MusicCategory

# Initialize the Dash app with Bootstrap
app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        'https://fonts.googleapis.com/css2?family=American+Typewriter:wght@400;700&display=swap',
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'
    ],
    assets_folder='assets',
    suppress_callback_exceptions=True
)

def create_layout():
    """Create the main layout of the application."""
    return html.Div([
        # Mini Header with Logo
        html.Div([
            html.Span("SUNDAI RADIO", className="mini-header-title")
        ], className="mini-header"),
        
        # Main Content
        html.Div([
            # SELECT CHANNEL Section
            html.Div([
                html.H2("SELECT CHANNEL", className="section-header"),
                create_category_grid(MusicCategory.get_samples())
            ], className="category-section"),
            
            # NOW PLAYING Section (initially hidden)
            html.Div([
                html.H2("NOW PLAYING", className="section-header"),
                html.Div(id="radio-player", className="radio-frame")
            ], className="player-section", id="player-section", style={"display": "none"}),
            
            # Mini Footer
            html.Div([
                html.P("© 2024 Sundai Radio - Your Source for Christian Music", className="footer-text")
            ], className="mini-footer")
        ], className="main-content")
    ], className="app-container")

# Add a hidden div for initial load
app.layout = html.Div([
    html.Div(id="_", style={"display": "none"}),
    create_layout()
])

# Add initial callback to autoplay piano station
@app.callback(
    [Output("radio-player", "children", allow_duplicate=True),
     Output("player-section", "style", allow_duplicate=True)],
    [Input("_", "children")] + [Input(f"category-{category.title}", "n_clicks") 
     for category in MusicCategory.get_samples()],
    prevent_initial_call=True
)
def update_radio_player(_, *args):
    try:
        ctx = dash.callback_context
        if not ctx.triggered:
            return dash.no_update, dash.no_update
        
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        # Handle initial load
        if trigger_id == "_":
            return None, {"display": "none"}
        
        # Handle category selection
        if trigger_id.startswith('category-'):
            category_name = trigger_id.replace('category-', '')
            selected_category = next(
                (cat for cat in MusicCategory.get_samples() if cat.title == category_name),
                None
            )
            
            if selected_category:
                return html.Iframe(
                    src=selected_category.iframe_url,
                    className="radio-frame",
                    style={
                        "width": "100%",
                        "height": "160px",
                        "border": "none",
                        "borderRadius": "10px"
                    }
                ), {"display": "block"}
        
        return dash.no_update, dash.no_update
    except Exception as e:
        print(f"Error in update_radio_player: {e}")
        return dash.no_update, dash.no_update

# Callback for sleep timer
@app.callback(
    Output("sleep-timer-modal", "is_open"),
    [Input("sleep-timer-button", "n_clicks"),
     Input("close-sleep-timer", "n_clicks"),
     Input("timer-15", "n_clicks"),
     Input("timer-30", "n_clicks"),
     Input("timer-60", "n_clicks"),
     Input("timer-120", "n_clicks")],
    [State("sleep-timer-modal", "is_open")]
)
def toggle_sleep_timer(n1, n2, t15, t30, t60, t120, is_open):
    ctx = dash.callback_context
    if not ctx.triggered:
        return is_open
    
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == "sleep-timer-button":
        return not is_open
    elif button_id == "close-sleep-timer":
        return False
    elif button_id in ["timer-15", "timer-30", "timer-60", "timer-120"]:
        # Handle timer selection
        return False
    
    return is_open

if __name__ == "__main__":
    app.run_server(debug=True, port=8081, host='0.0.0.0') 