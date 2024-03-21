# 1) Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
boy = float(input("Boyunuzu girin: "))
kilo = int(input("Kilonuzu girin: "))

vki = kilo/(boy * boy)

if vki < 18.5:
    print("Zayıf", vki)
elif vki >= 18.5 and vki < 25:
    print("Normal", vki)
elif vki >= 25 and vki < 30:
    print("Fazla Kilolu", vki)
elif vki >= 30:
    print("Obez") 

# 2) Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

ham_maas = int(input("Maaşınızı girin: "))
zam_orani = float(input("Zam oranını girin (1 ile 100 arası bir sayı giriniz.): "))

zamli_maas = ham_maas + (ham_maas * (zam_orani / 100))

print("Zamlı maaşınız: ", zamli_maas)

#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

sayi1 = int(input("1. Sayıyı Giriniz: "))
sayi2 = int(input("2. Sayıyı Giriniz: "))
sayi3 = int(input("3. Sayıyı Giriniz: "))

enBuyuk = None

if sayi1 > sayi2 and sayi1 > sayi3:
    enBuyuk = sayi1
    print("en büyük sayı : ",enBuyuk)
elif sayi2 > sayi1 and sayi2 > sayi3:
    enBuyuk = sayi2
    print("en büyük sayı : ",enBuyuk)
elif sayi3 > sayi1 and sayi3 > sayi2:
    enBuyuk = sayi3
    print("en büyük sayı : ",enBuyuk)
else:
    print("Lütfen farklı sayılar giriniz")

#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
pi = 3.14159

r = float(input("Yarı çapı giriniz :   "))

alan = pi * (r**2)

print("alan: ",alan)

cevre = 2 * pi * r
print("çevre: ",cevre)

#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

number = int(input("Your number please: "))
number = str(number)

reverse_number = number[::-1]

if number == reverse_number:

    print ("Your number is palindrom...")
else:
    print ("Your number is not palindrom...")



