import streamlit as st
from utils import setup_page
from streamlit_extras.colored_header import colored_header

setup_page("About", "👤")

# Custom CSS for About Page
st.markdown("""
<style>
    /* About Section */
    .about-intro {
        background: linear-gradient(145deg, #f8fafc 0%, #ffffff 100%);
        border-radius: 20px;
        padding: 40px;
        margin-bottom: 30px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.06);
        border-left: 5px solid #0078d4;
    }
    .about-intro h2 {
        color: #0055a5;
        font-size: 1.8rem;
        margin-bottom: 20px;
    }
    .about-intro p {
        font-size: 1.05rem;
        line-height: 1.8;
        color: #374151;
        margin-bottom: 15px;
    }
    
    /* Philosophy Card */
    .philosophy-card {
        background: linear-gradient(135deg, #1e3a5f 0%, #0d1b2a 100%);
        color: white;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        margin: 30px 0;
    }
    .philosophy-card blockquote {
        font-size: 1.5rem;
        font-style: italic;
        margin-bottom: 15px;
        opacity: 0.95;
    }
    .philosophy-card .translation {
        font-size: 1.1rem;
        opacity: 0.8;
    }
    
    /* Contact/Links Grid */
    .links-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }
    .link-card {
        background: white;
        border-radius: 16px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        transition: all 0.3s ease;
        text-decoration: none;
        display: block;
        border: 2px solid transparent;
    }
    .link-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.12);
        border-color: #0078d4;
    }
    .link-card .icon {
        font-size: 2.5rem;
        margin-bottom: 15px;
    }
    .link-card h4 {
        color: #1f2937;
        font-size: 1.1rem;
        margin-bottom: 8px;
    }
    .link-card p {
        color: #6b7280;
        font-size: 0.9rem;
        margin: 0;
    }
    
    /* Interests Section */
    .interests-container {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        margin: 20px 0;
    }
    .interest-tag {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        color: #0369a1;
        padding: 12px 24px;
        border-radius: 25px;
        font-size: 1rem;
        font-weight: 500;
        border: 1px solid #bae6fd;
        display: flex;
        align-items: center;
        gap: 8px;
    }
</style>
""", unsafe_allow_html=True)

st.title("👤 About Me")

colored_header(
    label="Who I Am",
    description="Beyond the code and data",
    color_name="blue-70",
)

# About Intro
st.markdown("""
<div class="about-intro">
    <h2>Hello! I'm André Amorim 👋</h2>
    <p>
        I'm a <strong>Software Engineer and Data Scientist</strong> from Rio de Janeiro, Brazil, 
        passionate about the intersection of technology and real-world impact. My journey in tech 
        started with electronics and evolved into a deep fascination with artificial intelligence, 
        data science, and environmental applications.
    </p>
    <p>
        Currently, I'm pursuing my Bachelor's degree in <strong>Mathematical and Earth Sciences</strong> 
        at UFRJ (Federal University of Rio de Janeiro), where I combine my love for mathematics with 
        practical applications in atmospheric science and machine learning.
    </p>
    <p>
        What drives me is the belief that technology, when thoughtfully applied, can be a powerful 
        force for positive change. Whether it's optimizing business processes with AI, analyzing 
        satellite data to understand climate patterns, or building intelligent systems that make 
        complex tools accessible to everyone — I find joy in solving challenging problems.
    </p>
</div>
""", unsafe_allow_html=True)

# Philosophy Quote
st.markdown("""
<div class="philosophy-card">
    <blockquote>"Labor omnia vincit, per aspera ad astra."</blockquote>
    <p class="translation">Work conquers all, through hardships to the stars.</p>
</div>
""", unsafe_allow_html=True)

# Interests Section
colored_header(
    label="Interests & Passions",
    description="What I enjoy outside of work",
    color_name="green-70",
)

st.markdown("""
<div class="interests-container">
    <span class="interest-tag">🤖 AI & Machine Learning</span>
    <span class="interest-tag">🌍 Climate Science</span>
    <span class="interest-tag">📊 Data Visualization</span>
    <span class="interest-tag">🚀 Innovation</span>
    <span class="interest-tag">📚 Continuous Learning</span>
    <span class="interest-tag">🎮 Technology</span>
    <span class="interest-tag">🧠 Problem Solving</span>
    <span class="interest-tag">⚡ Automation</span>
</div>
""", unsafe_allow_html=True)

# Connect Section
colored_header(
    label="Let's Connect",
    description="Find me on these platforms",
    color_name="violet-70",
)

st.markdown("""
<div class="links-grid">
    <a href="https://www.linkedin.com/in/andr%C3%A9-amorim-73943bb7/" target="_blank" class="link-card">
        <div class="icon">💼</div>
        <h4>LinkedIn</h4>
        <p>Professional network & updates</p>
    </a>
    <a href="https://lattes.cnpq.br/9153087289739313" target="_blank" class="link-card">
        <div class="icon">📄</div>
        <h4>Lattes CV</h4>
        <p>Academic curriculum</p>
    </a>
    <a href="https://github.com" target="_blank" class="link-card">
        <div class="icon">💻</div>
        <h4>GitHub</h4>
        <p>Code & projects</p>
    </a>
    <a href="https://deepmath.tech/" target="_blank" class="link-card">
        <div class="icon">🚀</div>
        <h4>Deepmath</h4>
        <p>Current company</p>
    </a>
    <a href="https://lasa.ufrj.br/" target="_blank" class="link-card">
        <div class="icon">🛰️</div>
        <h4>LASA - UFRJ</h4>
        <p>Research laboratory</p>
    </a>
    <a href="https://www.bcmt.ufrj.br/" target="_blank" class="link-card">
        <div class="icon">🎓</div>
        <h4>BCMT - UFRJ</h4>
        <p>Academic program</p>
    </a>
</div>
""", unsafe_allow_html=True)

# Fun Facts
colored_header(
    label="Fun Facts",
    description="A few things about me",
    color_name="orange-70",
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="background: white; border-radius: 16px; padding: 25px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.06);">
        <div style="font-size: 2.5rem; margin-bottom: 10px;">🌍</div>
        <h4 style="color: #374151; margin-bottom: 5px;">Global Experience</h4>
        <p style="color: #6b7280; font-size: 0.9rem;">Worked remotely with teams in France and Brazil</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: white; border-radius: 16px; padding: 25px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.06);">
        <div style="font-size: 2.5rem; margin-bottom: 10px;">🔬</div>
        <h4 style="color: #374151; margin-bottom: 5px;">Research Background</h4>
        <p style="color: #6b7280; font-size: 0.9rem;">Published research on atmospheric sciences & AI</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background: white; border-radius: 16px; padding: 25px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.06);">
        <div style="font-size: 2.5rem; margin-bottom: 10px;">⚡</div>
        <h4 style="color: #374151; margin-bottom: 5px;">Tech Passion</h4>
        <p style="color: #6b7280; font-size: 0.9rem;">Started with electronics, evolved to AI</p>
    </div>
    """, unsafe_allow_html=True)