from fleaflicker.api.FleaflickerAPIClient import FleaflickerAPIClient
from fleaflicker.enum.Sport import Sport


class TeamAPIClient(FleaflickerAPIClient):

    @classmethod
    def get_roster(cls,
                   *,
                   sport: Sport = Sport.NFL,
                   league_id: int,
                   team_id: int,
                   season: int = None,
                   scoring_period: int = None,
                   external_id_type: list[str] = None) -> dict:
        filters = [("sport", sport.name), ("league_id", league_id), ("team_id", team_id)]
        cls._add_filter_if_given("season", season, filters)
        cls._add_filter_if_given("scoring_period", scoring_period, filters)
        cls._add_filter_if_given("external_id_type", external_id_type, filters, parse_value_as_list=True)
        url = f"{cls._BASE_URL}{cls._ROSTER_ROUTE}"
        url = cls._add_filters(url, *filters)
        return cls._get(url=url)
