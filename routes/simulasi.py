import streamlit as st
import streamlit.components.v1 as components

def run():
    st.title("Tes Animasi HTML")

    st.write("Jika Anda melihat blok merah di bawah, berarti HTML sudah tampil.")

    html_code = """
    <div style='width:300px;height:200px;background:red;'>
        <h3 style='color:white;text-align:center;padding-top:60px;'>HTML OK</h3>
    </div>
    """

    components.html(html_code, height=250)
