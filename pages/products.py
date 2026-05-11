import streamlit as st
from utils import setup_page
from streamlit_extras.colored_header import colored_header

setup_page("Products", "�")

# Custom CSS for Products Landing Page
st.markdown("""
<style>
    /* Hero Section */
    .product-hero {
        background: linear-gradient(135deg, #1f4775 0%, #2f6f89 100%);
        color: white;
        padding: 60px 50px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 40px;
        position: relative;
        overflow: hidden;
    }
    .product-hero::before {
        display: none;
    }
    .product-hero h1 {
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 15px;
        color: white;
        position: relative;
        z-index: 1;
    }
    .product-hero .tagline {
        font-size: 1.4rem;
        opacity: 0.9;
        margin-bottom: 30px;
        position: relative;
        z-index: 1;
    }
    .product-hero .description {
        font-size: 1.1rem;
        color: rgba(255,255,255,0.86);
        max-width: 700px;
        margin: 0 auto 30px auto;
        line-height: 1.7;
        position: relative;
        z-index: 1;
    }
    
    /* Download Button */
    .download-btn {
        display: inline-block;
        background: linear-gradient(135deg, #0078d4 0%, #00a5a5 100%);
        color: white;
        padding: 18px 50px;
        border-radius: 50px;
        font-size: 1.2rem;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(0,120,212,0.4);
        position: relative;
        z-index: 1;
    }
    .download-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0,120,212,0.5);
        color: white;
    }
    .download-info {
        margin-top: 15px;
        font-size: 0.9rem;
        color: rgba(255,255,255,0.76);
        position: relative;
        z-index: 1;
    }
    
    /* Feature Cards */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 25px;
        margin: 40px 0;
    }
    .feature-card {
        background: white;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border-top: 4px solid;
    }
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 45px rgba(0,0,0,0.12);
    }
    .feature-card.files { border-color: #8b5cf6; }
    .feature-card.youtube { border-color: #ef4444; }
    .feature-card.gmail { border-color: #f59e0b; }
    .feature-card.calendar { border-color: #10b981; }
    .feature-card.drive { border-color: #06b6d4; }
    .feature-card.web { border-color: #ec4899; }
    
    .feature-card .icon {
        font-size: 2.5rem;
        margin-bottom: 15px;
    }
    .feature-card h3 {
        font-size: 1.2rem;
        color: #1f2937;
        margin-bottom: 12px;
    }
    .feature-card p {
        font-size: 0.95rem;
        color: #6b7280;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    .feature-card .capability-list {
        font-size: 0.85rem;
        color: #374151;
    }
    .feature-card .capability-list li {
        margin-bottom: 5px;
    }
    
    /* Tech Stack */
    .tech-section {
        background: linear-gradient(145deg, #f8fafc 0%, #ffffff 100%);
        border-radius: 20px;
        padding: 40px;
        margin: 40px 0;
        text-align: center;
    }
    .tech-section h3 {
        color: #1f2937;
        margin-bottom: 25px;
        font-size: 1.3rem;
    }
    .tech-badges {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 12px;
    }
    .tech-badge {
        background: linear-gradient(135deg, #0078d4 0%, #00a5a5 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 25px;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    /* Requirements Section */
    .requirements {
        background: #f0f9ff;
        border-radius: 16px;
        padding: 25px 30px;
        margin: 30px 0;
        border-left: 4px solid #0078d4;
    }
    .requirements h4 {
        color: #0055a5;
        margin-bottom: 15px;
    }
    .requirements ul {
        margin: 0;
        padding-left: 20px;
        color: #374151;
    }
    .requirements li {
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="product-hero">
    <h1>🤖 Atlas Desktop</h1>
    <p class="tagline">Your Intelligent Desktop Assistant</p>
    <p class="description">
        A powerful AI-powered assistant that seamlessly integrates with your file system, 
        Google services, YouTube, and the web. Automate tasks, find information, and boost 
        your productivity with natural language commands.
    </p>
    <a href="Atlas.exe" download class="download-btn">
        ⬇️ Download for Windows
    </a>
    <p class="download-info">Version 1.0 • Windows 10/11 • ~50 MB</p>
</div>
""", unsafe_allow_html=True)

# Features Section
colored_header(
    label="Powerful Capabilities",
    description="Everything you need in one intelligent assistant",
    color_name="blue-70",
)

st.html("""
<div class="features-grid">
    <div class="feature-card files">
        <div class="icon">🗂️</div>
        <h3>File System Management</h3>
        <p>Navigate, search, and organize your files with natural language commands.</p>
        <ul class="capability-list">
            <li>🔍 Search files across all drives</li>
            <li>📁 Create files and folder structures</li>
            <li>📊 View disk space and file details</li>
            <li>✅ Verify file existence and properties</li>
        </ul>
    </div>
    
    <div class="feature-card youtube">
        <div class="icon">🎥</div>
        <h3>YouTube Integration</h3>
        <p>Extract insights from videos without leaving your desktop.</p>
        <ul class="capability-list">
            <li>🔎 Search videos by keywords</li>
            <li>📝 Extract transcriptions and captions</li>
            <li>💬 Read video comments</li>
            <li>⬇️ Download videos for offline viewing</li>
        </ul>
    </div>
    
    <div class="feature-card gmail">
        <div class="icon">📧</div>
        <h3>Gmail Access</h3>
        <p>Stay on top of your inbox with intelligent email management.</p>
        <ul class="capability-list">
            <li>📬 List and filter emails by status</li>
            <li>📖 Read email content</li>
            <li>👤 Filter by sender</li>
            <li>📊 Analyze email patterns</li>
        </ul>
    </div>
    
    <div class="feature-card calendar">
        <div class="icon">📅</div>
        <h3>Google Calendar</h3>
        <p>Manage your schedule with voice-like natural commands.</p>
        <ul class="capability-list">
            <li>📋 View upcoming events</li>
            <li>➕ Create new events</li>
            <li>👥 Add attendees to meetings</li>
            <li>📍 Set locations and descriptions</li>
        </ul>
    </div>
    
    <div class="feature-card drive">
        <div class="icon">☁️</div>
        <h3>Google Drive</h3>
        <p>Access your cloud storage directly from your desktop.</p>
        <ul class="capability-list">
            <li>📂 List files in Drive</li>
            <li>⬇️ Download files locally</li>
            <li>🔍 Browse recent files</li>
        </ul>
    </div>
    
    <div class="feature-card web">
        <div class="icon">🌐</div>
        <h3>Web Search</h3>
        <p>Get real-time information from the web instantly.</p>
        <ul class="capability-list">
            <li>🔎 Search via DuckDuckGo</li>
            <li>📰 Get latest news</li>
            <li>💹 Check current information</li>
            <li>🌍 Research any topic</li>
        </ul>
    </div>
</div>
""")

# Tech Stack Section
st.markdown("""
<div class="tech-section">
    <h3>🛠️ Built With Modern Technology</h3>
    <div class="tech-badges">
        <span class="tech-badge">Python</span>
        <span class="tech-badge">LangChain</span>
        <span class="tech-badge">Principal IA providers</span>
        <span class="tech-badge">Google APIs</span>
        <span class="tech-badge">PyQt</span>
        <span class="tech-badge">DuckDuckGo</span>
    </div>
</div>
""", unsafe_allow_html=True)

# System Requirements
colored_header(
    label="System Requirements",
    description="What you need to run Atlas",
    color_name="green-70",
)

st.markdown("""
<div class="requirements">
    <h4>📋 Minimum Requirements</h4>
    <ul>
        <li><strong>Operating System:</strong> Windows 10 or Windows 11</li>
        <li><strong>Memory:</strong> 4 GB RAM (8 GB recommended)</li>
        <li><strong>Storage:</strong> 100 MB free disk space</li>
        <li><strong>Internet:</strong> Required for AI and cloud features</li>
        <li><strong>Google Account:</strong> Required for Gmail, Calendar, and Drive integration</li>
    </ul>
</div>
""", unsafe_allow_html=True)
