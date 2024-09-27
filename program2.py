def romanToInt(s: str) -> int:
    roman_map = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000
    }
    
    total = 0  
    
    for i in range(len(s)):
        if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
            total -= roman_map[s[i]]
        else:
            total += roman_map[s[i]]
    
    return total

# Example usage:
print(romanToInt("III"))     
print(romanToInt("LVIII"))   
print(romanToInt("MCMXCIV"))