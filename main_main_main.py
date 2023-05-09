import streamlit as st
import numpy as np
import pandas as pd
from io import StringIO


def bmi(berat_badan, tinggi_badan):
    tinggi_m = float(tinggi_badan) / 100  # convert cm to m
    BMI = float(berat_badan) / tinggi_m**2
    return BMI

def bmr_f(berat_badan_bmr,tinggi_badan_bmr,usia):
    BMR_f = (10 * float(berat_badan_bmr)) + (6.25 * float(tinggi_badan_bmr)) - (5 * float(usia)) - 161 
    return BMR_f
    
def bmr_m(berat_badan_bmr,tinggi_badan_bmr,usia):
    BMR_m = (10 * float(berat_badan_bmr)) + (6.25 * float(tinggi_badan_bmr)) - (5 * float(usia)) + 5
    return BMR_m

def tdee(bmr,aktif):
 
    if aktif == 'Jarang berolahraga':
        tdeee = bmr*1.2
    elif aktif == 'Berolahraga 1-3 hari per minggu':
        tdeee = bmr*1.375
    elif aktif == 'Berolahraga 3-5 hari per minggu':
        tdeee = bmr*1.55
    elif aktif == 'Berolahraga 6-7 hari per minggu':
        tdeee = bmr*1.725
    elif aktif == 'Memiliki pekerjaan fisik yang berat atau berolahraga dua kali dalam sehari' :
        tdeee = bmr*1.9
    else :
        tdeee = bmr*1.2
        
         
    return tdeee


# String yang akan dijadikan dataframe
data_karbo = """
Nama_k,kalori_k
Nasi Putih(1 Mangkok),204
Nasi Ketan(1 Mangkok),169
Nasi Uduk(1 Mangkok),260
Nasi Kebuli(1 Mangkok),159
Nasi Padang(1 Bungkus),664
Nasi Hoka Hoka Bento(1 Mangkok),150
Nasi Kuning(1 Mangkok),129
Nasi Goreng Ayam(1 Mangkok),329
Nasi Uduk Komplit(1 Bungkus),476 """


data_protein = """
Nama_p,kalori_p
Ayam goreng(1 Besar),260
Dada Ayam(100 gram),195
Daging Ayam(100 gram),167
Opor Ayam(1 Besar),329
Dada Ayam KFC(1 Besar),520
Fried Chicken(a&w)(1 Besar),360
Ayam MCD Spicy(1 Besar),273
Ikan(100 gram),84
Ikan Tongkol Goreng(100 gram),200
Ikan Kembung(100 gram),167
Ikan Mujair Goreng(100 gram), 169
Ikan Kembung Balado(100 gram),163
Ikan Panggang(100 gram),142
Ikan Tongkol(100 gram), 110
Ikan Layang(100 gram),112
Ikan Nila(100 gram),128 
Ikan Cakalang(100 gram),132
Ikan Bandeng Goreng(100 gram), 233
Ikan Patin(100 gram),90
Ikan Pindang Alfamart(100 gram),153
Telur(1 Besar),74
Telur Rebus(1 Besar),77
Telur Dadar(1 Besar),93
Telur Ceplok(100 gram),201
Telur Orak Arik(1 Besar),98
Telur Balado(1 Butir),71
Telur dengan Sayur(1 Besar), 106
Putih Telur(1 Besar),17
Sayur Campuran,60
Sayuran Rebus(Tanpa Daging),134
Sayur Bening Bayam,36
Sayuran Campur Matang,151
Sup Sayur Vegetarian,72
Sayur Lodeh,162
Lontong Sayur,452
Sayur Asem,80
Sayur Campur Tumis,120
Sayur Tahu Toge 250g, 259
Sayur Pakis,34
Sayuran Mentah(1 mangkok),24
Sayur Nangka(100 gram),66
Tahu Goreng(1 Buah),35
Tahu(100 gram),78
Tahu Kukus(100 gram),78
Tahu Bacem(1 Buah),24
Tahu isi(1 Buah),134
Semur Tahu,71
Oseng Tahu(100 gram),232
Tahu Kuning(100 gram),80
Tahu Sumedang(240 gram),282

"""



# Mengatur sidebar
st.sidebar.title("Navigasi")
options = ["Home Page","BMI Calculator","BMR Calculator" , "TDEE Calculator" , "Kalori list"]
choice = st.sidebar.selectbox("Pilih Halaman", options)

# Mengisi halaman utama dengan konten

if choice == "Home Page":
    st.title('APLIKASI DIET TOOLS')
    st.write('BMI,BMR,TDEE Calculator & Kalori List')
    st.markdown("---")
    st.subheader('Deskripsi')
    st.write('Website ini adalah Aplikasi untuk mencari beberapa parameter penunjang Diet yaitu BMI,BMR,TDEE dan list kalori pada makanan umum. Dengan menghitung keempat paramater tersebut, maka individu yang ingin melakukan Diet baik Menurunkan berat badan maupun Menaikan berat badan akan lebih bisa mendapatkan hasil yang lebih efisien dan maximal. metode perhitungan ini sudah diuji secara empiris oleh para ahli dan akan sangat berguna jika di implementasikan dalam teknik diet. \n')
    st.write("Note: Tekan tombol '>' pada pojok kiri atas untuk memilih Tools")
    st.markdown("---")
    st.subheader("Tujuan")
    st.write("""Web ini dibuat untuk melaksanakan project LPK kelompok 11 yang beranggotakan:\n
    -Deri Hamsa | 218827\n
    -Dimas Bagus Uditya | 2118835 \n
    -Sabrina Annisafitri | 2118980 """)
    
elif choice == "BMI Calculator":
    
    st.title('Body Mass Index Calculator')
    st.markdown("---")
    st.write("""
    Indeks massa tubuh (IMT) alias body mass index (BMI) adalah ukuran standar status gizi seseorang yang dilihat dari tinggi serta berat   badan.
    \nBerikut hasil BMI yang bisa Anda cocokkan.\n
    Berat badan kurang: kurang dari 18,5.\n
    Normal: 18,5 – 22,9.\n
    Berat badan berlebih: 23 – 24,9.\n
    Obesitas: 25 ke atas.\n
    """)
    st.markdown("---")

    
    st.subheader('Input Data')
    berat_badan = st.text_input('Masukkan Berat Badan: ')
    tinggi_badan = st.text_input('Masukkan Tinggi Badan: ')

    st.subheader('Hasil:')
    if berat_badan and tinggi_badan:
        body_mass_index = bmi(berat_badan, tinggi_badan)
        st.write(f"<h1 style='color: white; font-size: 15px; font-family: Arial'>BMI: {body_mass_index}</h1>", unsafe_allow_html=True)
        if body_mass_index <18.5:
            st.write('Berat Badan anda Kurang!')
        elif body_mass_index in np.arange (18.5,22.9,0.1):
            st.write('Berat Badan anda Normal!')
        elif body_mass_index in np.arange(23.0,24.9,0.1):
            st.write('Berat Badan anda Berlebihan')
        else:
            st.write('Anda Obesitas! Segera Atur Pola Makan!')
    st.markdown("---")
            
    
elif choice == "BMR Calculator":
    st.title("Basal Methabolic Rate Calculator")
    st.markdown("---")
    st.write("""Basal Metabolic Rate merupakan kebutuhan kalori minimal yang dibutuhkan untuk bertahan hidup pada saat kondisi tubuh sedang beristirahat tanpa melakukan kegiatan apa-apa. Jumlah tersebut merupakan jumlah kalori yang dibakar jika kita tidur selama 24 jam.
             \nBasal Metabolic Rate adalah dasar dari pencarian TDEE, anda bisa mencari TDEE menggunakan web ini juga.
             """)
    st.markdown("---")

    
    st.subheader("Input Data")
    gender = st.selectbox('Pilih jenis kelamin:', ['Pria', 'Wanita'])
    berat_badan_bmr = st.text_input('Masukkan Berat Badan: ')
    tinggi_badan_bmr = st.text_input('Masukkan Tinggi Badan: ')
    usia = st.text_input('Masukkan Usia anda: ')

    if berat_badan_bmr and tinggi_badan_bmr and usia:
        if gender == 'Pria':
            bmr = bmr_m(berat_badan_bmr,tinggi_badan_bmr,usia)
            st.subheader("Hasil:")
            st.write(f'BMR anda adalah {bmr}')
        elif gender == 'Wanita':
            bmr = bmr_f(berat_badan_bmr,tinggi_badan_bmr,usia)
            st.subheader("Hasil:")
            st.write(f'BMR anda adalah {bmr}')
          
elif choice == "TDEE Calculator":
    st.title("Total Daily Energy Expenditure (TDEE) Calculator")
    st.markdown("---")
    st.write("Jumlah total kalori yang kamu bakar setiap hari disebut total pengeluaran energi harian atau total daily energy expenditure (TDEE). Perhitungan TDEE meliputi: \n kalori yang dibakar melalui kegiatan olahraga maupun kalori yang dibakar melalu kegiatan non-olahraga")
    st.markdown("---")
    
    st.subheader("Input Data")
    gender = st.selectbox('Pilih jenis kelamin:', ['Pria', 'Wanita'])
    berat_badan_t = st.text_input('Masukkan Berat Badan: ')
    tinggi_badan_t = st.text_input('Masukkan Tinggi Badan: ')
    usia_t = st.text_input('Masukkan Usia anda: ')
    
    aktif = st.selectbox('Pilih Intensitas Aktifitas mu:', ['Pilih intensitas Aktifitas mu','Jarang berolahraga','Berolahraga 1-3 hari per minggu', 'Berolahraga 3-5 hari per minggu', 'Berolahraga 6-7 hari per minggu', 'Memiliki pekerjaan fisik yang berat atau berolahraga dua kali dalam sehari'])
    st.subheader("Hasil:")
    if berat_badan_t and tinggi_badan_t and usia_t:
        if gender == 'Pria':
            bmr = bmr_m(berat_badan_t,tinggi_badan_t,usia_t)
            # Menampilkan konten untuk BMR Pria
        elif gender == 'Wanita':
            bmr = bmr_f(berat_badan_t,tinggi_badan_t,usia_t)
            # Menampilkan konten untuk BMR Wanita
        
        
        tdee_value = tdee(bmr,aktif)
        tdee_value_cut = tdee_value - 500
        tdee_value_bulk = tdee_value + 500
        st.write('TDEE anda adalah: ',tdee_value, '\nJika anda ingin melakukan cutting maka kurangi 500 dari TDEE anda, yaitu senilai: ',tdee_value_cut, '\nJika anda ingin melakukan Bulking maka tambahkan 500 kalori dari TDEE anda yaitu senilai :', tdee_value_bulk , '\nPengurangan atau penambahan kalori tersebut adalah jumlah yg disarankan oleh Ahli, jika anda menguranginya senilai jumlah itu, anda akan mengurangi/menambah 2kg lemak dalam waktu satu bulan, memang terlihat kecil, tetapi itu adalah murni lemak tanpa dihitung berkurangnya massa air dan lain lain.\n')
        st.markdown("---")

elif choice == "Kalori list":
    st.title("Kalori List")
    st.markdown("---")
    st.write("""Page ini adalah informasi tentang perkiraan jumlah kalori dalam bahan makanan umum. kalori ini dihitung dari jumlah karbohidrat,protein dan lemak, dimana secara berurutan memiliki 4,4 dan 9 kalori.\n
    Page ini juga dilengkapi dengan Kalori checklist, Anda dapat menchecklist bahan makanan tersebut, dan jumlah kalori dan semua makanan tersebut akan dijumlahkan dibawah.\n""")
    st.markdown("---")
    
    st.subheader('List kalori Makanan Umum :\n')
        
# Buat dictionary untuk menyimpan makanan/minuman yang dipilih beserta kalori
    selected_items = {}

#     if st.button("Tekan jika anda ingin melihat berapa kalori yg ada dalam makanan umum"):

    # Buat dataframe dari string
    df_karbo = pd.read_csv(StringIO(data_karbo))
    df_protein = pd.read_csv(StringIO(data_protein))
#     df_sayur = pd.read_csv(StringIO(data_sayur))
            
            
    col1, col2, col3 = st.columns(3)

    with col1:
#         st.header("")
#         st.image("")
        for index, row in df_karbo.iterrows():
            st.write('\n',row['Nama_k'], row['kalori_k'])
            if st.checkbox('Tambah Makanan ini', key=f'tambah1_{index}_k'):
                # Tambahkan makanan/minuman yang dipilih beserta kalori ke dictionary
                selected_items[row['Nama_k']] = row['kalori_k']

    with col2:
#         st.header("")
#         st.image("")

        for index, row in df_protein.iterrows():
            st.write('\n',row['Nama_p'], row['kalori_p'])
            if st.checkbox('Tambah Makanan ini', key=f'tambah1_{index}_p'):
                # Tambahkan makanan/minuman yang dipilih beserta kalori ke dictionary
                selected_items[row['Nama_p']] = row['kalori_p']


    with col3:
#         st.header("")
#         st.image("")

        # Hitung total kalori dari semua makanan/minuman yang dipilih
        total_kalori = sum(selected_items.values())

        # Tampilkan total kalori
        st.write("Total kalori:", total_kalori) 
    
    
    


    
    
    
    
    
    

    
                

                              
    
    
    


    

    


