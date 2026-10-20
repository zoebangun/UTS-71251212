import streamlit as st
from data import user_data_by_username

def main():
    # set tab title -> https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation silahkan >
    st.set_page_config(page_title="DwTix - Login")

    # TODO (Soal 1a): deklarasi sesi
    #   - siapkan logged_in = False, uname = None, id = None, role = None di st.session_state
    #     HANYA jika belum ada (supaya tidak ter-reset saat halaman dimuat ulang)
    #   - kalau sudah login (user membuka app.py / form login lagi) -> pindah ke "pages/event.py"

    # kalau misal ada error itu gara gara versi streamlit minimal 1.52.0 ya
    # silahkan up pakai pip install --upgrade streamlit
    # page header (SUDAH JADI)
    st.header("Selamat datang kembali", text_alignment="center", divider="green")
    st.write("*Silahkan masuk menggunakan akun DwTix anda*")

    user_by_name = user_data_by_username()
    # form (SUDAH JADI)
    uname = st.text_input(label="Username", required=True)
    pword = st.text_input(label="Password", type="password", required=True)

    # submit
    if st.button(label="Login", type="primary"):
        # TODO (Soal 1b): cek login
        #   - username terdaftar dan password cocok -> simpan logged_in, uname, id, role ke st.session_state
        #   - salah -> st.error("Login gagal! Silahkan coba kembali.")
        #   - username yang TIDAK terdaftar tidak boleh membuat aplikasi error
        # TODO (Soal 1c): arah setelah login berhasil
        #   - Admin dan Staff -> "pages/dashboard.py"
        #   - role lain       -> "pages/event.py"
        pass

if __name__ == '__main__':
    main()
