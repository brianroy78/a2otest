from typing import List, Tuple

from tests.business.chess_utils import Point, same_diagonal, greater_than, lower_than, same_row, same_col, get_left_up, get_left_down, get_right_up, get_right_down


def solve_chess(dimension: int, k: int, queen_row: int, queen_col: int, obstacles_positions: List[Tuple[int, int]]) -> int:
    queen: Point = Point(queen_row, queen_col)
    left: int = 0
    right: int = dimension + 1
    up: int = dimension + 1
    down: int = 0
    left_up: Point = get_left_up(queen, dimension + 1)
    left_down: Point = get_left_down(queen)
    right_up: Point = get_right_up(queen, dimension + 1)
    right_down: Point = get_right_down(queen, dimension + 1)

    for obstacle_pos in obstacles_positions:
        obstacle: Point = Point(obstacle_pos[0], obstacle_pos[1])
        if same_row(queen, obstacle) and queen.col > obstacle.col > left:
            left = obstacle.col
            continue

        if same_row(queen, obstacle) and queen.col < obstacle.col < right:
            right = obstacle.col
            continue

        if same_col(queen, obstacle) and queen.row < obstacle.row < up:
            up = obstacle.row
            continue

        if same_col(queen, obstacle) and queen.row > obstacle.row > down:
            down = obstacle.row
            continue

        if same_diagonal(queen, obstacle) and queen.col > obstacle.col and queen.row < obstacle.row and lower_than(obstacle, left_up):
            left_up = obstacle
            continue

        if same_diagonal(queen, obstacle) and queen.col > obstacle.col and queen.row > obstacle.row and greater_than(obstacle, left_down):
            left_down = obstacle
            continue

        if same_diagonal(queen, obstacle) and queen.col < obstacle.col and queen.row < obstacle.row and lower_than(obstacle, right_up):
            right_up = obstacle
            continue

        if same_diagonal(queen, obstacle) and queen.col < obstacle.col and queen.row > obstacle.row and greater_than(obstacle, right_down):
            right_down = obstacle
            continue

    return ((right - left) - 2) + ((up - down) - 2) + ((right_down.col - left_up.col) - 2) + ((right_up.col - left_down.col) - 2)
