import json
import datetime

def item_meetingroom():
    with open("inventory_list.json","r") as f:
        obj = json.load(f)
    for i in obj:
        item_placement = i["placement"]["name"]
        if item_placement == "Meeting Room":
            print(i["name"])

def item_electronic():
    with open("inventory_list.json","r") as f:
        obj = json.load(f)
    for i in obj:
        item_type = i["type"]
        if item_type == "electronic":
            print(i["name"])

def item_furniture():
    with open("inventory_list.json","r") as f:
        obj = json.load(f)
    for i in obj:
        item_type = i["type"]
        if item_type == "furniture":
            print(i["name"])

def purchased16012020():
    with open("inventory_list.json","r") as f:
        obj = json.load(f)
    for i in obj:
        purchased_at = i["purchased_at"]
        date_purchased = datetime.datetime.utcfromtimestamp(purchased_at).strftime("%Y-%m-%d")
        if date_purchased == "2020-01-16":
            print(i["name"])

def item_brown():
    with open("inventory_list.json","r") as f:
        obj = json.load(f)
    for i in obj:
        tags = i["tags"]
        for j in tags:
            if j == "brown":
                print(i["name"])

print("1. Mencari item yang ada di Meeting Room")
print("2. Mencari item yang bertipe electronic")
print("3. Mencari item yang bertipe furniture")
print("4. Mencari item yang dibeli pada tanggal 16 Januari 2020")
print("5. Mencari item yang berwarna coklat")

num = input(f"Silahkan masukkan angka sesuai menu yang tersedia : ")
num = int(num)

if num == 1:
    item_meetingroom()
elif num == 2:
    item_electronic()
elif num == 3:
    item_furniture()
elif num == 4:
    purchased16012020()
elif num == 5:
    item_brown()