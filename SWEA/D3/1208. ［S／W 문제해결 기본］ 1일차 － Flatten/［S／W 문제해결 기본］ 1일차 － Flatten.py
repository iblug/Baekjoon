for t in range(10):
    n = int(input())
    data = list(map(int, input().split()))
    max_ = max(data)
    min_ = min(data)
    graph = {}
    for d in data:
        graph[d] = graph.get(d,0) + 1

    while n > 0:
        
        graph[max_] -= 1
        graph[max_-1] = graph.get(max_-1, 0) + 1
        
        graph[min_] -= 1
        graph[min_+1] = graph.get(min_+1, 0) + 1

        n -= 1

        if not graph[max_]:
            max_ -= 1
        if not graph[min_]:
            min_ += 1
        if min_ >= max_:
            break
        
    print(f'#{t+1} {max_-min_}')