from .data.location_data import LevelDataTable
from BaseClasses import Location

region_to_id = {
    "Main Story": 0x1,
    "Prequel Story": 0x2,
    "Bonus Levels": 0x3
}

index_to_subname = {
    1: "cleared",
    2: "Score Star 1",
    3: "Score Star 2",
    4: "Score Star 3",
    5: "Combo Star 1",
    6: "Combo Star 2",
    7: "Combo Star 3",
}

LOCATION_NAME_TO_ID = {
    f"{level.name} {subname}": 0x100 + i * 7 + j
    for i, level in enumerate(LevelDataTable.values())
    for j, subname in enumerate(index_to_subname.values())
}

class RhythmSproutLocation(Location):
    game: str = "RHYTHM SPROUT"


def create_all_locations(world):
    regions = {
        0x1: world.get_region("Main Story"),
        0x2: world.get_region("Prequel Story"),
        0x3: world.get_region("Bonus Levels"),
    }

    for level in LevelDataTable.values():
        region = regions[level.region_index]

        locations = {
            f"{level.name} {subname}": LOCATION_NAME_TO_ID[f"{level.name} {subname}"]
            for subname in index_to_subname.values()
        }

        region.add_locations(locations, RhythmSproutLocation)