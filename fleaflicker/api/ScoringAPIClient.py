from fleaflicker.api.FleaflickerAPIClient import FleaflickerAPIClient
from fleaflicker.enum.Sport import Sport


class ScoringAPIClient(FleaflickerAPIClient):

    @classmethod
    def get_league_boxscore(cls,
                            *,
                            sport: Sport = Sport.NFL,
                            league_id: int,
                            fantasy_game_id: int,
                            scoring_period: int = None) -> dict:
        filters = [("sport", sport.name), ("league_id", league_id), ("fantasy_game_id", fantasy_game_id)]
        cls._add_filter_if_given("scoring_period", scoring_period, filters)
        url = f"{cls._BASE_URL}{cls._LEAGUE_BOXSCORE_ROUTE}"
        url = cls._add_filters(url, *filters)
        return cls._get(url=url)

    @classmethod
    def get_league_rules(cls,
                         *,
                         sport: Sport = Sport.NFL,
                         league_id: int) -> dict:
        filters = [("sport", sport.name), ("league_id", league_id)]
        url = f"{cls._BASE_URL}{cls._LEAGUE_RULES_ROUTE}"
        url = cls._add_filters(url, *filters)
        return cls._get(url=url)
