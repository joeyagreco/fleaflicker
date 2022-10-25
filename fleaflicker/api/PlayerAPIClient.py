from fleaflicker.api.FleaflickerAPIClient import FleaflickerAPIClient
from fleaflicker.enum.Sport import Sport


class PlayerAPIClient(FleaflickerAPIClient):

    @classmethod
    def get_players(cls,
                    *,
                    sport: Sport = Sport.NFL,
                    league_id: int) -> dict:
        # TODO: add filters: https://www.fleaflicker.com/api-docs/index.html#/definitions/ws.flea.api.FetchLeagueActivityResponse
        filters = [("sport", sport.name), ("league_id", league_id)]
        url = f"{cls._BASE_URL}{cls._PLAYER_LISTING_ROUTE}"
        url = cls._add_filters(url, *filters)
        return cls._get(url=url)
