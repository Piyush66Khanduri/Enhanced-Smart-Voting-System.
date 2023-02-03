import smtplib
import pyotp
import main
def send_emil(g,tk):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.connect("smtp.gmail.com", 587)
        server.starttls()
        print("In starttls")
        server.login('piyushkhanduri65@gmail.com', 'jvbmwibyatadmnhh')
        s=genopt()
        res=str(g.get())
        server.sendmail('piyushkhanduri65@gmail.com',res,s)
        main.sent_det(tk,s)
    except:
        pass
def genopt():
    s=pyotp.random_base32()
    print(s[0::5])
    return s[0::5]
