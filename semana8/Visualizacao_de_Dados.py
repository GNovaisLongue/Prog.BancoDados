from collections import Counter, defaultdict
from matplotlib import pyplot as plt

# Exercícios
# 1 Construa um gráfico de linha que mostra o número de amigos por usuário.------------
def exercicio_um():
    #Semana 5 rede social
    users = [
        {"id": 0, "name": "Hero"},
        {"id": 1, "name": "Dunn"},
        {"id": 2, "name": "Sue"},
        {"id": 3, "name": "Chi"},
        {"id": 4, "name": "Thor"},
        {"id": 5, "name": "Clive"},
        {"id": 6, "name": "Hicks"},
        {"id": 7, "name": "Devin"},
        {"id": 8, "name": "Kate"},
        {"id": 9, "name": "Klein"},
    ]
    def number_of_friends (user):
        return len(user['friends'])
    friendships = [
        (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
        (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
    ]
    for user in users:
        user["friends"] = []
    for i, j in friendships:
        users[i]["friends"].append(users[j])
        users[j]["friends"].append(users[i])
    number_friends_by_id = []
    for user in users:
        number_friends_by_id.append([ user["id"], number_of_friends(user) ])

    def graph_exercicio_um():
        #cria um gráfico
        plt.plot ([user['id'] for user in users], [number_of_friends(user) for user in users], color='green', marker='o', linestyle='solid')
        #adiciona título
        plt.title ("Amigos por Usuário")#rótulo do eixo Y
        plt.xticks (range (len(users)) )#definir valores eixo X
        plt.yticks (range (len(users)//2))#definir valores eixo Y
        plt.ylabel ("Numero de amigos")
        plt.xlabel("Numero do Usuario")
        #mostra
        plt.show()
    graph_exercicio_um()


# 3 Construa um gráfico de dispersão envolvendo salário e tempo de experiência.
def exercicio_tres():
    #Semana 5 rede social
    salaries_and_tenures = [
        (83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6), (69000, 6.5), 
        (76000, 7.5), (60000, 2.5), (83000, 10), (48000, 1.9), (63000, 4.2),
        (85000, 8.7), (100000, 8.7)
    ]

    def generate_label(lista):
        labels = []
        letter = ord('a') #97
        for _ in enumerate(lista):
            labels.append(chr(letter)) #a
            letter += 1 #98 == 'b'
        return(labels)


    salary = [salario for salario, _ in salaries_and_tenures]
    tenures = [tenure for _, tenure in salaries_and_tenures]
    def graph_exercicio_tres():
        label = generate_label(salaries_and_tenures)
        plt.scatter (tenures, salary) 
        #rotula cada posição 
        for label, tenure_count, salary_count in zip(label, tenures, salary):
            plt.annotate(
                label,
                xy = (tenure_count, salary_count), # o ponto        
             xytext = (5, -5), #o quão longe está o texto do ponto        
             textcoords = 'offset points'    
          )
        plt.xticks( range(11) )
        plt.title ("Salaries vs Tenures") 
        plt.xlabel ("# Tenure") 
        plt.ylabel ("Salaries' values") 
        plt.show()
    graph_exercicio_tres()


# 4 Construa um histograma envolvendo dados de pagantes e não pagantes.
def exercicio_quatro():
    tenure_and_account_type = [    
        (0.7, 'paid'), (1.9,'unpaid'), (2.5,'paid'), (4.2,'unpaid'), (6,'unpaid'), 
        (6.5,'unpaid'), (7.5,'unpaid'), (8.1,'unpaid'), (8.7,'paid'), (10,'paid') 
    ]
    #Separar média de pagantes e não-pagantes
    paidType = [tenure for tenure, accType in tenure_and_account_type if accType == 'paid'] # [0.7, 2.5, 8.7, 10] 
    unpaidType = [tenure for tenure, accType in tenure_and_account_type if accType == 'unpaid'] # [1.9, 4.2, 6, 6.5, 7.5, 8.1]

    def graph_exercicio_quatro():
        histogram = Counter (tenure for _, tenure in tenure_and_account_type)
        xs = [i for i, _ in enumerate(histogram.keys())]
        #associar soma de paid com len('paid')
        med_paidType = sum(paidType)/histogram['paid']
        #associar soma de paid com len('paid')
        med_unpaidType = sum(unpaidType)/histogram['unpaid']
        plt.bar (xs, #0, 1 associados às palavras pain e unpaid
                [med_paidType, med_unpaidType], #paid e unpaid
        #          8 # largura de 8 para cada barra
                )
        plt.yticks ([1 * i for i in range (6)])
        plt.xticks (xs, histogram.keys())
        plt.ylabel("Média de Experiencia")
        plt.xlabel("Tipo de conta")
        plt.title ("Tempo médio de experiência vs Tipo de Conta")
        plt.show()
    graph_exercicio_quatro()

# 5 Construa um histograma de palavras em interesses. 
# Por exemplo, a palavra learning pode aparecer em machine learning e em deep learning. 
# Quebre cada interesse em palavras para fazer a contagem e montar o histograma.
def exercicio_cinco():
    interests = [
        (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
        (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"),
        (2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodel"), (2, "pandas"),
        (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"),
        (4, "machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm"),
        (5, "Python"), (5, "R"),(5, "Java"), (5, "C++"), (5, "Haskell"), (5, "programming languages"),
        (6, "theory"), (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), (7, "neural networks"),
        (8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificial intelligence"), (8, "Hadoop"),
        (9, "Java"), (9, "MapReduce"), (9, "Big Data"),
    ]
    #Separar palavras 
    words_and_counts = Counter(
        word
        for user, interest in interests
        for word in interest.lower().split() 
    )

    def graph_exercicio_cinco():
        xs = [i for i, _ in enumerate(words_and_counts.keys())]
        plt.bar (
            xs,
            [i for i in words_and_counts.values()],
            width=.5
        )
    
        plt.xticks (xs, words_and_counts.keys(), rotation='vertical')
        plt.ylabel("# repetições")
        plt.xlabel("Palavras")
        plt.title ("Palavras apresetadas ao menos uma vez")
        plt.show()
    graph_exercicio_cinco()
            


def main():
    exercicio_um()
    exercicio_tres()
    exercicio_quatro()
    exercicio_cinco()
    
main()