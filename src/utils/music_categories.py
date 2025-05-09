from dataclasses import dataclass
from utils.theme import RetroTheme

@dataclass
class MusicCategory:
    title: str
    icon: str
    color: str
    description: str
    iframe_url: str

    @classmethod
    def get_samples(cls):
        return [
            cls(
                title="PIANO",
                icon="fa-music",
                color="#B76E79",  # Dusty Rose
                description="Relaxing piano melodies for sleep",
                iframe_url="https://www.iheart.com/playlist/piano-sleep-312064750-UQ4kiR72df8tWn9hH7qS5T/?embed=true"
            ),
            cls(
                title="LOFI",
                icon="fa-headphones",
                color="#7B8B6F",  # Sage Green
                description="Chill beats to study and relax",
                iframe_url="https://www.iheart.com/playlist/lofi-study-chill-312064750-K5raECjnp1NmvsgmQ37hh5/?embed=true"
            ),
            cls(
                title="CHRISTIAN RAP",
                icon="fa-music",
                color="#D4A373",  # Warm Taupe
                description="Uplifting Christian hip-hop",
                iframe_url="https://www.iheart.com/playlist/christian-rap-312064750-U3pqhYaQvG5PA5QM1f5HwF/?embed=true"
            ),
            cls(
                title="CHRISTIAN COUNTRY",
                icon="fa-guitar",
                color="#9B6B6E",  # Muted Burgundy
                description="Country gospel and worship",
                iframe_url="https://www.iheart.com/playlist/country-christian-312064750-DYThp2V5TSunwDZo6vpjUG/?embed=true"
            ),
            cls(
                title="BABY SLEEP",
                icon="fa-baby",
                color="#A5B4A4",  # Soft Mint
                description="Sweet lullabies for little ones",
                iframe_url="https://www.iheart.com/playlist/sweet-lullabies-312064750-SiRneSBGHJuqh3evTRN2Xy/?embed=true"
            ),
            cls(
                title="RELAX",
                icon="fa-spa",
                color="#C4A484",  # Muted Peach
                description="Ambient piano and nature sounds",
                iframe_url="https://www.iheart.com/playlist/ambient-piano-312064750-7mmKLmVhZgJ7DcqkUbTGai/?embed=true"
            )
        ] 