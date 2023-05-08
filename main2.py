import streamlit as st
import numpy as np

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

# Mengatur halaman samping (sidebar)
st.sidebar.title("Navigasi")
options = ["BMI Calculator","BMR Calculator" , "TDEE Calculator"]
choice = st.sidebar.selectbox("Pilih Halaman", options)

# Mengisi halaman utama dengan konten
if choice == "BMI Calculator":
    
    st.title('Body Mass Index Calculator')
    st.write("""
    Indeks massa tubuh (IMT) alias body mass index (BMI) adalah ukuran standar status gizi seseorang yang dilihat dari tinggi serta berat   badan.
    \nBerikut hasil BMI yang bisa Anda cocokkan.\n
    Berat badan kurang: kurang dari 18,5.\n
    Normal: 18,5 – 22,9.\n
    Berat badan berlebih: 23 – 24,9.\n
    Obesitas: 25 ke atas.
             """)

    berat_badan = st.text_input('Masukkan data Berat Badan: ')
    tinggi_badan = st.text_input('Masukkan data Tinggi Badan: ')

    if berat_badan and tinggi_badan:
        body_mass_index = bmi(berat_badan, tinggi_badan)
        st.write('BMI:', body_mass_index)
        if body_mass_index <18.5:
            st.write('Berat Badan anda Kurang!')
        elif body_mass_index in range (18.5,22.9,0.1):
            st.write('Berat Badan anda Normal!')
        elif body_mass_index in range(23.0,24.9,0.1):
            st.write('Berat Badan anda Berlebihan')
        else:
            st.write('Anda Obesitas!')
    
elif choice == "BMR Calculator":
    st.title("BMR Calculator")
    st.write("penghitung basal metabolic rate")
    
    gender = st.selectbox('Pilih jenis kelamin:', ['Pria', 'Wanita'])
    berat_badan_bmr = st.text_input('Masukkan data Berat Badan: ')
    tinggi_badan_bmr = st.text_input('Masukkan data Tinggi Badan: ')
    usia = st.text_input('Masukkan Usia anda: ')

    if berat_badan_bmr and tinggi_badan_bmr and usia:
        if gender == 'Pria':
            bmr = bmr_m(berat_badan_bmr,tinggi_badan_bmr,usia)
            st.write(f'BMR anda adalah {bmr}')
            # Menampilkan konten untuk BMR Pria
        elif gender == 'Wanita':
            bmr = bmr_f(berat_badan_bmr,tinggi_badan_bmr,usia)
            st.write(f'BMR anda adalah {bmr}')
            # Menampilkan konten untuk BMR Wanita

elif choice == "TDEE Calculator":
    st.title("TDEE Calculator")
    st.write("penghitung basal metabolic rate")
    
    gender = st.selectbox('Pilih jenis kelamin:', ['Pria', 'Wanita'])
    berat_badan_t = st.text_input('Masukkan data Berat Badan: ')
    tinggi_badan_t = st.text_input('Masukkan data Tinggi Badan: ')
    usia_t = st.text_input('Masukkan Usia anda: ')
    
    aktif = st.selectbox('Pilih jenis kelamin:', ['Pilih intensitas Aktifitas mu','Jarang berolahraga','Berolahraga 1-3 hari per minggu', 'Berolahraga 3-5 hari per minggu', 'Berolahraga 6-7 hari per minggu', 'Memiliki pekerjaan fisik yang berat atau berolahraga dua kali dalam sehari'])
    
    if berat_badan_t and tinggi_badan_t and usia_t:
        if gender == 'Pria':
            bmr = bmr_m(berat_badan_t,tinggi_badan_t,usia_t)
            # Menampilkan konten untuk BMR Pria
        elif gender == 'Wanita':
            bmr = bmr_f(berat_badan_t,tinggi_badan_t,usia_t)
            # Menampilkan konten untuk BMR Wanita
        
        tdee_value = tdee(bmr,aktif)
        st.write('TDEE anda adalah: ',tdee_value)
    
    
    


    

    


