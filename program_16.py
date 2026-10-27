from typing import List
import random


def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0

    m, n = len(needle), len(haystack)
    lps = [0] * m

    j = 0
    for i in range(1, m):
        while j > 0 and needle[i] != needle[j]:
            j = lps[j - 1]

        if needle[i] == needle[j]:
            j += 1
            lps[i] = j

    i = j = 0

    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1

            if j == m:
                return i - j
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


class Randomizer:
    def __init__(self):
        self.count = 0
        self.sample = None

    def getRandom(self) -> int:
        return random.randint(0, self.count - 1)

    def sample_stream(self, stream: List[int]) -> int:
        self.count = 0
        self.sample = None

        for item in stream:
            self.count += 1

            if self.getRandom() == 0:
                self.sample = item

        return self.sample


print("strStr('hello', 'll'):", strStr("hello", "ll"))

r = Randomizer()
print("r.sample_stream([10, 20, 30, 40, 50]):", r.sample_stream([10, 20, 30, 40, 50]))