from docsumo.config import settings
from dataclasses import dataclass


def get_csv_file_path_for_name(file_name: str) -> str:
    dir_path = settings.CSV_DIR_PATH
    if not dir_path.endswith("/"):
        dir_path = f"{dir_path}/"
    file_path = dir_path + file_name
    return file_path


@dataclass
class Rectangle:
    x1: int
    y1: int
    x2: int
    y2: int


def is_rectangle_in_inside_inner_rectangle(
        outer_rect: Rectangle, inner_rect: Rectangle
) -> bool:
    # NOTE: I am also assuming that each rectangle is defined by two points in the
    # upper left ((x1|y1)) and lower right corner ((x2|y2)) and that your rectangles
    # are not rotated.
    return (
            outer_rect.x1 <= inner_rect.x1 <= inner_rect.x2 <= outer_rect.x2
            and outer_rect.y1 <= inner_rect.y1 <= inner_rect.y2 <= outer_rect.y2
    )
