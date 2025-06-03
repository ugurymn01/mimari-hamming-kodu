import tkinter as tk
from tkinter import messagebox

# Renk teması
arkaplan = '#d0f0c0'
buton_rengi = '#228B22'
yazi_rengi = 'white'

def parity_bitleri_hesapla(veri):
    n = len(veri)
    r = 0
    while (2**r) < (n + r + 1):
        r += 1
    return r

def encode_data(veri):
    n = len(veri)
    r = parity_bitleri_hesapla(veri)
    encoded = ['0'] * (n + r)
    j = 0
    k = 0

    for i in range(1, n + r + 1):
        if i == 2**j:
            j += 1
        else:
            encoded[i - 1] = veri[k]
            k += 1

    for i in range(r):
        pozisyon = 2**i
        parity = 0
        for j in range(1, n + r + 1):
            if j & pozisyon == pozisyon and encoded[j - 1] == '1':
                parity = 1 - parity
        encoded[pozisyon - 1] = str(parity)

    return ''.join(encoded)

def decode_data(encoded):
    n = len(encoded)
    r = parity_bitleri_hesapla(encoded)
    hatalı_pozisyon = 0

    for i in range(r):
        pos = 2**i
        parity = 0
        for j in range(1, n + 1):
            if j & pos == pos and encoded[j - 1] == '1':
                parity = 1 - parity
        hatalı_pozisyon += pos * parity

    if hatalı_pozisyon != 0:
        encoded = encoded[:hatalı_pozisyon - 1] + str(1 - int(encoded[hatalı_pozisyon - 1])) + encoded[hatalı_pozisyon:]

    decoded = ''
    j = 0
    for i in range(1, n + 1):
        if i != 2**j:
            decoded += encoded[i - 1]
        else:
            j += 1

    return decoded, hatalı_pozisyon

def encode():
    data = data_entry.get()
    if not data.isdigit() or not all(bit in '01' for bit in data):
        messagebox.showerror("Geçersiz giriş", "Lütfen geçerli bir binary veri girin!")
        return
    encoded = encode_data(data)
    encoded_label.config(text=f"Kodlanmış Veri: {encoded}")
    memory.set(encoded)

def simulate_error():
    encoded = memory.get()
    if not encoded:
        messagebox.showerror("Hata", "Bellekte veri yok!")
        return
    try:
        error_pos = int(error_pos_entry.get())
    except ValueError:
        messagebox.showerror("Hatalı giriş", "Pozisyon için sayı girin!")
        return
    if error_pos < 1 or error_pos > len(encoded):
        messagebox.showerror("Hatalı konum", "Pozisyon aralık dışında!")
        return

    encoded_list = list(encoded)
    encoded_list[error_pos - 1] = '0' if encoded_list[error_pos - 1] == '1' else '1'
    corrupted = ''.join(encoded_list)

    corrupted_label.config(text=f"Bozuk Veri: {corrupted}")
    memory.set(corrupted)

def decode():
    encoded = memory.get()
    if not encoded:
        messagebox.showerror("Hata", "Bellekte veri yok!")
        return
    decoded, error_pos = decode_data(encoded)
    if error_pos == 0:
        error_msg = "Hata tespit edilmedi."
    else:
        error_msg = f"Hata tespit edildi ve {error_pos}. konumda düzeltildi."
    decoded_label.config(text=f"Çözülen Veri: {decoded}\n{error_msg}")

# GUI Başlangıcı
root = tk.Tk()
root.title("Hamming SEC-DED Simülatörü")
root.configure(bg=arkaplan)

# Başlık
tk.Label(root, text="Hamming SEC-DED Simülatörü", font=("Arial", 16, "bold"), bg=arkaplan).grid(row=0, column=0, columnspan=2, pady=10)

# Giriş Alanı
tk.Label(root, text="Veriyi giriniz (binary):", bg=arkaplan, font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=5)
data_entry = tk.Entry(root, font=('Arial', 12))
data_entry.grid(row=1, column=1, padx=10, pady=5)

encode_button = tk.Button(root, text="Encode", command=encode, bg=buton_rengi, fg=yazi_rengi, font=('Arial', 12))
encode_button.grid(row=2, column=0, columnspan=2, pady=5)

encoded_label = tk.Label(root, text="Kodlanmış Veri: ", bg=arkaplan, font=('Arial', 12))
encoded_label.grid(row=3, column=0, columnspan=2, pady=5)

tk.Label(root, text="Hata Konumu:", bg=arkaplan, font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=5)
error_pos_entry = tk.Entry(root, font=('Arial', 12))
error_pos_entry.grid(row=4, column=1, padx=10, pady=5)

simulate_error_button = tk.Button(root, text="Hatayı Simüle Et", command=simulate_error, bg=buton_rengi, fg=yazi_rengi, font=('Arial', 12))
simulate_error_button.grid(row=5, column=0, columnspan=2, pady=5)

corrupted_label = tk.Label(root, text="Bozuk Veri: ", bg=arkaplan, font=('Arial', 12))
corrupted_label.grid(row=6, column=0, columnspan=2, pady=5)

decode_button = tk.Button(root, text="Decode", command=decode, bg=buton_rengi, fg=yazi_rengi, font=('Arial', 12))
decode_button.grid(row=7, column=0, columnspan=2, pady=5)

decoded_label = tk.Label(root, text="Çözülen Veri: ", bg=arkaplan, font=('Arial', 12))
decoded_label.grid(row=8, column=0, columnspan=2, pady=5)

memory = tk.StringVar()

root.mainloop()
