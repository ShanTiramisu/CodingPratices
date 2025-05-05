from collections import Counter

def two_sum(nums, target):
    '''
    Given an array of numbers and a target number,
    return the indices of the two numbers that add up to the target number.
    Example:
    nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    '''
    length = len(nums) 
    for i in range(length):
        j  = i + 1
        while j < length:
            if nums[i] + nums [j] == target:
                return [i, j]
            j += 1
    return []

def two_sum_hash(nums, target):
    lookup = {}
    for i, enum in enumerate(nums):
        complement = target - enum
        if complement in lookup:
            return [lookup[complement], i]
        lookup[enum] = i
    return []


def reverse_str(string):
    '''
    Given a string,
    return the reversed string.
    Example:
    input "hello"
    output "olleh"
    '''
    word = list(string)
    length = len(word)
    j = length - 1
    for i in range(length//2):
        temp = word[i]
        word[i] = word[j]
        word[j] = temp
        j -= 1 
    return ''.join(word)

def reverse_str_two_points(s):
    word = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1
    return ''.join(word)

        
def valid_palindrome(string):
    '''
    Given a string, 
    if the string is palindrome, then return True
    Ignore captialization, space and marks

    input "A man, a plan, a canal: Panama"
    Output: True
    '''
    chars = []
    for c in string:
        if c.isalnum():
            chars.append(c.lower())
            
    length = len(chars)
    j = length - 1
    for i in range(length//2):
        if chars[i] != chars[j]:
            return False
        j -= 1
    return True

def valid_palindrome_2points(string):
    '''
    Given a string, 
    if the string is palindrome, then return True
    Ignore captialization, space and marks

    input "A man, a plan, a canal: Panama"
    Output: True
    '''
    chars = []
    for c in string:
        if c.isalnum():
            chars.append(c.lower())
            
    left, right = 0, len(chars) - 1
    while left < right:
        if chars[left] != chars[right]:
            return False
        left += 1
        right -= 1
    return True

def is_valid_palindrome(nums):
    word = list(nums)
    left, right = 0, len(word) - 1
    while left < right:
        while left < right  and not word[left].isalnum():
            left += 1
        while left < right  and not word[right].isalum():
            right -= 1
        
        if word[left].lower() != word[right].lower():
            return False
        left += 1
        right -= 1
    return True



def is_anagram(s, t):
    '''
    Given two strings s and t,
    return True if t is an anagram of s, else return False
    '''
    sorted(s) == sorted(t)

def is_anagram_dict(s, t):
    '''
    Given two strings s and t,
    return True if t is an anagram of s, else return False
    '''
    if len(s) != len(t):
        return False
    count_s = {}
    count_t = {}
    for c in s:
        count_s[c] = count_s.get(c, 0) + 1
    for c in t:
        count_t[c] = count_t.get(c, 0) + 1
    return count_s == count_t

def is_anagram_inplace(s, t):
    if len(s) != len(t):
        return False
    count_s = {}
    for c in s:
        count_s[c] = count_s.get(c, 0) + 1
    
    for c in t:
        if c not in count_s:
            return False
        count_s[c] -= 1
        if count_s[c] < 0:
            return False
    return True


def count_chars(s):
    count_s = {}
    for c in s:
        if c in count_s:
            count_s[c] += 1
        else:
            count_s[c] = 1
    return count_s

def majority_element(nums):
    '''
    Given an array of numbers, return the element that appears more than n/2 times
    '''
    count_nums = {}
    for num in nums:
        count_nums[num] = count_nums.get(num, 0) + 1 
        if count_nums[num] > len(nums)//2:
            return num
    return

#boyer-moore
def majority_element_boyer_moore(nums):
    '''
    Given an array of numbers, return the element that appears more than n/2 times
    [3,2,3] output:3
    [2, ,2, 1, 1, 1, 2, 2] output:2
    [1, 1, 3, 2, 3] 
    '''
    count = 0
    canadidate = None
    for num in nums:
        if count == 0:
            canadidate = num
        if num == canadidate:
            count += 1
        else:
            count -=1
    if nums.count(canadidate) > len(nums)//2:
        return canadidate
    return None
    
#boyer-moore majority_element2_boyer_moore
def majority_element2_boyer_moore(nums):
    '''
    Given an array of numbers, return a array at most two element that appears more than n/3 times
    [3,2,3] output:[3]
    [2, 2, 1, 1, 1, 2, 2] output:[1,2]
    [1, 1, 3, 2, 3] output: [1, 3]
    '''
    if not nums:
        return []
    
    result = []
    count1 = 0
    count2 = 0
    canadidate1 = None
    canadidate2 = None
    for num in nums:
        if canadidate1 == num:
            count1 += 1
        elif canadidate2 == num:
            count2 += 1
        elif count1 == 0:
            canadidate1 = num
            count1 += 1
        elif count2 == 0:
            canadidate2 = num
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    
    if nums.count(canadidate1) > len(nums)//3:
        result.append(canadidate1)
    if canadidate2 != canadidate1 and nums.count(canadidate2) > len(nums)//3:
        result.append(canadidate2)
    return result


def intersect(nums1, nums2):
    res = []
    count_nums1 = {}
    for num1 in nums1:
        count_nums1[num1] = count_nums1.get(num1, 0) + 1


    for num2 in nums2:
        if count_nums1.get(num2, 0) > 0:
            res.append(num2)
            count_nums1[num2] -= 1
    return res


def longest_common_profix(strs):
    '''
    Given a list of strings, return the longest common prefix.
    '''
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        j = 0
        while j < len(prefix) and j < len(s) and prefix[j] == s[j]:
            j += 1
        prefix = prefix[:j]
        if not prefix:
            return ""
    return prefix


def is_valid(s):
    '''
    Given a string containing just the characters'(',')','{','}, '[', and ']', determine if the input string is valid.
    >>> is_valid("(){}[]")
    True
    '''
    result = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            print(result)
            topping = result.pop() if result else '#'
            if mapping[char] != topping:
                return False
        else:
            result.append(char)

    return not result

        
def remove_element(nums,val):
    '''
    Remove all instances of val in nums in-place and return the new length
    '''
    k  = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
        
def move_zeroes(nums):
    '''
    Move all 0's to the end of nums in-place, maintaining the order of non-zero elements.
    '''
    k = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1
    for i in range(k, len(nums)):
        nums[i] = 0
    return nums

def sorted_squares(nums):
    ''''
    Given a sorted array, return an array of the squares of each number, sorted in non-decreasing order.
    '''

    left = 0
    right = len(nums) - 1
    result = [0]*len(nums)
    for i in range(len(nums)-1, -1, -1):
        if nums[left]**2 > nums[right]**2:
            result[i] = nums[left]**2
            left += 1
        else:
            result[i] = nums[right]**2
            right -= 1
    return result

def merge(nums1, m, nums2, n):
    '''
    Merge nums2 into nums1 as one sorted array.
    '''
    p1 = m -1
    p2 = n - 1
    p = m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2 [p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -=1
        p -= 1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
    return nums1

def remove_duplicates(nums):
    '''
    Remove duplicates in-deplace from a sorted array and return the new length.
    '''
    if not nums:
        return 0
    i = 0
    j = 1
    while j < len(nums):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
        j += 1

    return i + 1

def find_anagrams(s, p):
    '''
    Find all start indices of p's anagrams in s.
    输入: s = "abab", p = "ab"
    输出: [0, 1, 2]
    '''
    result = []
    ls = len(s)
    lp = len(p)
    i = 0
    while i < ls - lp + 1:
        if sorted(s[i:i+lp]) == sorted(p):
            result.append(i)
        i += 1
    return result

def find_anagrams_silding_window(s, p):
    '''
    Find all start indices of p's anagrams in s.
    输入: s = "abab", p = "ab"
    输出: [0, 1, 2]
    '''
    result = []
    ls = len(s)
    lp = len(p)
    p_counter = Counter(p)
    window = Counter()

    for i in range(ls):
        window[s[i]] += 1
        if i >= lp:
            if window[s[i-lp]] == 1:
                del window[s[i-lp]] 
            else:
                 window[s[i-lp]] -= 1
        if  window == p_counter:
            result.append(i-lp+1)
    return result

def length_of_longest_substring(s):
    '''
    Find the length of the longest substring without repeating characters.
    >>> length_of_longest_substring("abcabcbb")
    >>> 3
    最长子串是 "abc"，长度是 3

    >>> length_of_longest_substring("bbbbb")
    >>> 1
    解释: 最长子串是 "b"，长度是 1

    >>>> length_of_longest_substring("pwwkew")
    >>> 3
    解释: 最长子串是 "wke"，长度是 
    right = 0 left =0 seen ={p}
    right = 1 left = 0 seen = {w, p}
    right = 2 left = 0 seen = {w} left =1 => seen ={} left = 2
    right = 3 left = 2 seen = {w, k}
    right = 4 left = 2 seen = {w, e, k}
    right = 5 left = 2 seen = {w,e,k} => seen ={e, k} left = 3
    right = 5 , left =3 seen = {k, e,w}
    '''
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        print(seen)
        max_len = max(max_len, right - left +1)            
    return max_len

if __name__ == "__main__":
    print("--------------------------------------------")
    #print(two_sum([2,7,11,15], 9))      # 输出 [0,1]
    #print(two_sum([3, 2, 4], 6))        # 输出 [1,2]
    #print(two_sum([3, 3], 6))           # 输出 [0,1]    
    #print(two_sum([1, 2, 3], 7))        # 输出 []

    print(two_sum_hash([2,7,11,15], 9))      # 输出 [0,1]
    print(two_sum_hash([3, 2, 4], 6))        # 输出 [1,2]
    print(two_sum_hash([3, 3], 6))           # 输出 [0,1]    
    print(two_sum_hash([1, 2, 3], 7))        # 输出 []

    print("--------------------------------------------")

   #print(reverse_str("hello"))    # 输出 olleh
    #print(reverse_str("Python"))   # 输出 nohtyP
    #print(reverse_str("a"))        # 输出 a
    #print(reverse_str(""))         # 输出 ""
    #print(reverse_str("reverse"))         # 输出 "esrever"

    print(reverse_str_two_points("hello"))    # 输出 olleh
    print(reverse_str_two_points("Python"))   # 输出 nohtyP
    print(reverse_str_two_points("a"))        # 输出 a
    print(reverse_str_two_points(""))         # 输出 ""
    print(reverse_str_two_points("reverse"))         # 输出 "esrever"
    print("--------------------------------------------")

    #print(valid_palindrome("A man, a plan, a canal: Panama"))  # True
    #print(valid_palindrome("race a car"))                      # False
    #print(valid_palindrome(" "))                               # True
    #print(valid_palindrome("0P"))                              # False
    print("--------------------------------------------")
    print(valid_palindrome_2points("A man, a plan, a canal: Panama"))  # True
    print(valid_palindrome_2points("race a car"))                      # False
    print(valid_palindrome_2points(" "))                               # True
    print(valid_palindrome_2points("0P"))                              # False

    #print(is_anagram_dict("banana", "abanan"))    # 输出 True
    #print(is_anagram_dict("CAR", "JAR"))   # 输出 False
    #print(is_anagram_dict("a","0"))        # 输出 False
    #print(is_anagram_dict("anagram", "nagaram"))         # 输出 True
    #print(is_anagram_dict("CAR", "nagaram"))         # 输出 False

    print("--------------------------------------------")
    print(is_anagram_inplace("banana", "abanan"))    # 输出 True
    print(is_anagram_inplace("CAR", "JAR"))   # 输出 False
    print(is_anagram_inplace("a","0"))        # 输出 False
    print(is_anagram_inplace("anagram", "nagaram"))         # 输出 True
    print(is_anagram_inplace("CAR", "nagaram"))         # 输出 False

    print("--------------------------------------------")
    print(majority_element([1, 1, 2, 2, 1]))         # 输出  1
    print(majority_element([3,2,3]))         # 输出 3
    print(majority_element([1, 1, 1, 2, 3]))         # 输出  1
    print(majority_element([1, 1, 3, 2, 3,2]))         # 输出 Nnoe

    #print(intersect([1, 2, 2, 1],[2, 2] ))         # 输出  [2, 2]
    #print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))         # 输出 [4, 9]

    #print(majority_element_boyer_moore([1, 1, 2, 2, 1]))         # 输出  1
    #print(majority_element_boyer_moore([3,2,3]))         # 输出 3
    #print(majority_element_boyer_moore([1, 1, 1, 2, 3]))         # 输出  1
    #print(majority_element_boyer_moore([1, 1, 3, 2, 3]))         # 输出 3
    #print(majority_element_boyer_moore([1, 2, 3, 4, 5]))         # 输出 3

    #print(majority_element2_boyer_moore([1, 1, 2, 2, 1]))         # 输出  1
    #print(majority_element2_boyer_moore([3,2,3]))         # 输出 3
    #print(majority_element2_boyer_moore([1, 1, 1, 2, 3]))         # 输出  1
    #print(majority_element2_boyer_moore([1, 1, 3, 2, 3]))         # 输出 3
    #print(majority_element2_boyer_moore([2, 2, 1, 1, 1, 2, 2]))         # 输出 3
    #print(majority_element2_boyer_moore(("")))         # 输出 3


    #print(longest_common_profix(["flower", "flow", "flight"]))         # 输出  1
    #print(longest_common_profix(["dog", "racecar", "car"]))         # 输出 3
    #print(longest_common_profix([""]))         # 输出  1
    #print(longest_common_profix(["a"]))         # 输出 3
    #print(longest_common_profix(["interspecies", "intersteller", "interstate"]))         # 输出 3


    print(is_valid("()"))         # 输出  1
    print(is_valid("(){}[]"))         # 输出 3
    print(is_valid("(]"))         # 输出  1
    print(is_valid("([)]"))         # 输出 3
    print(is_valid("{[]}"))         # 输出 3


    print(remove_element([0,1,2,2,3,0,4,2], 2))

    print(move_zeroes([0,1,0,3,12]))

    print(sorted_squares([-4, -1, 0, 1, 3, 10]))
    print(sorted_squares([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
    print(sorted_squares([-7, -3, 2, 3, 11]))  # [4, 9, 9, 49, 121]
    print(sorted_squares([-5, -3, -2, -1]))    # [1, 4, 9, 25]
    print(sorted_squares([0]))                 # [0]

    print(merge([1,2,3,0,0,0],3,[2, 5, 6], 3))

    print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))


    print(find_anagrams("abab","ab"))
    print(find_anagrams("cbaebabacd","abc"))
    print("--------------------------------------------")

    print(find_anagrams_silding_window("cbaebabacd","abc"))
    print(find_anagrams_silding_window("cbaebabacd","aeb"))
    print("--------------------------------------------")
    print(length_of_longest_substring("pwwkew"))
    print(length_of_longest_substring("bbbb"))