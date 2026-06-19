from BaseClasses import Item, ItemClassification
from .data.item_data import ItemDataTable

class RhythmSproutItem(Item):
    game: str = "RHYTHM SPROUT"

def get_random_filler_item_name() -> str:
    filler_list = ["Nothing"]
    return filler_list[0]

def create_all_items(world):
    item_pool: list[RhythmSproutItem] = []
    for item_data in ItemDataTable:
        for _ in range(ItemDataTable[item_data].amount):
            item_pool.append(world.create_item(item_data))

    number_of_items = len(item_pool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    item_pool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += item_pool

def create_item_with_correct_classification(world, name: str) -> RhythmSproutItem:
    classification = ItemDataTable[name].classification
    code = ItemDataTable[name].code

    return RhythmSproutItem(name=name, classification=classification, code=code, player=world.player)