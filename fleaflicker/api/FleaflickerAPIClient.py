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
    _LEAGUE_BOXSCORE_ROUTE = ConfigReader.get("api", "LEAGUE_BOXSCORE_ROUTE")
    _LEAGUE_DRAFT_BOARD_ROUTE = ConfigReader.get("api", "LEAGUE_DRAFT_BOARD_ROUTE")
    _LEAGUE_ROSTERS_ROUTE = ConfigReader.get("api", "LEAGUE_ROSTERS_ROUTE")
    _LEAGUE_RULES_ROUTE = ConfigReader.get("api", "LEAGUE_RULES_ROUTE")
    _LEAGUE_SCOREBOARD_ROUTE = ConfigReader.get("api", "LEAGUE_SCOREBOARD_ROUTE")
    _LEAGUE_STANDINGS_ROUTE = ConfigReader.get("api", "LEAGUE_STANDINGS_ROUTE")

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
    def _add_filter_if_given(key: str, value: Optional[Any], filter_list: list[tuple[str, Any]], **kwargs):
        """
        Helper method for adding filters.
        """
        parse_value_as_list: bool = kwargs.pop("parse_value_as_list", False)
        if value is not None:
            if parse_value_as_list is True:
                for v in value:
                    filter_list.append((key, v))
            else:
                filter_list.append((key, value))

    @staticmethod
    def _get(url: str) -> dict:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
