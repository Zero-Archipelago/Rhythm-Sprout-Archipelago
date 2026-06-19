from BaseClasses import Region
from .data.region_data import RegionDataTable

def create_and_connect_regions(world):
    new_regions = []
    for region_data in RegionDataTable:
        new_region = Region(region_data, world.player, world.multiworld)
        new_regions.append(new_region)
    world.multiworld.regions += new_regions

    for region in world.multiworld.regions:
        for exit in RegionDataTable[region.name].exits:
            region.connect(world.multiworld.get_region(exit, world.player))