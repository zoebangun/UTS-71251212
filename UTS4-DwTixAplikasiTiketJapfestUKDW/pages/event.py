import streamlit as st
from pathlib import Path
from logout import logout
from data import user_data_by_username, event_data

st.set_page_config(page_title="DwTix - Event")

# TODO (Soal 2): cek akses halaman ini
#   - belum login -> pindah ke "app.py"
#   (semua role boleh membuka halaman ini)

logout()
# tampilkan list (sponsor / pengisi acara / rundown), kalau can_edit muncul pilihan + tombol hapus dan form tambah (SUDAH JADI: daftar, selectbox, st.form dan input-nya)
def tampil_list(judul, key, kolom, can_edit):
    event = event_data()
    st.subheader(judul)

    if len(event[key]) == 0:
        st.info(f"Belum ada data {judul.lower()}.")

    pilihan = []
    for item in event[key]:
        teks = " — ".join(str(item[k]) for k in kolom)
        st.write(teks)
        pilihan.append(teks)

    # hapus data, buat admin dan staff
    if can_edit and len(pilihan) > 0:
        dipilih = st.selectbox(f"Pilih {judul} yang mau dihapus", pilihan)
        # TODO (Soal 5b): tombol dengan label f"Hapus {judul}" (contoh: "Hapus Sponsor")
        # HINT Membuat angka selalu 4 digit -> angka:04d -> 0000, 0001, dst
        #   klik -> item yang dipilih di selectbox dihapus dari event[key], lalu st.rerun()
        #   cara ambil index dari item yang dipilih di selectbox
        #   misal pilihan: ['Sponsor A - Gold', 'Sponsor B - Silver'], dipilihan index 0
        #   event_key: [{'nama':'Sponsor A', 'tier':'Gold'}, {'nama':'Sponsor B', 'tier':'Silver'}] pakai pilihan.index("Sponsor A")
        #   jadi index 0 di pilihan -> index 0 di event_key
        #   HINT : urutan isi list pilihan sama dengan urutan isi event[key]
        pass

    # form tambah data, buat admin dan staff
    if can_edit:
        with st.form(f"form_{key}", clear_on_submit=True):
            st.write(f"Tambah {judul}")
            data_baru = {}
            for k in kolom:
                data_baru[k] = st.text_input(k.replace("_", " ").title())
            if st.form_submit_button("Tambah"):
                # TODO (Soal 5c): proses data_baru
                # HINT : Silahkan cek bentuk tipe datanya apa biar tahu cara nambahinnya pakai apa
                #   - kalau ada field yang kosong / hanya spasi: st.error("Semua field wajib diisi!")
                #   - kalau semua terisi: tambahkan data_baru ke event[key], lalu st.rerun()
                pass


# untuk determine bisa ga edit ni page
def konten(can_edit):
    event = event_data()
    info = event["info"]


    # edit info utama event
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
    else :
        st.title(info["nama"])
        st.write(f"{info['tanggal']}  |  {info['lokasi']}")
        st.write(info["deskripsi"])
        st.write(f"🎟️ Harga tiket: Rp{info['harga_tiket']:,}  |  Kuota: {info['kuota']} orang")

    st.divider()
    tampil_list("Sponsor", "sponsor", ["nama", "tier"], can_edit)
    st.divider()
    tampil_list("Pengisi Acara", "pengisi_acara", ["nama", "jenis"], can_edit)
    st.divider()
    tampil_list("Rundown", "rundown", ["jam", "acara"], can_edit)


role = st.session_state.role
img_path = Path(__file__).parent.parent / "japfest.png"
st.image(img_path)

# TODO (Soal 5a): tentukan apakah user boleh mengubah isi halaman ini
#   hanya Admin dan Staff yang boleh; Peserta dan Pengunjung hanya melihat
can_edit = False   # <- ganti dengan pengecekan role
konten(can_edit)
