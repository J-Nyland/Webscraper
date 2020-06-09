import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
body =  f""" <html>
                        <div class="container" style="background-color: #CC2026;">
                            <br> <br> 
                            <h1>The system tried to move a completed EOL Winshuttle to complete winshuttle folder but failed</h1>
                    
                            <br>
                        </div>
 
                    </html>
                """
s = smtplib.SMTP('es12app2.corp.cmsdistribution.com:25')
msg = MIMEMultipart('alternative')
html  = MIMEText(body, 'html')
msg.attach(html)
msg['Subject'] = "Failed to Retrieve Email From Outlook"   
msg['To'] = ", ".join("james.cookland@cmsdistribution")
msg['html'] = body
 
s.sendmail("winshuttle@cms.com", "james.cookland@cmsdistribution.com", msg.as_string())





import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
body =  f""" <html>
                        <div class="container" style="background-color: #CC2026;">
                            <br> <br> 
                            <h1>The system failed to operate due to an error with the Chrome Driver. Please update the Chrome Driver being used</h1>
                    
                            <br>
                        </div>
 
                    </html>
                """
s = smtplib.SMTP('es12app2.corp.cmsdistribution.com:25')
msg = MIMEMultipart('alternative')
html  = MIMEText(body, 'html')
msg.attach(html)
msg['Subject'] = "Chrome Driver Error"   
msg['To'] = ", ".join("jonathan.nyland@cmsdistribution")
msg['html'] = body
 
s.sendmail("winshuttle@cms.com", "jonathan.nyland@cmsdistribution.com", msg.as_string())