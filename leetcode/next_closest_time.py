class Solution:
    def nextClosestTime(self, time):
        hours, minutes = time.split(":")
        numbers = set()
        for i in (hours + minutes):
            numbers.add(int(i))
        numbers = list(numbers)
        numbers.sort()

        m = int(minutes[1])
        m_index = numbers.index(m)

        if m_index < len(numbers) - 1:
            return "{}:{}{}".format(hours, minutes[0], numbers[m_index + 1])
        else:
            m = numbers[0]

        M = int(minutes[0])
        M_index = numbers.index(M)

        if M_index < len(numbers) - 1 and numbers[M_index + 1] < 6:
            return "{}:{}{}".format(hours, numbers[M_index + 1], m)
        else:
            M = numbers[0]

        h = int(hours[1])
        H = int(hours[0])
        h_index = numbers.index(h)

        if H < 2:
            if h_index < len(numbers) - 1:
                return "{}{}:{}{}".format(H, numbers[h_index + 1], M, m)
            else:
                h = numbers[0]
        else:
            if h_index < len(numbers) - 1 and numbers[h_index + 1] <= 3:
                return "{}{}:{}{}".format(H, numbers[h_index + 1], M, m)
            else:
                h = numbers[0]

        H_index = numbers.index(H)
        if H_index < len(numbers) - 1 and numbers[H_index + 1] <= 2:
            return "{}{}:{}{}".format(numbers[H_index + 1], h, M, m)
        else:
            return "{}{}:{}{}".format(numbers[0], h, M, m)


c = Solution()
print(c.nextClosestTime("22:23"))
