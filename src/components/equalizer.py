from dash import html, dcc
import plotly.graph_objects as go
from utils.theme import RetroTheme
import numpy as np

class AudioProcessor:
    def __init__(self):
        self.frequencies = [60, 170, 310, 600, 1000, 3000, 6000, 12000, 14000, 16000]
        self.gains = [0] * 10
        self.sample_rate = 44100
        
    def apply_eq(self, audio_data):
        """Apply equalizer settings to audio data."""
        if not audio_data:
            return audio_data
            
        # Convert to frequency domain
        fft_data = np.fft.fft(audio_data)
        freqs = np.fft.fftfreq(len(audio_data), 1/self.sample_rate)
        
        # Apply gains for each frequency band
        for i, (freq, gain) in enumerate(zip(self.frequencies, self.gains)):
            # Find frequency indices within band
            band_indices = np.where((np.abs(freqs) >= freq * 0.7) & 
                                  (np.abs(freqs) <= freq * 1.3))[0]
            
            # Apply gain
            fft_data[band_indices] *= (10 ** (gain/20))
            
        # Convert back to time domain
        return np.real(np.fft.ifft(fft_data))

def create_equalizer():
    """Create an animated equalizer component."""
    # Initialize equalizer values
    initial_values = [0.5] * 10
    
    # Create frequency labels
    frequencies = ['60Hz', '170Hz', '310Hz', '600Hz', '1kHz', '3kHz', '6kHz', '12kHz', '14kHz', '16kHz']
    
    # Create the figure
    fig = go.Figure()
    
    # Add bars with slower transitions
    for i, value in enumerate(initial_values):
        fig.add_trace(go.Bar(
            x=[i],
            y=[value],
            marker_color=RetroTheme.get_color_for_index(i),
            width=0.8,
            hoverinfo='none'
        ))
    
    # Update layout for smoother appearance
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=300,
        xaxis=dict(
            showticklabels=True,
            ticktext=frequencies,
            tickvals=list(range(10)),
            tickangle=45,
            gridcolor='rgba(125, 78, 87, 0.1)',
            zerolinecolor='rgba(125, 78, 87, 0.1)',
            tickfont=dict(color='#7D4E57')
        ),
        yaxis=dict(
            showticklabels=True,
            range=[0, 1],
            ticktext=['-12dB', '-6dB', '0dB', '+6dB', '+12dB'],
            tickvals=[0, 0.25, 0.5, 0.75, 1],
            gridcolor='rgba(125, 78, 87, 0.1)',
            zerolinecolor='rgba(125, 78, 87, 0.1)',
            tickfont=dict(color='#7D4E57')
        ),
        dragmode=False,
        hovermode=False,
        modebar=dict(
            remove=['zoom', 'pan', 'select', 'lasso', 'zoomIn', 'zoomOut', 'autoScale', 'resetScale']
        ),
        transition_duration=800  # Slower transition duration
    )
    
    # Create the layout
    return html.Div([
        html.H2("EQUALIZER", className="equalizer-title"),
        dcc.Graph(
            id="equalizer-graph",
            figure=fig,
            config={'displayModeBar': False},
            className="equalizer-graph"
        ),
        dcc.Interval(
            id='equalizer-interval',
            interval=100,  # Update every 100ms for smoother animation
            n_intervals=0
        )
    ], className="equalizer-container") 