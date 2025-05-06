from collections import defaultdict,Counter, deque
from collections import defaultdict
import MinHeap

def valid_Palindrome_2(s):
    '''
    valid_Palindrome_2("abca"):
    True
    '''
    def valid_palindrome(l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return valid_palindrome(left,right-1) or valid_palindrome(left+1, right)
    return True


def group_anagrams(strs):
    '''
    group_anagrams["eat","tea","tan","ate","nat","bat"]
    >>> [["eat","tea","ate"],["tan","nat"],["bat"]]
    '''
    anagrams_map = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        anagrams_map[key].append(word)
    return list(anagrams_map.values())

def expand_from_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1: right]

def longest_palindromic_substring(s):
    '''
    输入: s = "babad"
    输出: "bab"  （或者 "aba" 也可以）
    '''
    if not s:
        return ""
    
    longest = ""
    
    for i in range(len(s)):
        p1 = expand_from_center(s, i, i)
        p2 = expand_from_center(s, i, i +1)
        longer = p1 if len(p1) > len(p2) else p2
        if len(longer)>len(longest):
            longest = longer
    return longest


def sliding_window_maximum(s, k):
    '''
    输入: nums = [1,3,-1,-3,5,3,6,7], k = 3  
    输出: [3,3,5,5,6,7]
    i = 0
    dq = {0}
    i = 1
    dq = {1}
    i = 2
    dq = {1, 2}
    result = [3]
    i = 3
    dq = {1,2,3}
    result = [3,3]
    i = 4
    dq = {}
    dq = {4}
    result = [3,3,5]
    i = 5
    dq = {4,5}
    result = [3,3,5,5]
    i = 6
    dq = {}
    dq = {6}
    result = [3,3,5,5,6]
    i = 7
    dp = {}
    dq = {7}
    result = [3,3,5,5,6,7]

    输入: nums = [1,3,-1,-3,-4,3,6,7], k = 3  
    输出: [3,3,-1,5,6,7]
    when i = 0
    dq = {0}
    when i = 1
    dq = {1}
    wen in = 2
    dq = {1,2}
    result = [3]
    when i = 3
    dq = {1,2,3}
    result = [3,3]
    i = 4
    dq = {1,2,3,4}
    dq = {2,3,4}
    '''
    if not s or k == 0:
        return []
    result = []

    dq = deque()  # 存的是索引，不是值
    for i in range(len(s)):
        # 1. 弹出队尾所有比当前值小的索引（维护递减）
        while dq and s[dq[-1]] < s[i]:
            dq.pop()
        # 2. 加入当前索引
        dq.append(i)
        # 3. 移除滑出窗口外的左边元素
        if dq[0] < i - k + 1:
            dq.popleft()
        # 4. 如果窗口形成了，加入当前最大值（队首索引对应的值）
        if i >= k - 1:
            result.append(s[dq[0]])
    return result


def sliding_window_minimum(nums, k):
    '''
    输入: nums = [1,3,-1,-3,5,3,6,7], k = 3  
    输出: [-1, -3, -3, -3, 3, 3]
    '''
    dq = deque() 
    result = []

    if not nums or k == 0:
        return []
    
    for i in range(len(nums)):
        while dq and nums[dq[-1]] > nums[i]:
            dq.pop()

        dq.append(i)

        if dq[0] < i - k + 1:
            dq.popleft()
        # 4. 如果窗口形成了，加入当前最大值（队首索引对应的值）
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

def longest_subarray_sum_leq_k(nums, k):
    '''
    输入: nums = [1,2,1,0,1,1,0], k = 4
    输出: 5

    '''
    left = 0
    window_sum = 0
    max_len = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum > k and left <= right:
            window_sum -= nums[left]
            left += 1

        max_len = max(max_len, right -left+1)

    return max_len


#Longest Substring with At Most K Distinct Characters
def longest_substring_k_distinct(s, k):
    '''
    输入: s = "eceba", k = 2
    输出: 3

    '''
    window = {}
    left = 0
    max_len = 0
    for right in range(len(s)):
        window[s[right]] = window.get(s[right],0) + 1
        
        while len(window) > k:
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


 #Sliding Window Median 
def sliding_window_median(nums, k):
    ''''
    sliding_window_median([1, 3, -1, -3, 5, 3, 6, 7], 3)
    '''
    result = []

    lo = MinHeap.MinHeap(len(nums))  # Max-heap (as negative numbers)
    hi = MinHeap.MinHeap(len(nums)) # Min-heap
    delayed = defaultdict(int)
    median = 0

    for i in range(k):
        lo.insert(-nums[i])
        hi.insert(-lo.removeMin())
        
        if hi.size > lo.size:
            lo.insert(-hi.removeMin())

    if k % 2 == 1:
        median = float(-lo.storage[0])
        result.append(median)
    else:
        median = (-lo.storage[0] + hi.storage[0])/2
        result.append(median)

    for i in range(k, len(nums)):
        pre_num = nums[i - k]
        delayed[pre_num] += 1

        balance = -1 if pre_num <= median else 1

        if nums[i] <= median:
            balance += 1
            lo.insert(-nums[i])
        else:
            balance -= 1
            hi.insert(nums[i])

        if balance < 0:
            lo.insert(-hi.removeMin())
        elif balance > 0:
            hi.insert(-lo.removeMin())


        while lo and delayed[-lo.storage[0]] > 0:
            delayed[-lo.storage[0]] -= 1
            lo.removeMin()

        
        while hi and delayed[hi.storage[0]] > 0:
            delayed[hi.storage[0]] -= 1
            hi.removeMin()

        if k % 2 == 1:
            median = float(-lo.storage[0])
            result.append(median)
        else:
            median = (-lo.storage[0] + hi.storage[0])/2
            result.append(median)

    return result

def sliding_window_average(nums, k):
    '''
    输入: nums = [1,3,2,6,-1,4,1,8,2], k = 5
    输出: [2.2, 2.8, 2.4, 3.6, 2.8]
    '''
    if not nums or k == 0:
        return []
    window_sum = 0
    result = []
    for i in range(len(nums)):

        if i >= k:
            window_sum -= nums[i-k]

        window_sum += nums[i]

        if i >= k-1:
            result.append(window_sum/k)
    return result

def minimum_window_substring(s, t):
    '''
    输入: s = "ADOBECODEBANC", t = "ABC"  
    输出: "BANC"
    '''
    if not s or not t:
        return ""
    
    need = Counter(t)
    window = {}
    have = 0
    count_need = len(need)
    left = 0
    res = ""
    len_res = float('inf')

    for right in range(len(s)):
        c = s[right]
        window[c] = window.get(c, 0) + 1
        
        if c in need and window[c] == need[c]:
            have += 1
        
        while have == count_need:

            if right - left + 1 < len_res:
                res = s[left:right+1]
                len_res = right - left + 1

            if s[left] in need and window[s[left]] == need[s[left]]:
                have -= 1
            window[s[left]] -= 1

            left += 1

    return res

def top_K_Frequent_Elements(nums, k):
    result_dic = {}
    result = []
    for num in nums:
        if num is result_dic:
            result_dic[num] += 1
        else:
            result_dic[num] = result_dic.get(num, 0) + 1
    
    for ele,count in result_dic:
        result_dic[ele] 
    return result


if __name__ == "__main__":
    print("--------------------------------------------")
    #print(valid_Palindrome_2("abca"))
    #print(valid_Palindrome_2("abc"))

    #print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    #print(minimum_window_substring("ADOBECODEBANC", "ABC"))

    #print(sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3 ))

    #print(sliding_window_minimum([1,3,-1,-3,5,3,6,7], 3 ))
    #print(sliding_window_average([1,3,2,6,-1,4,1,8,2], 5))
    print("--------------------------------------------")
    print(longest_subarray_sum_leq_k([1,3,2,6,-1,4,1,8,2], 5))
    print("--------------------------------------------")
    print(longest_substring_k_distinct("eceba", 2))
    print(longest_substring_k_distinct("eceba", 2))     # ➜ 3 ("ece")
    print(longest_substring_k_distinct("aa", 1))        # ➜ 2 ("aa")
    print(longest_substring_k_distinct("abcadcacacaca", 3))  # ➜ 11
    print(longest_substring_k_distinct("", 2))          # ➜ 0
    print(longest_substring_k_distinct("a", 0))         # ➜ 0

    print(sliding_window_median([1, 3, -1, -3, 5, 3, 6, 7], 3))

    



