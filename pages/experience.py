import streamlit as st
from utils import setup_page
from streamlit_extras.colored_header import colored_header

setup_page("Experience", "💼")

# Custom CSS for Experience Page
st.markdown("""
<style>
    /* Timeline Styling */
    .timeline-item {
        background: white;
        border-radius: 16px;
        padding: 30px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        border-left: 4px solid #0078d4;
        position: relative;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .timeline-item:hover {
        transform: translateX(5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.1);
    }
    .timeline-item .company {
        font-size: 1.3rem;
        font-weight: 700;
        color: #0055a5;
        margin-bottom: 5px;
    }
    .timeline-item .role {
        font-size: 1.1rem;
        color: #374151;
        font-weight: 500;
        margin-bottom: 8px;
    }
    .timeline-item .date-location {
        font-size: 0.9rem;
        color: #6b7280;
        margin-bottom: 15px;
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
    }
    .timeline-item .description {
        font-size: 0.98rem;
        line-height: 1.7;
        color: #4b5563;
        margin-bottom: 15px;
    }
    .timeline-item .achievements {
        background: #f0f9ff;
        border-radius: 10px;
        padding: 15px 20px;
        margin-bottom: 15px;
    }
    .timeline-item .achievements h4 {
        font-size: 0.9rem;
        color: #0369a1;
        margin-bottom: 10px;
    }
    .timeline-item .achievements ul {
        margin: 0;
        padding-left: 20px;
    }
    .timeline-item .achievements li {
        font-size: 0.9rem;
        color: #374151;
        margin-bottom: 5px;
    }
    .tech-stack {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }
    .tech-badge {
        background: linear-gradient(135deg, #0078d4 0%, #00a5a5 100%);
        color: white;
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    /* Education Card */
    .education-card {
        background: linear-gradient(145deg, #f8fafc 0%, #ffffff 100%);
        border-radius: 16px;
        padding: 25px 30px;
        margin-bottom: 20px;
        border-left: 4px solid #10b981;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .education-card .institution {
        font-size: 1.2rem;
        font-weight: 700;
        color: #047857;
        margin-bottom: 5px;
    }
    .education-card .degree {
        font-size: 1.05rem;
        color: #374151;
        font-weight: 500;
        margin-bottom: 5px;
    }
    .education-card .period {
        font-size: 0.9rem;
        color: #6b7280;
        margin-bottom: 12px;
    }
    .education-card .description {
        font-size: 0.95rem;
        color: #4b5563;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

st.title("💼 Professional Journey")

# Tabs for Professional, Academic Research, and Education
tab1, tab2, tab3 = st.tabs(["🏢 Professional Experience", "🔬 Academic Research", "🎓 Education"])

with tab1:
    colored_header(
        label="Professional Career",
        description="Industry experience in software engineering and technology",
        color_name="blue-70",
    )
    
    # Experience 1 - Deepmath (Current)
    st.markdown("""
    <div class="timeline-item">
        <div class="company">🚀 Deepmath</div>
        <div class="role">Software & AI Engineering Lead</div>
        <div class="date-location">
            <span>📅 December 2024 - Present</span>
            <span>📍 Rio de Janeiro, Brazil (Remote)</span>
        </div>
        <div class="description">
            Responsible for the redesign and modernization of the internal ecosystem of strategic applications, 
            including CRM and employee management software. Focus on performance, scalability, systemic integration, 
            and technical sustainability.
        </div>
        <div class="achievements">
            <h4>🏆 Key Achievements</h4>
            <ul>
                <li>Architectural modernization of critical business systems</li>
                <li>AI integration in sales and management processes</li>
                <li>Implementation of solutions connecting strategy and technology</li>
            </ul>
        </div>
        <div class="tech-stack">
            <span class="tech-badge">Python</span>
            <span class="tech-badge">AI/ML</span>
            <span class="tech-badge">Software Architecture</span>
            <span class="tech-badge">LangChain</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Experience 2 - S4Sys
    st.markdown("""
    <div class="timeline-item">
        <div class="company">⚡ S4Sys</div>
        <div class="role">Power Platform Developer & Innovation Specialist</div>
        <div class="date-location">
            <span>📅 April 2024 - November 2024 (8 months)</span>
            <span>📍 Rio de Janeiro, Brazil (Hybrid)</span>
        </div>
        <div class="description">
            Innovation and Automation Specialist responsible for designing and implementing solutions that drive 
            process modernization and operational efficiency. Built insightful business reports using Power BI, 
            empowering data-driven decision-making.
        </div>
        <div class="achievements">
            <h4>🏆 Key Achievements</h4>
            <ul>
                <li>Automations that significantly reduced manual processes</li>
                <li>BI dashboards for strategic decision support</li>
                <li>AI integration into engineering systems</li>
            </ul>
        </div>
        <div class="tech-stack">
            <span class="tech-badge">Power Platform</span>
            <span class="tech-badge">Power BI</span>
            <span class="tech-badge">Power Automate</span>
            <span class="tech-badge">Python</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Experience 3 - Deepmath (Software Engineer)
    st.markdown("""
    <div class="timeline-item">
        <div class="company">🔧 Deepmath</div>
        <div class="role">Software Engineer</div>
        <div class="date-location">
            <span>📅 January 2024 - April 2024 (4 months)</span>
            <span>📍 Nantes, France (Remote)</span>
        </div>
        <div class="description">
            Software Engineer in Intelligent Engineering Systems Development. Development of intuitive and efficient 
            GUIs with strong focus on enhancing user experience. Led initiatives for building intelligent agents 
            aimed at automating GUI interactions.
        </div>
        <div class="achievements">
            <h4>🏆 Key Achievements</h4>
            <ul>
                <li>GUI development for complex engineering systems</li>
                <li>Workflow automation through intelligent agents</li>
                <li>Advanced computational geometry manipulation</li>
            </ul>
        </div>
        <div class="tech-stack">
            <span class="tech-badge">Python</span>
            <span class="tech-badge">GUI Development</span>
            <span class="tech-badge">Sharpley</span>
            <span class="tech-badge">Automation</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Experience 4 - Deepmath (R&D AI)
    st.markdown("""
    <div class="timeline-item">
        <div class="company">🧠 Deepmath</div>
        <div class="role">R&D in Artificial Intelligence</div>
        <div class="date-location">
            <span>📅 May 2023 - December 2023 (8 months)</span>
            <span>📍 Nantes, France (Remote)</span>
        </div>
        <div class="description">
            Research and Development in AI, implementing advanced AI and Machine Learning methods for engineering 
            simulations, including Computational Fluid Dynamics (CFD) and mesh generation. Developed the Engineering 
            Assistant (EA), an AI system for democratizing CFD simulations.
        </div>
        <div class="achievements">
            <h4>🏆 Key Achievements</h4>
            <ul>
                <li>Development of Engineering Assistant (EA) for CFD democratization</li>
                <li>Implementation of reinforcement learning for mesh optimization</li>
                <li>Advanced statistical analysis of engineering simulations</li>
            </ul>
        </div>
        <div class="tech-stack">
            <span class="tech-badge">PyTorch</span>
            <span class="tech-badge">TensorFlow</span>
            <span class="tech-badge">Machine Learning</span>
            <span class="tech-badge">CFD</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Experience 5 - PBGseg
    st.markdown("""
    <div class="timeline-item">
        <div class="company">🔌 PBGseg</div>
        <div class="role">Electronics Technician</div>
        <div class="date-location">
            <span>📅 June 2019 - March 2023 (3 years 10 months)</span>
            <span>📍 Rio de Janeiro, Brazil</span>
        </div>
        <div class="description">
            Installation and management of electronic security systems, including fire alarms and CCTV. 
            Risk analysis and specification of security equipment for corporate and residential environments.
        </div>
        <div class="tech-stack">
            <span class="tech-badge">Electronics</span>
            <span class="tech-badge">CCTV</span>
            <span class="tech-badge">Fire Systems</span>
            <span class="tech-badge">Risk Analysis</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    colored_header(
        label="Academic Research Experience",
        description="Research positions and academic projects",
        color_name="violet-70",
    )
    
    # CNPq/LASA
    st.markdown("""
    <div class="timeline-item">
        <div class="company">🛰️ CNPq (LASA - UFRJ)</div>
        <div class="role">Undergraduate Research Fellow</div>
        <div class="date-location">
            <span>📅 December 2022 - April 2024 (1 year 5 months)</span>
            <span>📍 Rio de Janeiro, Brazil (Hybrid)</span>
        </div>
        <div class="description">
            Data analyst in remote sensing at the Laboratory of Environmental Satellite Applications (LASA), 
            conducting research on satellite data analysis for atmospheric behavior monitoring. Research crucial 
            for meteorology and air quality understanding.
        </div>
        <div class="achievements">
            <h4>🏆 Key Achievements</h4>
            <ul>
                <li>Atmospheric data analysis for aerosol monitoring</li>
                <li>Contribution to air quality and climate change research</li>
                <li>Application of remote sensing and spatial analysis techniques</li>
            </ul>
        </div>
        <div class="tech-stack">
            <span class="tech-badge">Python</span>
            <span class="tech-badge">R</span>
            <span class="tech-badge">Google Earth Engine</span>
            <span class="tech-badge">Power BI</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # UFRJ Smart Cities
    st.markdown("""
    <div class="timeline-item">
        <div class="company">🏙️ UFRJ - Smart Cities Extension</div>
        <div class="role">Data Scientist</div>
        <div class="date-location">
            <span>📅 September 2022 - May 2023 (9 months)</span>
            <span>📍 Rio de Janeiro, Brazil (Remote)</span>
        </div>
        <div class="description">
            Initiative of the Institute of Mathematics at UFRJ serving as a bridge between companies and academia, 
            proposing state-of-the-art solutions for challenging business problems using data science and machine learning.
        </div>
        <div class="tech-stack">
            <span class="tech-badge">Pandas</span>
            <span class="tech-badge">Scikit-Learn</span>
            <span class="tech-badge">XGBoost</span>
            <span class="tech-badge">Power BI</span>
            <span class="tech-badge">Folium</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # LACPEX
    st.markdown("""
    <div class="timeline-item">
        <div class="company">🌪️ UFRJ (LACPEX)</div>
        <div class="role">Data Analyst</div>
        <div class="date-location">
            <span>📅 June 2022 - May 2023 (1 year)</span>
            <span>📍 Rio de Janeiro, Brazil</span>
        </div>
        <div class="description">
            Laboratory for Short-Term Forecasting and Extreme Events. Applied AI techniques (supervised and 
            unsupervised learning) to identify atmospheric characteristics associated with extreme meteorological events.
        </div>
        <div class="tech-stack">
            <span class="tech-badge">R</span>
            <span class="tech-badge">Python</span>
            <span class="tech-badge">Statistics</span>
            <span class="tech-badge">Data Visualization</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    colored_header(
        label="Education",
        description="Academic foundation and formal degrees",
        color_name="green-70",
    )
    
    # UFRJ
    st.markdown("""
    <div class="education-card">
        <div class="institution">🎓 UFRJ - Federal University of Rio de Janeiro</div>
        <div class="degree">Bachelor's Degree in Mathematical and Earth Sciences</div>
        <div class="period">📅 March 2019 - Present (Expected completion)</div>
        <div class="description">
            Multidisciplinary education with focus on applied mathematics, data science, remote sensing, 
            and technological innovation. Academic research in atmospheric analysis, extreme weather events, 
            and AI applications in meteorology.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Technical School
    st.markdown("""
    <div class="education-card">
        <div class="institution">🔧 Visconde de Mauá State Technical School</div>
        <div class="degree">Integrated Technical Degree in Electronics</div>
        <div class="period">📅 January 2009 - December 2013</div>
        <div class="description">
            Technical training in electronics, embedded systems, and industrial automation. 
            Foundation in hardware, circuit design, and electronic systems integration.
        </div>
    </div>
    """, unsafe_allow_html=True)
