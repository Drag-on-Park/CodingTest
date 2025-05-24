def solution(topping):
    set_1 = {}
    set_2 = set()
    answer = 0
    cnt = 1

    for num in topping:
        set_1[num] = set_1.get(num,0) + 1
    for i, num in enumerate(topping):
        set_2.add(num)
        set_1[num] -= 1
        if set_1[num] == 0:
            del set_1[num]
        if len(set_1.keys()) == len(set_2):
            answer += 1
    print(answer)
    return answer

topping = [1,2,2,3,1,5,4] # 1
solution(topping)
