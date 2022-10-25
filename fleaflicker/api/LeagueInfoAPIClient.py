from fleaflicker.api.FleaflickerAPIClient import FleaflickerAPIClient
from fleaflicker.enum.Sport import Sport


class LeagueInfoAPIClient(FleaflickerAPIClient):

    @classmethod
    def get_league_activity_feed(cls, *, sport: Sport = Sport.NFL, league_id: int, result_offset: int = None) -> dict:
        filters = [("sport", sport.name), ("league_id", league_id)]
        cls._add_filter_if_given("result_offset", result_offset, filters)
        url = f"{cls._BASE_URL}{cls._LEAGUE_ACTIVITY_ROUTE}"
        url = cls._add_filters(url, *filters)
        return cls._get(url=url)
