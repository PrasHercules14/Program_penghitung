print("\n <<<<<< Selamat Datang Users >>>>>> \n")
print("Perkenalkan namaku adalah Dwayne bruce pras, panggil saja Pras")
print("Note: Script ini digunakan sebagai tool menghitung rumus-rumus sederhana saja \r\nBukan untuk keperluan ilegal seperti hacking.")
print(" ===================")
print("| Bruce Pras Script | ")
print("|___________________|")
print("          |")
print("          |")
print("          |")
print(" -------------------")
print(" Developing by Pras")
print(" -------------------")
print("\rScript ini tentu saja didapatkan secara gratis dan open source, artinya kalian dapat memodifikasi atau")
print("Mengubah sumber kode didalamnya atau mendistribusikan ulang secara bebas.")
# diatas adalah opening dan perkenalan nama diri saya sendiri
print("\n PERKENALAN DIRI TERLEBIH DAHULU \n") # stage pertama perkenalan diri terlebih dahulu
'''
      {---} Materi Yang Akan Di Bahas Nanti {---}
   1. Perkenalan diri
   2. Menjumlahkan bilangan tugas-tugas sekolah
   3. Membandingkan semua bilangan yang diinputkan oleh user
   4. Hasil operation assignment
'''
nama_user = input("Siapa namamu: ")
print("Hai", nama_user, "salam kenal") # greeting user name
print("- Tipe data namamu adalah: ", type(nama_user)) # ini adalah tipe data pada user
# diatas adalah nama user
print("\nNote: saat mengisi usia, pastikan menggunakan angka saja jangan huruf atau angka dikombinasikan dengan huruf.")
usia_user = int(input("Berapakah usiamu: "))
print("Oooo.. jadi usiamu saat ini adalah: ", usia_user, ", berarti udah gedhe dong.. wkwkwkw") # umur nya udah tua.. awokawokawok
print("- Tipe data usiamu adalah: ", type(usia_user)) # ini adalah tipe data usia user
# diatas adalah usia user
alamat_user = input("\nMasukan alamatmu: ")
print("Jadi alamat rumahmu di: ", alamat_user, "ya?")
print("- Tipe data alamatmu adalah: ", type(alamat_user)) # ini adalah tipe data pada alamat user
# diatas adalah alamat user yang sekarang ia berada
nomor_telepon = int(input("\nMasukan nomor telepon: "))
print("- Mac address: ", hex(id(nomor_telepon))) # mac address digunakan sebagai alat penanda atau token dari variable itu
print("Terima kasih banyak", nama_user, "yang telah mengisi formulir ini, saya harap anda dapat menjawab soal-soal \r\nTugas sekolah anda")
print("Dan menghitungnya dengan baik")
# diatas adalah nomor telepon user
# dan terima kasih buat anda yang telah memasukan identitas diri
print("\n MENGHITUNG RUMUS-RUMUS SEDERHANA \n") # stage kedua yaitu user dipersilahkan menghitung rumus-rumus nya
print("Note: kalian dapat mengubah/mengganti angka nya sesuka hati untuk menghitung bilanganya") # alert for users
print("Oh iya, sekalian dibawah ini ada berupa operation assignment nya juga ya.. hehehehehe \r\n") # alert for users 2nd
masukan1 = int(input("Masukan angka yang ke 1: ")) # angka yang harus dimasukan oleh user yang kesatu
masukan2 = int(input("Masukan angka yang ke 2: ")) # angka yang harus dimasukan oleh user yang kedua
# diatas adalah input + variable nya khusus user
print("\r\nMac Address Masukan 1 adalah", hex(id(masukan1))) # adalah tanda untuk inputan user
print("Kode binary nya adalah", format(masukan1, '08b')) # kode binary adalah input yang di input oleh user ke memori
print("\r\nMac Address Masukan 2 adalah", hex(id(masukan2))) # adalah tanda untuk inputan user
print("Kode binary nya adalah", format(masukan2, '08b')) # kode binary adalah input yang di input oleh user ke memori
hasil1 = masukan1 + masukan2
print("\r\nHasil dari",masukan1,"+",masukan2,"=",hasil1) # ini adalah hasil dari penambahan user
# diatas adalah penambahan jumlah variable yang dimasukan oleh user

hasil2 = masukan1 - masukan2
print("\r\nHasil dari",masukan1,"-",masukan2,"=",hasil2) # ini adalah pengurangan user
# diatas adalah pengurangan pada penjumlahan

hasil3 = masukan1 * masukan2
print("\r\nHasil dari",masukan1,"x",masukan2,"=",hasil3) # ini adalah perkalian user
# diatas adalah perkalian yang users berhasil masukan

hasil4 = masukan1 / masukan2
print("\r\nHasil dari",masukan1,"/",masukan2,"=",hasil4) # ini adalah pembagian usual user
# diatas adalah pembagian biasa yang dimasukan oleh users itu sendiri

hasil5 = masukan1 // masukan2
print("\r\nHasil dari",masukan1,"//",masukan2,"=",hasil5) # ini adalah pembagian yang dibulatkan ke bawah usual user
# diatas adalah pembagian yang metode nya dibulatkan ke bawah

hasil6 = masukan1 % masukan2
print("\r\nHasil dari",masukan1,"%",masukan2,"=",hasil6) # ini adalah pembagian yang dilakukan oleh user
# diatas adalah modulus yang metode nya mirip pembagian pembulatan ke bawah, yang itu adalah keblikanya

hasil7 = masukan1 ** masukan2
print("\r\nHasil dari",masukan1,"**",masukan2,"=",hasil7) # ini adalah pangkat yang dilakukan oleh user
# diatas adalah bilangan pangkat yang sudah di hitung sendiri oleh user
# diatas adalah Aritmatika sederhana nya saja

print("\n PERBANDINGAN 2 BUAH NILAI \n") # stage yang ketiga adalah perbandingan 2 buah nilai dan operasi logika
lebih_besar = masukan1 > masukan2
print(masukan1,"Lebih besar dari",masukan2,"=",lebih_besar) # ini adalah bilangan yang lebih besar
lebih_kecil = masukan1 < masukan2
print(masukan1,"Lebih kecil dari",masukan2,"=",lebih_kecil) # ini adalah bilangan yang lebih kecil
lebih_besar_samadengan = masukan1 >= masukan2
print(masukan1,"Lebih besar sama dengan dari",masukan2,"=",lebih_besar_samadengan) # lebih besar sama dengan nya
lebih_kecil_samadengan = masukan1 <= masukan2
print(masukan1,"Lebih kecil sama dengan",masukan2,"=",lebih_kecil_samadengan) # lebih kecil sama dengan nya
sama_dengan = masukan1 == masukan2
print(masukan1,"sama dengan",masukan2,"=",sama_dengan) # sama dengan bilangan
tak_sama_dengan = masukan1 != masukan2
print(masukan1,"tak sama dengan",masukan2,"=",tak_sama_dengan) # tak sama dengan
print("\r\nDibawah ini adalah Identify pada bilangan nya") # identify pada suatu bilangan termudah
identify_1 = masukan1 is masukan2
print(masukan1,"is",masukan2,"=",identify_1) # identify is nya
identify_2 = masukan1 is not masukan2
print(masukan1,"is not",masukan2,"=",identify_2) # identify is not nya

print("\n BERIKUT INI ADALAH NILAI LOGIKA BOOLEAN \n") # stage yang keempat adalah menampilkan nilai logika
x = masukan1
y = not x
print(x,"Not =",y) # ini adalah not dari x not y
i = masukan2
q = not i
print(i,"Not =",q) # ini adalah not dari i not q
print() # ini ibaratnya kayak backspace... wkwkwkwkwkwk
logic_or = lebih_besar or lebih_kecil
print(lebih_besar,"OR",lebih_kecil,"=",logic_or) # ini adalah nilai dari OR nya
logic_and = lebih_besar and lebih_kecil
print(lebih_besar,"AND",lebih_kecil,"=",logic_and) # ini adalah nilai dari AND nya
logic_xor = lebih_besar ^ lebih_kecil
print(lebih_besar,"XOR",lebih_kecil,"=",logic_xor) # ini adalah nilai dari XOR nya
print("\r\nLogika boolean diatas diambil dari penjumlahan Lebih besar dan Lebih kecil") # note for users

print("\n MENGHITUNG BILANGAN KEDUA DENGAN OPERASI ASSIGNMENT \n") # stage yang kelima adalah menjumlahkan bilangan dengan OA
print("Operasi ini mirip dengan perhitungan aritmatika sederhana") # note for users
inputan1 = int(input("\r\nMasukan angka yang pertama: ")) # angka yang pertama
inputan2 = int(input("Masukan angka yang kedua: ")) # angka yang kedua
a = inputan1
b = inputan2

a += b
print("\r\nHasil dari Operation Assignment Pertambahan Adalah: ",a) # pertambahan Operation assignment

a -= b
print("Hasil dari Operation Assignment Pengurangan Adalah: ",a) # pengurangan Operation assignment

a *= b
print("Hasil dari Operation Assignment Pengalian Adalah: ",a) # pengalianya Operation assignment

a /= b
print("Hasil dari Operation Assignment Pembagian Adalah: ",a) # pembagian Operation assignment

a //= b
print("Hasil dari Operation Assignment Pembagian Kebawah Adalah: ",a) # pembagian bulat Operation assignment

a %= b 
print("Hasil dari Operation Assignment Modulus Adalah: ",a) # modulus Operation assignment

a **= b
print("Hasil dari Operation Assignment Pemangkatan Adalah: ",a) # pemangkatan Operation assignment

print("\r\nIni adalah Nilai Logika Booleanya") # nilai logika booleanya
c = True
d = False
print("\r\nPerlu diingat bahwa akan ada 2 variable yaitu C dan D, \r\nVariable C Adalah True, sedangkan D adalah False")
print("Kalau mau dirubah ya silahkan aja ndak papa\r\n") # note for users

c |= d
print("Hasil dari Operation Assignment OR Adalah: ",c) # or Operation assignment

c ^= d 
print("Hasil dari Operation Assignment XOR Adalah: ",c) # XOR Operation assignment

c &= d
print("Hasil dari Operation Assignment AND Adalah: ",c) # and Operation assignment