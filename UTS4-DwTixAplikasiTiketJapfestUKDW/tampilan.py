import streamlit as st

# KODE INI DIBERIKAN KE MAHASISWA (tidak perlu dikerjakan)
# rows: list of dict dengan key "id", "nama", "status_bayar", "status_tiket"
def tampil_peserta(rows):
    st.subheader("Daftar Peserta")
    st.caption(f"Menampilkan {len(rows)} peserta")

    if len(rows) == 0:
        st.info("Tidak ada peserta yang cocok.")
        return

    st.dataframe(
        [
            {
                "ID": r["id"],
                "Nama": r["nama"],
                "Status Bayar": r["status_bayar"],
                "Status Tiket": r["status_tiket"],
            }
            for r in rows
        ],
        hide_index=True,
        use_container_width=True,
    )
