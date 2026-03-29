import qrcode

#INPUT UPI ID

upi_id = input("Enter your UPI ID= ")


#upi url upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE

phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
gpay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'


#create QR codes for wach payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
gpay_qr = qrcode.make(gpay_url)


#tos ave QR as img

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('phonepe_qr.png')
gpay_qr.save('phonepe_qr.png')



#Display qr codes

phonepe_qr.show()
paytm_qr.show()
gpay_qr.show()
