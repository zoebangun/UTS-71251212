import streamlit as st
from data import user_data_by_username
from logout import logout

st.set_page_config(page_title="DwTix - Profile")

# Soal 2: cek akses halaman ini
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")
# semua role boleh membuka halaman ini

logout()
st.header("Profile", text_alignment="center", divider="green")

with st.expander("Edit Profile"):
    uname = st.text_input("Username", value=st.session_state.uname, disabled=True)
    user = user_data_by_username()[st.session_state.uname]

    email = st.text_input("Email", value=user["email"] if user["email"] is not None else "")
    pword = st.text_input("Password", type="password", value=user["password"] if user["password"] is not None else "")
    gender = st.text_input("Gender", value=user["gender"] if user["gender"] is not None else "")
    phone = st.text_input("Phone", value=user["phone"] if user["phone"] is not None else "")
    address = st.text_input("Address", value=user["address"] if user["address"] is not None else "")

    if st.button("Ubah Data", type="primary"):
        # Soal 3: bandingkan isi form dengan data user yang tersimpan
        data_baru = {
            "email": email,
            "password": pword,
            "gender": gender,
            "phone": phone,
            "address": address,
        }

        perubahan = []
        for key, val in data_baru.items():
            lama = user[key]
            if lama is None:
                lama = ""
            if str(lama) != str(val):
                perubahan.append(key)

        if len(perubahan) == 0:
            st.info("Belum ada perubahan loh ya")
        else:
            for key in perubahan:
                user[key] = data_baru[key]
            st.success(f"{uname}, anda mengubah: {', '.join(perubahan)}")
