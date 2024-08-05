import qrcode

ssid = input("Enter the ssid : ") #SSID means Service Set Identifier. Name of the wifi
encryption = input("Enter the encryption (WPA/WPA2/WEP) : ") 
password = input("Enter the password : ")
wifi = f"WIFI:T:{encryption};S:{ssid};P:{password};;" #WIFI specifies that this qrcode is related with the wifi network, T specifies type of encryption, S specifies the SSID or name of the wifi, P specifies the password of the wifi and finally the two semicolon specifies the end of the qrcode data string, which simply means after the semicolon there is no any data included.
maker = qrcode.make(wifi)
maker.save("Password.png")