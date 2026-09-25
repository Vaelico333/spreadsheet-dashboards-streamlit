import streamlit as st
import json

def dashboards_app() -> None:
    def create_original_tab(name: str) -> None:
        "Create the tabs for the original projects"
        col_img, col_txt = st.columns(2)
        with col_img:
            with open("./files.json", encoding="UTF-8") as file:
                links_dict = json.load(file)

            st.image(f"./img/dashboard_{name}.png", link=f"{links_dict[name]['link']}")
            st.write("*Click on the picture to go to the original file*")
        with col_txt:
            with st.expander("**About this dashboard**"):

                with open(f"./text/{name}.md", encoding="UTF-8") as f:
                    text_project = f.read()

                sections = text_project.split("---")
                st.write(sections[0], unsafe_allow_html=True)
                sections_titles = {"**Overview**":"🔭", 
                                "**The Dashboard**":"📊", 
                                "**Business Intelligence**":"💶", 
                                "**What I learned**":"📝"}
                index = 1
                for title, icon in sections_titles.items():
                    with st.expander(label=title, icon=icon, type="step"):
                        st.write(sections[index], unsafe_allow_html=True)
                        index += 1

    @st.cache_data
    def create_python_tab(name: str) -> None:
        "Create a tab for the Python dashboard"
        st.header(f"Python {name} dashboard")
        pass

    def create_main_tab(name: str, tab) -> None:
        "Create the main tab"
        tabs_dict = {"excel":
                    {"music":"Music streaming services study", 
                    "netflix":"Netflix users study", 
                    "sales":"Cosmetics Sales Study"
                    },
                    "gs":
                    {"perfumes":"Perfumes sales study", 
                    "churn":"Internet Service churn study"
                    }}
        with tab:
            with open(f"./text/front_{name}.md", encoding="UTF-8") as file:
                write_text = file.read()
                st.write(write_text)
            projects_selector = st.menu_button(label="Available projects", 
                                    options=list(tabs_dict[name].values()),
                                    key=f"menu_{name}",
                                    type="primary")

            for subtab_name, subtab_title in tabs_dict[name].items():
                if subtab_title == projects_selector:
                    original_tab, python_tab = st.tabs(["Original project", "Python version"])
                    with original_tab:
                        create_original_tab(subtab_name)
                    with python_tab:
                        create_python_tab(subtab_name)
            if not projects_selector:
                subtab_name = list(tabs_dict[name].keys())[0]
                original_tab, python_tab = st.tabs(["Original project", "Python version"])
                with original_tab:
                    create_original_tab(subtab_name)
                with python_tab:
                    create_python_tab(subtab_name)

    favicon = "./img/logo.png"
    st.set_page_config(
        page_title="Spreadsheets into Python dashboards", 
        page_icon= favicon,
        layout="wide",
        )
    st.title(body='📊 From Excel to Python 🐍: Creating a modern Dashboard')

    tab_excel, tab_gs = st.tabs(
        ["Excel", "Google Sheets"], 
        on_change="rerun")
    create_main_tab(name="excel", tab=tab_excel)
    create_main_tab(name="gs", tab=tab_gs)

if __name__ == '__main__':
    dashboards_app()