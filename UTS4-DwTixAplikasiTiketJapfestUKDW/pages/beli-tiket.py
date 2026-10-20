import streamlit as st
from logout import logout
from data import user_data_by_username, participant_data_by_id, event_data

st.set_page_config(page_title="DwTix - Beli Tiket")

# TODO (Soal 2): cek akses halaman ini
#   - belum login -> pindah ke "app.py"
#   - role selain Peserta dan Pengunjung -> pindah ke "pages/dashboard.py"

logout()
st.title("Beli Tiket")

info = event_data()["info"]
peserta = participant_data_by_id()
user = user_data_by_username()[st.session_state.uname]
user_id = st.session_state.id

st.write(f"{info['nama']}  |  Harga: Rp{info['harga_tiket']:,}  |  Kuota: {info['kuota']}")

# TODO (Soal 4a) CREATE - tombol "Beli Tiket"
#   Tolak pembelian (st.error) kalau:
#   - data profile belum lengkap: email, gender, phone, address ada yang None / kosong / hanya spasi
#   - kuota habis: jumlah tiket di `peserta` sudah >= info["kuota"]
#   Kalau lolos, tambahkan ke `peserta` dengan ID baru berurutan (ID02, ID03, ...):
#   {"user_id": user_id, "status_bayar": "Paid", "status_tiket": "Belum Check-In"}
#   lalu tampilkan st.success

# tampilkan sisa kuota (SUDAH JADI)
st.write(f"Sisa kuota: {info['kuota'] - len(peserta)}")

# TODO (Soal 4b) READ - subheader "Tiket Saya"
#   tampilkan HANYA tiket milik user yang login (ID, status bayar, status tiket)
#   kalau belum punya: st.info("Kamu belum punya tiket.")
#   petunjuk: tiket milik user = tiket yang `user_id`-nya sama dengan user_id di atas
