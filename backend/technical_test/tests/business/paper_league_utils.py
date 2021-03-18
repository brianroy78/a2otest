from typing import Tuple, Dict, List


class Constant:
    END: str = 'FIN'
    CAT_NAME_FORMAT_ERROR = 'incorrect format, %s is not a valid category name'
    RESULT_MATCH_FORMAT_ERROR = 'incorrect format, %s is not a valid result match'
    WINNER_POINTS = 2
    LOSER_POINTS = 1
    RESPONSE_TEMP = '\n %s %s'
    DRAW = 'EMPATE'


class Pair:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score


class GameData:
    def __init__(self, matches: int, results: Dict[str, Pair], champion_name, sub_champion_name):
        self.matches = matches
        self.results = results
        self.champion_name = champion_name
        self.sub_champion_name = sub_champion_name

    def update_champions(self, champion: str, sub_champion: str):
        self.champion_name = champion
        self.sub_champion_name = sub_champion

    def is_draw(self) -> bool:
        return self.results[self.champion_name].score == self.results[self.sub_champion_name].score

    def get_missing_matches(self) -> int:
        return get_missing_matches(len(self.results), self.matches)

    def update_results(self, winner_name: str, loser_name: str):
        self.results = add_points(add_points(self.results, winner_name, Constant.WINNER_POINTS), loser_name, Constant.LOSER_POINTS)

    def is_there_champion(self) -> bool:
        return len(self.champion_name) > 0

    def update_positions(self, winner_name: str, loser_name: str):
        champion: Pair = self.results[self.champion_name]
        sub_champion: Pair = self.results[self.sub_champion_name]
        if sub_champion.score > champion.score:
            champion, sub_champion = sub_champion, champion

        champion, sub_champion = compare(self.results[winner_name], champion, sub_champion)
        champion, sub_champion = compare(self.results[loser_name], champion, sub_champion)
        self.champion_name = champion.name
        self.sub_champion_name = sub_champion.name

    def get_final_name(self):
        return Constant.DRAW if self.is_draw() else self.champion_name

    def inc_matches(self):
        self.matches += 1


class Utils:

    @staticmethod
    def get_new_game():
        return GameData(0, dict(), '', '')

    @staticmethod
    def is_valid_category_name(name: str) -> bool:
        return is_valid_name(name) and ' ' not in name

    @staticmethod
    def is_valid_match_data(data: List[str]) -> bool:
        return len(data) == 4 and is_valid_name(data[0]) and is_valid_name(data[2]) and data[1].isnumeric() and data[3].isnumeric()

    @staticmethod
    def get_winner_loser_name(host_name: str, host_points: int, visitor_name: str, visitor_points: int) -> Tuple[str, str]:
        return (host_name, visitor_name) if host_points > visitor_points else (visitor_name, host_name)


def get_missing_matches(total_teams: int, total_matches: int) -> int:
    return ((total_teams - 1) * total_teams) - total_matches


def add_points(results: Dict[str, Pair], pair_name: str, points: int) -> Dict[str, Pair]:
    if pair_name not in results:
        results[pair_name] = Pair(pair_name, points)
    else:
        results[pair_name].score += points
    return results


def is_valid_name(name: str) -> bool:
    return 0 < len(name) < 17


def compare(new: Pair, first: Pair, second: Pair) -> Tuple[Pair, Pair]:
    if new.name == first.name or new.name == second.name:
        return first, second
    if new.score > first.score:
        return new, first
    if new.score > second.score:
        return first, new
    return first, second
