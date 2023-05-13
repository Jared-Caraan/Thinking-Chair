# Convert roman numerals to integer value

def romanToInt(s: str) -> int:

        result = 0

        for i in range(len(s)):
            if s[i] == 'I':
                result += 1
            elif s[i] == 'V':
                if i != 0 and s[i-1] == 'I':
                         result += 3
                else:
                    result += 5
            elif s[i] == 'X':
                if i != 0 and s[i-1] == 'I':
                         result += 8
                else:
                    result += 10
            elif s[i] == 'L':
                if i != 0 and s[i-1] == 'X':
                         result += 30
                else:
                    result += 50
            elif s[i] == 'C':
                if i != 0 and s[i-1] == 'X':
                         result += 80
                else:
                    result += 100
            elif s[i] == 'D':
                if i != 0 and s[i-1] == 'C':
                         result += 300
                else:
                    result += 500
            elif s[i] == 'M':
                if i != 0 and s[i-1] == 'C':
                         result += 800
                else:
                    result += 1000
        
        return result

print(romanToInt('MCMXCIV'))