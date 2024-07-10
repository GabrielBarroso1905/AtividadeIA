import matplotlib.pyplot as plt
import random

# Coordenadas aproximadas das capitais dos estados do Nordeste, Sudeste e Sul
coordenadas_capitais = {
    'Bahia': (-16.9716, -38.5016),
    'Sergipe': (-10.9472, -38.0731),
    'Alagoas': (-9.6612, -36.6502),
    'Pernambuco': (-10.0476, -34.8770),
    'Paraíba': (-7.1219, -36.7241),
    'Ceará': (-5.7172, -38.5437),
    'Piauí': (-5.0892, -42.8015),
    'Maranhão': (-5.0909, -45.4248),
    'Espírito Santo': (-20.3155, -40.3128),
    'Minas Gerais': (-18.5122, -44.5550),
    'Rio de Janeiro': (-22.9068, -43.1729),
    'São Paulo': (-23.5505, -46.6333),
    'Paraná': (-25.4284, -49.2733),
    'Santa Catarina': (-27.5954, -48.5480),
    'Rio Grande do Sul': (-30.0328, -51.2302),
     'Rio Grande do Norte': (-5.7172, -36.5437),  # Adicionando Rio Grande do Norte com coordenadas fictícias
}

# Definir as conexões entre as cidades dos estados do Nordeste, Sudeste e Sul
conexoes = {
    'Bahia': ['Piauí', 'Pernambuco', 'Alagoas', 'Sergipe', 'Espírito Santo', 'Minas Gerais'],
    'Sergipe': ['Alagoas', 'Bahia'],
    'Alagoas': ['Sergipe', 'Pernambuco'],
    'Pernambuco': ['Alagoas', 'Paraíba', 'Ceará', 'Bahia', 'Piauí'],
    'Paraíba': ['Pernambuco', 'Ceará', 'Rio Grande do Norte'],
    'Ceará': ['Piauí', 'Paraíba', 'Pernambuco', 'Rio Grande do Norte'],
    'Piauí': ['Maranhão', 'Bahia', 'Ceará', 'Pernambuco'],
    'Maranhão': ['Piauí', 'Bahia'],
    'Espírito Santo': ['Minas Gerais', 'Rio de Janeiro', 'Bahia'],
    'Minas Gerais': ['Espírito Santo', 'São Paulo', 'Rio de Janeiro', 'Bahia'],
    'Rio de Janeiro': ['Minas Gerais', 'São Paulo'],
    'São Paulo': ['Minas Gerais', 'Rio de Janeiro', 'Paraná'],
    'Paraná': ['Santa Catarina', 'São Paulo', 'Rio Grande do Sul'],
    'Santa Catarina': ['Paraná', 'Rio Grande do Sul'],
    'Rio Grande do Sul': ['Santa Catarina', 'Paraná'],
    'Rio Grande do Norte': ['Ceará','Paraíba'],  # Lista vazia para Rio Grande do Norte

   
}

cores_disponiveis = ['red', 'blue', 'yellow', 'brown']

# Dicionário para armazenar as cores de cada cidade
cores_cidades = {}

# Função para verificar se uma cor está sendo usada por algum vizinho
def cor_repetida(estado, cor):
    for conexao in conexoes[estado]:
        if conexao in cores_cidades and cores_cidades[conexao] == cor:
            return True
    return False

# Função recursiva para atribuir cores às cidades sem repetir entre vizinhos
def atribuir_cores_recursivo(estado):
    # Obtém todas as cores dos vizinhos
    cores_vizinhas = set()
    for conexao in conexoes[estado]:
        if conexao in cores_cidades:
            cores_vizinhas.add(cores_cidades[conexao])
    
    # Converte cores_disponiveis para um conjunto para facilitar a verificação
    cores_disponiveis_set = set(cores_disponiveis)
    
    # Verifica todas as cores disponíveis
    for cor in cores_disponiveis:
        if cor not in cores_vizinhas:
            cores_cidades[estado] = cor
            break
    else:
        # Se todas as cores disponíveis estiverem sendo usadas pelos vizinhos, escolhe aleatoriamente uma delas
        cores_possiveis = list(cores_disponiveis_set - cores_vizinhas)
        cores_cidades[estado] = random.choice(cores_possiveis)
    
    # Chama recursivamente para os vizinhos
    for conexao in conexoes[estado]:
        if conexao not in cores_cidades:
            atribuir_cores_recursivo(conexao)

# Função para desenhar o mapa e mostrar
def desenhar_mapa():
    atribuir_cores_recursivo('Rio Grande do Sul')

    fig, ax = plt.subplots(figsize=(12, 10))
    
    for estado, coords in coordenadas_capitais.items():
        cor = cores_cidades[estado]
        ax.scatter(coords[1], coords[0], color=cor, s=700, label=estado, edgecolors='black', linewidth=1.5)
        ax.text(coords[1], coords[0], estado, fontsize=10, ha='center', va='center')
        
        for conexao in conexoes[estado]:
            if conexao in coordenadas_capitais:
                ax.plot([coords[1], coordenadas_capitais[conexao][1]], [coords[0], coordenadas_capitais[conexao][0]], color=cor)

    ax.set_title('Mapa das Conexões entre Cidades dos Estados do Nordeste, Sudeste e Sul')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Chamar a função para desenhar o mapa
desenhar_mapa()
