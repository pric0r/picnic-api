"""Model schemas."""

from pydantic import BaseModel


def calculate_eur_per_kg(unit_quantity_sub: str) -> float:
    price, unit = unit_quantity_sub.split("€/")
    if unit == "kg":
        return float(price)
    if unit == "L":
        return float(price)
    if unit == "100g":
        return float(price) * 10


class Item(BaseModel):
    name: str
    unit_quantity_sub: str

    @property
    def eur_per_kg(self):
        return calculate_eur_per_kg(self.unit_quantity_sub)
