"""Test schema models."""

from picnic_price.schema import calculate_eur_per_kg


def test_calculate_eur_per_kg():
    assert calculate_eur_per_kg("1.50€/kg") == 1.5
    assert calculate_eur_per_kg("1.50€/100g") == 15.0
