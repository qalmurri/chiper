import string as str

# membuat variabel untuk menampung alfabet
alfa = list(str.ascii_lowercase)


# fungsi untuk melakukan enkripsi
def encrypt(sentence, shifting):
    sentence = sentence.lower()
    res = ''
    for char in sentence:
        """
        melakukan pengecekan index per huruf pada string input dan memasukkan
        rumus cesar cipher
        """
        if char in alfa:
            oldindex = alfa.index(char)
            newindex = (oldindex + shifting) % 26
            afterencrypt = alfa[newindex]
            res = res + afterencrypt
        else:
            res = res + " "
    return res


while (True):
    try:
        shifter = int(input('Masukkan cipher key (dalam angka): '))
        if shifter < 1:
            print("Cipher key kurang dari satu. Silakan coba lagi")
        else:
            sentence = input('Masukkan kalimat yang ingin dienkripsi : ')
            encryptresult = encrypt(sentence, shifter)
            print(
                f'Hasil kalimat {sentence} yang sudah dienkripsi dengan cipher key sejumlah {shifter} adalah = {encryptresult}')
            stat = input('Ingin mengulang program? (y/n)\n')
            if stat == 'n':
                print("Keluar dari program")
                break
    except:
        print("Format input yang diminta salah. Silakan coba lagi")
