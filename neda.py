import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Dr. Neda Najafi",
    page_icon="🩺",
    layout="wide"
)

# --- Custom CSS for styling ---
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #f0f7ff 0%, #ffffff 100%);
    font-family: 'Helvetica', sans-serif;
}
h1, h2, h3 {
    color: #1c3d5a;
}
.sidebar .sidebar-content {
    background: linear-gradient(180deg, #cce7ff 0%, #e8f4ff 100%);
}
.profile-pic {
    border-radius: 50%;
    margin-bottom: 15px;
}
.social-icons a {
    margin: 0 10px;
    text-decoration: none;
    font-size: 22px;
}
</style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("🩺 Dr. Neda Najafi")
st.sidebar.markdown("#### Navigation")
page = st.sidebar.radio("", ["Home", "About", "Experience", "Education", "Contact"])

st.sidebar.markdown("---")
st.sidebar.markdown("#### Connect with Me")
st.sidebar.markdown(
    """
    <div class="social-icons">
        <a href="https://instagram.com/" target="_blank">📸 Instagram</a><br>
        <a href="https://linkedin.com/" target="_blank">💼 LinkedIn</a><br>
        <a href="mailto:nedaanajafi@gmail.com">✉️ Email</a>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Main Content ---
if page == "Home":
    st.title("Dr. Neda Najafi")
    st.subheader("Medical Doctor | Honor Medalist | Graduate of Russia with Distinction")

    st.image("neda.jpg", width=220)

    st.write("""
    Welcome to my professional portfolio.  
    I am **Dr. Neda Najafi**, a dedicated medical doctor currently practicing in **Ahvaz**, 
    with a strong focus on preventive healthcare, patient education, and modern treatment methods.
    """)

elif page == "About":
    st.header("About Me")
    st.write("""
    I am a **medical doctor and honor medalist** who graduated from a top medical university in Russia with a **perfect GPA**.  
    Currently, I work at a specialized clinic in Ahvaz and manage my **private practice**, where I provide high-quality, 
    patient-centered medical services following **international healthcare standards**.

    My approach combines science, empathy, and precision to ensure the best possible outcomes for every patient.
    """)

    st.subheader("Specializations & Skills")
    st.markdown("""
    - General and specialized medical practice  
    - Advanced diagnosis and treatment methods  
    - Preventive medicine and patient education  
    - Clinical and private practice experience  
    - Multilingual: Persian, English, Russian  
    """)

elif page == "Experience":
    st.header("Professional Experience")
    st.markdown("""
    **Specialized Clinic – Ahvaz**  
    *Active Physician*  
    - Providing expert consultations and treatments for diverse patient needs  
    - Collaborating with multidisciplinary healthcare teams  
    - Ensuring patient safety and quality of care  

    **Private Medical Office – Ahvaz**  
    *Founder & Lead Physician*  
    - Managing a private healthcare practice  
    - Offering personalized patient care and preventive programs  

    **Achievements:**  
    🏅 Graduated with a **Gold Medal** and **Perfect GPA** from a Russian medical university
    """)

elif page == "Education":
    st.header("Education")
    st.markdown("""
    **Doctor of Medicine (M.D.) – Russian State Medical University**  
    Graduated with distinction and received an **Honor Medal** for academic excellence.  

    **Certifications & Courses:**  
    - Advanced Clinical Diagnosis – Moscow, 2023  
    - Patient Communication & Ethics – Online Certification, 2024  
    """)

elif page == "Contact":
    st.header("Contact Me")
    st.markdown("""
    📍 **Private Office:** "Iran Negin Complex, Entrance 2, 2nd Floor, 6th West Street, Kianpars, Ahvaz, Iran" 
    📞 **Phone (Office):** 09917425895  
    📞 **Clinic:** 061-33914893  
    📧 **Email:** [nedanaanjafi@gmail.com](mailto:neda.najafi@example.com)
    """)

    # --- Embedded Google Map ---
    st.markdown("""
    <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d716.3337864820586!2d48.68478866754923!3d31.345815416848332!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3fc3df1b461a5895%3A0x7704fc0303ea6647!2z2YXYrNiq2YXYuSDYp9uM2LHYp9mGINmG2q_bjNmG!5e0!3m2!1sen!2s!4v1761553170140!5m2!1sen!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade">
        width="100%" height="350" style="border:0;" allowfullscreen="" loading="lazy">
    </iframe>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("© 2025 Dr. Neda Najafi | All rights reserved.")

