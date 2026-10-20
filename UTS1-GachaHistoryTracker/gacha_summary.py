import streamlit as st
from history_gacha import history_gacha

st.title("Gacha History Tracker")

# TODO 1: Buat pilihan pengurutan waktu dengan st.radio () dengan pilihan "Terbaru (Descending)" atau "Terlama (Ascending)"
urutan = st.radio("Urutkan Berdasarkan Waktu Pull:", ("Terbaru (Descending)", "Terlama (Ascending)"))

# TODO 2: Tentukan is_descending berdasarkan value urutan
if urutan == "Terbaru (Descending)":
    is_descending = True
else:
    is_descending = False

# TODO 3: Urutkan data berdasarkan timestamp
sorted_history = list(history_gacha)
n = len(sorted_history)

# GUNAKAN BUBBLE SORT
# 1. Buat nested loop untuk mengambil data 2 item
# 2. Bandingkan nilai "timestamp" antara kedua elemen tersebut berdasarkan status is_descending
# 3. Lakukan penukaran posisi elemen (swapping) jika posisi timestamp tidak sesuai dengan urutan yang dipilih
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if is_descending:
            if sorted_history[j]["timestamp"] < sorted_history[j + 1]["timestamp"]:
                temp = sorted_history[j]
                sorted_history[j], sorted_history[j + 1] = sorted_history[j + 1], temp
        else:
            if sorted_history[j]["timestamp"] > sorted_history[j + 1]["timestamp"]:
                temp = sorted_history[j]
                sorted_history[j], sorted_history[j + 1] = sorted_history[j + 1], temp

# TODO 4: Kelompokkan item bintang 5 dan 4 menggunakan perulangan for biasa
five_stars = []
four_stars = []

for item in history_gacha:
    #jika 5 star tambahkan ke five_stars
    #jika 4 star tambahkan ke four_stars
    if item["rarity"] == 5:
        five_stars.append(str(item["item"]))
    elif item["rarity"] == 4:
        four_stars.append(str(item["item"]))

# TODO 5: Tampilkan Summary Pity & Drop
st.subheader("Summary Pity & Drop")
col1, col2, col3 = st.columns(3)
col1.metric("Total Pull", len(history_gacha)) #total pull
col2.metric("Total Bintang 5 ", len(five_stars)) #total 5 star
col3.metric("Total Bintang 4 ", len(four_stars)) #total 4 star

# TODO 6: Menampilkan Summary Nama-Nama Bintang 5 & 4

with st.expander("Lihat Summary 5 star & 4 star"):
    # Tampilan Bintang 5
    
    # Tampilan Bintang 4

    if len(five_stars) > 0:
        st.write("Bintang 5:" + ", ".join(five_stars))
    if len(four_stars) > 0:
        st.write("Bintang 4:" + ", ".join(four_stars)) 

st.divider()

# TODO 7: Tampilkan History Pull
st.subheader("History Pull")
for data in sorted_history:

    # jika bintang 5 tampilkan dengan st.warning

    # jika bintang 4 tampilkan dengan st.success

    # selain itu dengan st.info

    # FORMAT TAMPILAN DATA: <Nama Item> (Rarity: <Rarity> star) — <Timestamp>
    text = f"{data["item"]} (Rarity: {data["rarity"]} star) - {data["timestamp"]}"
    if data["rarity"] == 5:
        st.success(text)
    elif data["rarity"] == 4:
        st.info(text)
    else:
        st.write(text)
    
