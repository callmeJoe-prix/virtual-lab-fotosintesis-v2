import streamlit as st

st.title("📝 Survey Virtual Lab Fotosintesis")

st.write("""
Silakan isi survey berikut untuk membantu meningkatkan kualitas Virtual Lab.
Klik tombol di bawah untuk membuka Google Form:
""")

google_form_url = "https://forms.gle/abcd1234efgh5678"   # GANTI DENGAN LINK FORM ANDA

st.link_button("📤 Buka Survey", google_form_url)

st.info("Survey akan membuka tab baru di browser Anda.")
