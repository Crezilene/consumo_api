# consumo_api
Este script tem como finalidade enviar um e-mail semanal do consumo da API em questão

# Bibliotecas utilizadas
import MySQLdb <br>
import pandas as pd <br>
import smtplib <br>
from email.mime.multipart import MIMEMultipart <br>
from email.mime.text import MIMEText <br>
from email.mime.base import MIMEBase <br>
from email import encoders
