import MySQLdb
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Conexão com o MySQL
conexao = MySQLdb.connect(
    host="167.86.*******",
    user="********",
    password="*********",
    database="bkp"
)

query = """
SELECT 
    req.DataHora as Data_Hora,
    req.ADE,
    req.LogEnt,
    req.CPF,
    req.Orgao,
    req.Matricula,
    req.InstituidorMatricula as Instituidor_Matricula,
    req.Nome,
    req.DataNascimento as Data_de_Nascimento,
    req.Situacao,
    req.Produto,
    req.UF,
    req.IdadeMaxima as Idade_Maxima,
    req.Limite,
    req.Banco,
    req.Agencia,
    req.Conta,
    res.Status,
    res.Descricao,
    req.Margem as Margem_Informada,
    res.MargemCalculada as Margem_Calculada
FROM bkp.logacessochaverequest req JOIN bkp.logacessochaveresponse res ON req.DataHora = res.DataHora
WHERE req.DataHora >= CURDATE() - INTERVAL 30 DAY;
"""
dados = pd.read_sql(query, conexao)

arquivo_excel = "relatorio_master.xlsx"
dados.to_excel(arquivo_excel, index=False)

conexao.close()

# Configuração do e-mail
remetente = "e-mail@email.com.br"
destinatarios = ["e-mail@email.com.br",
                 "e-mail@email.com.br"]
senha_email = "***************"
assunto = "Relatório Master"
corpo_email = "Segue em anexo o relatório de consumo de APIs dos últimos 30 dias."

# Criação da mensagem de e-mail
mensagem = MIMEMultipart()
mensagem['From'] = remetente
mensagem['To'] = ', '.join(destinatarios)
mensagem['Subject'] = assunto

mensagem.attach(MIMEText(corpo_email, 'plain'))

# Anexar o arquivo Excel
with open(arquivo_excel, "rb") as anexo:
    parte = MIMEBase('application', 'octet-stream')
    parte.set_payload(anexo.read())
    encoders.encode_base64(parte)
    parte.add_header('Content-Disposition',
                     f"attachment; filename= {arquivo_excel}")
    mensagem.attach(parte)

# Enviar o e-mail
try:
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(remetente, senha_email)
    servidor.sendmail(remetente, destinatarios, mensagem.as_string())
    servidor.quit()
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar o e-mail: {str(e)}")
