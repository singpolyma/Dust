import yaml
import email
import smtplib

from core.util import encodeAddress

class MailHandler:
  def __init__(self):
    f=open('config/emailServer.yaml', 'r')
    self.config=yaml.load(f.read())
    f.close()

  def handle(self, msock, msg, addr):
    print('-----------------')
    print(msg.decode('ascii'))

    msg=msg.decode('ascii')
    mail=email.message_from_string(msg)
    to=mail['To']
    frm=mail['From']

    print('To:', to, 'From:', frm)

    tod=to.split('@')[1]
    frmd=frm.split('@')[1]

    addressKey=encodeAddress(addr)

    sender=self.config['senders'][addressKey]
    if not sender:
      print('Unknown sender', addr)
    else:
      if not tod in sender['to']:
        print('Illegal to address', tod, sender['to'])
      elif not frmd in sender['from']:
        print('Illegal from address', frmd, sender['from'])
      else:
        print('Sending...')
        #    smtp = smtplib.SMTP(self.config['smtpHost'])
        #    smtp.set_debuglevel(1)
        #    smtp.sendmail(frm, to, msg)
        #    smtp.quit()

