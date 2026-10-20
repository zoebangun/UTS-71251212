import streamlit as st
from logout import logout
from data import user_data_by_username, participant_data_by_id, event_data

st.set_page_config(page_title="DwTix - Beli Tiket")

# Soal 2: cek akses halaman ini
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")
elif st.session_state.role not in ["Peserta", "Pengunjung"]:
    st.switch_page("pages/dashboard.py")

logout()
st.title("Beli Tiket")

info = event_data()["info"]
peserta = participant_data_by_id()
user = user_data_by_username()[st.session_state.uname]
user_id = st.session_state.id

st.write(f"{info['nama']}  |  Harga: Rp{info['harga_tiket']:,}  |  Kuota: {info['kuota']}")

# Soal 4a: CREATE - tombol "Beli Tiket"
if st.button("Beli Tiket", type="primary"):
    # cek kelengkapan profile
    incomplete = (
        user["email"] is None or str(user["email"]).strip() == "" or
        user["gender"] is None or str(user["gender"]).strip() == "" or
        user["phone"] is None or str(user["phone"]).strip() == "" or
        user["address"] is None or str(user["address"]).strip() == ""
    )
    if incomplete:
        st.error("Profile belum lengkap, lengkapi dulu sebelum membeli tiket.")
    elif len(peserta) >= info["kuota"]:
        st.error("Kuota tiket sudah habis.")
    else:
        # buat ID baru berurutan
        existing_ids = list(peserta.keys())
        # ambil angka terbesar dari ID
        max_num = 0
        for pid in existing_ids:
            try:
                num = int(pid.replace("ID", ""))
                if num > max_num:
                    max_num = num
            except:
                pass
        new_id = f"ID{max_num+1}"
        peserta[new_id] = {
            "user_id": user_id,
            "status_bayar": "Paid",
            "status_tiket": "Belum Check-In"
        }
        st.success(f"Tiket berhasil dibeli dengan ID {new_id}")

# tampilkan sisa kuota (SUDAH JADI)
st.write(f"Sisa kuota: {info['kuota'] - len(peserta)}")

# Soal 4b: READ - subheader "Tiket Saya"
st.subheader("Tiket Saya")
my_tickets = []
for pid, pdata in peserta.items():
    if pdata["user_id"] == user_id:
        my_tickets.append((pid, pdata))

if len(my_tickets) == 0:
    st.info("Kamu belum punya tiket.")
else:
    for pid, pdata in my_tickets:
        st.write(f"{pid} | Status Bayar: {pdata['status_bayar']} | Status Tiket: {pdata['status_tiket']}")
