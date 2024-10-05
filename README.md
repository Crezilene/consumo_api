# consumo_api
Este script tem como finalidade enviar um e-mail semanal do consumo da API em questão

# Bibliotecas utilizadas
import MySQLdb
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
