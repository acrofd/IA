import networkx as nx
import matplotlib.pyplot as plt

#Se incializa un array de las estaciones y sus conexiones.
graph = { "Shinjuku": [ "Yoyogi", "Shin-Okubo", "Ochanomizu"],
        "Yoyogi": ["Shinjuku", "Sendagaya", "Harajuku"],
        "Ochanomizu": ["Tokyo", "Suidobashi", "Shinjuku"],
        "Sendagaya": ["Yoyogi", "Shinanomachi"],
        "Shinanomachi": ["Sendagaya", "Yotsuya"],
        "Yotsuya": ["Shinanomachi", "Iichigaya"],
        "Iichigaya": ["Yotsuya", "Iidabashi"],
        "Iidabashi": ["Iichigaya", "Suidobashi"],
        "Akihabara": ["Ochanomizu", "Kanda", "Okachimachi"],
        "Tokyo": ["Ochanomizu", "Yurakucho", "Kanda"],
        "Shin-Okubo": ["Takadanobaba", "Shinjuku"],
        "Takadanobaba": ["Mejiro", "Shin-Okubo"],
        "Mejiro": ["Ikebukuro", "Takadanobaba"],
        "Ikebukuro": ["Mejiro", "Otsuka"],
        "Otsuka": ["Ikebukuro", "Sugamo"],
        "Sugamo": ["Otsuka", "Komagome"],
        "Komagome": ["Sugamo", "Tabata"],
        "Tabata": ["Komagome", "Nishi-Nippori"],
        "Nishi-Nippori": ["Tabata", "Nippori"],
        "Nippori": ["Nishi-Nippori", "Uguisudani"],
        "Uguisudani": ["Nippori", "Ueno"],
        "Ueno":['Uguisudani', "Okachimachi"],
        "Okachimachi": ["Akihabara", "Ueno"],
        "Kanda": ["Akihabara", "Kanda"],
        "Yurakucho": ["Tokyo", "Shimbashi"],
        "Shimbashi": ["Yurakucho", "Hamamatsucho"],
        "Tamachi": ["Hamamatsucho", "Shinagawa"],
        "Shinagawa": ["Tamachi", "Osaki"],
        "Osaki": ["Shinagawa", "Gotanda"],
        "Gotanda": ["Osaki", "Meguro"],
        "Meguro": ["Gotanda", "Ebisu"],
        "Ebisu": ["Meguro", "Shibuya"],
        "Shibuya": ["Ebisu", "Harajuku"],
        "Harajuku":["Yoyogi", "Shibuya"]
          }

#Metodo para generar las uniones en el grafo
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges

edges = generate_edges(graph)
#print(generate_edges(graph))


#Se crea un grafo y se le anaden los valores
G = nx.Graph()
G.add_edges_from(edges)

#Se anaden los pesos asociados al tiempo en min
G['Shinjuku']['Yoyogi']['weight']=1
G['Yoyogi']['Sendagaya']['weight']=2
G['Sendagaya']['Shinanomachi']['weight']=2
G['Shinanomachi']['Yotsuya']['weight']=2
G['Yotsuya']['Iichigaya']['weight']=2
G['Iichigaya']['Iidabashi']['weight']=2
G['Iidabashi']['Suidobashi']['weight']=2
G['Suidobashi']['Ochanomizu']['weight']=3
G['Ochanomizu']['Akihabara']['weight']=2
G['Shinjuku']['Ochanomizu']['weight']=10
G['Ochanomizu']['Tokyo']['weight']=4
G['Kanda']['Tokyo']['weight']=4
G['Kanda']['Akihabara']['weight']=2
G['Akihabara']['Okachimachi']['weight']=1
G['Okachimachi']['Ueno']['weight']=2
G['Ueno']['Uguisudani']['weight']=3
G['Uguisudani']['Nippori']['weight']=2
G['Nippori']['Nishi-Nippori']['weight']=1
G['Nishi-Nippori']['Tabata']['weight']=2
G['Tabata']['Komagome']['weight']=2
G['Komagome']['Sugamo']['weight']=2
G['Sugamo']['Otsuka']['weight']=2
G['Otsuka']['Ikebukuro']['weight']=4
G['Ikebukuro']['Mejiro']['weight']=3
G['Mejiro']['Takadanobaba']['weight']=2
G['Takadanobaba']['Shin-Okubo']['weight']=2
G['Shin-Okubo']['Shinjuku']['weight']=3
G['Shinjuku']['Yoyogi']['weight']=1
G['Yoyogi']['Harajuku']['weight']=3
G['Harajuku']['Shibuya']['weight']=2
G['Shibuya']['Ebisu']['weight']=2
G['Ebisu']['Meguro']['weight']=2
G['Meguro']['Gotanda']['weight']=2
G['Gotanda']['Osaki']['weight']=2
G['Osaki']['Shinagawa']['weight']=4
G['Shinagawa']['Tamachi']['weight']=3
G['Tamachi']['Hamamatsucho']['weight']=2
G['Hamamatsucho']['Shimbashi']['weight']=3
G['Shimbashi']['Yurakucho']['weight']=2
G['Yurakucho']['Tokyo']['weight']=1

#Ejemplo obtener tiempo entre dos estaciones continuas
#print(G.get_edge_data('Shimbashi', 'Yurakucho'))
#print(G.get_edge_data('Yurakucho', 'Yoyogi'))

#print(nx.astar_path(G,"Yoyogi", "Tokyo"))

#Se dibuja con los nombres y se imprime
#nx.draw(G, with_labels=True)
#plt.show()

