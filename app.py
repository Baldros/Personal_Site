"""
Main portfolio landing page.
"""

import streamlit as st

from utils import get_featured_image_data_uri, load_css, render_navbar, render_sidebar_chat


st.set_page_config(
    page_title="Andre Amorim | Software Engineer & AI Specialist",
    page_icon="A",
    layout="wide",
)
load_css()
render_sidebar_chat()

hero_image = get_featured_image_data_uri()
hero_style = f' style="--hero-image: url(\'{hero_image}\');"' if hero_image else ""

st.markdown(
    """
<style>
    .hero-section {
        --hero-image: linear-gradient(135deg, #17243a, #204669);
        min-height: 68vh;
        max-height: 760px;
        display: grid;
        align-items: end;
        margin: -1.25rem calc(50% - 50vw) 2.25rem;
        padding: 4rem max(2rem, calc((100vw - 1180px) / 2)) 3.25rem;
        background-image:
            linear-gradient(90deg, rgba(27,57,91,0.90) 0%, rgba(36,87,122,0.72) 46%, rgba(58,111,137,0.28) 100%),
            var(--hero-image);
        background-size: cover;
        background-position: center;
        color: #ffffff;
    }

    .hero-copy {
        max-width: 760px;
    }

    .hero-kicker {
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;
        margin-bottom: 1rem;
        padding: 0.45rem 0.75rem;
        border: 1px solid rgba(255,255,255,0.24);
        border-radius: 999px;
        color: rgba(255,255,255,0.84);
        font-size: 0.86rem;
        font-weight: 700;
        text-transform: uppercase;
    }

    .hero-section h1 {
        max-width: 760px;
        margin: 0 0 1rem;
        color: #ffffff !important;
        font-size: 4rem;
        line-height: 1.02;
    }

    .hero-section .subtitle {
        max-width: 660px;
        margin: 0 0 1.65rem;
        color: rgba(255,255,255,0.86);
        font-size: 1.2rem;
        line-height: 1.65;
    }

    .hero-actions,
    .metric-strip,
    .highlights-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.8rem;
    }

    .hero-actions a {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-height: 2.85rem;
        padding: 0.72rem 1.05rem;
        border-radius: 8px;
        font-weight: 720;
        border: 1px solid rgba(255,255,255,0.3);
    }

    .hero-actions .primary-action {
        background: #ffffff;
        color: #152033;
    }

    .hero-actions .secondary-action {
        color: #ffffff;
        background: rgba(255,255,255,0.1);
    }

    .metric-strip {
        margin: 0 0 2.25rem;
    }

    .metric {
        flex: 1 1 12rem;
        min-height: 7.75rem;
        padding: 1.25rem;
        border-radius: 8px;
        background: #ffffff;
        border: 1px solid var(--atlas-border);
        box-shadow: var(--atlas-shadow);
    }

    .metric strong {
        display: block;
        margin-bottom: 0.3rem;
        color: var(--atlas-ink);
        font-size: 1.55rem;
        line-height: 1.1;
    }

    .metric span {
        color: var(--atlas-muted);
        font-size: 0.94rem;
        line-height: 1.45;
    }

    .section-heading {
        margin: 2.25rem 0 1rem;
    }

    .section-heading p {
        margin: 0.35rem 0 0;
        max-width: 680px;
        color: var(--atlas-muted);
        line-height: 1.65;
    }

    .summary-panel {
        display: grid;
        grid-template-columns: minmax(0, 1.45fr) minmax(280px, 0.75fr);
        gap: 1rem;
        align-items: stretch;
        margin: 1rem 0 2.25rem;
    }

    .summary-card,
    .focus-panel {
        padding: 1.45rem;
        border-radius: 8px;
        background: #ffffff;
        border: 1px solid var(--atlas-border);
        box-shadow: var(--atlas-shadow);
    }

    .summary-card p,
    .focus-panel p {
        color: #415066;
        line-height: 1.75;
        margin: 0 0 0.9rem;
    }

    .focus-panel {
        background: #1f4775;
        color: #ffffff;
    }

    .focus-panel h3,
    .focus-panel p {
        color: #ffffff !important;
    }

    .focus-panel ul {
        margin: 1rem 0 0;
        padding-left: 1.05rem;
    }

    .focus-panel li {
        margin-bottom: 0.55rem;
        color: rgba(255,255,255,0.82);
    }

    .highlights-container {
        margin: 1rem 0 2.25rem;
    }

    .highlight-card {
        flex: 1 1 16rem;
        padding: 1.25rem;
        border-radius: 8px;
        background: #ffffff;
        border: 1px solid var(--atlas-border);
        box-shadow: var(--atlas-shadow);
    }

    .highlight-card.ai { border-top: 4px solid var(--atlas-blue); }
    .highlight-card.data { border-top: 4px solid var(--atlas-green); }
    .highlight-card.research { border-top: 4px solid var(--atlas-violet); }
    .highlight-card.product { border-top: 4px solid var(--atlas-amber); }

    .highlight-card h3 {
        margin: 0 0 0.55rem;
        font-size: 1.04rem;
    }

    .highlight-card p {
        margin: 0;
        color: var(--atlas-muted);
        line-height: 1.62;
    }

    .philosophy-quote {
        margin: 2.5rem 0 0.25rem;
        padding: 2rem;
        border-radius: 8px;
        background: linear-gradient(135deg, #1f4775, #2f6f89);
        color: #ffffff;
    }

    .philosophy-quote blockquote {
        margin: 0 0 0.6rem;
        color: #ffffff;
        font-size: 1.4rem;
        font-style: italic;
        line-height: 1.55;
    }

    .philosophy-quote p {
        margin: 0;
        color: rgba(255,255,255,0.72);
    }

    @media (max-width: 860px) {
        .hero-section {
            min-height: 620px;
            padding: 3rem 1.25rem 2.5rem;
        }

        .hero-section h1 {
            font-size: 2.7rem;
        }

        .summary-panel {
            grid-template-columns: 1fr;
        }
    }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    f"""
<section class="hero-section"{hero_style}>
    <div class="hero-copy">
        <div class="hero-kicker">Software Engineering + Applied AI</div>
        <h1>Andre Amorim</h1>
        <p class="subtitle">
            Software engineer and AI specialist building practical automation,
            intelligent agents, data products, and modern business systems.
        </p>
        <div class="hero-actions">
            <a class="primary-action" href="experience" target="_self">View experience</a>
            <a class="secondary-action" href="products" target="_self">Explore Atlas Desktop</a>
            <a class="secondary-action" href="https://github.com/Baldros" target="_blank">GitHub</a>
        </div>
    </div>
</section>
""",
    unsafe_allow_html=True,
)

render_navbar()

st.markdown(
    """
<div class="metric-strip">
    <div class="metric">
        <strong>AI systems</strong>
        <span>Agentic workflows, LLM integration, automation, and applied machine learning.</span>
    </div>
    <div class="metric">
        <strong>Business tools</strong>
        <span>CRM modernization, Power Platform, dashboards, and process automation.</span>
    </div>
    <div class="metric">
        <strong>Research depth</strong>
        <span>Remote sensing, atmospheric analysis, and data science at UFRJ research labs.</span>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="section-heading">
    <h2>Executive Summary</h2>
    <p>Focused engineering profile for organizations that need AI work connected to real operations.</p>
</div>

<div class="summary-panel">
    <div class="summary-card">
        <p>
            Andre combines software engineering, data science, and automation experience to build systems
            that reduce manual work and make technical processes easier to operate.
        </p>
        <p>
            His recent work centers on AI-enabled business applications, CRM modernization, intelligent
            assistants, Power Platform solutions, and analytics for strategic decision-making.
        </p>
        <p>
            The academic side adds a strong quantitative foundation: remote sensing, atmospheric data,
            environmental analysis, and machine learning research at UFRJ.
        </p>
    </div>
    <aside class="focus-panel">
        <h3>Current focus</h3>
        <p>Production-oriented AI and software systems that are useful beyond prototypes.</p>
        <ul>
            <li>Agent orchestration with tools and verified context</li>
            <li>Automation across business workflows</li>
            <li>Data products that support operational decisions</li>
            <li>Desktop assistant experience through Atlas Desktop</li>
        </ul>
    </aside>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="section-heading">
    <h2>Core Expertise</h2>
    <p>Four areas where his background connects engineering execution with measurable business value.</p>
</div>

<div class="highlights-container">
    <div class="highlight-card ai">
        <h3>Artificial Intelligence & LLMs</h3>
        <p>Tool-using agents, LangChain/LangGraph workflows, model integration, and applied ML systems.</p>
    </div>
    <div class="highlight-card data">
        <h3>Data Science & Analytics</h3>
        <p>Python/R analysis, BI dashboards, predictive modeling, and decision-support reporting.</p>
    </div>
    <div class="highlight-card research">
        <h3>Environmental Research</h3>
        <p>Satellite data, atmospheric analysis, remote sensing, and scientific data workflows.</p>
    </div>
    <div class="highlight-card product">
        <h3>Product Automation</h3>
        <p>Atlas Desktop demonstrates local AI assistance, integrations, and practical task automation.</p>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="philosophy-quote">
    <blockquote>"Labor omnia vincit, per aspera ad astra."</blockquote>
    <p>Work conquers all, through hardships to the stars.</p>
</div>
""",
    unsafe_allow_html=True,
)
