class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        ans = []
        replace = []
        for i in range(len(indexes)):
            replace.append([indexes[i], sources[i], targets[i]])
        replace.sort(key=lambda x: x[0])
        ans.append(S[0:replace[0][0]])
        for i in range(len(replace)):
            match = True
            for j in range(0, len(replace[i][1])):
                if S[j + replace[i][0]] != replace[i][1][j]:
                    if i < len(replace) - 1:
                        ans.append(S[replace[i][0]:replace[i+1][0]])
                    else:
                        ans.append(S[replace[i][0]:])
                    match = False
                    break
            if match:
                ans.append(replace[i][2])
                if i < len(replace) - 1:
                    ans.append(S[(replace[i][0] + len(replace[i][1])):replace[i+1][0]])
                else:
                    ans.append(S[(replace[i][0] + len(replace[i][1])):])

        return "".join(ans)


c = Solution()
print(c.findReplaceString(S="vmokgggqzp", indexes=[3,5,1], sources=["kg","ggq","mo"], targets=["s","so","bfr"]))
