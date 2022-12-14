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

    @classmethod
    def get_draft_board(cls,
                        *,
                        sport: Sport = Sport.NFL,
                        league_id: int,
                        season: int,
                        draft_number: int = None,
                        external_id_type: list[str] = None) -> dict:
        filters = [("sport", sport.name), ("league_id", league_id), ("season", season)]
        cls._add_filter_if_given("draft_number", draft_number, filters)
        cls._add_filter_if_given("external_id_type", external_id_type, filters, parse_value_as_list=True)
        url = f"{cls._BASE_URL}{cls._LEAGUE_DRAFT_BOARD_ROUTE}"
        url = cls._add_filters(url, *filters)
        return cls._get(url=url)

    @classmethod
    def get_league_rosters(cls,
                           *,
                           sport: Sport = Sport.NFL,
                           league_id: int,
                           season: int = None,
                           scoring_period: int = None,
                           external_id_type: list[str] = None) -> dict:
        filters = [("sport", sport.name), ("league_id", league_id)]
        cls._add_filter_if_given("season", season, filters)
        cls._add_filter_if_given("scoring_period", scoring_period, filters)
        cls._add_filter_if_given("external_id_type", external_id_type, filters, parse_value_as_list=True)
        url = f"{cls._BASE_URL}{cls._LEAGUE_ROSTERS_ROUTE}"
        url = cls._add_filters(url, *filters)
        return cls._get(url=url)

    @classmethod
    def get_league_standings(cls,
                             *,
                             sport: Sport = Sport.NFL,
                             league_id: int,
                             season: int = None) -> dict:
        filters = [("sport", sport.name), ("league_id", league_id)]
        cls._add_filter_if_given("season", season, filters)
        url = f"{cls._BASE_URL}{cls._LEAGUE_STANDINGS_ROUTE}"
        url = cls._add_filters(url, *filters)
        return cls._get(url=url)

    @classmethod
    def get_league_transactions(cls,
                                *,
                                sport: Sport = Sport.NFL,
                                league_id: int,
                                team_id: int = None,
                                result_offset: int = None) -> dict:
        filters = [("sport", sport.name), ("league_id", league_id)]
        cls._add_filter_if_given("team_id", team_id, filters)
        cls._add_filter_if_given("result_offset", result_offset, filters)
        url = f"{cls._BASE_URL}{cls._LEAGUE_TRANSACTIONS_ROUTE}"
        url = cls._add_filters(url, *filters)
        return cls._get(url=url)

    @classmethod
    def get_trades(cls,
                   *,
                   sport: Sport = Sport.NFL,
                   league_id: int) -> dict:
        # TODO: add filters https://www.fleaflicker.com/api-docs/index.html#/definitions/ws.flea.api.FetchLeagueActivityResponse
        filters = [("sport", sport.name), ("league_id", league_id)]
        url = f"{cls._BASE_URL}{cls._TRADES_ROUTE}"
        url = cls._add_filters(url, *filters)
        return cls._get(url=url)
