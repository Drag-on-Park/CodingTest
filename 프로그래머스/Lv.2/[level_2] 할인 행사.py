############# 제출
# 연속할인품목**
# dictionary(want + number)
# 하나씩 반복 확인 (continue)
# 2중 반복 disc[] > pop > disc[1:] > pop > disc[2:]
def solution(want, number, discount):
    answer = 0
    dict_inv = {}
    popped_disc = []
    dict_inv_c = {}

    for idx, i in enumerate(want):
        dict_inv.get(0,1)
        dict_inv[i] = number[idx]

    popped_disc = discount.copy()
    
    for x in range(len(discount)):
        dict_inv_c = dict_inv.copy()  
        ## copy()
        for i in popped_disc:
            # 원하는 품목에 들어있지 않음
            if i not in dict_inv_c:
                popped_disc.pop(0)
                break
            # 원하는 품목에 들어있다면 -1
            if i in dict_inv:
                dict_inv_c[i] -= 1    
            # 원하는 품목에서 삭제
            if dict_inv_c[i] == 0:
                del dict_inv_c[i]
                          
            if not dict_inv_c:
                answer += 1
                popped_disc.pop(0)
                break
    print(f"answer: {answer}")
    return answer

# return 0일 때 

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
solution(want, number, discount)
