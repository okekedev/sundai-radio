class RetroTheme:
    # 70s Color Palette
    orange_rust = "#D35400"
    avocado_green = "#567D46"
    harvest_gold = "#E59866"
    chocolate_brown = "#6E2C00"
    mustard_yellow = "#D4AC0D"
    sunset_orange = "#E67E22"
    earthy_red = "#922B21"
    warm_tan = "#E6B0AA"
    
    # Background colors
    background_light = "#FAE5D3"
    background_dark = "#FEF5E7"
    
    # Font families
    title_font = "American Typewriter, serif"
    body_font = "American Typewriter, serif"
    
    # Font sizes
    large_title = "34px"
    title1 = "28px"
    title2 = "22px"
    title3 = "20px"
    headline = "17px"
    body = "16px"
    callout = "15px"
    subheadline = "14px"
    footnote = "12px"
    caption = "11px"
    
    # Corner radius
    corner_radius = "12px"
    
    # Get color for genre
    @staticmethod
    def get_color_for_genre(genre_title):
        color_map = {
            "Piano": RetroTheme.harvest_gold,
            "Lofi": RetroTheme.avocado_green,
            "Christian Rap": RetroTheme.orange_rust,
            "Christian Country": RetroTheme.earthy_red,
            "Baby Sleep": RetroTheme.warm_tan,
            "Relax": RetroTheme.sunset_orange,
            "Christian Rock": RetroTheme.earthy_red,
            "Lo-Fi": RetroTheme.chocolate_brown,
            "Classical": RetroTheme.harvest_gold,
            "Meditation": RetroTheme.warm_tan,
            "Positive Pop": RetroTheme.orange_rust
        }
        return color_map.get(genre_title, RetroTheme.mustard_yellow)
    
    # Get color for index (used in equalizer)
    @staticmethod
    def get_color_for_index(index):
        colors = [
            RetroTheme.orange_rust,
            RetroTheme.avocado_green,
            RetroTheme.harvest_gold,
            RetroTheme.mustard_yellow,
            RetroTheme.sunset_orange,
            RetroTheme.earthy_red,
            RetroTheme.warm_tan
        ]
        return colors[index % len(colors)]
    
    # CSS styles
    @staticmethod
    def get_styles():
        return {
            "main-container": {
                "backgroundColor": RetroTheme.background_light,
                "minHeight": "100vh",
                "padding": "20px"
            },
            "header-container": {
                "textAlign": "center",
                "marginBottom": "30px"
            },
            "retro-title": {
                "fontFamily": RetroTheme.title_font,
                "fontSize": RetroTheme.title2,
                "letterSpacing": "5px",
                "marginBottom": "15px"
            },
            "animated-separator": {
                "height": "4px",
                "background": f"linear-gradient(to right, {RetroTheme.orange_rust}, {RetroTheme.avocado_green}, {RetroTheme.harvest_gold}, {RetroTheme.mustard_yellow}, {RetroTheme.sunset_orange}, {RetroTheme.earthy_red}, {RetroTheme.warm_tan})",
                "animation": "separator-animation 12s linear infinite"
            },
            "category-card": {
                "backgroundColor": RetroTheme.background_dark,
                "borderRadius": RetroTheme.corner_radius,
                "padding": "20px",
                "textAlign": "center",
                "cursor": "pointer",
                "transition": "transform 0.2s",
                "boxShadow": "2px 2px 4px rgba(0,0,0,0.2)"
            },
            "category-card:hover": {
                "transform": "scale(1.05)"
            },
            "category-icon": {
                "fontSize": "40px",
                "marginBottom": "10px"
            },
            "category-title": {
                "fontFamily": RetroTheme.body_font,
                "fontSize": RetroTheme.headline,
                "fontWeight": "bold",
                "textTransform": "uppercase",
                "letterSpacing": "1px"
            }
        } 