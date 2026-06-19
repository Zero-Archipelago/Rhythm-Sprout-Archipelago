from BaseClasses import ItemClassification
import dataclasses

@dataclasses.dataclass()
class ItemData:
    name: str
    amount: int
    code: int
    classification: ItemClassification

ItemDataTable = {
    "Star": ItemData(name="Star", amount=203, code=0x100, classification=ItemClassification.progression)
}