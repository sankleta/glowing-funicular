class UnionFind:
    def __init__(self, size):
        self.elements = []
        self.size = size
        for i in range(0, size):
            self.elements.append([i, 0])

    def find_root_and_compress(self, pointer, index):
        compress = []
        while pointer != index:
            compress.append(index)
            index = pointer
            parent = self.elements[pointer]
            pointer = parent[0]
        if len(compress) > 1:
            for i in compress:
                self.elements[i][0] = pointer
        return pointer

    def find(self, element_no):
        element = self.elements[element_no - 1]
        index = self.find_root_and_compress(element[0], element_no - 1)
        return index

    def union(self, first_element_no, second_element_no):
        first_root_index = self.find(first_element_no)
        second_root_index = self.find(second_element_no)
        if first_root_index != second_root_index:
            first_cluster_root = self.elements[first_root_index]
            second_cluster_root = self.elements[second_root_index]
            if first_cluster_root[1] > second_cluster_root[1]:
                self.elements[second_cluster_root[0]][0] = first_cluster_root[0]
            elif second_cluster_root[1] > first_cluster_root[1]:
                self.elements[first_cluster_root[0]][0] = second_cluster_root[0]
            else:
                first_cluster_root[1] = first_cluster_root[1]+1
                self.elements[second_cluster_root[0]][0] = first_cluster_root[0]
            self.size -= 1
