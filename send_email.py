import smtplib
import ssl
from email.message import EmailMessage

setor = "B"
nome = "Equipe dos dados"

msg = EmailMessage()
msg["Subject"] = f"Planilha de dados do departamento: {setor}"

body = f"""
<p>Olá, {nome}</p>
<p>Segue em anexo a planilha com os resultados desse mês</p>
</p>Atenciosamente,</p>
<p>Mr. Robot</p>
"""

msg["From"] = "seu_e-mail"
msg["to"] = "e-mail_destinatário"
password = "senha_do_seu_e-mail"
msg.add_header("Content-Type", "text/html; charset=utf-8")
msg.set_payload(body, charset="utf-8")


context = ssl.create_default_context()
with smtplib.SMTP("smtp-mail.outlook.com", 587) as conexao:
    conexao.ehlo()
    conexao.starttls(context=context)
    conexao.login(msg["From"], password)
    conexao.send_message(msg)
