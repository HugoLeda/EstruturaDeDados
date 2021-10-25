# 1
grafo = [
  {
    "vertice": 'a',
    "arestas": ['c', 'd', 'f']
  },
  {
    "vertice": 'b',
    "arestas": ['d', 'e']
  },
  {
    "vertice": 'c',
    "arestas": ['a', 'f']
  },
  {
    "vertice": 'd',
    "arestas": ['a', 'b', 'e', 'f']
  },
  {
    "vertice": 'e',
    "arestas": ['b', 'd']
  },
  {
    "vertice": 'f',
    "arestas": ['a', 'c', 'd']
  },
  {
    "vertice": 'g',
    "arestas": []
  }
]

for i in grafo:
  print(i)
