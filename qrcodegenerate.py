import qrcode

def qrcode_generate(text):
   qr=qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=20,
      border=4,
   )
   qr.add_data(text)
   qr.make(fit=True)
   img=qr.make_image(fill_color="black",back_color="white")
   img.save("qrcode2.png")
   

# qrcode_generate("https://www.google.com")

url=input("Enter the url: ")
qrcode_generate(url)