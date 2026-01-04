import streamlit as st
import pandas as pd
from utils import setup_page
from streamlit_extras.colored_header import colored_header
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "ai_agent", "Context", "tables")

setup_page("Skills", "🛠️")

# Custom CSS for Skills Page
st.markdown("""
<style>
    /* Skill Category Cards */
    .skill-category {
        background: white;
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        border-top: 4px solid;
        transition: transform 0.3s ease;
    }
    .skill-category:hover {
        transform: translateY(-3px);
    }
    .skill-category.ds { border-color: #8b5cf6; }
    .skill-category.ai { border-color: #ec4899; }
    .skill-category.bi { border-color: #06b6d4; }
    .skill-category.auto { border-color: #f59e0b; }
    .skill-category.remote { border-color: #10b981; }
    .skill-category.lang { border-color: #6366f1; }
    
    .skill-category h3 {
        font-size: 1.2rem;
        color: #1f2937;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .skill-list {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }
    
    .skill-tag {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        color: #0369a1;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        border: 1px solid #bae6fd;
        transition: all 0.2s ease;
    }
    .skill-tag:hover {
        background: linear-gradient(135deg, #0078d4 0%, #00a5a5 100%);
        color: white;
        border-color: transparent;
    }
    
    .skill-tag.primary {
        background: linear-gradient(135deg, #0078d4 0%, #00a5a5 100%);
        color: white;
        border: none;
    }
    
    /* Certifications Table Styling */
    .cert-header {
        background: linear-gradient(135deg, #1e3a5f 0%, #0d1b2a 100%);
        color: white;
        padding: 25px 30px;
        border-radius: 16px 16px 0 0;
        margin-bottom: 0;
    }
    .cert-header h3 {
        margin: 0;
        font-size: 1.3rem;
        color: white;
    }
    .cert-header p {
        margin: 5px 0 0 0;
        opacity: 0.8;
        font-size: 0.95rem;
    }
    
    /* Language Proficiency */
    .language-item {
        display: flex;
        align-items: center;
        gap: 15px;
        padding: 10px 0;
    }
    .language-name {
        font-weight: 600;
        color: #374151;
        min-width: 100px;
    }
    .language-level {
        background: #dbeafe;
        color: #1e40af;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("🛠️ Skills & Certifications")

colored_header(
    label="Technical Expertise",
    description="Technologies and tools I work with",
    color_name="blue-70",
)

# Skills Grid
col1, col2 = st.columns(2)

with col1:
    # Data Science & ML
    st.markdown("""
    <div class="skill-category ds">
        <h3>📊 Data Science & Machine Learning</h3>
        <div class="skill-list">
            <span class="skill-tag primary">Python</span>
            <span class="skill-tag primary">R</span>
            <span class="skill-tag primary">SQL</span>
            <span class="skill-tag">TensorFlow</span>
            <span class="skill-tag">PyTorch</span>
            <span class="skill-tag">Scikit-learn</span>
            <span class="skill-tag">Pandas</span>
            <span class="skill-tag">NumPy</span>
            <span class="skill-tag">Seaborn</span>
            <span class="skill-tag">Matplotlib</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Data Visualization & BI
    st.markdown("""
    <div class="skill-category bi">
        <h3>📈 Data Visualization & BI</h3>
        <div class="skill-list">
            <span class="skill-tag primary">Power BI</span>
            <span class="skill-tag">Folium</span>
            <span class="skill-tag">Strategic Dashboards</span>
            <span class="skill-tag">Executive Reports</span>
            <span class="skill-tag">Data Storytelling</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Remote Sensing
    st.markdown("""
    <div class="skill-category remote">
        <h3>🛰️ Remote Sensing & Environmental</h3>
        <div class="skill-list">
            <span class="skill-tag primary">Google Earth Engine</span>
            <span class="skill-tag">Remote Sensing</span>
            <span class="skill-tag">Atmospheric Analysis</span>
            <span class="skill-tag">Satellite Processing</span>
            <span class="skill-tag">Climate Modeling</span>
            <span class="skill-tag">Aerosol Analysis</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # AI & LLMs
    st.markdown("""
    <div class="skill-category ai">
        <h3>🤖 Artificial Intelligence & LLMs</h3>
        <div class="skill-list">
            <span class="skill-tag primary">LangChain</span>
            <span class="skill-tag primary">Agno</span>
            <span class="skill-tag">LLM Integration</span>
            <span class="skill-tag">Intelligent Agents</span>
            <span class="skill-tag">Reinforcement Learning</span>
            <span class="skill-tag">Prompt Engineering</span>
            <span class="skill-tag">Context Management</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Automation & Software
    st.markdown("""
    <div class="skill-category auto">
        <h3>⚙️ Automation & Software Engineering</h3>
        <div class="skill-list">
            <span class="skill-tag primary">Power Automate</span>
            <span class="skill-tag primary">Power Apps</span>
            <span class="skill-tag">GUI Development</span>
            <span class="skill-tag">ETL Pipelines</span>
            <span class="skill-tag">Systems Integration</span>
            <span class="skill-tag">Sharpley</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Languages
    st.markdown("""
    <div class="skill-category lang">
        <h3>🌐 Languages</h3>
        <div style="padding: 10px 0;">
            <div class="language-item">
                <span class="language-name">🇧🇷 Portuguese</span>
                <span class="language-level">Native</span>
            </div>
            <div class="language-item">
                <span class="language-name">🇺🇸 English</span>
                <span class="language-level">Full Professional Proficiency</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Certifications Section
st.markdown("<br>", unsafe_allow_html=True)

colored_header(
    label="Certifications",
    description="Professional development and continuous learning",
    color_name="violet-70",
)

st.markdown("""
<div class="cert-header">
    <h3>📜 Professional Certifications</h3>
    <p>Courses and certifications from recognized platforms</p>
</div>
""", unsafe_allow_html=True)

# Load and display certifications from CSV
try:
    df = pd.read_csv(os.path.join(DATA_DIR, "Certifications.csv"))
    df.columns = ["Course Title", "Certificate", "Course Link"]
    
    # Clean up the data
    df["Course Title"] = df["Course Title"].str.strip()
    
    # Create clickable links
    df["View Certificate"] = df["Certificate"].apply(
        lambda x: f'<a href="{x}" target="_blank">🔗 View</a>' if pd.notna(x) and x.strip() else "—"
    )
    df["Course Page"] = df["Course Link"].apply(
        lambda x: f'<a href="{x}" target="_blank">📚 Course</a>' if pd.notna(x) and x.strip() else "—"
    )
    
    # Display styled dataframe
    display_df = df[["Course Title", "View Certificate", "Course Page"]]
    
    st.markdown(
        display_df.to_html(escape=False, index=False),
        unsafe_allow_html=True
    )
    
except Exception as e:
    st.warning(f"Could not load certifications: {e}")
    
    # Fallback: Display hardcoded certifications
    st.markdown("""
    | Course | Platform |
    |--------|----------|
    | AI Agents Fundamentals | Hugging Face |
    | A/B Testing in Python | DataCamp |
    | Introduction to Data Ethics | DataCamp |
    | Reinforcement Learning with Gymnasium | DataCamp |
    | Deep Learning with PyTorch | DataCamp |
    | Power Apps: Business App Development | Udemy |
    | Supervised Learning with scikit-learn | DataCamp |
    | Santander Bootcamp 2023 - Data Science | DIO |
    | Data Manipulation with pandas | DataCamp |
    | Introduction to SQL | DataCamp |
    | Power BI Complete - Basic to Advanced | Udemy |
    """)
