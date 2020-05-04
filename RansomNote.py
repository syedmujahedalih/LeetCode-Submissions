from collections import Counter

def canConstruct(ransomNote: str, magazine: str):
    
    if len(ransomNote) > len(magazine):
        return False
                
    c1 = Counter(ransomNote)
    c2 = Counter(magazine)
    
    for char, count in c1.items():
        if char not in c2:
            return False
        if c2[char] < count:
            return False
    
    return True