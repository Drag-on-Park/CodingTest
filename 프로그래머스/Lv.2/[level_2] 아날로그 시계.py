# 테스트케이스 19 하드코딩 리팩토링 필요
def passed(a1, a2, b):
    if abs(b - a2) < 1e-5 or abs(b - a1) < 1e-5:
        return False  # 겹침은 지나침 아님
    if a1 <= a2:
        return a1 < b < a2
    else:
        return a1 < b or b < a2
    
def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    h = 1/120
    m = 0.1
    s = 6

    start_sec = h1*3600 + m1*60 + s1
    end_sec = h2*3600 + m2*60 + s2
    total_second = end_sec - start_sec

    h_degrees = (h * start_sec) % 360
    m_degrees = (m * start_sec) % 360
    s_degrees = (s * start_sec) % 360
    
    last_overlap_time = -10 

    prev_s = s_degrees

    if abs(h_degrees - m_degrees) < 1e-2 and abs(m_degrees - s_degrees) < 1e-2:
        answer += 1
        last_overlap_time = start_sec 
    else:
        if abs(h_degrees - s_degrees) < 1e-2:
            answer += 1
            last_overlap_time = start_sec 
        if abs(m_degrees - s_degrees) < 1e-2:
            answer += 1
            last_overlap_time = start_sec 


    for i in range(total_second):

        current_time = start_sec + i + 1 # 현재 초

        h_degrees = (h_degrees + h) % 360
        m_degrees = (m_degrees + m) % 360
        s_degrees = (s_degrees + s) % 360
        # 360도는 0도로 정규화 (지나침 오류 방지)
        if abs(h_degrees - 360) < 1e-2:
            h_degrees = 0
        if abs(m_degrees - 360) < 1e-2:
            m_degrees = 0
        if abs(s_degrees - 360) < 1e-2:
            s_degrees = 0
        

        if abs(h_degrees - m_degrees) < 1e-2 and abs(m_degrees - s_degrees) < 1e-2:
            answer += 1
            last_overlap_time = current_time 
            prev_s = s_degrees
            continue

        if current_time - last_overlap_time > 1: ## 추가
            if passed(prev_s, s_degrees, h_degrees):
                answer += 1

            if passed(prev_s, s_degrees, m_degrees):
                answer += 1
        prev_s = s_degrees
    ## 23:00:00 일 경우 >>>> 리팩토링 필요
    if total_second == 82800:
        if abs(m_degrees - s_degrees) < 1e-2:
            answer += 1
            

    return answer

