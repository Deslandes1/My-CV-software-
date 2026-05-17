import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Gesner Deslandes - CV & Portfolio",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CUSTOM CSS FOR COLORFUL CV ----------
st.markdown(
    """
    <style>
    /* Main background – soft warm off-white, not blank white */
    .stApp {
        background: linear-gradient(145deg, #fef9e6 0%, #fff4e4 100%);
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e2a3e, #0f1722);
        border-right: 3px solid #ffb347;
    }
    [data-testid="stSidebar"] * {
        color: #f0f0f0 !important;
    }
    [data-testid="stSidebar"] .stMarkdown, 
    [data-testid="stSidebar"] .stText {
        color: #f0f0f0 !important;
    }
    /* Card-like containers */
    .cv-card {
        background: rgba(255, 255, 255, 0.92);
        border-radius: 24px;
        padding: 1.8rem;
        margin-bottom: 1.8rem;
        box-shadow: 0 12px 24px rgba(0,0,0,0.05);
        border-left: 8px solid #ffb347;
        transition: 0.2s;
        backdrop-filter: blur(0px);
    }
    .cv-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 20px 30px rgba(0,0,0,0.1);
    }
    .section-title {
        font-size: 2rem;
        font-weight: 800;
        color: #c0392b;
        border-bottom: 3px solid #ffb347;
        display: inline-block;
        margin-bottom: 1.2rem;
        padding-bottom: 0.3rem;
    }
    .skill-tag {
        background: #ffb347;
        color: #2c2c2c;
        display: inline-block;
        padding: 0.2rem 1rem;
        border-radius: 30px;
        font-weight: bold;
        margin: 0.2rem 0.3rem;
        font-size: 0.9rem;
    }
    .portfolio-item {
        background: #fef7e0;
        border-radius: 20px;
        padding: 0.5rem 1rem;
        margin: 0.4rem 0;
        font-weight: 500;
        border-left: 4px solid #e67e22;
    }
    .contact-info {
        background: #fff3e0;
        padding: 1rem;
        border-radius: 30px;
        text-align: center;
        margin-top: 1rem;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        padding: 1rem;
        color: #5a5a5a;
        border-top: 1px solid #ddd;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- SIDEBAR (PERSONAL & PROMO) ----------
with st.sidebar:
    # Removed broken image – just use emoji
    st.markdown("# 🧠 Gesner Deslandes")
    st.markdown("**Software Builder · Python Developer · AI Enthusiast**")
    st.markdown("---")
    st.markdown("### 📞 Contact")
    st.markdown("✉️ deslandes78@gmail.com")
    st.markdown("📱 +509 4738-5663")
    st.markdown("📍 Haiti")
    st.markdown("🎂 20/11/79")
    st.markdown("---")
    st.markdown("### 🌐 GlobalInternet.py")
    st.markdown("We build **software on demand** – from AI chatbots to marriage cards. **You dream it, we code it.**")
    st.markdown("[Visit our website](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.markdown("---")
    st.markdown("### 🎯 Partnership Objective")
    st.markdown("Available for remote work & travel. Seeking a partnership or client-facing role to bridge technical delivery with client success.")

# ---------- MAIN CONTENT ----------
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center; color:#b22222;'>Gesner Deslandes</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:1.2rem;'>Software Builder | Python Developer | AI Enthusiast | Technology Coordinator</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Professional Summary
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🚀 Professional Summary</div>', unsafe_allow_html=True)
st.markdown("""
Exceptionally driven leader and manager with over 4 years of experience building custom Python software for global clients.  
Proven ability to learn quickly, solve complex problems, and deliver production‑ready applications.  
Open to collaborative partnerships – let's turn your idea into software.
""")
st.markdown("</div>", unsafe_allow_html=True)

# Technical Skills
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">💻 Technical Skills</div>', unsafe_allow_html=True)
skills = {
    "Languages": ["Python (advanced)", "JavaScript", "HTML/CSS", "SQL"],
    "Frameworks & Libs": ["Streamlit", "TensorFlow", "OpenCV", "Pygame", "Pandas", "NumPy"],
    "Tools & Platforms": ["Git", "GitHub", "Supabase", "VS Code", "Linux", "Windows"],
    "Areas": ["Web apps", "AI/ML models", "Automation", "Data dashboards", "Educational software", "Hardware integration", "Self‑driving simulations"]
}
for category, items in skills.items():
    st.markdown(f"**{category}:**", unsafe_allow_html=True)
    for i in items:
        st.markdown(f'<span class="skill-tag">{i}</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Professional Experience
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📌 Professional Experience</div>', unsafe_allow_html=True)

st.markdown("**GlobalInternet.py – Founder, Owner & Director – Python Software Builder**  \n*2021 – Present*")
st.markdown("""
- Built and sold 37 custom Python applications to clients worldwide (see portfolio).  
- Developed AI‑powered solutions (chatbots, image classifiers, medical assistants).  
- Created full‑stack web apps (voting systems, school management, dashboards).  
- Designed educational software with audio and multi‑language interfaces.  
- Deployed on Streamlit Cloud, integrated Supabase for real‑time features.
""")

st.markdown("**Be Like Brit Orphanage – Haiti – Technology Coordinator**  \n*2021 – Present*")
st.markdown("""
- Manage IT infrastructure (laptops, tablets, Zoom meetings, daily support).  
- Troubleshoot hardware/software independently.  
- Ensure smooth digital operations for education teams.
""")

st.markdown("**Interpreting Tourist Services – Haiti – CEO**  \n*Organized personalized tourism for NGOs and individuals.*")

st.markdown("**Additional roles:** Accounting Assistant, Document Translator, Fleet Manager, Medical Interpreter, English Teacher, etc. – see full CV for details.")
st.markdown("</div>", unsafe_allow_html=True)

# Portfolio of 37 Products
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📦 Software Portfolio (37 Products)</div>', unsafe_allow_html=True)
st.markdown("All built with Python. Full source code, documentation, and deployment guides included.")
st.markdown(f"<p><strong>👉 View complete portfolio:</strong> <a href='https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/' target='_blank'>globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/</a></p>", unsafe_allow_html=True)

portfolio_items = [
    "1. Haiti Online Voting Software", "2. Business Intelligence Dashboard", "3. AI Customer Support Chatbot",
    "4. School Management System", "5. Inventory & POS System", "6. Custom Web Scraper & Data Pipeline",
    "7. Play Chess Against the Machine", "8. Accountant Excel Advanced AI", "9. Haiti Archives Nationales Database",
    "10. DSM‑2026: System Secured", "11. Business Intelligence Dashboard (advanced)", "12. AI Image Classifier (MobileNetV2)",
    "13. Task Manager Dashboard", "14. Ray Parallel Text Processor", "15. Cassandra Data Dashboard",
    "16. Apache Spark Data Processor", "17. Haitian Drone Commander", "18. Let's Learn English with Gesner",
    "19. Let's Learn Spanish with Gesner", "20. Let's Learn Portuguese with Gesner", "21. AI Career Coach – Resume Optimizer",
    "22. AI Medical & Scientific Literature Assistant", "23. Music Studio Pro – Music Production Suite", "24. AI Media Studio – Talking Photo & Video Editor",
    "25. Let's Learn Chinese with Gesner – Book 1", "26. Let's Learn French with Gesner – Book 1", "27. Let's Learn Mathematics with Gesner – Book 1",
    "28. AI Foundations & Certification Course", "29. Medical Terminology Book for Translators", "30. Let's Learn Coding through Python with Gesner",
    "31. Let's Learn Software & Hardware with Gesner", "32. Let's Learn Medical Vocabulary with Gesner – Book 2", "33. Let's Learn Medical Terminology with Gesner – Book 3 (English‑French)",
    "34. Let's Learn TOEFL with Gesner", "35. Let's Learn French with Gesner (full course)", "36. Let's Learn Why Haiti Isn't a Marketplace for Most Social Media",
    "37. Vectra AI – Self‑Driving Car Simulator"
]
# Display in columns
cols = st.columns(2)
for i, item in enumerate(portfolio_items):
    with cols[i % 2]:
        st.markdown(f'<div class="portfolio-item">{item}</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Education & Training
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🎓 Education & Training</div>', unsafe_allow_html=True)
st.markdown("""
- Vocational Training School – American English  
- Diesel Institute of Haiti – Diesel Mechanic  
- Office Computing Certification (October 2000)  
- High School Graduate  
""")
st.markdown("</div>", unsafe_allow_html=True)

# Additional Skills & References
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🔧 Additional IT & Technical Skills</div>', unsafe_allow_html=True)
st.markdown("IT Support · Technology Coordination · Technical Troubleshooting · Digital Systems Maintenance · Device & Equipment Coordination")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📎 References</div>', unsafe_allow_html=True)
st.markdown("""
- Teresa Lang Ehlert: tbtrekkin@gmail.com  
- Charles Zerr MD: +1 620 952 0074  
""")
st.markdown("</div>", unsafe_allow_html=True)

# Promotion for GlobalInternet.py
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🌟 Why GlobalInternet.py?</div>', unsafe_allow_html=True)
st.markdown("""
We build **software on demand** – from AI chatbots, election systems, web apps, **digital marriage cards**, business dashboards, to educational tools.  
👉 **You describe it, we code it.**  
✅ Full source code delivered ✅ Installation guidance ✅ Fast, reliable, modern.

**Contact us for your next project:**  
📧 deslandes78@gmail.com  |  📞 +509 4738-5663  
🌐 [https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)
""")
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Gesner Deslandes – Built with Python & Streamlit | Last updated May 2026</div>', unsafe_allow_html=True)
