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
df_cwbLond.to_csv('CwbLond CapSoc 5000.csv', sep=',', index=False)

# -------------------------------------------
bairros = []
for i in range(len(dadosEmpresa)):
    linha = dadosEndereco.iloc[i]
    if linha['municipio'] == 'CURITIBA':
        bairros.append(linha['bairro'])

bairrosSemRepet = []
for i in range(len(bairros)):
    if bairros[i] not in bairrosSemRepet:
        bairrosSemRepet.append(bairros[i])

fig = plt.figure(figsize=(13, 8))
plt.rc('ytick', labelsize=7)
plt.grid()
plt.hist(bairros, bins=len(bairrosSemRepet), orientation='horizontal', rwidth=0.7)
plt.title('Número de empresas por bairro em Curitiba')
plt.xlabel('Quantidade')
plt.ylabel('Bairro')
plt.show()
