import pandas as pd
import streamlit as st
import os

from src.repository import Content


class Application:
    def __init__(self, content: Content) -> None:
        self.content = content

    def configure_page(self) -> None:
        st.set_page_config(
            page_title=self.content.TITLE, page_icon=self.content.MY_AVATAR_SRC
        )

        yandex_metric_script = os.getenv("YANDEX_METRIC_SCRIPT", "")
        st.components.v1.html(yandex_metric_script, height=0)

        hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    def header(self) -> None:
        col1, col2 = st.columns(2)
        col1.image(self.content.MY_AVATAR_SRC)
        col2.header(self.content.TITLE)
        col2.text(self.content.POSITION)
        st.markdown(self.content.PREVIEW)
        st.divider()

    def metrics(self) -> None:
        st.header("My progress in metrics")
        col1, col2, col3 = st.columns(3)
        for n, metric in enumerate(self.content.METRICS):
            if n % 2 == 0:
                col1.metric(metric.name, metric.value, metric.delta, help=metric.info)
            else:
                col2.metric(metric.name, metric.value, metric.delta, help=metric.info)
        st.divider()

    def story(self) -> None:
        st.header("Story")
        st.write(self.content.SMALL_STORY)

    def education(self) -> None:
        st.header("Education")
        for education in self.content.EDUCATIONS:
            st.text(education.university.value)
            col1, col2, col3, col4 = st.columns(4)
            col1.text(education.level.value)
            col2.text(education.program.value)
            col3.text(education.since_to)
            col4.text("With honor? " + str(education.with_honor))

    def work(self) -> None:
        st.header("Work")
        for work_experience in self.content.WORK_EXPERIENCE:
            col1, col2, col3, col4 = st.columns(4)
            st.text(work_experience.employer.company.value)
            col2.text(work_experience.employer.place.value)
            col3.text(work_experience.employer.type.value)
            col4.text("# Empl. = " + str(work_experience.employer.cnt_employees))
            col2.text(work_experience.position.value)
            col4.text(work_experience.since_to)
            col1, _, _ = st.columns(3)
            col1.divider()

    def papers(self) -> None:
        st.header("Papers")
        for paper in self.content.PAPERS:
            st.markdown(f"[{paper.name} – {paper.year}]({paper.link})")

    def conferences(self) -> None:
        st.header("Conferences")
        df = pd.DataFrame(self.content.CONFERENCES).sort_values(by=["year", "month"])
        st.dataframe(df, hide_index=True)

    def contacts(self) -> None:
        st.header("Contact with me")
        st.markdown(f"[Send me a letter by using email]({self.content.EMAIL})")
        col1, col2, col3 = st.columns(3)
        col1.markdown(f"[LinkedIn]({self.content.LINKEDIN_LINK})")
        col2.markdown(f"[GitHub]({self.content.GITHUB_LINK})")
        col3.markdown(f"[Telegram]({self.content.TELEGRAM_LINK})")

    def run(self, *args, **kwargs) -> None:
        self.configure_page()
        self.header()
        self.metrics()
        self.story()
        self.education()
        self.work()
        self.papers()
        self.conferences()
        self.contacts()
