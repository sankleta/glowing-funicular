class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        out = []
        minimum = None
        maximum = None
        for i in intervals:
            if minimum is not None:
                if i[0] > maximum:
                    out.append([minimum, maximum])
                    minimum = i[0]
                    maximum = i[1]
                else:
                    if i[1] > maximum:
                        maximum = i[1]
            else:
                minimum = i[0]
                maximum = i[1]
        out.append([minimum, maximum])
        return out


a = Solution()
print(a.merge([[1, 4], [0, 4]]))
