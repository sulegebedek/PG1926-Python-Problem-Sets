list=[]
index = int(input("Kaç sayı gireceksiniz: "))

for i in range(index):
  number = list.append(int(input("sayı giriniz:")))
print("\n")
print(list)
print("\n")
enBuyuk = list[0]

for j in list:
  
  if j % 2 != 0 :
    
    if j > enBuyuk:
      enBuyuk = j

print("En buyuk tek sayı: {}".format(enBuyuk))


  

