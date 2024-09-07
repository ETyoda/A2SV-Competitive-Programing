def string_task(s):
    vowels = set("aoyeuiAOYEUI") 
    result = []
    for char in s:
        if char not in vowels: 
            result.append('.')
            result.append(char.lower())  
    return ''.join(result)
s = input()
print(string_task(s))
