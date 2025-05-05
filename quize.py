def two_sum(nums, target):
    '''
    two_sum([2,4,6,5], 9)
    '''
    num_dict = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in num_dict:
            return [i, num_dict[complement]]
        num_dict[nums[i]] = i
    return None

def reverse_string(s):
    '''
    reverse_string('hello')
    'olleh'
    '''
    word = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1
    return ''.join(word)

def valid_palindrome(s):
    '''
    valid_palindrome('c,are,erac'):
    True
    '''

    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

def valid_anagram(s, t):
    '''
    valid_anagram("anagram", "nagaram")
    True
    '''
    s_counter = {}
    if len(s) != len(t):
        return False
    
    for c1, c2 in zip(s, t):
        s_counter[c1] = s_counter.get(c1, 0) + 1
        s_counter[c2] = s_counter.get(c2, 0) - 1
    return all(v == 0 for v in s_counter.values())


def longest_substr_without_repeat_chars(s):
    '''
    longest_substr_without_repeat_chars("pwwkew")
    3
    '''
    left = 0
    max_len = 0
    seen = set()
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len= max(max_len, right - left + 1)
    return max_len