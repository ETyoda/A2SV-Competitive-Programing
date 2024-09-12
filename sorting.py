def min_moves_to_equal(s, t):
    # Initialize pointers for both strings from the end
    i, j = len(s) - 1, len(t) - 1
    
    # Find the length of the longest common suffix
    while i >= 0 and j >= 0 and s[i] == t[j]:
        i -= 1
        j -= 1
    
    # Length of the longest common suffix
    common_suffix_length = len(s) - (i + 1)
    
    # Compute total moves needed
    total_moves = (len(s) - common_suffix_length) + (len(t) - common_suffix_length)
    
    return total_moves

# Input strings
s = input().strip()
t = input().strip()

# Calculate and print the result
print(min_moves_to_equal(s, t))
