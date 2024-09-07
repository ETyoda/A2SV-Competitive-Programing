def decode_string(n, s):
    word = []
    for i in range(n):       
        if i % 2 == 0:
            word.insert(0, s[i])  
        else:
            word.append(s[i])  
    if n % 2 != 0:
        word.reverse()  
    return ''.join(word)
n = int(input())
s = input()
result = decode_string(n,s)
print(result)