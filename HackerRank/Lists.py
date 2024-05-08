if __name__ == '__main__':
    N = int(input())
    arr =[]
    for i in range(N):
        item = input()
        if "insert" in item:
            num = item.split()
            arr.insert(int(num[1]),int(num[2]))
        elif "remove" in item :
            num = item.split()
            arr.remove(int(num[1]))
        elif "append" in item :
            num = item.split()
            arr.append(int(num[1]))
        elif "sort" in item:
            arr.sort() 
        elif "pop" in item:
            arr.pop()
        elif "reverse" in item:
            arr.reverse()
        elif "print" in item:
            print(arr)