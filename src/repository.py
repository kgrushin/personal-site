from dataclasses import dataclass, field
from pathlib import Path

from src.entities.education import (
    Education,
    Universities,
    EducationLevels,
    EducationDirections,
)
from src.entities.geo import Cities
from src.entities.metrics import Metric
from src.entities.papers import Paper
from src.entities.work import (
    Employers,
    Conference,
    WorkExperience,
    Positions,
    Companies,
)


@dataclass
class Content:
    TITLE: str = "Konstantin Grushin"
    POSITION: str = "Data Scientist / Developer (Full-stack)"
    PREVIEW: str = """
    Hi {user}! I'm glad to see you on my personal website!
    Here you're able to:
    - [:scroll: Read small story about me](#story)
    - [:school: Get know with my education](#education)
    - [:trophy: Have a look at my work experience](#work)
    - [:page_with_curl: Meet my papers (mostly in Russian :flag-ru:)](#papers)
    - [:briefcase: Conferences I've participated as a speaker](#conferences)
    - [:mailbox: Contact with me](#contact-with-me)
    """

    STATIC_IMAGES_FOLDER: Path = Path("static/images/")
    MY_AVATAR_SRC: str = str(STATIC_IMAGES_FOLDER / Path("avatar.jpeg"))

    SMALL_STORY: str = """
    I’ve been completely into the sphere of information technology and computer science since my childhood. 
    Now I am Master of Mathematics and Computer Science. I also received my bachelor’s in management. 
    All of my education has been completed with honour. I believe this shows how diligent I am in my work. 

    I have developed plenty of machine learning models. In most cases creating table models with custom approaches 
    to select the best solution. However, I spent a great amount of time learning how to develop NLP and CV models 
    at university. 
    
    I have a strong knowledge of developing modern API using Python. I have been learning JavaScript and 
    frontend technologies and I am convinced that learning a new language reinforces and 
    strengthens the skills one already possesses. 
    
    I am forever curious about low-level programming, for instance, 
    what hides behind different protocols and high-level programming languages.
    """

    CONFERENCES: list[Conference] = field(
        default_factory=lambda: [
            Conference(
                "WorkShop",
                Companies.RENAISSANCE,
                "10",
                "2019",
                "Is Optimal Binning a good idea?",
                Cities.MOSCOW,
                30,
            ),
            Conference(
                "WorkShop",
                Companies.OTKRITIE,
                "06",
                "2022",
                "JupyterLab. How to use all possibilities?",
                Cities.MOSCOW,
                30,
            ),
            Conference(
                "ComDS",
                Companies.VTB,
                "06",
                "2023",
                "What's better: boosting vs linear models?",
                Cities.MOSCOW,
                50,
            ),
            Conference(
                "ComDS",
                Companies.VTB,
                "07",
                "2023",
                "Talks about classic ML Pipeline",
                Cities.MOSCOW,
                50,
            ),
        ]
    )

    WORK_EXPERIENCE: list[WorkExperience] = field(
        default_factory=lambda: [
            WorkExperience(
                Employers.BIN_BANK.value,
                Positions.JUNIOR_DATA_SCIENTIST,
                "2018/09 - 2019/01",
            ),
            WorkExperience(
                Employers.RUSSIAN_STANDARD.value,
                Positions.JUNIOR_DATA_SCIENTIST,
                "2019/01 - 2019/06",
            ),
            WorkExperience(
                Employers.RENAISSANCE.value,
                Positions.MIDDLE_DATA_SCIENTIST,
                "2019/06 - 2020/02",
            ),
            WorkExperience(
                Employers.OTKRITIE.value,
                Positions.MIDDLE_DATA_SCIENTIST,
                "2020/02 - 2022/02",
            ),
            WorkExperience(
                Employers.OTKRITIE.value,
                Positions.LEAD_DATA_SCIENTIST,
                "2022/02 - CURRENT",
            ),
            WorkExperience(
                Employers.VTB.value,
                Positions.LEAD_DATA_SCIENTIST,
                "2023/05 - CURRENT (Part-Time)",
            ),
        ]
    )

    EDUCATIONS: list[Education] = field(
        default_factory=lambda: [
            Education(
                Universities.MOSCOW_AVIATION,
                EducationLevels.BACHELOR,
                EducationDirections.MANAGEMENT,
                "2015/09 - 2019/06",
                with_honor=True,
            ),
            Education(
                Universities.FINANCIAL,
                EducationLevels.MASTER,
                EducationDirections.CS,
                "2019/09 - 2021/06",
                with_honor=True,
            ),
        ]
    )

    PAPERS: list[Paper] = field(
        default_factory=lambda: [
            Paper(
                "Make catalog of ML features better",
                "https://habr.com/ru/companies/otkritie/articles/718240/",
                2023,
            ),
            Paper(
                "ML pipeline for classic bank models",
                "https://habr.com/ru/companies/otkritie/articles/725928/",
                2023,
            ),
            Paper(
                "Using Gradient Boosting to improve model effectiveness",
                "https://habr.com/ru/companies/otkritie/articles/738618/",
                2023,
            ),
        ]
    )

    STATIC_FILES_FOLDER: Path = Path("static/files/")
    MY_CV_RU_SRC: str = str(STATIC_FILES_FOLDER / Path("CV_grushin_ke_ru.pdf"))
    MY_CV_EN_SRC: str = str(STATIC_FILES_FOLDER / Path("CV_grushin_ke_en.pdf"))

    GITHUB_LINK: str = "https://github.com/kgrushin"
    LINKEDIN_LINK: str = "https://www.linkedin.com/in/kgrushin/"
    TELEGRAM_LINK: str = "https://t.me/kgrushin"
    EMAIL: str = "mailto:k.e.grushin@gmail.com"

    def __post_init__(self) -> None:
        self.METRICS: list[Metric] = [
            Metric(
                "Educations",
                len(self.EDUCATIONS),
                len(self.EDUCATIONS),
                "How many levels of education I graduated",
            ),
            Metric("Papers", len(self.PAPERS), len(self.PAPERS), info=None),
            Metric(
                "Conferences",
                len(self.CONFERENCES),
                len(self.CONFERENCES),
                "Conferences I participated in as a speaker",
            ),
            Metric("Worked years", 4, 4, info=None),
            Metric("Models developed", 32, 32, info=None),
            Metric(
                "Mentored",
                12,
                12,
                "How many people I've mentored and helped to grow (my teammates)",
            ),
        ]
