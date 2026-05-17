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

# ---------- TRANSLATIONS (English, French, Spanish) ----------
def get_translations(lang):
    texts = {
        "en": {
            "name": "Gesner Deslandes",
            "title": "Software Builder | Python Developer | AI Enthusiast | Technology Coordinator",
            "sidebar_name": "Gesner Deslandes",
            "sidebar_role": "Software Builder · Python Developer · AI Enthusiast",
            "contact": "Contact",
            "email": "deslandes78@gmail.com",
            "phone": "+509 4738-5663",
            "location": "Haiti",
            "dob": "20/11/79",
            "company": "GlobalInternet.py",
            "company_desc": "We build **software on demand** – from AI chatbots to marriage cards. **You dream it, we code it.**",
            "visit_website": "Visit our website",
            "partnership": "Partnership Objective",
            "partnership_text": "Available for remote work & travel. Seeking a partnership or client-facing role to bridge technical delivery with client success.",
            "professional_summary": "🚀 Professional Summary",
            "summary_text": "Exceptionally driven leader and manager with over 4 years of experience building custom Python software for global clients.\nProven ability to learn quickly, solve complex problems, and deliver production‑ready applications.\nOpen to collaborative partnerships – let's turn your idea into software.",
            "tech_skills": "💻 Technical Skills",
            "languages": "Languages",
            "frameworks": "Frameworks & Libs",
            "tools": "Tools & Platforms",
            "areas": "Areas",
            "experience": "📌 Professional Experience",
            "exp_global": "**GlobalInternet.py – Founder, Owner & Director – Python Software Builder**  \n*2021 – Present*",
            "exp_global_items": "- Built and sold 37 custom Python applications to clients worldwide (see portfolio).\n- Developed AI‑powered solutions (chatbots, image classifiers, medical assistants).\n- Created full‑stack web apps (voting systems, school management, dashboards).\n- Designed educational software with audio and multi‑language interfaces.\n- Deployed on Streamlit Cloud, integrated Supabase for real‑time features.",
            "exp_brit": "**Be Like Brit Orphanage – Haiti – Technology Coordinator**  \n*2021 – Present*",
            "exp_brit_items": "- Manage IT infrastructure (laptops, tablets, Zoom meetings, daily support).\n- Troubleshoot hardware/software independently.\n- Ensure smooth digital operations for education teams.",
            "exp_tourism": "**Interpreting Tourist Services – Haiti – CEO**  \n*Organized personalized tourism for NGOs and individuals.*",
            "exp_other": "**Additional roles:** Accounting Assistant, Document Translator, Fleet Manager, Medical Interpreter, English Teacher, etc. – see full CV for details.",
            "portfolio": "📦 Software Portfolio (37 Products)",
            "portfolio_desc": "All built with Python. Full source code, documentation, and deployment guides included.",
            "view_portfolio": "👉 View complete portfolio:",
            "education": "🎓 Education & Training",
            "education_text": "- Vocational Training School – American English\n- Diesel Institute of Haiti – Diesel Mechanic\n- Office Computing Certification (October 2000)\n- High School Graduate",
            "additional_skills": "🔧 Additional IT & Technical Skills",
            "additional_skills_text": "IT Support · Technology Coordination · Technical Troubleshooting · Digital Systems Maintenance · Device & Equipment Coordination",
            "references": "📎 References",
            "refs": "- Teresa Lang Ehlert: tbtrekkin@gmail.com\n- Charles Zerr MD: +1 620 952 0074",
            "why_global": "🌟 Why GlobalInternet.py?",
            "why_text": "We build **software on demand** – from AI chatbots, election systems, web apps, **digital marriage cards**, business dashboards, to educational tools.\n👉 **You describe it, we code it.**\n✅ Full source code delivered ✅ Installation guidance ✅ Fast, reliable, modern.\n\n**Contact us for your next project:**  \n📧 deslandes78@gmail.com  |  📞 +509 4738-5663",
            "footer": "Gesner Deslandes – Built with Python & Streamlit | Last updated May 2026"
        },
        "fr": {
            "name": "Gesner Deslandes",
            "title": "Développeur logiciel | Python | Passionné d'IA | Coordinateur technique",
            "sidebar_name": "Gesner Deslandes",
            "sidebar_role": "Développeur logiciel · Python · Passionné d'IA",
            "contact": "Contact",
            "email": "deslandes78@gmail.com",
            "phone": "+509 4738-5663",
            "location": "Haïti",
            "dob": "20/11/79",
            "company": "GlobalInternet.py",
            "company_desc": "Nous construisons des **logiciels sur demande** – des chatbots IA aux faire-parts de mariage. **Vous rêvez, nous codons.**",
            "visit_website": "Visitez notre site web",
            "partnership": "Objectif de partenariat",
            "partnership_text": "Disponible pour travail à distance et déplacements. Je cherche un partenariat ou un rôle client pour allier expertise technique et réussite client.",
            "professional_summary": "🚀 Résumé professionnel",
            "summary_text": "Leader et gestionnaire exceptionnel avec plus de 4 ans d'expérience dans la création de logiciels Python personnalisés pour des clients mondiaux.\nCapacité prouvée à apprendre rapidement, résoudre des problèmes complexes et livrer des applications prêtes pour la production.\nOuvert à des partenariats collaboratifs – transformons votre idée en logiciel.",
            "tech_skills": "💻 Compétences techniques",
            "languages": "Langages",
            "frameworks": "Frameworks & bibliothèques",
            "tools": "Outils & plateformes",
            "areas": "Domaines",
            "experience": "📌 Expérience professionnelle",
            "exp_global": "**GlobalInternet.py – Fondateur, propriétaire & directeur – Créateur de logiciels Python**  \n*2021 – Présent*",
            "exp_global_items": "- 37 applications Python personnalisées vendues dans le monde (voir portfolio).\n- Solutions IA (chatbots, classificateurs d'images, assistants médicaux).\n- Applications web complètes (systèmes de vote, gestion scolaire, tableaux de bord).\n- Logiciels éducatifs avec audio et interfaces multilingues.\n- Déploiement sur Streamlit Cloud, intégration Supabase pour temps réel.",
            "exp_brit": "**Orphelinat Be Like Brit – Haïti – Coordinateur technique**  \n*2021 – Présent*",
            "exp_brit_items": "- Gestion de l'infrastructure IT (ordinateurs, tablettes, réunions Zoom, support quotidien).\n- Dépannage matériel/logiciel.\n- Assurer le bon fonctionnement numérique pour les équipes éducatives.",
            "exp_tourism": "**Interpreting Tourist Services – Haïti – PDG**  \n*Organisation de tourisme personnalisé pour ONG et particuliers.*",
            "exp_other": "**Autres rôles :** Assistant comptable, traducteur documentaire, gestionnaire de flotte, interprète médical, professeur d'anglais, etc. – voir CV complet.",
            "portfolio": "📦 Portfolio logiciel (37 produits)",
            "portfolio_desc": "Tous construits avec Python. Code source, documentation et guides d'installation inclus.",
            "view_portfolio": "👉 Voir le portfolio complet :",
            "education": "🎓 Éducation & formation",
            "education_text": "- École de formation professionnelle – Anglais américain\n- Institut diesel d'Haïti – Mécanicien diesel\n- Certification bureautique (octobre 2000)\n- Diplômé du secondaire",
            "additional_skills": "🔧 Compétences techniques supplémentaires",
            "additional_skills_text": "Support IT · Coordination technique · Dépannage · Maintenance systèmes numériques · Coordination d'équipements",
            "references": "📎 Références",
            "refs": "- Teresa Lang Ehlert: tbtrekkin@gmail.com\n- Charles Zerr MD: +1 620 952 0074",
            "why_global": "🌟 Pourquoi GlobalInternet.py ?",
            "why_text": "Nous construisons des **logiciels sur demande** – chatbots IA, systèmes électoraux, applications web, **faire-parts de mariage numériques**, tableaux de bord, outils éducatifs.\n👉 **Vous décrivez, nous codons.**\n✅ Code source complet ✅ Guide d'installation ✅ Rapide, fiable, moderne.\n\n**Contactez-nous pour votre prochain projet :**  \n📧 deslandes78@gmail.com  |  📞 +509 4738-5663",
            "footer": "Gesner Deslandes – Construit avec Python & Streamlit | Dernière mise à jour mai 2026"
        },
        "es": {
            "name": "Gesner Deslandes",
            "title": "Creador de software | Desarrollador Python | Entusiasta de IA | Coordinador técnico",
            "sidebar_name": "Gesner Deslandes",
            "sidebar_role": "Creador de software · Python · Entusiasta de IA",
            "contact": "Contacto",
            "email": "deslandes78@gmail.com",
            "phone": "+509 4738-5663",
            "location": "Haití",
            "dob": "20/11/79",
            "company": "GlobalInternet.py",
            "company_desc": "Construimos **software a pedido** – desde chatbots de IA hasta tarjetas de boda. **Tú lo sueñas, nosotros lo codificamos.**",
            "visit_website": "Visite nuestro sitio web",
            "partnership": "Objetivo de asociación",
            "partnership_text": "Disponible para trabajo remoto y viajes. Busco una asociación o rol orientado al cliente para unir experiencia técnica y éxito del cliente.",
            "professional_summary": "🚀 Resumen profesional",
            "summary_text": "Líder y gerente excepcional con más de 4 años de experiencia creando software Python personalizado para clientes globales.\nCapacidad probada para aprender rápido, resolver problemas complejos y entregar aplicaciones listas para producción.\nAbierto a colaboraciones – convirtamos tu idea en software.",
            "tech_skills": "💻 Habilidades técnicas",
            "languages": "Lenguajes",
            "frameworks": "Frameworks y librerías",
            "tools": "Herramientas y plataformas",
            "areas": "Áreas",
            "experience": "📌 Experiencia profesional",
            "exp_global": "**GlobalInternet.py – Fundador, propietario y director – Creador de software Python**  \n*2021 – Presente*",
            "exp_global_items": "- 37 aplicaciones Python personalizadas vendidas a clientes globales (ver portafolio).\n- Soluciones IA (chatbots, clasificadores de imágenes, asistentes médicos).\n- Aplicaciones web completas (sistemas de votación, gestión escolar, paneles).\n- Software educativo con audio e interfaces multilingües.\n- Despliegue en Streamlit Cloud, integración Supabase para tiempo real.",
            "exp_brit": "**Orfanato Be Like Brit – Haití – Coordinador técnico**  \n*2021 – Presente*",
            "exp_brit_items": "- Gestión de infraestructura IT (laptops, tablets, reuniones Zoom, soporte diario).\n- Solución de problemas hardware/software.\n- Asegurar operaciones digitales fluidas para equipos educativos.",
            "exp_tourism": "**Interpreting Tourist Services – Haití – CEO**  \n*Organización de turismo personalizado para ONG y particulares.*",
            "exp_other": "**Otros roles:** Asistente contable, traductor documental, administrador de flota, intérprete médico, profesor de inglés, etc. – ver CV completo.",
            "portfolio": "📦 Portafolio de software (37 productos)",
            "portfolio_desc": "Todos construidos con Python. Código fuente, documentación y guías de instalación incluidos.",
            "view_portfolio": "👉 Ver portafolio completo:",
            "education": "🎓 Educación y formación",
            "education_text": "- Escuela de formación profesional – Inglés americano\n- Instituto Diesel de Haití – Mecánico diesel\n- Certificación en ofimática (octubre 2000)\n- Graduado de secundaria",
            "additional_skills": "🔧 Habilidades técnicas adicionales",
            "additional_skills_text": "Soporte IT · Coordinación técnica · Solución de problemas · Mantenimiento de sistemas digitales · Coordinación de equipos",
            "references": "📎 Referencias",
            "refs": "- Teresa Lang Ehlert: tbtrekkin@gmail.com\n- Charles Zerr MD: +1 620 952 0074",
            "why_global": "🌟 ¿Por qué GlobalInternet.py?",
            "why_text": "Construimos **software a pedido** – chatbots IA, sistemas electorales, aplicaciones web, **tarjetas de boda digitales**, paneles, herramientas educativas.\n👉 **Tú lo describes, nosotros lo codificamos.**\n✅ Código fuente completo ✅ Guía de instalación ✅ Rápido, confiable, moderno.\n\n**Contáctenos para su próximo proyecto:**  \n📧 deslandes78@gmail.com  |  📞 +509 4738-5663",
            "footer": "Gesner Deslandes – Construido con Python & Streamlit | Última actualización mayo 2026"
        }
    }
    return texts[lang]

# ---------- SIDEBAR (PERSONAL & PROMO) ----------
lang = st.sidebar.selectbox("🌐 Language / Idioma / Langue", ["English", "Français", "Español"])
lang_code = {"English": "en", "Français": "fr", "Español": "es"}[lang]
t = get_translations(lang_code)

with st.sidebar:
    st.markdown(f"# 🧠 {t['sidebar_name']}")
    st.markdown(f"**{t['sidebar_role']}**")
    st.markdown("---")
    st.markdown(f"### 📞 {t['contact']}")
    st.markdown(f"✉️ {t['email']}")
    st.markdown(f"📱 {t['phone']}")
    st.markdown(f"📍 {t['location']}")
    st.markdown(f"🎂 {t['dob']}")
    st.markdown("---")
    st.markdown(f"### 🌐 {t['company']}")
    st.markdown(t['company_desc'])
    st.markdown(f"[{t['visit_website']}](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.markdown("---")
    st.markdown(f"### 🎯 {t['partnership']}")
    st.markdown(t['partnership_text'])

# ---------- MAIN CONTENT ----------
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align:center; color:#b22222;'>{t['name']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; font-size:1.2rem;'>{t['title']}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Professional Summary
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown(f'<div class="section-title">{t["professional_summary"]}</div>', unsafe_allow_html=True)
st.markdown(t['summary_text'])
st.markdown("</div>", unsafe_allow_html=True)

# Technical Skills
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown(f'<div class="section-title">{t["tech_skills"]}</div>', unsafe_allow_html=True)
skills = {
    t["languages"]: ["Python (advanced)", "JavaScript", "HTML/CSS", "SQL"],
    t["frameworks"]: ["Streamlit", "TensorFlow", "OpenCV", "Pygame", "Pandas", "NumPy"],
    t["tools"]: ["Git", "GitHub", "Supabase", "VS Code", "Linux", "Windows"],
    t["areas"]: ["Web apps", "AI/ML models", "Automation", "Data dashboards", "Educational software", "Hardware integration", "Self‑driving simulations"]
}
for category, items in skills.items():
    st.markdown(f"**{category}:**")
    for i in items:
        st.markdown(f'<span class="skill-tag">{i}</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Professional Experience
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown(f'<div class="section-title">{t["experience"]}</div>', unsafe_allow_html=True)

st.markdown(t['exp_global'])
st.markdown(t['exp_global_items'])

st.markdown(t['exp_brit'])
st.markdown(t['exp_brit_items'])

st.markdown(t['exp_tourism'])

st.markdown(t['exp_other'])
st.markdown("</div>", unsafe_allow_html=True)

# Portfolio of 37 Products
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown(f'<div class="section-title">{t["portfolio"]}</div>', unsafe_allow_html=True)
st.markdown(t['portfolio_desc'])
st.markdown(f"<p><strong>{t['view_portfolio']}</strong> <a href='https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/' target='_blank'>globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/</a></p>", unsafe_allow_html=True)

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
cols = st.columns(2)
for i, item in enumerate(portfolio_items):
    with cols[i % 2]:
        st.markdown(f'<div class="portfolio-item">{item}</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Education & Training
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown(f'<div class="section-title">{t["education"]}</div>', unsafe_allow_html=True)
st.markdown(t['education_text'])
st.markdown("</div>", unsafe_allow_html=True)

# Additional Skills
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown(f'<div class="section-title">{t["additional_skills"]}</div>', unsafe_allow_html=True)
st.markdown(t['additional_skills_text'])
st.markdown("</div>", unsafe_allow_html=True)

# References
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown(f'<div class="section-title">{t["references"]}</div>', unsafe_allow_html=True)
st.markdown(t['refs'])
st.markdown("</div>", unsafe_allow_html=True)

# Promotion for GlobalInternet.py
st.markdown('<div class="cv-card">', unsafe_allow_html=True)
st.markdown(f'<div class="section-title">{t["why_global"]}</div>', unsafe_allow_html=True)
st.markdown(t['why_text'])
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown(f'<div class="footer">{t["footer"]}</div>', unsafe_allow_html=True)
