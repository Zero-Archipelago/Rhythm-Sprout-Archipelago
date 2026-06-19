import dataclasses

@dataclasses.dataclass()
class RegionData:
    name: str
    region_index: int
    locations: list[str] | str
    exits: list[str] | str

RegionDataTable = {
    "Menu": RegionData(name="Menu", region_index=0x0, locations=[], exits=["Main Story", "Prequel Story", "Bonus Levels"]),
    "Main Story": RegionData(name="Main Story", region_index=0x1, locations=[], exits=[]),
    "Prequel Story": RegionData(name="Prequel Story", region_index=0x1, locations=[], exits=[]),
    "Bonus Levels": RegionData(name="Bonus Levels", region_index=0x1, locations=[], exits=[])
}