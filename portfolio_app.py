import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Ammar's Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 2rem;
    }
    .profile-container {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 2rem 0;
    }
    .section-header {
        color: #1f77b4;
        font-size: 2rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 0.5rem;
    }
    .project-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    .project-card:hover {
        transform: translateY(-5px);
    }
    .skill-badge {
        display: inline-block;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        font-weight: bold;
    }
    .contact-link {
        font-size: 1.2rem;
        color: #667eea;
        text-decoration: none;
        margin: 0.5rem;
    }
    .hero-text {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }
    .subtitle {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<p class="hero-text">👨‍💻 Ammar\'s Portfolio</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Python Developer</p>', unsafe_allow_html=True)

# Profile Section
st.markdown("---")
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
    <div style='text-align: center; padding: 2rem;'>
        <div style='font-size: 180px;'>👨‍💻</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown('<div class="section-header">About Me</div>', unsafe_allow_html=True)
    st.markdown("""
    ### Hello! 👋
    
    I'm **Ammar**, a passionate Python developer with expertise in building applications, 
    and automation solutions. I love creating innovative projects that solve 
    real-world problems and make life easier.
    
    🎯 **What I Do:**
    - Develop Python applications and tools
    - Sometimes explore AI and machine learning
    - Design user-friendly GUI applications
    
    💡 **My Mission:**
    To leverage technology to create impactful solutions that enhance user experiences and 
    drive innovation.
    """)

st.markdown("---")

# Projects Section
st.markdown('<div class="section-header">🚀 Featured Projects</div>', unsafe_allow_html=True)

# Project 1 - Grocery Application
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### 🛒 Grocery Application
    
    A comprehensive grocery shopping application built with Streamlit that makes online 
    grocery shopping easy and convenient. Browse through various categories including 
    snacks, beverages, dairy products, and more!(WARNING: IS ONLY A TEST APP YOU CANT BUY ANYTHING)
    
    **Features:**
    - 📦 Multiple product categories
    - 🔍 Easy navigation and search
    - 💳 User-friendly interface
    - 🛍️ Streamlined shopping experience
    
    **Technologies:** Python, Streamlit
    """)

with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🌐 Visit Grocery App", use_container_width=True, type="primary"):
        st.link_button("Open App", "https://grocery-application.streamlit.app/#snacks", use_container_width=True)
    
    st.link_button("🔗 Direct Link", "https://grocery-application.streamlit.app/#snacks", use_container_width=True)

st.markdown("---")

# More Projects Section
st.markdown("### 📁 Other Projects")

projects_cols = st.columns(3)

with projects_cols[0]:
    st.markdown("""
    #### 🔐 Password generator
    Generate strong and secure passwords
    - Customizable length
    - Character options
    - Easy to use
    """)

with projects_cols[1]:
    st.markdown("""
    #### 🔐 Password Manager
    Secure password management system
    - Encryption support
    - User-friendly GUI
    - Password generation
    """)

with projects_cols[2]:
    st.markdown("""
    #### 📊 Expense Handler
    Track and manage personal expenses
    - Expense tracking
    - Data visualization
    - Report generation
    """)

st.markdown("---")

# Skills Section
st.markdown('<div class="section-header">💻 Skills & Technologies</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Programming Languages")
    skills = ["Python"]
    for skill in skills:
        st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)

with col2:
    st.markdown("#### Frameworks & Libraries")
    frameworks = ["Streamlit", "PyQt5", "CustomTkinter"]
    for fw in frameworks:
        st.markdown(f'<span class="skill-badge">{fw}</span>', unsafe_allow_html=True)

with col3:
    st.markdown("#### Tools & Technologies")
    tools = ["Git", "VS Code"]
    for tool in tools:
        st.markdown(f'<span class="skill-badge">{tool}</span>', unsafe_allow_html=True)

st.markdown("---")

# Contact Section
st.markdown('<div class="section-header">📬 Get In Touch</div>', unsafe_allow_html=True)

contact_col1, contact_col2, contact_col3 = st.columns(3)

with contact_col1:
    st.markdown("""
    ### 📧 Email
    Want to collaborate or have a question?
    Feel free to reach out!
    """)

with contact_col2:
    st.markdown("""
    ### 💼 GitHub
    Check out my repositories and
    contributions on GitHub
    """)

with contact_col3:
    st.markdown("""
    ### 🌐 Portfolio
    Explore my projects and
    see what I've built
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>Made with ❤️ by Ammar using Streamlit</p>
    <p>© 2026 All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)















