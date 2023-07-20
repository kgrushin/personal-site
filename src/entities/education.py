from dataclasses import dataclass
from enum import Enum


class Universities(str, Enum):
    FINANCIAL = "Financial University under the Government of the Russian Federation"
    MOSCOW_AVIATION = "Moscow Aviation University"


class EducationLevels(str, Enum):
    BACHELOR = "Bachelor's degree"
    MASTER = "Master's degree"


class EducationDirections(str, Enum):
    MANAGEMENT = "Management in aviation industry (Economy)"
    CS = "Computer Science and Math (ML, DL etc.)"


@dataclass
class Education:
    university: Universities
    level: EducationLevels
    program: EducationDirections
    since_to: str
    with_honor: bool
