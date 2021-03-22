num1=int(input("Baslangıc degerini giriniz:"))
num2=int(input("Bitis degerini giriniz:"))

for num1 in range(num2) :
  if num1 % 3 == 0:
    if num1 % 5 == 0:
      print("FizzBuzz")
    else:
      print("Fizz")
  elif num1 % 5 == 0:
    print("Buzz")
  else:
    print(num1)
  
  