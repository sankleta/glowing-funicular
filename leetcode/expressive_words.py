class Solution:
    def counter(self, word):
        letter_count = []
        count_index = None
        if len(word) >= 2:
            for i in range(len(word)):
                if i > 0:
                    if word[i - 1] == word[i]:
                        letter_count[count_index][1] = letter_count[count_index][1] + 1
                    else:
                        letter_count.append([word[i], 1])
                        count_index += 1
                else:
                    letter_count.append([word[0], 1])
                    count_index = 0
        elif word:
            letter_count.append([word[0], 1])
        return letter_count

    def expressiveWords(self, S, words):
        ans = 0
        if len(S) == 0 or len(words) == 0:
            return ans

        if len(S) > 2:
            s_count = self.counter(S)
            for word in words:
                word_count = self.counter(word)
                if len(s_count) == len(word_count):
                    is_stretchy = True
                    for i in range(len(s_count)):
                        if s_count[i][0] == word_count[i][0]:
                            if s_count[i][1] < 3:
                                if s_count[i][1] != word_count[i][1]:
                                    is_stretchy = False
                                    break
                            else:
                                if s_count[i][1] < word_count[i][1]:
                                    is_stretchy = False
                                    break
                        else:
                            is_stretchy = False
                            break
                    if is_stretchy:
                        ans += 1
        else:
            for i in words:
                if i == S:
                    ans += 1
        return ans


c = Solution()
print(c.expressiveWords("heeellooo", ["hello", "hi", "helo"]))
