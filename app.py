import streamlit as st

# Konfigurasi dasar halaman
st.set_page_config(
    page_title="Virtual Lab Fotosintesis",
    layout="wide",
    page_icon="🌱"
)

# Navigasi halaman
pg = st.navigation(
    [
        st.Page("routes/pendahuluan.py", title="Pendahuluan", icon="🏠"),
        st.Page("routes/teori.py", title="Teori Fotosintesis", icon="📘"),
        st.Page("routes/simulasi.py", title="Simulasi Interaktif", icon="🧪"),
        st.Page("routes/kuis.py", title="Kuis", icon="❓"),
    ]
)

# Sidebar
with st.sidebar:
    st.write("## Pengaturan :gear:")
    st.write("Selamat datang di Virtual Lab Fotosintesis 👇")
    st.write("- Gunakan menu di bawah untuk berpindah halaman.")

pg.run()
