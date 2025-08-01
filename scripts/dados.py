import json
import csv

class Dados:

    def __init__(self, dados):
        self.dados = dados
        self.colunas = self.__get_col()
        self.linhas = self.__size_data()

    def __leitura_json(path):
        dados_json = []
        with open(path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    def __leitura_csv(path):
        # Verificando as chaves dos dicionários
        # spamreader é um iterador que lê o arquivo CSV
        dados_csv = []
        with open(path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    @classmethod
    def leitura_dados(cls, path, tipo_arquivo):
        dados = []
        
        if tipo_arquivo == 'csv':
            dados = cls.__leitura_csv(path)
        elif tipo_arquivo == 'json':
            dados = cls.__leitura_json(path)
        return cls(dados)

    def __get_col (self):
     return list(self.dados[0].keys())
    
    def rename_col(self, key_mapping):
        new_dados = []

        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp) 

        self.dados = new_dados
        self.colunas = self.__get_col()

    def __size_data(self):
        return len(self.dados)
    
    def join(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)
        return Dados(combined_list)
    
    def __transformando_dados_tabela(self):
        dados_combinados_tabela = [self.colunas]

        for row in self.dados:
            linha = []
            for coluna in self.colunas:
                linha.append(row.get(coluna,'Indisponivel'))
            dados_combinados_tabela.append(linha)

        return dados_combinados_tabela
        
    def salvando_dados(self, path):
        dados_combinados_tabela = self.__transformando_dados_tabela()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)
        print(f'Salvo em:{path}')