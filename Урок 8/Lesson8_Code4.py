from collections import deque

g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]

def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    deq = deque([start])
    # до внешнего цикла отметим, что мы посетили первую вершину
    is_visited[start] = True

    while len(deq) > 0:
        # пока длина очереди больеш нуля, т.е. есть вершина
        current = deq.pop()
        # из конца очереди извлекаем вершину и проверяем её с финишом
        if current == finish:
            # return parent
            break

        # просматриваем все вершины, которые связаны с нашей текущей вершиной
        # в цикле пройдёмся по строке каррент в нашей матрице смежности.
        for i, vertex in enumerate(graph[current]):
            # если очередная вершина равна единице, т.е. мы можем перейти из текущей вершины в эту
            # и при этом мы её ещё не посещали

            if vertex == 1 and not is_visited[i]:
                # отмечаем вершину как посещённую
                is_visited[i] = True
                # в списке парент указываем из какой вершины мы пришли
                parent[i] = current
                # добавляем в начало очереди итую вершину
                deq.appendleft(i)
    # если очередь опустеет, то цикл вайл завершится: значит из старт нельзя попасть в финиш
    else:
        return f'Из вершины {start} нельзя попасть в вершину{finish}'

    # [2, 0, None, None, 2, 6, 4, 6]
    # logika: idjom
    # v
    # 5 - j
    # indeks(t.k.nam
    # nado
    # popast
    # ' v 5 vers"inu) - tam vidim 6... idjom v indeks 6 - tam vidim 4... idjom v indeks 4 i tam vidim 2.
    #
    # poluc
    # "ajetsja: 5 -> 6 -> 4 -> 2

    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return f'кратчайший путь {list(way)} длинною в {cost} условных единиц'

s = int(input('От какой вершины идти: '))
f = int(input('До какой вершины идти: '))

print(bfs(g, s, f))