from pathlib import Path
import time
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Jane Doe"
PAGE_ICON = ":wave:"
NAME = "Jane Doe"
DESCRIPTION = """
Recent graduate of the Czechitas Digital Academy Data, transitioning from marketing to data analytics, passionate about leveraging data to drive business decisions.
"""
EMAIL = "janedoe@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/janedoe/",
    "GitHub": "https://github.com/janedoe/data-portfolio",
    "Twitter": "https://twitter.com/janedoe",
}
PROJECTS = {
    "Sales Dashboard - Comparing sales across three stores":
    "https://youtu.be/Sb0A9i6d320",
    "Income and Expense Tracker - Web app with NoSQL database":
    "https://youtu.be/3egaMfE9388",
    "Desktop Application - Excel2CSV converter with user settings & menubar":
    "https://youtu.be/LzCfNanQ_9c",
    "MyToolBelt - Custom MS Excel add-in to combine Python & Excel":
    "https://pythonandvba.com/mytoolbelt/",
}
SECTIONS = {
    "Experience": "Experience",
    "Tech stack": "Tech stack",
    "Graduation Project": "Graduation Project",
    "Job Interests": "Job Interests",
    "Projects": "Projects",
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
    my_radio = st.radio("Select Section", list(SECTIONS.keys()))
    awesomeness_level = st.slider("Awesomeness Level", 0, 10, 0)
    excitement_level = st.slider("Excitement Level", 0, 10, 0)
    st.text(f"Your excitement level is at {excitement_level * 10}%!")

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
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

if my_radio == "Experience":
    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Previous Experience")
    st.write("""
    - ✔️ 5 years experience in Marketing, specializing in digital campaigns and customer engagement.
    - ✔️ Strong analytical skills and experience with market research and data-driven strategies.
    - ✔️ Proven ability to work cross-functionally and deliver results in a fast-paced environment.
    """)

if my_radio == "Tech stack":
    # --- TECH STACK ---
    st.write('\n')
    st.subheader("Tech Stack")
    st.write("""
    - 👩‍💻 Programming: Python (Pandas, Scikit-learn), SQL
    - 📊 Data Visualization: Power BI, MS Excel, Plotly
    - 📚 Modeling: Logistic regression, linear regression, decision trees
    - 🗄️ Databases: Postgres, MongoDB, MySQL
    """)

if my_radio == "Graduation Project":
    # --- GRADUATION PROJECT ---
    st.write('\n')
    st.subheader("Graduation Project")
    st.write("""
    **Project Title: Customer Segmentation Analysis**
    - Developed a comprehensive customer segmentation analysis for a retail company.
    - Utilized clustering techniques to identify distinct customer segments.
    - Collaborated with a team of three classmates and worked closely with the retail company to ensure the project's relevance and impact.
    - Presented findings to company stakeholders, providing actionable insights for targeted marketing strategies.
    """)

if my_radio == "Job Interests":
    # --- JOB INTERESTS ---
    st.write('\n')
    st.subheader("Job Interests")
    st.write("""
    Jane is currently seeking opportunities in:
    - Data Analyst roles within the tech industry.
    - Business Intelligence positions in retail or finance sectors.
    - Junior Data Scientist roles where she can apply and further develop her skills.
    - Companies that value continuous learning and professional development.
    """)

if my_radio == "Projects":
    # --- PROJECTS & ACCOMPLISHMENTS ---
    st.write('\n')
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[🏆 {project}]({link})")

# --- FUN ELEMENTS ---
for i in range(awesomeness_level + 1):
    awesomeness_level = i
    with st.sidebar:
        st.write("🎉" * i)
    time.sleep(0.2)

# --- FUN ELEMENT 2: ANIMATED PROGRESS BAR ---
progress_bar = st.sidebar.progress(0)
for percent_complete in range(101):
    time.sleep(0.05)
    progress_bar.progress(percent_complete)

# --- FUN ELEMENT 3: DYNAMIC MESSAGE ---
dynamic_message = st.sidebar.empty()
for i in range(awesomeness_level + 1):
    dynamic_message.text(f"Awesomeness level: {i}")
    time.sleep(0.2)