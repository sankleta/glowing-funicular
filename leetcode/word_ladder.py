import collections
import string


class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(set)

    def add(self, start, end):
        self.graph[start].add(end)
        self.graph[end].add(start)

    def bfs(self, start, end):
        visited = set()
        queue = collections.deque()
        queue.append([start,1])
        while queue:
            node, level = queue.popleft()
            if node in visited:
                continue
            if node == end:
                return level
            for i in self.graph[node]:
                queue.append([i, level+1])
            visited.add(node)
        return 0


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        wordList.append(beginWord)
        alphabet = list(string.ascii_lowercase)
        graph = Graph()
        for i in range(len(beginWord)):
            for j in alphabet:
                for l in wordList:
                    generated_word = l[:i] + j + l[i + 1:]
                    if generated_word!=l and generated_word in wordSet:
                        graph.add(l, generated_word)

        return graph.bfs(beginWord, endWord)


a = Solution()
print(a.ladderLength("a", "c",["a","b","c"]))