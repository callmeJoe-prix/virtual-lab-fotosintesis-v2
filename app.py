import streamlit as st

st.set_page_config(page_title="Virtual Lab Fotosintesis", layout="wide")

# Sistem Navigasi Manual (PALING STABIL)
st.sidebar.title("📘 Navigasi")
page = st.sidebar.radio(
    "Pilih Halaman:",
    ["Pendahuluan", "Teori", "Simulasi", "Kuis"]
)

# Impor file halaman
if page == "Pendahuluan":
    from routes.pendahuluan import run
    run()

elif page == "Teori":
    from routes.teori import run
    run()

elif page == "Simulasi":
    from routes.simulasi import run
    run()

elif page == "Kuis":
    from routes.kuis import run
    run()
