import smtplib

fromaddr = 'technologiesarchitect@gmail.com'
toaddrs  = 'satishseshadri@gmail.com'
msg = 'There was a terrible error that occured and I wanted you to know!'


# Credentials (if needed)
username = 'technologiesarchitect@gmail.com'
print ("Enter password for " + username)
password = input()

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()


