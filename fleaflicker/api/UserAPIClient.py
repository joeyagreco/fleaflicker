from fleaflicker.api.FleaflickerAPIClient import FleaflickerAPIClient
from fleaflicker.enum.Sport import Sport


class UserAPIClient(FleaflickerAPIClient):

    @classmethod
    def get_user_leagues(cls,
                         *,
                         sport: Sport = Sport.NFL,
                         user_id: int = None,
                         email: str = None,
                         season: int = None) -> dict:
        filters = [("sport", sport.name)]
        cls._add_filter_if_given("user_id", user_id, filters)
        cls._add_filter_if_given("email", email, filters)
        cls._add_filter_if_given("season", season, filters)
        url = f"{cls._BASE_URL}{cls._USER_LEAGUES_ROUTE}"
        url = cls._add_filters(url, *filters)
        return cls._get(url=url)

    @classmethod
    def get_team_picks(cls,
                       *,
                       sport: Sport = Sport.NFL,
                       league_id: int,
                       team_id: int = None) -> dict:
        filters = [("sport", sport.name), ("league_id", league_id)]
        cls._add_filter_if_given("team_id", team_id, filters)
        url = f"{cls._BASE_URL}{cls._TEAM_PICKS_ROUTE}"
        url = cls._add_filters(url, *filters)
        return cls._get(url=url)
