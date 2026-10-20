import streamlit as st
from pathlib import Path
from logout import logout
from data import event_data

st.set_page_config(page_title="DwTix - Event")

# Soal 2: cek akses halaman ini
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")
# semua role boleh membuka halaman ini

logout()

# ambil role user
role = st.session_state.role
img_path = Path(__file__).parent.parent / "japfest.png"
st.image(img_path)

# tentukan hak edit
can_edit = role in ["Admin", "Staff"]

# ambil data event
event = event_data()
info = event["info"]

# tampilkan info utama
if can_edit:
    with st.expander("Edit Info Event"):
        nama = st.text_input("Nama Event", value=info["nama"])
        tanggal = st.text_input("Tanggal", value=info["tanggal"])
        lokasi = st.text_input("Lokasi", value=info["lokasi"])
        deskripsi = st.text_area("Deskripsi", value=info["deskripsi"])
        harga = st.number_input("Harga Tiket", min_value=0, step=5000, value=info["harga_tiket"])
        kuota = st.number_input("Kuota", min_value=0, step=1, value=info["kuota"])
        if st.button("Simpan", type="primary"):
            info["nama"] = nama
            info["tanggal"] = tanggal
            info["lokasi"] = lokasi
            info["deskripsi"] = deskripsi
            info["harga_tiket"] = int(harga)
            info["kuota"] = int(kuota)
            st.rerun()
else:
    st.title(info["nama"])
    st.write(f"{info['tanggal']}  |  {info['lokasi']}")
    st.write(info["deskripsi"])
    st.write(f"🎟️ Harga tiket: Rp{info['harga_tiket']:,}  |  Kuota: {info['kuota']} orang")

st.divider()

# tampilkan list sponsor/pengisi acara/rundown
def tampil_list(judul, key, kolom):
    st.subheader(judul)

    if len(event[key]) == 0:
        st.info(f"Belum ada data {judul.lower()}.")

    pilihan = []
    for item in event[key]:
        teks = " — ".join(str(item[k]) for k in kolom)
        st.write(teks)
        pilihan.append(teks)

    # hapus data
    if can_edit and len(pilihan) > 0:
        dipilih = st.selectbox(f"Pilih {judul} yang mau dihapus", pilihan)
        if st.button(f"Hapus {judul}"):
            idx = pilihan.index(dipilih)
            del event[key][idx]
            st.rerun()

    # tambah data
    if can_edit:
        with st.form(f"form_{key}", clear_on_submit=True):
            st.write(f"Tambah {judul}")
            data_baru = {}
            for k in kolom:
                data_baru[k] = st.text_input(k.replace("_", " ").title())
            if st.form_submit_button("Tambah"):
                kosong = any(v is None or str(v).strip() == "" for v in data_baru.values())
                if kosong:
                    st.error("Semua field wajib diisi!")
                else:
                    event[key].append(data_baru)
                    st.rerun()

tampil_list("Sponsor", "sponsor", ["nama", "tier"])
st.divider()
tampil_list("Pengisi Acara", "pengisi_acara", ["nama", "jenis"])
st.divider()
tampil_list("Rundown", "rundown", ["jam", "acara"])
