import pandas as pd
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACa75bb17b70803ed6bf0d7a8fcb1f760e"
auth_token  = "8d0044a72f9df2c5dfc6fc2e7720f063"
client = Client(account_sid, auth_token)

# Instalar
# pandas
# openpyxl
# twilio

# Passo a passo de solução
# Abrir os 6 arquivos em excel

lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511975835935",
            from_="+16204009965",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

# Para cada arquivo vamos verificar se algum valor daquele arquivo é maior que 55.000 na coluna de vendas
# Se for maior que 55.000 -> enviar um SMS com o nome, mês e as vendas do vendedor