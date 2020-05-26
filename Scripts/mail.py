
# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("theprofessor646@gmail.com", "Python@123") 
  
# message to be sent 
message = "Hi there , your desired accuracy has been achieved sucessfully"
  
# sending the mail 
s.sendmail("theprofessor646@gmail.com", "sauravrana646@gmail.com", message) 
  
# terminating the session 
s.quit() 
