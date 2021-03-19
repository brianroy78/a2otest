from typing import Tuple, List


def parse_data(text: str) -> Tuple[int, int, int, int, List[Tuple[int, int]]]:
    data = text.split('\n')
    n, k = data.pop(0).split(' ')
    rq, cq = data.pop(0).split(' ')
    obstacles: List[Tuple[int, int]] = list()
    for obs in data:
        if obs == '\n' or len(obs) == 0:
            continue
        row, col = obs.split(' ')
        obstacles.append((int(row), int(col)))
    return int(n), int(k), int(rq), int(cq), obstacles


class Point:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col


def same_diagonal(a: Point, b: Point) -> bool:
    return abs(a.row - a.col) == abs(b.row - b.col) or a.row + a.col == b.row + b.col


def greater_than(a: Point, b: Point) -> bool:
    return to_scalar(a) > to_scalar(b)


def lower_than(a: Point, b: Point) -> bool:
    return to_scalar(a) < to_scalar(b)


def to_scalar(a: Point) -> int:
    return a.row * (a.col - 1) + a.row


def same_row(a: Point, b: Point) -> bool:
    return a.row == b.row


def same_col(a: Point, b: Point) -> bool:
    return a.col == b.col


def get_left_up(a: Point, dim: int) -> Point:
    total = a.row + a.col
    return Point(
        dim if total > dim else total,
        0 if total < dim else abs(dim - total)
    )


def get_left_down(a: Point) -> Point:
    return Point(
        0 if a.col >= a.row else (a.row - a.col),
        0 if a.col <= a.row else (a.col - a.row)
    )


def get_right_up(a: Point, dim: int) -> Point:
    return Point(
        dim if a.col <= a.row else a.row + (dim - a.col),
        dim if a.col >= a.row else a.col + (dim - a.row)
    )


def get_right_down(a: Point, dim: int) -> Point:
    total = a.row + a.col
    return Point(
        0 if total < dim else total - dim,
        dim if total > dim else total
    )
