if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(n,0,-1):
    	if arr[i-2]<arr[i-1]:
    		print(arr[i-2])
    		break