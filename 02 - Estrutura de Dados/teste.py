T = int(input())

for i in range(T):
   
    N, K = map(int, input().split())
    GARRAFAS = N//K + N%K
    print(GARRAFAS)