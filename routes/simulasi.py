import streamlit as st
import streamlit.components.v1 as components

def run():
    st.title("🧪 Simulasi Interaktif (Mirip comphot-biotool)")
    st.write("Grafik dan animasi akan berubah sesuai parameter di bawah.")

    # Slider parameter
    light = st.slider("Intensitas Cahaya", 0, 2000, 500)
    co2 = st.slider("Konsentrasi CO₂", 0, 1200, 400)

    # Load HTML animation
    with open("assets/animation.html", "r") as f:
        animation_html = f.read()

    # tampilkan animasi
    component = components.html(
        animation_html,
        height=450,
        width=700,
        scrolling=False,
    )

    # Kirim parameter slider → JS di HTML
    components.html(f"""
    <script>
        window.parent.postMessage(
            {{type: "update", light: {light}, co2: {co2}}},
            "*"
        );
    </script>
    """, height=0)

import streamlit as st

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
    st.write("## Menu :gear:")
    st.write("Gunakan menu di atas untuk berpindah halaman.")

pg.run()
