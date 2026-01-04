# Main app:
"""
Main app page - Professional Portfolio Landing Page
"""

import streamlit as st
from streamlit_extras.colored_header import colored_header
from utils import render_navbar, load_css, render_sidebar_chat

# Setup page
st.set_page_config(page_title="André Amorim | Software Engineer & AI Specialist", page_icon="🚀", layout="wide")
load_css()
render_sidebar_chat()

# Custom CSS for enhanced landing page
st.markdown("""
<style>
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #0055a5 0%, #00a5a5 100%);
        color: white;
        padding: 60px 40px;
        border-radius: 0 0 30px 30px;
        margin: -1rem -1rem 2rem -1rem;
        text-align: center;
    }
    .hero-section h1 {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 10px;
        color: white;
    }
    .hero-section .subtitle {
        font-size: 1.3rem;
        opacity: 0.95;
        margin-bottom: 20px;
    }
    .hero-section .tagline {
        font-size: 1rem;
        opacity: 0.85;
        font-style: italic;
    }
    
    /* Social Links */
    .social-links {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 25px;
    }
    .social-links a {
        background: rgba(255,255,255,0.2);
        color: white;
        padding: 12px 24px;
        border-radius: 25px;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .social-links a:hover {
        background: rgba(255,255,255,0.35);
        transform: translateY(-2px);
    }
    
    /* Summary Card */
    .summary-card {
        background: linear-gradient(145deg, #ffffff 0%, #f8fafc 100%);
        border-left: 5px solid #0078d4;
        border-radius: 16px;
        padding: 35px 40px;
        margin: 30px 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.08);
    }
    .summary-card h2 {
        color: #0055a5;
        font-size: 1.6rem;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .summary-card p {
        font-size: 1.05rem;
        line-height: 1.8;
        color: #374151;
        margin-bottom: 16px;
    }
    
    /* Highlight Cards */
    .highlights-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }
    .highlight-card {
        background: white;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        border-top: 4px solid;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .highlight-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }
    .highlight-card.ai { border-color: #8b5cf6; }
    .highlight-card.data { border-color: #06b6d4; }
    .highlight-card.research { border-color: #10b981; }
    .highlight-card h3 {
        font-size: 1.1rem;
        margin-bottom: 10px;
        color: #1f2937;
    }
    .highlight-card p {
        font-size: 0.95rem;
        color: #6b7280;
        line-height: 1.6;
    }
    
    /* Philosophy Quote */
    .philosophy-quote {
        background: linear-gradient(135deg, #1e3a5f 0%, #0d1b2a 100%);
        color: white;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        margin: 40px 0;
    }
    .philosophy-quote blockquote {
        font-size: 1.4rem;
        font-style: italic;
        margin-bottom: 15px;
        opacity: 0.95;
    }
    .philosophy-quote .translation {
        font-size: 1rem;
        opacity: 0.75;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1>André Amorim</h1>
    <p class="subtitle">Software Engineer & AI Specialist</p>
    <p class="tagline">Transforming businesses through Artificial Intelligence and Digital Innovation</p>
    <div class="social-links">
        <a href="https://www.linkedin.com/in/andr%C3%A9-amorim-73943bb7/" target="_blank">
            🔗 LinkedIn
        </a>
        <a href="https://lattes.cnpq.br/9153087289739313" target="_blank">
            📄 Lattes CV
        </a>
        <a href="https://github.com/Baldros" target="_blank">
            💻 GitHub
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# Render Navbar (after hero)
render_navbar()

# Executive Summary Section
colored_header(
    label="Executive Summary",
    description="Building intelligent solutions for real-world challenges",
    color_name="blue-70",
)

st.markdown("""
<div class="summary-card">
    <h2>👋 About Me</h2>
    <p>
        Software Engineer and Data Scientist specialized in the intersection of <strong>Artificial Intelligence</strong>, 
        <strong>business automation</strong>, and <strong>digital transformation</strong>. With consolidated experience 
        in R&D of intelligent systems, I work on modernizing corporate ecosystems, integrating high-performance AI 
        solutions into strategic applications such as CRM and management systems.
    </p>
    <p>
        My professional trajectory combines solid technical expertise in <strong>Python</strong>, <strong>Machine Learning</strong>, 
        and <strong>Microsoft Power Platform</strong> with deep knowledge in environmental data analysis and remote sensing, 
        resulting from academic research at the Laboratory of Environmental Satellite Applications (LASA-UFRJ).
    </p>
    <p>
        Currently, I lead architectural redesign initiatives for legacy systems at <strong>Deepmath</strong>, focusing on 
        scalability, technical sustainability, and intelligent agent integration. Previously, I worked as an Innovation 
        and Automation Specialist at <strong>S4Sys</strong>, developing complex automations and BI reports that drove 
        operational efficiency.
    </p>
</div>
""", unsafe_allow_html=True)

# Highlights Section
colored_header(
    label="Core Expertise",
    description="Key areas where I deliver impact",
    color_name="blue-70",
)

st.markdown("""
<div class="highlights-container">
    <div class="highlight-card ai">
        <h3>🤖 Artificial Intelligence & LLMs</h3>
        <p>Development of intelligent agents, LLM integration, and machine learning solutions for engineering and business applications.</p>
    </div>
    <div class="highlight-card data">
        <h3>📊 Data Science & Analytics</h3>
        <p>Advanced analytics, predictive modeling, and business intelligence dashboards that drive strategic decision-making.</p>
    </div>
    <div class="highlight-card research">
        <h3>🌍 Environmental Research</h3>
        <p>Remote sensing, atmospheric analysis, and climate modeling using satellite data and AI techniques.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Philosophy Quote
st.markdown("""
<div class="philosophy-quote">
    <blockquote>"Labor omnia vincit, per aspera ad astra."</blockquote>
    <p class="translation">Work conquers all, through hardships to the stars.</p>
</div>
""", unsafe_allow_html=True)
