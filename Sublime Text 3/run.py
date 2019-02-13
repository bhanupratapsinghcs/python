if __name__ == '__main__':
    n = int(input())
    #arr = map(int, input().split())
    lst = []
    for i in range(n+1):
    	lst.append([])
        lst[i] = int(input()) 
lst.sort()
print(n-1)
