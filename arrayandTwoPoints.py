def remove_element(nums, val):
    '''
    Give a number of array, if element in array is equal to val, then remove val.
    >>> remove_element([2,3,4,2,5], 2)
    output:3, new array should be [3, 4, 5]
    '''

    
    k = 0 # k is index of result array only count when element is not equal to val
    for i in range(len(nums)): # go through all elements in nums
        if nums[i] != val: # check each element if element is not equal to val
            nums[k] = nums[i] #place index of k for return array
            k += 1 # increase k (for next index in the return array)
    return k

def move_zeroes(nums):
    '''
    Given an number of array, move all zeros at the end of array. Keep the order of array.
    >>> move_zeros([0,1,0,3,12])
    [1, 3, 12, 0, 0]
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
    >>> sorted_squares([-4, -1, 0, 3, 10])
    [0, 1, 9, 16, 100]
    '''
    left = 0
    right = len(nums) -1
    result = [0] *len(nums)
    for i in range(right, -1, -1):
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
    >>> merge([1,2,3,0,0,0], 3, [2, 5, 6], 3)
    [1,2,2,3,5,6]
    >>> merge([4,5,6,0,0,0], 3, [1,2,3], 3)
    [1,2,3,4,5,6]
    '''
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -=1
        p -= 1
        print(nums1)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
        print(nums1)
    return nums1


if __name__ == "__main__":
    #print(remove_element([0,1,2,2,3,0,4,2], 2))

    #print(move_zeroes([0,1,0,3,12]))

    #print(sorted_squares([-4, -1, 0, 1, 3, 10]))
    #print(sorted_squares([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
    #print(sorted_squares([-7, -3, 2, 3, 11]))  # [4, 9, 9, 49, 121]
    #print(sorted_squares([-5, -3, -2, -1]))    # [1, 4, 9, 25]
    #print(sorted_squares([0]))                 # [0]

    
    #print(merge([1,2,3,0,0,0],3,[2, 5, 6], 3))
    print(merge([4,5,6,0,0,0],3,[1, 2, 3], 3))
