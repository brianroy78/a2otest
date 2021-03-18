from typing import List

from tests.business.paper_league_utils import Constant, GameData, Utils


def solve_paper_league(data: str) -> str:
    game_data: GameData = Utils.get_new_game()
    is_processing: bool = False
    output: str = ''

    for line_ in data.split("\n"):
        line: str = line_.strip()
        if line == '\n' or len(line) == 0:
            continue

        if line == Constant.END:
            output += Constant.RESPONSE_TEMP % (game_data.get_final_name(), game_data.get_missing_matches())
            is_processing = False
            continue

        if not is_processing:
            if not Utils.is_valid_category_name(line):
                return Constant.CAT_NAME_FORMAT_ERROR % line
            is_processing = True
            game_data: GameData = Utils.get_new_game()
            continue

        if is_processing:
            game_data.inc_matches()
            match_data: List[str] = line.split(' ')
            if not Utils.is_valid_match_data(match_data):
                return Constant.RESULT_MATCH_FORMAT_ERROR % line

            winner_name, loser_name = Utils.get_winner_loser_name(*match_data)
            game_data.update_results(winner_name, loser_name)
            if not game_data.is_there_champion():
                game_data.update_champions(winner_name, loser_name)
            else:
                game_data.update_positions(winner_name, loser_name)
    return output
