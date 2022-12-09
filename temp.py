from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('/home/joaofmds/Estudos/Cursos/Python/e-mail/template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='João Souza', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'João Felipe Mendes de Souza'
msg['to'] = meu_email
msg['subject'] = 'Atenção: este é um e-mail de teste.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('imagem.jpeg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print('E-mail não enviado.')
        print('Erro', e)