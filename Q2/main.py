import json

def phone_numbers_blank():
    with open("profile_list.json","r") as f:
        obj = json.load(f)
    for i in obj:
        phone_numbers = i["profile"]["phones"]
        if len(phone_numbers) == 0:
            print(i["username"])

def have_articles():
    with open("profile_list.json","r") as f:
        obj = json.load(f)
    for i in obj:
        articles = i["articles:"]
        if len(articles) > 0:
            print(i["username"])

def find_annis():
    with open("profile_list.json","r") as f:
        obj = json.load(f)
    for i in obj:
        nama = i["profile"]["full_name"]
        tmp_nama = nama.lower()
        if tmp_nama.find("annis") != -1:
            print(i["username"])

def articles2020():
    with open("profile_list.json","r") as f:
        obj = json.load(f)
    for i in obj:
        articles = i["articles:"]
        for j in articles:
            tmp = j["published_at"]
            if tmp[:4] == "2020":
                print(i["username"])

def born1986():
    with open("profile_list.json","r") as f:
        obj = json.load(f)
    for i in obj:
        birthday = i["profile"]["birthday"]
        birth_year = birthday[:4]
        if birth_year == "1986":
            print(i["username"])

def tips_title():
    with open("profile_list.json","r") as f:
        obj = json.load(f)
    for i in obj:
        articles = i["articles:"]
        for j in articles:
            title = j["title"].lower()
            if title.find("tips") != -1:
                print(j["title"])

def before082019():
    with open("profile_list.json","r") as f:
        obj = json.load(f)
    for i in obj:
        articles = i["articles:"]
        for j in articles:
            publish = j["published_at"]
            year = int(publish[:4])
            month = int(publish[5:7])
            if year < 2019:
                print(j["title"])
            elif year == 2019 and month < 8:
                print(j["title"])


print("1. Mencari users yang tidak punya nomor telepon")
print("2. Mencari users yang mempunyai artikel")
print("3. Mencari users yang namanya ada kata 'annis'")
print("4. Mencari users yang mempunyai artikel pada tahun 2020")
print("5. Mencari users yang lahir pada tahun 1986")
print("6. Mencari artikel yang memiliki kata 'tips' pada judulnya")
print("7. Mencari artikel yang terpublish sebelum Agustus 2019")

num = input(f"Silahkan masukkan angka sesuai menu yang tersedia : ")
num = int(num)

if num == 1:
    phone_numbers_blank()
elif num == 2:
    have_articles()
elif num == 3:
    find_annis()
elif num == 4:
    articles2020()
elif num == 5:
    born1986()
elif num == 6:
    tips_title()
elif num == 7:
    before082019()