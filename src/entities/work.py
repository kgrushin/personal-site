from dataclasses import dataclass
from enum import Enum

from src.entities.geo import Cities


class Positions(str, Enum):
    JUNIOR_DATA_SCIENTIST = "Junior Data Scientist"
    MIDDLE_DATA_SCIENTIST = "Middle Data Scientist"
    LEAD_DATA_SCIENTIST = "Lead Data Scientist"


class CompanyTypes(str, Enum):
    BANK = "BANK"
    IT = "IT"


class Companies(str, Enum):
    OTKRITIE = "Otkritie"
    RENAISSANCE = "Renaissance"
    BIN_BANK = "BinBank"
    VTB = "VTB"
    RUSSIAN_STANDARD = "Russian Standard"


@dataclass
class Employer:
    company: Companies
    type: CompanyTypes
    cnt_employees: int
    place: Cities


class Employers(Enum):
    VTB = Employer(Companies.VTB, CompanyTypes.BANK, 50_000, Cities.MOSCOW)
    OTKRITIE = Employer(Companies.OTKRITIE, CompanyTypes.BANK, 30_000, Cities.MOSCOW)
    BIN_BANK = Employer(Companies.BIN_BANK, CompanyTypes.BANK, 10_000, Cities.MOSCOW)
    RENAISSANCE = Employer(
        Companies.RENAISSANCE, CompanyTypes.BANK, 5_000, Cities.MOSCOW
    )
    RUSSIAN_STANDARD = Employer(
        Companies.RUSSIAN_STANDARD, CompanyTypes.BANK, 10_000, Cities.MOSCOW
    )


@dataclass
class WorkExperience:
    employer: Employer
    position: Positions
    since_to: str


@dataclass
class Conference:
    name: str
    organizer: Companies
    subject: str
    month: str
    year: str
    place: Cities
    cnt_participant: int
