# Полный ориентированный взвешенный граф задан матрицей смежности.
# Постройте матрицу кратчайших путей между его вершинами. Гарантируется,
# что в графе нет циклов отрицательного веса.


def floyd_warshall(nodes_no, paths):
    for k in range(nodes_no):
        for i in range(nodes_no):
            for j in range(nodes_no):
                if paths[i][j] > (paths[i][k] + paths[k][j]):
                    paths[i][j] = (paths[i][k] + paths[k][j])


nodes_no = int(input())
paths = []
for i in range(nodes_no):
    line = list(map(lambda x: int(x), input().split()))
    paths.append(line)

floyd_warshall(nodes_no, paths)
for line in paths:
    print(" ".join([str(elem) for elem in line]))
