import streamlit as st
import pandas as pd
import numpy as np
import time

import requests
from bs4 import BeautifulSoup

def crawl_real_data():
    url = "https://nemesis.assai.id/"
    # CATATAN: Pastikan website mengizinkan scraping (cek robots.txt)
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # ... Logika untuk mencari elemen HTML (misal <h2>, <a>, dll) ...
        # ... Ekstrak teksnya dan masukkan ke dalam list/DataFrame ...
        return data_yang_sudah_diekstrak
    else:
        return error_message

st.set_page_config(
    page_title="Rahasia Indonesia Dashboard",
    page_icon="🕸️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Mengubah warna teks utama */
    .css-1d391kg {
        padding-top: 1rem;
    }
    
    /* Efek glow pada judul */
    h1 {
        text-shadow: 0 0 10px #00ff00;
        color: #00ff00 !important;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Styling untuk kartu metrik */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #00ff00;
    }
    [data-testid="stMetricDelta"] {
        color: #ff4b4b; /* Merah untuk alert */
    }
    
    /* Background gradient tipis */
    .stApp {
        background: linear-gradient(180deg, rgba(14,17,23,1) 0%, rgba(20,30,40,1) 100%);
    }
    
    /* Mengubah warna font sidebar */
    .css-1vq4p4l {
        padding: 2rem 1rem;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def simulate_crawling_data():
    """Fungsi ini menghasilkan data palsu untuk simulasi."""
    # Data Artikel/Laporan
    reports_data = {
        "ID": [f"RI-{i:03d}" for i in range(1, 11)],
        "Judul": [
            "Analisis Malware XYZ Varian Baru",
            "Kerentanan Kritis pada Protokol SSH",
            "Kebocoran Data Database Pelanggan E-commerce",
            "Deteksi Serangan DDoS Skala Besar",
            "Update: Ransomware Kelompok 'Phantom'",
            "Eksploitasi Zero-Day Ditemukan di Browser",
            "Panduan Mitigasi Phishing Internal",
            "Laporan Insiden: Akses Ilegal Jaringan Korporat",
            "Tinjauan Keamanan API Perbankan",
            "Tren Ancaman Siber Kuartal 3"
        ],
        "Kategori": ["Malware", "Vulnerability", "Data Breach", "Network", "Ransomware", "Vulnerability", "Phishing", "Incident", "AppSec", "Threat Intel"],
        "Tingkat Bahaya": ["Tinggi", "Kritis", "Tinggi", "Sedang", "Kritis", "Kritis", "Sedang", "Tinggi", "Sedang", "Rendah"],
        "Tanggal": pd.date_range(end=pd.Timestamp.today(), periods=10).strftime("%Y-%m-%d")
    }
    df_reports = pd.DataFrame(reports_data)
    
    # Data Statistik Sistem (untuk chart)
    chart_data = pd.DataFrame(
        np.random.randn(20, 3) * [10, 5, 2] + [50, 20, 5],
        columns=['Ancaman Diblokir', 'Percobaan Login Gagal', 'Pemindaian Port']
    )
    
    return df_reports, chart_data

df_reports, chart_data = simulate_crawling_data()

with st.sidebar:
    st.image("https://placehold.co/200x100/111/0f0?text=RAHASIA+INDONESIA", use_container_width=True)
    st.markdown("## Kontrol Panel")
    st.markdown("Dashboard ini menampilkan simulasi data yang dikumpulkan dari berbagai sumber intelijen.")
    
    # Filter Interaktif
    st.markdown("### Filter Data")
    kategori_terpilih = st.multiselect(
        "Pilih Kategori:",
        options=df_reports["Kategori"].unique(),
        default=df_reports["Kategori"].unique()[:3]
    )
    
    tingkat_bahaya = st.selectbox(
        "Tingkat Bahaya:",
        ["Semua", "Kritis", "Tinggi", "Sedang", "Rendah"]
    )
    
    st.markdown("---")
    st.markdown("Status Sistem: **ONLINE** 🟢")
    if st.button("Jalankan Ulang Crawler"):
        with st.spinner("Mengumpulkan data terbaru..."):
            time.sleep(2) # Simulasi waktu tunggu
        st.success("Data berhasil diperbarui!")
        st.rerun()

st.title("🕸️ RAHASIA INDONESIA Aggregator")
st.markdown("<p style='text-align: center; color: #888;'>Sistem Pemantauan dan Pengumpulan Data Ancaman Terpadu</p>", unsafe_allow_html=True)
st.divider()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Total Sumber Dipantau", value="142", delta="5 Baru")
with col2:
    st.metric(label="Insiden Kritis Hari Ini", value="3", delta="-2 Menurun", delta_color="inverse")
with col3:
    st.metric(label="Volume Data (GB)", value="45.2", delta="1.2 GB")
with col4:
    st.metric(label="Status Jaringan", value="Aman", delta="100% Uptime")

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("📊 Aktivitas Ancaman (24 Jam Terakhir)")
st.area_chart(chart_data, color=["#ff0000", "#ffaa00", "#00ff00"])

df_filtered = df_reports[df_reports["Kategori"].isin(kategori_terpilih)]
if tingkat_bahaya != "Semua":
    df_filtered = df_filtered[df_filtered["Tingkat Bahaya"] == tingkat_bahaya]

st.subheader("📑 Laporan Intelijen Terbaru")
st.markdown("Berikut adalah hasil pengambilan data simulasi dari target:")

# Mewarnai sel berdasarkan tingkat bahaya
def color_danger(val):
    color = 'green'
    if val == 'Kritis':
        color = 'red'
    elif val == 'Tinggi':
        color = 'orange'
    elif val == 'Sedang':
        color = 'yellow'
    return f'color: {color}'

st.dataframe(
    df_filtered.style.map(color_danger, subset=['Tingkat Bahaya']),
    use_container_width=True,
    hide_index=True
)

st.divider()
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.8rem;'>
    <p>Data yang ditampilkan adalah simulasi (Mock Data). Crawler backend sesungguhnya memerlukan script terpisah.</p>
    <p>Powered by Streamlit | Developed for Rahasia Indonesia</p>
</div>
""", unsafe_allow_html=True)
