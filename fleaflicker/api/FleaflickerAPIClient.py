from abc import ABC
from typing import Optional, Any

import requests

from fleaflicker.util.ConfigReader import ConfigReader


class FleaflickerAPIClient(ABC):
    """
    Should be inherited by all API Clients.
    Fleaflicker API Documentation: https://www.fleaflicker.com/api-docs/index.html
    """
    _BASE_URL = ConfigReader.get("api", "BASE_URL")

    # ROUTES
    _LEAGUE_ACTIVITY_ROUTE = ConfigReader.get("api", "LEAGUE_ACTIVITY_ROUTE")

    @classmethod
    def _build_route(cls, base_url: str, *args) -> str:
        args = (str(arg).replace("/", "") for arg in args)
        return f"{base_url}/{'/'.join(args)}"

    @classmethod
    def _add_filters(cls, url: str, *args) -> str:
        """
        Adds filters to the given url.
        """
        if len(args) > 0:
            symbol = "?"
            for i, arg in enumerate(args):
                if i > 0:
                    symbol = "&"
                url = f"{url}{symbol}{arg[0]}={arg[1]}"
        return url

    @staticmethod
    def _add_filter_if_given(key: str, value: Optional[Any], filter_list: list[tuple[str, Any]]):
        """
        Helper method for adding filters.
        """
        if value is not None:
            filter_list.append((key, value))

    @staticmethod
    def _get(url: str) -> dict:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
