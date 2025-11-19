import streamlit as st
import pandas as pd

st.title("Teori Fotosintesis")
st.write("""
Kehidupan di Bumi secara fundamental bergantung pada energi yang berasal dari matahari. Fotosintesis merupakan satu-satunya
proses yang memiliki signifikansi biologis yang mampu memanen energi tersebut. Sebagian besar sumber daya energi planet ini,
baik yang baru (biomassa) maupun yang purba (bahan bakar fosil), merupakan hasil dari aktivitas fotosintetik. Secara harfiah,
istilah fotosintesis berarti "sintesis menggunakan cahaya." Organisme fotosintetik memanfaatkan energi surya untuk menyintesis 
senyawa karbon kompleks. Lebih spesifik, energi cahaya menggerakkan sintesis karbohidrat dan menghasilkan oksigen dari karbon
dioksida dan air, sesuai dengan persamaan stoikiometri berikut:
""")

# --- Tambahan: Tampilan Persamaan Reaksi Fotosintesis ---
st.subheader("Persamaan Reaksi Fotosintesis")
# Menggunakan st.latex untuk menampilkan persamaan kimia yang diformat dengan baik
st.latex(
    r"""
    \text{6 CO}_2 + \text{6 H}_2\text{O} \xrightarrow[\text{Klorofil}]{\text{Energi Cahaya}} \text{C}_6\text{H}_{12}\text{O}_6 + \text{6 O}_2
    """
)

st.write("""
Energi yang tersimpan dalam molekul karbohidrat ini kemudian dapat dimanfaatkan untuk mendukung berbagai proses seluler pada tumbuhan dan
berfungsi sebagai sumber energi utama bagi semua bentuk kehidupan.
""")

# --- Video Penjelasan ---
st.subheader("🎥 Penjelasan Singkat Fotosintesis")
video_file = "assets/video/fotosintesis_intro.mp4"
st.video(video_file)

# --- Struktur Kloroplas ---
st.header("Struktur Kloroplas")
st.image("assets/images/kloroplas_diagram.png", caption="Letak Kloroplas")
st.image("assets/images/kloroplas.png", caption="Struktur Kloroplas")
st.write("""
Kloroplas pada tumbuhan tingkat tinggi dilingkupi oleh dua membran, yaitu membran dalam dan membran luar, yang secara kolektif disebut sebagai
selubung (envelope). Wilayah kloroplas yang berada di dalam membran dalam dan mengelilingi membran tilakoid dikenal sebagai stroma.
Stroma mengandung enzim yang bertanggung jawab untuk mengkatalisis fiksasi karbon dan jalur biosintetik lainnya. Membran tilakoid terlipat secara
ekstensif dan dalam banyak visualisasi tampak tersusun bertumpuk seperti koin, yang disebut granum. Meskipun demikian, secara aktual, 
membran tilakoid membentuk satu atau beberapa sistem membran besar yang saling terhubung, dengan interior dan eksterior yang terdefinisikan dengan 
baik terhadap stroma. Struktur organisasi ini sangat penting dalam memfasilitasi proses penyimpanan energi fotosintetik.  
""")

# --- Reaksi Terang ---
st.header("Reaksi Terang")
st.image("assets/images/light_reaction.png", caption="Reaksi Terang")
st.write("""
Skema Z adalah representasi skematis dari organisasi keseluruhan membran pada kloroplas. Penyerapan cahaya merah oleh Fotosistem II (PSII) menghasilkan 
suatu oksidator kuat dan reduktan lemah. Sebaliknya, cahaya far-red yang diserap oleh Fotosistem I (PSI) menghasilkan suatu oksidator lemah dan reduktan kuat. 
Oksidator kuat yang dihasilkan oleh PSII berfungsi untuk mengoksidasi air (H₂O), sementara reduktan kuat yang diproduksi oleh PSI 
mereduksi NADP⁺ menjadi NADPH. Pemahaman terhadap skema ini sangat mendasar bagi interpretasi transport elektron fotosintetik. 
Istilah P680 dan P700 merujuk pada panjang gelombang serapan maksimum dari klorofil pusat reaksi yang masing-masing terdapat pada PSII dan PSI.
""")

# --- Grafik Respon Cahaya ---
st.subheader("Grafik Laju Fotosintesis vs Intensitas Cahaya")
df_light = pd.read_csv("assets/graphs/kurva_cahaya.csv")
st.line_chart(df_light, x="Light", y="Rate")

# --- Reaksi Gelap (Siklus Calvin) ---
st.header("Siklus Calvin (Reaksi Gelap)")
st.image("assets/images/calvin_cycle.png", caption="Siklus Calvin")
st.write("""
Siklus Calvin, dinamai berdasarkan penemunya Melvin Calvin, merupakan sebuah siklus reaksi kimia dalam fotosintesis yang mengubah CO2 dan beberapa komponen 
menjadi gliseraldehida 3-fosfat (G3P) dan akhirnya menjadi glukosa. Siklus ini tidak memerlukan cahaya (disebut juga reaksi gelap) dan berlangsung di stroma kloroplas. 
""")

st.header("**Bagaimana tahapan dan cara kerja siklus Calvin?**")
st.write("""
1. Fiksasi CO2: CO2 diikat oleh RuBP (ribulosa 1,5-bisfosfat) dan diubah menjadi G3P (gliseraldehida 3-fosfat).
2. Reduksi: G3P diubah menjadi PGA (asam fosfogliserat) dengan bantuan ATP dan NADPH2.
3. Regenerasi: PGA diubah kembali menjadi RuBP agar siklus dapat terus berlangsung.

**1. Fiksasi CO2:** Proses dimulai ketika karbon dioksida (CO2) dari udara diambil dan diikat ke molekul karbon yang lebih besar, ribulosa bisfosfat (RuBP). Reaksi ini dimediasi oleh 
enzim RuBisCO (ribulosa-1,5-bisfosfat karboksilase/oksigenase), yang menghasilkan dua molekul asam 3-fosfogliserat (3-PGA).

**2. Reduksi:** Selanjutnya, molekul 3-PGA diubah menjadi molekul gliseraldehida-3-fosfat (G3P) melalui serangkaian reaksi redoks. Proses ini melibatkan konsumsi energi dari ATP 
(adenosin trifosfat) dan pengurangan NADPH (nikotinamida adenin dinukleotida fosfat) yang dihasilkan selama tahap terang fotosintesis.

**3. Regenerasi:** Sebagian G3P yang dihasilkan dari tahap sebelumnya digunakan untuk meregenerasi RuBP. Tahap ini penting karena RuBP diperlukan kembali untuk fiksasi karbon baru. 
Proses regenerasi RuBP melibatkan beberapa langkah dan membutuhkan energi ATP yang dihasilkan selama tahap terang fotosintesis. Setelah tahapan-tahapan ini selesai, siklus Calvin akan 
kembali ke titik awal dan dapat terus berulang untuk menghasilkan lebih banyak G3P, yang selanjutnya digunakan untuk membangun karbohidrat seperti glukosa.
""")

# --- Faktor-Faktor yang Mempengaruhi ---
st.header("Faktor-Faktor Pembatas Fotosintesis")
st.image("assets/images/faktor_fotosintesis.png", caption="Faktor-faktor Pembatas Fotosintesis")
st.write("""
Deskripsi masing-masing faktor:
- **1. Intensitas cahaya**
    Fotosintesis tidak terjadi tanpa adanya cahaya, sehingga tidak ada fotosintesis pada malam hari, melainkan hanya pada siang hari. Ada tiga atribut sinar matahari yang penting dalam fotosintesis,
yaitu intensitas, kualitas, dan durasi paparan cahaya.
**2. CO₂**
Karbon dioksida sebagai molekul gas sangat sedikit di atmosfer, hanya 0,03% di antara gas-gas atmosfer lainnya. Hal ini menyebabkan ketersediaan dan kelangkaan CO2 untuk konsumsi tanaman berkurang, 
sehingga menjadi faktor pembatas fotosintesis. Eksperimen menunjukkan bahwa peningkatan konsentrasi karbon dioksida menyebabkan peningkatan laju fotosintesis jika cahaya dan suhu bukan merupakan 
faktor pembatas. Namun, CO2 mulai terakumulasi setelah batas tertentu dan memperlambat proses fotosintesis, bahkan mungkin menghambatnya.
**3. Suhu**
Semua proses biokimia dan biologi terjadi pada kisaran suhu optimum pada semua organisme hidup. Fotosintesis juga merupakan proses biologis, dan laju fotosintesis telah diamati meningkat pada 
rentang suhu 6 hingga 37 derajat Celcius. Jaringan tanaman mati pada suhu 43 derajat Celcius, sehingga terjadi penurunan fotosintesis secara tiba-tiba. Suhu yang lebih tinggi juga menyebabkan 
denaturasi protein dan inaktivasi enzim yang terlibat, yang pada gilirannya mengatur reaksi gelap enzimatik fotosintesis. Di atas 25-30 derajat Celcius, laju fotosintesis menurun.
""")

# --- Pigmen Fotosintetik ---
st.header("Pigmen Fotosintetik")
st.image("assets/images/pigment_spectrum.png", caption="Spektrum Pigmen")
st.write("""
- Klorofil a  
- Klorofil b  
- Karotenoid  
""")

# --- Ringkasan & Kesimpulan ---
st.markdown("---")
st.subheader("Kesimpulan")
st.write("""
Fotosintesis adalah proses kompleks tetapi sangat penting...  
(ditambah kesimpulan ringkas)
""")

df_light = pd.read_csv("assets/graphs/kurva_cahaya.csv")
st.line_chart(df_light, x="Light", y="Rate")

df_co2 = pd.read_csv("assets/graphs/grafik_co2.csv")
st.line_chart(df_co2, x="CO2", y="Rate")
