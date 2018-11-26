class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbours = []


class Graph:
    def __init__(self):
        self.vertexes = []

    def add_pair_sweet_couple(self, vertex1, vertex2):

        iter = 0
        for v in self.vertexes:
            if v.value == vertex1.value:
                vertex1 = v
                self.vertexes.pop(iter)
            iter += 1

        iter = 0
        for v in self.vertexes:
            if v.value == vertex2.value:
                vertex2 = v
                self.vertexes.pop(iter)
            iter += 1

        vertex1.neighbours.append(vertex2)
        vertex2.neighbours.append(vertex1)
        self.vertexes.append(vertex1)
        self.vertexes.append(vertex2)

    def dfs(self, start, searched_elem):
        is_visited = {v.value: False for v in self.vertexes}
        stack = [start]

        while stack:
            vertex = stack.pop()

            if vertex.value == searched_elem.value:
                return True

            if is_visited[vertex.value]:
                continue
            is_visited[vertex.value] = True
            for neighbour in vertex.neighbours:
                stack.append(neighbour)
        return False


def reading_graph_from_file(graph, filename):
    with open(filename) as file:
        strings = file.readlines()

    for line in strings[1:]:
        pair = line.split(" ")
        graph.add_pair_sweet_couple(Vertex(int(pair[0])), Vertex(int(pair[1])))


graph = Graph()

reading_graph_from_file(graph, "in2")

wedding_count = 0
for i in range(graph.vertexes.__len__()):
    for j in range(i + 1, graph.vertexes.__len__()):
        if not graph.dfs(graph.vertexes[i], graph.vertexes[j]):
            if (graph.vertexes[i].value % 2 == 0 and graph.vertexes[j].value % 2 != 0) or (
                    graph.vertexes[i].value % 2 != 0 and graph.vertexes[j].value % 2 == 0):
                wedding_count += 1
                print("%d - %d" % (graph.vertexes[i].value, graph.vertexes[j].value))

print("All weddings: %d" % wedding_count)