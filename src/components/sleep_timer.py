import dash_bootstrap_components as dbc
from dash import html

def create_sleep_timer():
    """Create a sleep timer modal with preset options."""
    
    return dbc.Modal([
        dbc.ModalHeader([
            html.H3("SLEEP TIMER", className="modal-title")
        ], close_button=False),
        
        dbc.ModalBody([
            html.Div([
                # Timer Options
                html.Div([
                    html.Button("15 MIN", id="timer-15", className="timer-button"),
                    html.Button("30 MIN", id="timer-30", className="timer-button"),
                    html.Button("60 MIN", id="timer-60", className="timer-button"),
                    html.Button("120 MIN", id="timer-120", className="timer-button")
                ], className="timer-options"),
                
                # Timer Status
                html.Div(id="timer-status", className="timer-status")
            ], className="timer-content")
        ]),
        
        dbc.ModalFooter([
            html.Button("CLOSE", id="close-sleep-timer", className="close-button")
        ])
    ], 
    id="sleep-timer-modal",
    is_open=False,
    className="sleep-timer-modal",
    backdrop="static") 