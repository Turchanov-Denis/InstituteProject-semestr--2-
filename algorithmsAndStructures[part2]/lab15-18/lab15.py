# Решить задачу о раскраске графа.
from igraph import *
from sympy import solve, symbols

# Зададим количество вершин
NumberOfVertices = 8
# Перечислим все ребра нашего графа
EdgesList = [(0,1), (0,4), (0,5),  (1,7), (1,2), (2,3), (2,7), (1,3), (3,4), (3,6), (4,5), (4,6),(5,6), (6,7)]

# Инициализируем граф, обозначив его вершины с помощью символов x1,...x8
TestGraph = Graph()
TestGraph.add_vertices(NumberOfVertices)
TestGraph.add_edges(EdgesList)
x1, x2, x3, x4, x5, x6, x7, x8 = symbols("x1 x2 x3 x4 x5 x6 x7 x8")
TestGraph.vs["name"] = [x1, x2, x3, x4, x5, x6, x7, x8]
TestGraph.vs["label"] = TestGraph.vs["name"]

# Генерируем уравнения для системы, определяющей раскраску
EquationList=[]
for edge in EdgesList:
    EquationList.append("x%d^2 + x%d * x%d + x%d^2"%(edge[0]+1,edge[0]+1,edge[1]+1,edge[1]+1))
for vertice in range(NumberOfVertices):
    EquationList.append("x%d^3-1"%(vertice+1))

# Сопоставляем кубическим корням из единицы красную, зеленую и синию краски
Roots = solve(x1**3-1)
RootsToColors = {Roots[0]: "red", Roots[1]: "green", Roots[2]: "blue"}

# Непосредственно решаем систему уравнений
Colorings = solve(EquationList, dict=True)
print("The number of colorings is %d."%len(Colorings))

# Если система совместна, то выводим k-ю раскраску. 
# Если нет, то делаем вывод о том, что граф нельзя раскрасить в три цвета.
if(Colorings):
    # Раскрашиваем вершины графа
    k = 0
    RawColors = [Colorings[k][vertice] for vertice in TestGraph.vs["name"]]
    ColorDictionary = [RootsToColors[color] for color in RawColors]
    TestGraph.vs["color"]=ColorDictionary
    
    # Укладываем граф на плоскость и рисуем
    Layout = TestGraph.layout_kamada_kawai()
    visual_style = {}
    visual_style["vertex_size"] = 40
    visual_style["bbox"] = (300, 300)
    plot(TestGraph, layout=Layout, **visual_style)
else:
    print("The graph is non-colorable.")