def passed(prev_s, s, target):
    # 초침이 360도를 넘어갈 때 처리
    if prev_s > s:  # 초침이 360도를 지남
        return prev_s <= target or target <= s
    return prev_s <= target <= s

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    # 각 바늘의 초당 이동 각도
    h_speed = 1/120  # 시침: 360° / (12 * 3600) = 0.008333°/초
    m_speed = 0.1    # 분침: 360° / (60 * 60) = 0.1°/초
    s_speed = 6      # 초침: 360° / 60 = 6°/초

    # 시간을 초 단위로 변환
    start_sec = h1 * 3600 + m1 * 60 + s1
    end_sec = h2 * 3600 + m2 * 60 + s2
    total_seconds = end_sec - start_sec

    # 시작 시점 각도
    h_deg = (h_speed * start_sec) % 360
    m_deg = (m_speed * start_sec) % 360
    s_deg = (s_speed * start_sec) % 360

    # 시작 시점 겹침은 지나침으로 카운트하지 않음
    prev_s = s_deg

    # 루프: start_sec + 1부터 end_sec까지
    for i in range(total_seconds):
        current_time = start_sec + i + 1

        # 각도 업데이트
        h_deg = (h_deg + h_speed) % 360
        m_deg = (m_deg + m_speed) % 360
        s_deg = (s_speed * current_time) % 360

        # 세 바늘이 겹치는 경우는 지나침으로 카운트하지 않음
        if abs(h_deg - m_deg) < 1e-5 and abs(m_deg - s_deg) < 1e-5:
            prev_s = s_deg
            continue

        # 초침이 시침 또는 분침을 지났는지 확인
        passed_hour = passed(prev_s, s_deg, h_deg)
        passed_minute = passed(prev_s, s_deg, m_deg)

    
        if passed_hour:
            answer += 1
        elif passed_minute:
            answer += 1

        prev_s = s_deg

    return answer

# 테스트
result = solution(0, 0, 0, 23, 59, 59)
print(f"총 횟수: {result}")