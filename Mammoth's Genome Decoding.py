def decode_genome(n, s):
    
    from collections import Counter
    count = Counter(s)
    
    a_count = count['A']
    c_count = count['C']
    g_count = count['G']
    t_count = count['T']
    question_count = count['?']
    
    
    target_count = n // 4
    

    a_needed = target_count - a_count
    c_needed = target_count - c_count
    g_needed = target_count - g_count
    t_needed = target_count - t_count
    
    
    if (a_needed < 0 or c_needed < 0 or g_needed < 0 or t_needed < 0 or 
        a_needed + c_needed + g_needed + t_needed != question_count):
        return "==="

    result = []
    for char in s:
        if char == '?':
            if a_needed > 0:
                result.append('A')
                a_needed -= 1
            elif c_needed > 0:
                result.append('C')
                c_needed -= 1
            elif g_needed > 0:
                result.append('G')
                g_needed -= 1
            elif t_needed > 0:
                result.append('T')
                t_needed -= 1
        else:
            result.append(char)
    
    return ''.join(result)


n = int(input().strip())
s = input().strip()


print(decode_genome(n, s))
