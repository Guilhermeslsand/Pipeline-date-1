from dados import Dados

#Caminhos dos arquivos
path_dados_combinados = 'data_processed/dados_combinados.csv'
path_csv = 'data_raw/dados_empresaB.csv'
path_json = 'data_raw/dados_empresaA.json'

#Extract
dados_empresaA = Dados.leitura_dados(path_json, 'json')
print(f'\nExemplo de dados empresa A:\n{dados_empresaA.dados[0]}\n')
print(f'Colunas da Empresa A:\n{dados_empresaA.colunas}\n')
print(f'Tamanho de linhas empresa A:\n{dados_empresaA.linhas}\n')

dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print(f'Exemplo de dados empresa B:\n{dados_empresaB.dados[0]}\n')
print(f'Colunas da Empresa B:\n{dados_empresaB.colunas}\n')
print(f'Tamanho de linhas empresa B:\n{dados_empresaB.linhas}\n')

#Transform

#Map para organizar as colunas entre os arquivos
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_col(key_mapping)
print(f'Exemplo de dados empresa B transformados:\n{dados_empresaB.dados[0]}\n')
print(f'Colunas da Empresa B transformados:\n{dados_empresaB.colunas}\n')
print(f'Tamanho de linhas empresa B:\n{dados_empresaB.linhas}\n')

dados_fusao = Dados.join(dados_empresaB,dados_empresaA)
print(f'Exemplo de dados fusao:\n{dados_fusao.dados[0]}\n')
print(f'Exemplo de dados fusao:\n{dados_fusao.dados[-1]}\n')
print(f'Colunas da datos fusao:\n{dados_fusao.colunas}\n')
print(f'Tamanho de linhas dados fusao:\n{dados_fusao.linhas}\n')

#Load
dados_fusao.salvando_dados(path_dados_combinados)
