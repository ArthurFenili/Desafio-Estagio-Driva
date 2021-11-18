import pandas as pd
import matplotlib.pyplot as plt

# Lê os arquivos csv
dadosEmpresa = pd.read_csv('DadosEmpresa.csv', sep=',')
dadosEndereco = pd.read_csv('DadosEndereco.csv', sep=',')

# -------------------------------------------
# Gera arquivo csv com as empresas quem tem opção_pelo_simples como SIM.

opSimplesSim = []
for i in range(len(dadosEmpresa)):
    linha = dadosEmpresa.iloc[i]
    if linha['opcao_pelo_simples'] == 'SIM':
        opSimplesSim.append(linha)

df_opSimplesSim = pd.DataFrame(opSimplesSim)
df_opSimplesSim.to_csv('Empresas opção_pelo_simples SIM.csv', sep=',', index=False, columns=['razao_social'])

# -------------------------------------------
# Gera arquivo csv com as empresas de Curitiba ou Londrina com capital social maior que 5000 reais

listaEmpresas = []
for i in range(len(dadosEmpresa)):
    linhaEmpresa = dadosEmpresa.iloc[i]
    linhaEndereco = dadosEndereco.iloc[i]
    if (linhaEndereco['municipio'] == 'CURITIBA' or 'LONDRINA') and (linhaEmpresa['capital_social'] > 5000):
        listaEmpresas.append(linhaEmpresa)

df_cwbLond = pd.DataFrame(listaEmpresas)
df_cwbLond['bairro'] = dadosEndereco['bairro']
df_cwbLond['municipio'] = dadosEndereco['municipio']
df_cwbLond.to_csv('CwbLond CapSoc 5000.csv', sep=',', index=False)

# -------------------------------------------
# Gera gráfico mostrando o total de empresas por bairro em Curitiba

bairros = []
for i in range(len(dadosEmpresa)):
    linha = dadosEndereco.iloc[i]
    if linha['municipio'] == 'CURITIBA':
        bairros.append(linha['bairro'])

bairrosSemRepet = []
for i in range(len(bairros)):
    if bairros[i] not in bairrosSemRepet:
        bairrosSemRepet.append(bairros[i])

fig = plt.figure(figsize=(12, 54))
plt.rc('ytick', labelsize=7)
plt.grid()
plt.hist(bairros, bins=len(bairrosSemRepet), orientation='horizontal', rwidth=0.7)
plt.title('Número de empresas por bairro em Curitiba')
plt.xlabel('Quantidade')
plt.ylabel('Bairro')
# plt.show()
plt.savefig("totalEmpresas.png")

# -------------------------------------------
# Gera um gráfico mostrando os bairros de Curitiba com maiores médias de capital social

# Observando esses dois arquivos, uma análise que eu faria seria uma visualização dos bairros nos quais a média de
# capital social é mais alta, pois assim, daria uma ideia ao cliente de quais bairros supostamente dão mais lucro e
# permitem maior crescimento da empresa. Na implementação utilizei os bairros da cidade de Curitiba.

bairros = []
capitalSocial = []
for i in range(len(dadosEmpresa)):
    linhaEndereco = dadosEndereco.iloc[i]
    linhaEmpresa = dadosEmpresa.iloc[i]
    if linhaEndereco['municipio'] == 'CURITIBA':
        bairros.append(linhaEndereco['bairro'])
        capitalSocial.append(linhaEmpresa['capital_social'])

bairrosSemRepet = []
for i in range(len(bairros)):
    if bairros[i] not in bairrosSemRepet:
        bairrosSemRepet.append(bairros[i])

numeroDoBairro = []
for i in range(len(bairrosSemRepet)):
    numeroDoBairro.append(i)

bairrosNumerados = dict(zip(bairrosSemRepet, numeroDoBairro))

capSocialPorBairro = []
totalEmpresasPorBairro = []
for i in range(len(bairrosSemRepet)):
    capSocialPorBairro.append(0)
    totalEmpresasPorBairro.append(0)
for i in range(len(bairros)):
    capSocialPorBairro[bairrosNumerados[bairros[i]]] += capitalSocial[i]
    totalEmpresasPorBairro[bairrosNumerados[bairros[i]]] += 1
for i in range(len(capSocialPorBairro)):
    capSocialPorBairro[i] /= totalEmpresasPorBairro[i]

mediaTotal = sum(capSocialPorBairro) / len(capSocialPorBairro)
topCapitalSocial = [0]
topBairro = ['OUTROS']
for i in range(1, len(capSocialPorBairro)):
    if capSocialPorBairro[i] > mediaTotal:
        topCapitalSocial.append(capSocialPorBairro[i])
        topBairro.append(bairrosSemRepet[i])
    else:
        topCapitalSocial[0] += capSocialPorBairro[i]

plt.figure(figsize=(12,9))
plt.pie(topCapitalSocial, labels=topBairro, autopct='%1.1f%%', pctdistance=0.7, startangle=90)
plt.title('Bairros de Curitiba com as maiores médias de capital social')
# plt.show()
plt.savefig("mediaCapitalSocial.png")
