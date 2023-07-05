def replace_code(s):
    return s.replace("A#", "a").replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g")

def solution(m, musicinfos):
    answer = '(None)'
    m = replace_code(m)
    l = 0
    for i in musicinfos:
        s_t, e_t, song, code = i.split(',')
        s_h, s_m = map(int, s_t.split(':'))
        e_h, e_m = map(int, e_t.split(':'))
        s_t = s_h*60+s_m
        e_t = e_h*60+e_m
        now_l = e_t-s_t
        code = replace_code(code)
        code = code*(now_l//len(code))+code[:now_l%len(code)]
        if m in code:
            if l < now_l:
                answer = song
                l = now_l
    return answer