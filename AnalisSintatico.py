import csv
import os

# GRAMATICA UTILIZADA
# 1. E  -> T E'
# 2. E' -> + T E' | ε
# 3. T  -> F T'
# 4. T' -> * F T' | ε
# 5. F  -> id | ( E )

# Caminhos dos arquivos para a tabela de parsing e a entrada
caminho_tabela = 'C:/Users/pedro/OneDrive/Área de Trabalho/Faculdade/TrabalhosCompiladores/tabela.csv'
caminho_entrada = 'C:/Users/pedro/OneDrive/Área de Trabalho/Faculdade/TrabalhosCompiladores/entrada.txt'

# Função para ler a tabela LL(1) a partir de um arquivo CSV
def ler_tabela_LL1(arquivo_csv):
    tabela = {}  # Dicionário para armazenar a tabela LL(1)
    with open(arquivo_csv, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        # A primeira linha contém os terminais (ignorando a primeira célula)
        terminais = [terminal.strip() for terminal in next(reader)[1:]]  # Remover espaços em branco dos terminais
        
        # Iterar sobre as linhas restantes (cada linha representa um não-terminal)
        for linha in reader:
            nao_terminal = linha[0].strip()  # Remover espaços em branco dos não-terminais
            producoes = [producao.strip() for producao in linha[1:]]  # Remover espaços em branco das produções
            
            # Mapeia o não-terminal para um dicionário de produções (terminal -> produção)
            tabela[nao_terminal] = {terminais[i]: producoes[i] if producoes[i] != 'EMPTY' else '' for i in range(len(terminais))}
    
    # Retorna a tabela LL(1) montada
    return tabela

# Função que implementa o analisador sintático usando a tabela LL(1)
def analisador_sintatico(tabela, entrada, simbolo_inicial):
    pilha = [simbolo_inicial]  # Inicia a pilha com o símbolo inicial
    entrada = entrada.split() + ['EMPTY']  # Entrada com símbolo de fim de string ('EMPTY')
    idx = 0  # Índice que acompanha a posição atual na entrada

    # Loop principal que continua enquanto houver elementos na pilha
    while len(pilha) > 0:
        topo = pilha.pop()  # Pega o topo da pilha
        corrente = entrada[idx]  # Pega o símbolo corrente da entrada

        # Exibe o estado atual da pilha e da entrada
        print(f"Pilha: {pilha}")
        print(f"Entrada: {entrada}")
        print(f"Índice: {idx}")
        print(f"Topo: {topo}, Corrente: {corrente}")

        # Se o topo da pilha é igual ao símbolo corrente da entrada, avança o índice
        if topo == corrente:  # Correspondência
            idx += 1
        elif topo in tabela:  # Se o topo é um não-terminal
            # Busca a produção correspondente na tabela LL(1)
            producao = tabela[topo].get(corrente, None)
            if producao is not None:
                # Se a produção é vazia (representada por 'V'), não faz nada
                if producao == 'V':  
                    continue  # Não faz nada, já que 'V' é uma produção vazia
                else:
                    # Insere a produção na pilha em ordem reversa
                    pilha.extend(reversed(producao.split()))
            else:
                # Erro se nenhuma produção foi encontrada
                print(f"Erro: Nenhuma produção encontrada para {topo} com corrente {corrente}.")
                return
        else:
            # Erro se o símbolo no topo da pilha for inválido (nem terminal, nem não-terminal)
            print(f"Erro: Símbolo inválido '{topo}'.")
            return

    # Verifica se a pilha está vazia e se todos os símbolos foram processados
    if len(pilha) == 0 and corrente == 'EMPTY':
        print("Análise concluída com sucesso.")
    else:
        print("Erro na análise.")

# Função principal que executa o processo
if __name__ == "__main__":
    # Lê a tabela LL(1) do arquivo CSV
    tabela = ler_tabela_LL1(caminho_tabela)

    # Lê a entrada do arquivo
    with open(caminho_entrada, 'r', encoding='utf-8') as file:
        entrada = file.read().strip()  # Remove espaços em branco ao redor

    simbolo_inicial = 'E'  # Definir o símbolo inicial de acordo com a gramática

    # Verifica se há espaços indesejados na entrada e os remove
    entrada = " ".join(entrada.split())

    # Executa o analisador sintático
    analisador_sintatico(tabela, entrada, simbolo_inicial)
