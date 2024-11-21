import math


def get_path(P, u, v):
    path = [u]
    while u != v:
        u = P[u][v] # P содержит промежуточные верщины между начальной и конечной вершиной
        # Мы ищем промежуточные вершины пока не дойдем до точки отсчета
        path.append(u)

    return path


V = [[0, 1, math.inf, math.inf, 2, math.inf],
     [1, 0, 3, math.inf, math.inf, math.inf],
     [math.inf, 3, 0, 7, math.inf, 10],
     [math.inf, math.inf, 7, 0, 4, math.inf],
     [2, math.inf, math.inf, 4, 0, 1],
     [math.inf, math.inf, 10, math.inf, 1, 0]]

N = len(V) # число вершин в графе
P = [[v for v in range(N)] for u in range(N)] # начальный список предыдущих вершин для поиска кратчайших маршрутов

for k in range(N):
    for i in range(N):
        for j in range(N):
            d = V[i][k] + V[k][j]
            if V[i][j] > d: # Если полученная длина от точки i до j через точку k меньше уже существующей
                V[i][j] = d # То меняем значение
                P[i][j] = k # номер промежуточной вершины при движении от i к j

# нумерация вершин начинается с нуля
start = 1
end = 5
print(get_path(P, end, start))