import dataclasses
from Options import OptionGroup, Toggle, PerGameCommonOptions


class BonusLevels(Toggle):
    """If the Bonus Levels should be included."""
    display_name = "Bonus Levels"

@dataclasses.dataclass()
class RhythmSproutOptions(PerGameCommonOptions):
    bonus_levels: BonusLevels

option_groups = [
    OptionGroup(
        "Test",
        [BonusLevels]
    )
]

option_presets = {
    "Test": {
        "bonus_levels": True
    }
}