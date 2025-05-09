import dash_bootstrap_components as dbc
from dash import html
from utils.theme import RetroTheme

def create_category_grid(categories):
    """Create a grid of music category cards."""
    
    return html.Div([
        # Category Card
        html.Div([
            # Category Icon
            html.Div([
                html.I(className=f"fas {category.icon} category-icon", style={"color": category.color})
            ], className="category-icon-container"),
            
            # Category Title
            html.H3(category.title, className="category-title"),
            
            # Category Description
            html.P(category.description, className="category-description")
        ], 
        id=f"category-{category.title}",
        className="category-card",
        n_clicks=0,
        **{"data-category": category.title})
        
        for category in categories
    ], className="category-grid") 