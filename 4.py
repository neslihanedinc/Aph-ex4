data=[
    {"name": "murat", "age": 25 , "city": "Giresun"},
    {"name": "ilayda","age": 23 , "city": "Mardin"},
    {"name": "derya" , "age": 24 ,"city": "Ordu"}]
def sort_list_of_dicts(data,key):
    #sort_list_of_dicts fonksiyonu, iki parametre alır:
    #data: Sıralanacak liste.key: Sıralama için kullanılacak anahtar.
    sorted_list=sorted(data,key=lambda x:x[key]) #sorted_list değişkeni, sıralanmış listeyi tutar ve bu liste fonksiyonun sonucu olarak döner.
#lambda x: x[key]: Bu bir anonim (isimsiz) fonksiyondur. Her bir sözlüğü (x) alır ve anahtarın (key) değerini döndürür. Sıralama bu değere göre yapılır.
#lambda nasıl çalışır
    return sorted_list
sorted_by_age=sort_list_of_dicts(data,"age")
print("\n sorted by age:")
for item in sorted_by_age:
    print(item)

sorted_by_name=sort_list_of_dicts(data,"name")
print("\n sorted_by_name:")
for item in sorted_by_name:
    print(item)

    
