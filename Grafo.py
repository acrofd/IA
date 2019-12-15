import networkx as nx


#Se incializa un array de las estaciones y sus conexiones.
graph = { "Shinjuku": [ "Yoyogi", "Shin-Okubo", "Ochanomizu","Sendagaya"],
        "Yoyogi": ["Shinjuku", "Sendagaya", "Harajuku"],
        "Ochanomizu": ["Tokyo", "Suidobashi", "Shinjuku"],
        "Sendagaya": ["Yoyogi", "Shinanomachi", "Shinjuku"],
        "Shinanomachi": ["Sendagaya", "Yotsuya"],
        "Yotsuya": ["Shinanomachi", "Iichigaya"],
        "Iichigaya": ["Yotsuya", "Iidabashi"],
        "Iidabashi": ["Iichigaya", "Suidobashi"],
        "Suidobashi": ["Ochanomizu","Iidabashi", "Akihabara", ],
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
        "Kanda": ["Akihabara", "Tokyo"],
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

#Se anaden los pesos asociados a la distancia en km
G['Shinjuku']['Yoyogi']['weight']=0.77
G['Shinjuku']['Ochanomizu']['weight']=7.8
G['Shinjuku']['Sendagaya']['weight']=1.6
G['Shin-Okubo']['Shinjuku']['weight']=1.2
G['Yoyogi']['Sendagaya']['weight']=1
G['Yoyogi']['Harajuku']['weight']=1.5
G['Sendagaya']['Shinanomachi']['weight']=0.84
G['Shinanomachi']['Yotsuya']['weight']=1.2
G['Yotsuya']['Iichigaya']['weight']=0.8
G['Iichigaya']['Iidabashi']['weight']=1.4
G['Iidabashi']['Suidobashi']['weight']=0.88
G['Suidobashi']['Ochanomizu']['weight']=1.1
G['Suidobashi']['Akihabara']['weight']=1.7
G['Ochanomizu']['Tokyo']['weight']=2.45
G['Kanda']['Tokyo']['weight']=1.23
G['Kanda']['Akihabara']['weight']=0.73
G['Akihabara']['Okachimachi']['weight']=1
G['Okachimachi']['Ueno']['weight']=0.63
G['Ueno']['Uguisudani']['weight']=1.1
G['Uguisudani']['Nippori']['weight']=0.87
G['Nippori']['Nishi-Nippori']['weight']=0.61
G['Nishi-Nippori']['Tabata']['weight']=0.75
G['Tabata']['Komagome']['weight']=1.5
G['Komagome']['Sugamo']['weight']=0.91
G['Sugamo']['Otsuka']['weight']=1.1
G['Otsuka']['Ikebukuro']['weight']=2
G['Ikebukuro']['Mejiro']['weight']=1.15
G['Mejiro']['Takadanobaba']['weight']=0.86
G['Takadanobaba']['Shin-Okubo']['weight']=1
G['Harajuku']['Shibuya']['weight']=1.5
G['Shibuya']['Ebisu']['weight']=1.5
G['Ebisu']['Meguro']['weight']=1.5
G['Meguro']['Gotanda']['weight']=1.2
G['Gotanda']['Osaki']['weight']=0.84
G['Osaki']['Shinagawa']['weight']=2.1
G['Shinagawa']['Tamachi']['weight']=2.2
G['Tamachi']['Hamamatsucho']['weight']=1.46
G['Hamamatsucho']['Shimbashi']['weight']=1.26
G['Shimbashi']['Yurakucho']['weight']=1.1
G['Yurakucho']['Tokyo']['weight']=0.77

