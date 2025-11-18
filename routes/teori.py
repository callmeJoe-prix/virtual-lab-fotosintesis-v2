import streamlit as st

st.title("🧪 Teori Fotosintesis")
st.write("---")

# --- Tabs Layout ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Apa itu Fotosintesis?",
    "Struktur Kloroplas",
    "Reaksi Terang",
    "Reaksi Gelap (Calvin)",
    "Faktor-Faktor",
    "Pigmen Fotosintetik"
])

# -------------------------------
# 1. Apa Itu Fotosintesis?
# -------------------------------
with tab1:
    st.header("🌿 Apa Itu Fotosintesis?")
    st.write(
        """
Fotosintesis adalah proses biologis penting di mana tumbuhan menggunakan energi cahaya
untuk mengubah:

🌬️ **CO₂** + 💧 **H₂O** + ☀️ **Cahaya**  
➡️ 🍬 **Glukosa** + 🌫️ **Oksigen (O₂)**

Proses ini menjadi dasar kehidupan di bumi.
        """
    )

    st.subheader("Diagram Reaksi:")
    st.code(
        """
CO₂ + H₂O + Cahaya
        ↓
    C₆H₁₂O₆ + O₂
        """,
        language="text",
    )


# -------------------------------
# 2. Struktur Kloroplas
# -------------------------------
with tab2:
    st.header("🏛️ Struktur Kloroplas")

    st.write("Kloroplas memiliki beberapa bagian penting seperti **grana**, **tilakoid**, dan **stroma**.")

    st.image("assets/kloroplas.png", caption="Struktur Kloroplas", use_column_width=True)

    st.subheader("Diagram Sederhana Kloroplas:")
    st.code(
        """
   _________________________________
  |                                 |
  |   🌿 K L O R O P L A S          |
  |                                 |
  |   [Grana]   [Grana]   [Grana]   |
  |   (tilakoid tumpuk)             |
  |                                 |
  |          ~ STROMA ~            |
  |  (tempat reaksi gelap)          |
  |_________________________________|
        """,
        language="text",
    )


# -------------------------------
# 3. Reaksi Terang
# -------------------------------
with tab3:
    st.header("☀️ Reaksi Terang")

    st.write(
        """
Reaksi terang terjadi di **membran tilakoid** dan memerlukan cahaya untuk:

- memecah air (**fotolisis**) → menghasilkan oksigen  
- menghasilkan **ATP**  
- menghasilkan **NADPH**
        """
    )

    st.image("assets/reaksi-terang.png", caption="Diagram Reaksi Terang", use_column_width=True)

    st.subheader("Diagram Aliran Elektron:")
    st.code(
        """
       ☀️ Cahaya
          ↓
   [Fotosistem II] —— fotolisis H₂O
          ↓               |
   transport elektron →  O₂↑
          ↓
   ATP Synthase → ⚡ ATP
          ↓
   [Fotosistem I]
          ↓
       NADPH ↑
        """,
        language="text"
    )


# -------------------------------
# 4. Reaksi Gelap (Calvin Cycle)
# -------------------------------
with tab4:
    st.header("🌙 Reaksi Gelap (Siklus Calvin)")

    st.write(
        """
Siklus Calvin terjadi di **stroma** kloroplas dan menghasilkan glukosa melalui 3 tahap:

1️⃣ *Karboksilasi*  
2️⃣ *Reduksi* (menggunakan ATP & NADPH)  
3️⃣ *Regenerasi* RuBP
        """
    )

    st.image("assets/calvin-cycle.png", caption="Siklus Calvin", use_column_width=True)

    st.subheader("Diagram Siklus Calvin:")
    st.code(
        """
           🌬️ CO₂
             ↓
      ┌───────────────┐
      |   Karboksilasi |
      └──────┬────────┘
             ↓
   ⚡ ATP & 🔋 NADPH digunakan
             ↓
      ┌───────────────┐
      |   Reduksi      |
      └──────┬────────┘
             ↓
         🍬 Glukosa
             ↓
      ┌───────────────┐
      | Regenerasi     |
      └───────────────┘
        """,
        language="text",
    )


# -------------------------------
# 5. Faktor-Faktor
# -------------------------------
with tab5:
    st.header("📊 Faktor-Faktor yang Mempengaruhi Fotosintesis")

    st.write(
        """
Beberapa faktor yang berpengaruh:

🔸 Intensitas cahaya  
🔸 Konsentrasi CO₂  
🔸 Suhu  
🔸 Ketersediaan air  
🔸 Jumlah klorofil  
        """
    )

    st.image("assets/grafik-cahaya.png", caption="Hubungan Intensitas Cahaya", use_column_width=True)

    st.subheader("Diagram Kurva Cahaya:")
    st.code(
        """
Laju Fotosintesis ↑
   |
   |                _________ titik jenuh
   |              /
   |            /
   |          /
   |________/_____________________→ Intensitas Cahaya
        """,
        language="text",
    )


# -------------------------------
# 6. Pigmen Fotosintetik
# -------------------------------
with tab6:
    st.header("🎨 Pigmen Fotosintetik")

    st.write(
        """
Pigmen utama fotosintesis:

🌱 **Klorofil a**  
🌿 **Klorofil b**  
🟠 **Karotenoid**

Masing-masing menyerap cahaya pada panjang gelombang berbeda.
        """
    )

    st.image("assets/spektrum-pigmen.png", caption="Spektrum Penyerapan Pigmen", use_column_width=True)

    st.subheader("Diagram Spektrum:")
    st.code(
        """
Penyerapan Pigmen
↑
| 🌊 Biru      🔴 Merah
|  ███████      ██████   ← Klorofil a
|  ██████       ████     ← Klorofil b
|   ██           █       ← Karotenoid
|________________________________________→ Panjang Gelombang
        """,
        language="text",
    )

st.write("---")
st.success("Halaman teori fotosintesis selesai ditampilkan!")
