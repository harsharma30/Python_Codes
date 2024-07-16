class Solution:
    def isPalin(self, N):

        str_N = str(N)

        start = 0
        end = len(str_N) - 1

        while start <= end:
            if str_N[start] != str_N[end]:
                return 0  
            start += 1
            end -= 1
        return 1


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())

        obj = Solution()
        print(int(obj.isPalin(n)))


