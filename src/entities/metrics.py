from dataclasses import dataclass
from typing import Optional


@dataclass
class Metric:
    name: str
    value: int
    delta: Optional[int]
    info: Optional[str]
