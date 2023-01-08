import qrcode

name = input("plz enter name: ")
phone_number = input("plz enter phone number: ")

img = qrcode.make(name + phone_number)

img.save("qrcode.png")