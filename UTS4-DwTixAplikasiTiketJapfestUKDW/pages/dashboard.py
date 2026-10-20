import streamlit as st
from logout import logout
from data import user_data_by_username, participant_data_by_id
from tampilan import tampil_peserta

st.set_page_config(page_title="DwTix - Dashboard")

# TODO (Soal 2): cek akses halaman ini
#   - belum login -> pindah ke "app.py"
#   - role selain Admin dan Staff -> pindah ke "pages/event.py"

# JANGAN PERNAH RAGU UNTUK CEK DATA PAKAI st.write() ya dari pada ngawang
st.title(f"Welcome, {st.session_state.role} 👋")
logout()

# gabungkan data peserta dengan nama user (SUDAH JADI)
users = user_data_by_username()
rows = []
for pid, p in participant_data_by_id().items():
    nama = next(u for u, d in users.items() if d["id"] == p["user_id"])
    rows.append({"id": pid, "nama": nama, "status_bayar": p["status_bayar"], "status_tiket": p["status_tiket"]})

# tabel peserta, beli = Paid, undangan = Invitation (SUDAH JADI)
tampil_peserta(rows)
