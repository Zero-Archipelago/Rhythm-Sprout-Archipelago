from worlds.AutoWorld import World
from .items import create_all_items, create_item_with_correct_classification, RhythmSproutItem
from .locations import create_all_locations
from .options import RhythmSproutOptions
from .regions import create_and_connect_regions
from .rules import set_rules
from .web_world import RhythmSproutWebWorld


class RhythmSproutWorld(World):
    """Description here"""
    game = "RHYTHM SPROUT"
    web = RhythmSproutWebWorld()

    item_name_to_id = {}
    location_name_to_id = {}

    options_dataclass = RhythmSproutOptions
    options: RhythmSproutOptions

    required_client_version = (0, 6, 7)

    def create_regions(self):
        create_and_connect_regions(self)
        create_all_locations(self)

    def create_items(self):
        create_all_items(self)

    def create_item(self, name: str) -> RhythmSproutItem:
        return create_item_with_correct_classification(world=self, name=name)

    def set_rules(self):
        set_rules(self)
