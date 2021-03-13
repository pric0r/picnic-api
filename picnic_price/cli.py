"""CLI to pull prices form PicNic API."""

from pathlib import Path

import typer
from typer import Argument, Option
from python_picnic_api import PicnicAPI

from picnic_price.picnic import search_items
from picnic_price.utils import credentials_from_file, filter_cheapest_items


CREDENTIALS_PATH: Path = Path("secrets/credentials.json")

app = typer.Typer(
    no_args_is_help=True,
    add_completion=False,
)


@app.command()
def cheapest(
    search_term: str = Argument(..., help="Search term for product."),
    n: int = Option(default=5, help="Max. number of cheapest findings to show."),
    username: str = Option(None, help="Username of Picnic account."),
    password: str = Option(None, help="Password of Picnic account."),
    country_code: str = Option(default="DE", help="Country code of shop."),
):
    # connect to picnic api
    if (not username) or (not password):
        print("loading credentials from config file...")
        username, password, country_code = credentials_from_file(path=CREDENTIALS_PATH)
    picnic = PicnicAPI(username=username, password=password, country_code=country_code)
    # search items, filter cheapest
    items = search_items(picnic_api=picnic, term=search_term)
    cheapest_items = filter_cheapest_items(items=items, max_n=n)
    # format results
    for item in cheapest_items:
        print(f"* {item.name}: {item.unit_quantity_sub}")


def main():
    app()


if __name__ == "__main__":
    main()
