### Varos-Programação - Aulas Gratuitas

# Importação das bibliotecas
import pandas as pd
import datetime
import yfinance as yf
from matplotlib import pyplot as plt
import mplcyberpunk
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

# Determinação de variáveis
ativos = ["^BVSP", "BRL=X", "ITSA4.SA", "^IXIC", "^DJI", "^GSPC", "^TNX"]
hoje = datetime.datetime.now()
um_ano_atras = hoje - datetime.timedelta(days=365)
dados_mercado = yf.download(ativos, um_ano_atras, hoje)
dados_fechamento = dados_mercado['Adj Close'] # Utiliza somente os dados ajustados do fechamento
dados_fechamento.columns = ['Dólar', 'ITSA4', 'Ibovespa', 'Dow Jones', 'S&P 500', 'NASDAQ', 'Treasury Yield 10 Years'] # Substitui os nomes das colunas
dados_fechamento = dados_fechamento.dropna() # Retira os NaN da tabela
dados_fechamento_mensal = dados_fechamento.resample('M').last()
dados_fechamento_anual = dados_fechamento.resample('Y').last()
retorno_anual = dados_fechamento_anual.pct_change().dropna() # Retorno anual em porcentagem
retorno_mensal = dados_fechamento_mensal.pct_change().dropna() # Retorno mensal em porcentagem
retorno_diario = dados_fechamento.pct_change().dropna() # Retorno diário em porcentagem

# Loc['linha', 'coluna'] -> referenciar elementos a partir do nome;
#print(retorno_diario.loc['2023-03-31']) # Imprime as colunas que se quer (nesse caso Dólar, ITSA4 e Ibovespa)
#print(retorno_diario.loc['2023-03-31', 'Dólar']) # Imprime somente a do Dólar
#print('*' * 50)
# Iloc -> selecionar elementos como uma matriz.
#print(retorno_diario.iloc[0, 0]) # [0, 0] -> Primeira linha e primeira coluna
#print('*' * 50)
retorno_dia_dolar = retorno_diario.iloc[-1, 0] # Busca a última cotação de fechamento do dólar
#print(retorno_dia_dolar)
#print('*' * 50)
retorno_dia_ITSA4 = retorno_diario.iloc[-1, 1]
#print(retorno_dia_ITSA4)
#print('*' * 50)
retorno_dia_ibovespa = retorno_diario.iloc[-1, 2]
#print(retorno_dia_ibovespa)
#print('*' * 50)
retorno_dia_nasdaq = retorno_diario.iloc[-1, 3]
retorno_dia_dowjones = retorno_diario.iloc[-1, 4]
retorno_dia_s_p500 = retorno_diario.iloc[-1, 5]
retorno_dia_treasury_10_years = retorno_diario.iloc[-1, 6]

retorno_mes_dolar = retorno_mensal.iloc[-1, 0]
retorno_mes_ITSA4 = retorno_mensal.iloc[-1, 1]
retorno_mes_ibovespa = retorno_mensal.iloc[-1, 2]
retorno_mes_nasdaq = retorno_mensal.iloc[-1, 3]
retorno_mes_dowjones = retorno_mensal.iloc[-1, 4]
retorno_mes_s_p500 = retorno_mensal.iloc[1, 5]
retorno_mes_treasury_10_years = retorno_mensal.iloc[-1, 6]

retorno_ano_dolar = retorno_anual.iloc[-1, 0]
retorno_ano_ITSA4 = retorno_anual.iloc[-1, 1]
retorno_ano_ibovespa = retorno_anual.iloc[-1, 2]
retorno_ano_nasdaq = retorno_anual.iloc[-1, 3]
retorno_ano_dowjones = retorno_anual.iloc[-1, 4]
retorno_ano_s_p500 = retorno_anual.iloc[-1, 5]
retorno_ano_treasury_10_years = retorno_anual.iloc[-1, 6]

retorno_dia_dolar = round(retorno_dia_dolar * 100, 2) # Arredonda, multiplica por 100 e tem 2 casas decimais
retorno_dia_ITSA4 = round(retorno_dia_ITSA4 * 100, 2)
retorno_dia_ibovespa = round(retorno_dia_ibovespa * 100, 2)
retorno_dia_nasdaq = round(retorno_dia_nasdaq * 100, 2)
retorno_dia_dowjones = round(retorno_dia_dowjones * 100, 2)
retorno_dia_s_p500 = round(retorno_dia_s_p500 * 100, 2)
retorno_dia_treasury_10_years = round(retorno_dia_treasury_10_years * 100, 2)

retorno_mes_dolar = round(retorno_mes_dolar * 100, 2)
retorno_mes_ITSA4 = round(retorno_mes_ITSA4 * 100, 2)
retorno_mes_ibovespa = round(retorno_mes_ibovespa * 100, 2)
retorno_mes_nasdaq = round(retorno_mes_nasdaq * 100, 2)
retorno_mes_dowjones = round(retorno_mes_dowjones * 100, 2)
retorno_mes_s_p500 = round(retorno_mes_s_p500 * 100, 2)
retorno_mes_treasury_10_years = round(retorno_mes_treasury_10_years * 100, 2)

retorno_ano_dolar = round(retorno_ano_dolar * 100, 2)
retorno_ano_ITSA4 = round(retorno_ano_ITSA4 * 100, 2)
retorno_ano_ibovespa = round(retorno_ano_ibovespa * 100, 2)
retorno_ano_nasdaq = round(retorno_ano_nasdaq * 100, 2)
retorno_ano_dowjones = round(retorno_ano_dowjones * 100, 2)
retorno_ano_s_p500 = round(retorno_ano_s_p500 * 100, 2)
retorno_ano_treasury_10_years = round(retorno_ano_treasury_10_years * 100, 2)

# Gráficos da performace dos ativos
plt.style.use('cyberpunk')
dados_fechamento.plot(y = 'Dólar', use_index = True, legend = False)
plt.title('Fechamento Dólar')
plt.savefig('Dólar-Fechamento.png', dpi = 300)
#plt.show()

plt.style.use('cyberpunk')
dados_fechamento.plot(y = 'ITSA4', use_index = True, legend = False)
plt.title('Fechamento ITSA4')
plt.savefig('ITSA4-Fechamento.png', dpi = 300)
#plt.show()

plt.style.use('cyberpunk')
dados_fechamento.plot(y = 'Ibovespa', use_index = True, legend = False)
plt.title('Fechamento Ibovespa')
plt.savefig('Ibovespa-Fechamento.png', dpi = 300)
#plt.show()

plt.style.use('cyberpunk')
dados_fechamento.plot(y = 'NASDAQ', use_index = True, legend = False)
plt.title('Fechamento NASDAQ')
plt.savefig('NASDAQ-Fechamento.png', dpi = 300)
#plt.show()

plt.style.use('cyberpunk')
dados_fechamento.plot(y = 'Dow Jones', use_index = True, legend = False)
plt.title('Fechamento Dow Jones')
plt.savefig('DowJones-Fechamento.png', dpi = 300)
#plt.show()

plt.style.use('cyberpunk')
dados_fechamento.plot(y = 'S&P 500', use_index = True, legend = False)
plt.title('Fechamento S&P 500')
plt.savefig('S&P_500-Fechamento.png', dpi = 300)
#plt.show()

plt.style.use('cyberpunk')
dados_fechamento.plot(y = 'Treasury Yield 10 Years', use_index = True, legend = False)
plt.title('Fechamento Treasury Yield 10 Years')
plt.savefig('Treasury_Yield_10_Years-Fechamento.png', dpi = 300)
#plt.show()

# Acessar o arquivo .env com a senha para acesso ao e-mail
load_dotenv()

# Buscando a senha no arquivo .env
senha = os.environ.get('senha')

# Email de saída (envio)
email = 'hilariogrossi@gmail.com'

# Mensagem de envio do email
msg = EmailMessage()
msg['Subject'] = 'Mercado do dia anterior'
msg['From'] = 'Hilário GO - Python'
msg['To'] = 'hilariogrossi@yahoo.com.br', 'gabrielminardi@gmail.com', 'patriciaminardi@yahoo.com.br'
msg.set_content(f'''Prezado irmão, segue o relatório diário:

_____________________________________________________________________________

Ibovespa:

No ano o Ibovespa está tendo uma rentabilidade de {retorno_ano_ibovespa} %, 
enquanto no mês a rentabilidade é de {retorno_mes_ibovespa} %.

No último dia útil o fechamento do Ibovespa foi de {retorno_dia_ibovespa} %.
_____________________________________________________________________________

ITSA4:

No ano o ITSA4 está tendo uma rentabilidade de {retorno_ano_ITSA4} %, 
enquanto no mês a rentabilidade é de {retorno_mes_ITSA4} %.

No último dia útil o fechamento do ITSA4 foi de {retorno_dia_ITSA4} %.
_____________________________________________________________________________

Dólar:

No ano o Dólar está tendo uma rentabilidade de {retorno_ano_dolar} %, 
enquanto no mês a rentabilidade é de {retorno_mes_dolar} %.

No último dia útil o fechamento do Dólar foi de {retorno_dia_dolar} %.
_____________________________________________________________________________

Nasdaq:

No ano a Nasdaq está tendo uma rentabilidade de {retorno_ano_nasdaq} %,
enquanto no mês a rentabilidade é de {retorno_mes_nasdaq} %.

No último dia útil o fechamento da Nasdaq foi de {retorno_dia_nasdaq} %.
_____________________________________________________________________________

Dow Jones:

No ano o Dow Jones está tendo uma rentabilidade de {retorno_ano_dowjones} %,
enquanto no mês a rentabilidade é de {retorno_mes_dowjones} %.

No último dia útil o fechamento do Dow Jones foi de {retorno_dia_dowjones} %.
_____________________________________________________________________________

S&P 500:

No ano o S&P 500 está tendo uma rentabilidade de {retorno_ano_s_p500} %,
enquanto no mês a rentabilidade é de {retorno_mes_s_p500} %.

No último dia útil o fechamento do S&P 500 foi de {retorno_dia_s_p500} %.
_____________________________________________________________________________

Treasury Yield 10 Years:

No ano o Treasury Yield 10 Years está tendo uma rentabilidade de {retorno_ano_treasury_10_years} %,
enquanto no mês a rentabilidade é de {retorno_mes_treasury_10_years} %.

No último dia útil o fechamento do Treasury Yield 10 Years foi de {retorno_dia_treasury_10_years} %.



Abr4ços,

Hilário Grossi de Oliveira.



''')
