import streamlit as st

st.set_page_config(
    page_title="Virtual Lab Fotosintesis",
    layout="wide",
    page_icon="🌱"
)

# ==============================
# NAVIGASI
# ==============================
pg = st.navigation(
    [
        st.Page("routes/pendahuluan.py", title="Pendahuluan", icon="🏠"),
        st.Page("routes/teori.py", title="Teori Fotosintesis", icon="📘"),
        st.Page("routes/simulasi.py", title="Simulasi Interaktif", icon="🧪"),
        st.Page("routes/kuis.py", title="Kuis", icon="❓"),
        st.Page("routes/survey.py", title="Survey", icon="📝"),
    ]
)

# ==============================
# SIDEBAR
# ==============================
with st.sidebar:
    st.write("## Menu :gear:")
    st.write("Gunakan menu di atas untuk berpindah halaman.")

# ==============================
# JALANKAN HALAMAN
# ==============================
pg.run()
