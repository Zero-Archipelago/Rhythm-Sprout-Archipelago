from typing import Any, Dict

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld


class RhythmSproutWebWorld(WebWorld):
    game_info_languages: list[str] = ["en"]
    item_descriptions: list[str] = []
    location_descriptions: list[str] = []
    options_page: bool | str = True
    options_presets: Dict[str, Dict[str, Any]] = {}
    theme: str = "grass"
    tutorials: list[Tutorial] = []
