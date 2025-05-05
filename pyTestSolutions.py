def two_sum(nums, target):
    '''
    Given an array of numbers and a target number,
    return the indices of the two numbers that add up to the target number.
    Example:
    nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    '''
    j = 1
    for i in range(len(nums)):
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
    return []

def reverse_str(string):
    '''
    Given a string,
    return the reversed string.
    Example:
    input "hello"  > oellh > olleh >
    output "olleh"
    '''
    word = list(string)
    length = len(string)
    temp = ""
    for i in range(length//2):
        temp = word[i]
        word[i] = word[length-1-i]
        word[length-1-i] = temp
    return "".join(word)

def valid_palindrome(string):
    '''
    Given a string, 
    if the string is palindrome, then return True
    Ignore captialization, space and marks

    input "A man, a plan, a canal: Panama"
    Output: True
    '''
    chars = []
    for s in string:
        if s.isalnum():
            chars.append(s.lower())
    
    for i in range(len(chars)//2):
        if chars[i] != chars[len(chars)-1-i]:
            return False
    return True
        


def is_anagram(s, t):
    '''
    Given two strings s and t,
    return True if t is an anagram of s, else return False
    '''
    return sorted(s) == sorted(t)

def is_anagram_dict(s, t):
    '''
    Given two strings s and t,
    return True if t is an anagram of s, else return False
    '''
    if len(s) != len(t):
        return False
    
    count_s, count_t = {}, {}
    for c in s:
        count_s[c] = count_s.get(c, 0) + 1
    for c in t:
        count_t[c] = count_t.get(c, 0) + 1

    return count_s == count_t

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
    for c in nums:
        count_nums[c] = count_nums.get(c, 0) + 1
        if count_nums[c] > len(nums)//2:
            return c
    return None

    


#boyer-moore
def majority_element_boyer_moore(nums):
    '''
    Given an array of numbers, return the element that appears more than n/2 times
    [3,2,3] output:3
    [2, ,2, 1, 1, 1, 2, 2] output:2
    [1, 1, 3, 2, 3]
    '''
    count = 0
    candidate = None
    for c in nums:
        if count == 0:
            candidate = c
        if candidate == c:
            count += 1
        else:
            count -= 1
    
    if nums.get(candidate) > len(nums)//2:
        return candidate
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
    count1, count2 = 0, 0
    candidate1, candidate2 = {}, {}
    for c in nums:
        if candidate1 == c:
            count1 += 1
        elif candidate2 == c:
            count2 += 1
        elif count1 == 0:
            candidate1 = c
            count1 += 1
        elif count2 == 0:
            candidate2 = c
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    
    if nums.count(candidate1) > len(nums)//3:
        result.append(candidate1)
    if candidate1 != candidate2 and nums.count(candidate2) > len(nums)//3:
        result.append(candidate2)
    return result

def intersect(nums1, nums2):
    '''
    Given two integer arrays nums1 and nums2,
    return an array of their intersection.

    Each element in the result should appear as many times as it shows in both arrays
    you may return the result in any order.

    Example:
    >>> intersect([1,2,2,1], [2,2])
    [2, 2]
    '''
    result = []
    count_nums1 = {}
    for num in nums1:
        count_nums1[num] = count_nums1.get(num, 0) + 1 
    for num in nums2:
        if count_nums1.get(num, 0) > 0:
            result.append(num)
            count_nums1[num] -= 1
    return result




def longest_common_profix(strs):
    '''
    Given a list of strings, return the longest common prefix.
    '''
    if not strs:
        return ""

    prefix = strs[0]

    for string in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(string) and string[i] == prefix[i]:
            i += 1
        prefix = prefix[:i]
        if not prefix:
            return ""
    return prefix

def is_valid(s):
    '''
    Given a string containing just the characters'(',')','{','}, '[', and ']', determine if the input string is valid.
    >>> is_valid("(){}[]")
    True
    '''
    pass


def remove_element(nums,val):
    '''
    Remove all instances of val in nums in-place and return the new length
    '''
    pass
        
def move_zeroes(nums):
    '''
    Move all 0's to the end of nums in-place, maintaining the order of non-zero elements.
    '''
    pass

def sorted_squares(nums):
    ''''
    Given a sorted array, return an array of the squares of each number, sorted in non-decreasing order.
    '''

    pass


if __name__ == "__main__":
    print("--------------------------------------------")
    print(two_sum([2,7,11,15], 9))      # 输出 [0,1]
    print(two_sum([3, 2, 4], 6))        # 输出 [1,2]
    print(two_sum([3, 3], 6))           # 输出 [0,1]    
    print(two_sum([1, 2, 3], 7))        # 输出 []
    print("--------------------------------------------")
    print(reverse_str("hello"))    # 输出 olleh
    print(reverse_str("Python"))   # 输出 nohtyP
    print(reverse_str("a"))        # 输出 a
    print(reverse_str(""))         # 输出 ""
    print(reverse_str("reverse"))         # 输出 "esrever"
    print("--------------------------------------------")
    print(valid_palindrome("A man, a plan, a canal: Panama"))  # True
    print(valid_palindrome("race a car"))                      # False
    print(valid_palindrome(" "))                               # True
    print(valid_palindrome("0P"))                              # False
    print("--------------------------------------------")
    print(is_anagram_dict("banana", "abanan"))    # 输出 True
    print(is_anagram_dict("CAR", "JAR"))   # 输出 False
    print(is_anagram_dict("a","0"))        # 输出 False
    print(is_anagram_dict("anagram", "nagaram"))         # 输出 True
    print(is_anagram_dict("CAR", "nagaram"))         # 输出 False
    print("--------------------------------------------")
    print(majority_element2_boyer_moore([1, 1, 2, 2, 1]))         # 输出  1
    print(majority_element2_boyer_moore([3,2,3]))         # 输出 3
    print(majority_element2_boyer_moore([1, 1, 1, 2, 3]))         # 输出  1
    print(majority_element2_boyer_moore([1, 1, 3, 2, 3]))         # 输出 3
    print(majority_element2_boyer_moore([2, 2, 1, 1, 1, 2, 2]))         # 输出 3
    print(majority_element2_boyer_moore(("")))         # 输出 3
    print("--------------------------------------------")
    print(intersect([1, 2, 2, 1],[2, 2] ))         # 输出  [2, 2]
    print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))         # 输出 [4, 9]
    print("--------------------------------------------")
    print(longest_common_profix(["flower", "flow", "flight"]))         # 输出  1
    print(longest_common_profix(["dog", "racecar", "car"]))         # 输出 3
    print(longest_common_profix([""]))         # 输出  1
    print(longest_common_profix(["a"]))         # 输出 3
    print(longest_common_profix(["interspecies", "intersteller", "interstate"]))         # 输出 3
    print("--------------------------------------------")
    print(is_valid("()"))         # 输出  True
    print(is_valid("(){}[]"))         # 输出 True
    print(is_valid("(]"))         # 输出  False
    print(is_valid("([)]"))         # 输出 False
    print(is_valid("{[]}"))         # 输出 True
