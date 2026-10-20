import streamlit as st
from data import user_data_by_username
from logout import logout

# TODO (Soal 2): cek akses halaman ini
#   - belum login -> pindah ke "app.py"
#   (semua role boleh membuka halaman ini)

logout()
st.header("Profile", text_alignment="center", divider="green")

with st.expander("Edit Profile"):
    uname = st.text_input("Username", value=st.session_state.uname, disabled=True )
    email = st.text_input("Email", value=user_data_by_username()[st.session_state.uname]["email"])
    pword = st.text_input("Password", type="password", value=user_data_by_username()[st.session_state.uname]["password"])
    gender = st.text_input("Gender", value=user_data_by_username()[st.session_state.uname]["gender"])
    phone = st.text_input("Phone", value=user_data_by_username()[st.session_state.uname]["phone"])
    address = st.text_input("Address", value=user_data_by_username()[st.session_state.uname]["address"])
    if st.button("Ubah Data", type="primary"):
        # TODO (Soal 3): bandingkan isi form dengan data user yang tersimpan
        #   - data lama yang None dianggap sama dengan "" (kolom kosong)
        #   - kalau tidak ada yang berubah: st.info("Belum ada perubahan loh ya")
        #   - kalau ada: simpan HANYA field yang berubah ke data user,
        #     lalu st.success berisi nama field yang diubah
        pass
