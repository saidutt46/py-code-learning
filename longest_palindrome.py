def longest_palindrome(s):
    unique_set = set(s)
    unique_char_indices = []
    palindromes = []
    possible_sets = []
    if len(s) == 1:
        print(s)
        return s
    else:
        for i in unique_set:
            current_indices = []
            for index, val in enumerate(s):
                if val == i:
                    current_indices.append(index)
            unique_char_indices.append(current_indices)
        for unique_char_set in unique_char_indices:
            for check_set in unique_char_set:
                for mash in range(check_set):
                    possible_sets.append(s[mash:check_set + 1])
        for possibility in possible_sets:
            if possibility == possibility[::-1]:
                palindromes.append(possibility)
        if len(palindromes) == 0:
            if s == '':
                return ''
            else:
                return s[0]
        else:
            return max(palindromes, key=len)
            
                
                
print(longest_palindrome('ac'))