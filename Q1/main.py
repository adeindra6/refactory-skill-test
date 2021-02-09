def check(str):
    new_str = ""
    for i,character in enumerate(str):
        if i % 30 == 0:
            new_str += "\n"
        new_str += character
    new_str = new_str[1:]
    return new_str

resto = input(f"Masukkan nama restoran : ")
date = input(f"Masukkan tanggal dan jam dengan format (dd/mm/yyyy hh:mm:ss) : ")
cashier = input(f"Masukkan nama kasir : ")
items = []
prices = []
item = ""

while(item != "exit"):
    item = input(f'Masukkan nama item (masukkan "exit" untuk keluar) : ')
    if(item != "exit"):
        items.append(item)
        price = input(f"Masukkan harga item : ")
        prices.append(price)

resto = check(resto)
print(resto.center(30))

tanggal = "Tanggal : " + date
print(tanggal.center(30))

kasir = "Nama Kasir : " + cashier
kasir = check(kasir)
print(kasir.center(30))

print("==============================")

total = 0

for item,price in zip(items,prices):
    cetak_item = item + "{:.>25}".format("Rp" + f'{int(price):,d}'.replace(",","."))
    cetak_item = check(cetak_item)
    print(cetak_item)
    total = total + int(price)

cetak_total = "\nTotal" + '{:.>24}'.format("Rp" + f'{int(total):,d}'.replace(",","."))
cetak_total = check(cetak_total)
print(cetak_total)