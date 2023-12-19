print("Lunapark'a hoşgeldiniz.")
boy = int(input('Boyunuzun uzunluğunu giriniz\n'))

if boy >= 120:
    yas = int(input("Yaşınzı nedir?\n"))

    if yas < 12:
        print("Bilet ücretiniz: 15 TL")
    elif yas < 18:
        print("Bilet ücretiniz: 25 TL")
    else:
        print("Bilet ücretiniz: 35 TL")
else:
    print("Lunaparak'a girme koşulunu sağlamıyorsunuz...")
