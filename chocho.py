from pathlib import Path
import time
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "profile-pic.png"
resume_file = current_dir / "assets" / "CV.pdf"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Pavel Chocholouš"
PAGE_ICON = ":wave:"
NAME = "Pavel Chocholouš"
DESCRIPTION = """
Skilled DBA, troubleshooter & DB developer with extensive experience in automation, monitoring, tuning, and MSSQL. Passionate about developing people and communities.
"""
EMAIL = "pavel@chocholous.net"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/pavel-chocholous/",
    "GitHub": "https://github.com/pavel242242/digital-resume-template-streamlit",
    "Twitter": "https://twitter.com/pavel242",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores":
    "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database":
    "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar":
    "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel":
    "https://pythonandvba.com/mytoolbelt/",
}
SECTIONS = {
    "Professional Summary": "Summary",
    "Experience": "Exp",
    "Tech stack": "Hard-skills",
    "Career history": "CV",
    "Portfolio": "Projects",
    "Community Involvement": "Community",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- LOAD PDF ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- PROFILE PIC ---
profile_pic = Image.open(profile_pic)

with st.sidebar:
    my_radio = st.radio("Navigation", list(SECTIONS.keys()))
    awesomeness_level = st.slider("Awesomeness Level", 0, 10, 0)
    experience_level = st.slider("Experience Level", 0, 20, 10)
    show_email = st.checkbox("Show Email", True)
    select_project = st.selectbox("Select a Project", list(PROJECTS.keys()))

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    if show_email:
        st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

if my_radio == "Professional Summary":
    # --- PROFESSIONAL SUMMARY ---
    st.write('\n')
    st.subheader("Professional Summary")
    st.write("""
    Skilled DBA, troubleshooter & DB developer. Most of my career is connected with automation, monitoring, tuning, MSSQL, small/medium/big data. But people are more important than technology, finding, hiring, developing, mentoring, leading them, all that. Being honest. Open. Unbiased. Dedicated. Work-hard, play-hard. Passionate about communities.
    """)

if my_radio == "Experience":
    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Experience & Qualifications")
    st.write(f"""
    - ✔️ {experience_level} years experience in automation, monitoring, tuning, and MSSQL
    - ✔️ Strong hands-on experience and knowledge in data management and analysis
    - ✔️ Proven track record in team leadership and mentoring
    - ✔️ Passionate about community involvement and development
    """)

if my_radio == "Tech stack":
    # --- SKILLS ---
    st.write('\n')
    st.subheader("Tech Stack")
    st.write("""
    - 👩‍💻 Programming: Python, SQL, VBA, Powershell
    - 📊 Tools: Octopus Deploy, TeamCity, Git, Graphite, Grafana, VictorOps, Power BI
    - 🗄️ Databases: MSSQL, Postgres, Hadoop, Hive, Pig, Redshift, BigQuery
    """)

if my_radio == "Career history":
    # --- WORK HISTORY ---
    st.write('\n')
    st.subheader("Career History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**DataOps, DBA & Data Security Guru**")
    st.write("2020")
    st.write("""
    - ► Tools: Git, Powershell, Graphite, Grafana, VictorOps, MSSQL/SSAS, JIRA, Power BI, CDH, Postgres
    - ► Tasks: Operations, high availability, integration of custom monitoring, decommissioning, people care
    - ► Teams: Prague (2 ETL devs), Brno (3-4 DBAs), USA (1 DBA)
    """)

    # --- JOB 2
    st.write('\n')
    st.write("🚧", "**DBA Team Lead, Data Architect**")
    st.write("2017 - 2020")
    st.write("""
    - ► Tools: MSSQL/SSAS, Postgres, CitusDB, Hadoop, Hive, Pig, Redshift, BigQuery
    - ► Tasks: Event data, DWH, DM, Data Acquisition
    - ► Team: DAQ Team Lead (2-3 devs + myself)
    """)

    # --- JOB 3
    st.write('\n')
    st.write("🚧", "**Data Architect, Analyst, Principal, DBA, Data Acquisition TL**")
    st.write("2013 - 2017")
    st.write("""
    - ► Tools: MSSQL 2005/2012, SSIS, SSAS, SSRS
    - ► Tasks: Reports for sales, finance (IFRS), user activity
    """)

    # --- JOB 4
    st.write('\n')
    st.write("🚧", "**ETL Developer, DBA, Data Analyst, Reporting**")
    st.write("2010 - 2013")
    st.write("""
    - ► Companies: Self-employed, contact centers, GE Money Bank
    - ► Tools: MSSQL, Avaya, CTI, ASP, PHP, VB.NET, PL/SQL
    - ► Tasks: SW development, WIN, Linux, Telephony admin, business analysis, vendor management
    """)

if my_radio == "Portfolio":
    # --- Projects & Accomplishments ---
    st.write('\n')
    st.subheader("Projects & Accomplishments")
    st.write("---")
    st.write(f"[{select_project}]({PROJECTS[select_project]})")

if my_radio == "Community Involvement":
    # --- COMMUNITY INVOLVEMENT ---
    st.write('\n')
    st.subheader("Community Involvement")
    st.write("---")
    st.write("""
    - **CzechPass**: Co-founder/Co-organizer - grew group to biggest MS Data Platform event in CZ and regular monthly off-line meetups
    - **Czechitas**: Mentor, Lector, Coach, Product Developer, Fundraiser - from mentoring wannabe junior data analysts to preparing a full SQL crash course in SnowFlake
    - **Prague Data Punkers**: Speaker, evangelist
    - **TestStack**: Dots connector
    - **Prague DevOps Days**: Dogsbody
    - **Prague Postgres Developers**: Member
    """)

# --- ADDING AWESOMENESS ---
for i in range(awesomeness_level + 1):
    awesomeness_level = i
    with st.sidebar:
        st.write("🎉" * i)
    time.sleep(0.2)
