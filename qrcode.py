import segno 

link=input("link...")
qrcode = segno.make_qr(link)

qrcode.save("qrcode.png",scale=5)
