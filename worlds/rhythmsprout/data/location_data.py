import dataclasses


@dataclasses.dataclass()
class LevelData:
    name: str
    region_index: int
    level_index: int


LevelDataTable = {
    "Broccoli Castle": LevelData(name="Broccoli Castle", region_index=0x1, level_index=0x01),
    "Autumn Fields": LevelData(name="Autumn Fields", region_index=0x1, level_index=0x02),
    "Winter Woods": LevelData(name="Winter Woods", region_index=0x1, level_index=0x03),
    "Haunted Mansion": LevelData(name="Haunted Mansion", region_index=0x1, level_index=0x04),
    "Mansion Dungeon": LevelData(name="Mansion Dungeon", region_index=0x1, level_index=0x05),
    "Count Arelle": LevelData(name="Count Arelle", region_index=0x1, level_index=0x06),
    "Jammin' Jungle": LevelData(name="Jammin' Jungle", region_index=0x1, level_index=0x07),
    "Fruitopia": LevelData(name="Fruitopia", region_index=0x1, level_index=0x08),
    "Gingerbread House": LevelData(name="Gingerbread House", region_index=0x1, level_index=0x09),
    "Candy Factory": LevelData(name="Candy Factory", region_index=0x1, level_index=0x0A),
    "Candy Mama": LevelData(name="Candy Mama", region_index=0x1, level_index=0x0B),
    "Candy Lane": LevelData(name="Candy Lane", region_index=0x1, level_index=0x0C),
    "Daddy Elevator": LevelData(name="Daddy Elevator", region_index=0x1, level_index=0x0D),
    "Daddy Club": LevelData(name="Daddy Club", region_index=0x1, level_index=0x0E),
    # "King Sugar Daddy": LevelData(name="King Sugar Daddy", region_index=0x1, level_index=0x0F),
    "Cloud Highway": LevelData(name="Cloud Highway", region_index=0x1, level_index=0x011),
    "Cauliflower Kingdom": LevelData(name="Cauliflower Kingdom", region_index=0x1, level_index=0x012),
    "Cauliflower Tower": LevelData(name="Cauliflower Tower", region_index=0x1, level_index=0x013),
    "K-FLOW": LevelData(name="K-FLOW", region_index=0x1, level_index=0x014),
    "K-FLOW Official Fan Club": LevelData(name="K-FLOW Official Fan Club", region_index=0x1, level_index=0x015),

    "Volcano Valley": LevelData(name="Volcano Valley", region_index=0x2, level_index=0x01),
    "Chili Inc": LevelData(name="Chili Inc", region_index=0x2, level_index=0x02),
    "Prison Escape": LevelData(name="Prison Escape", region_index=0x2, level_index=0x03),
    "Power Peppers": LevelData(name="Power Peppers", region_index=0x2, level_index=0x04),
    "Mrs Chili": LevelData(name="Mrs Chili", region_index=0x2, level_index=0x05),

    "Level 26": LevelData(name="Level 26", region_index=0x3, level_index=0x01),
    "Level 27": LevelData(name="Level 27", region_index=0x3, level_index=0x02),
    "Level 28": LevelData(name="Level 28", region_index=0x3, level_index=0x03),
    "Level 29": LevelData(name="Level 29", region_index=0x3, level_index=0x04),
    "Level 30": LevelData(name="Level 30", region_index=0x3, level_index=0x05),
}
