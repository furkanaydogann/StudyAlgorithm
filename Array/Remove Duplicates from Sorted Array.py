#Remove Duplicates from Sorted Array

#Input: nums = [1,1,2]
#Output: 2, nums = [1,2,_]
#Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
#It does not matter what you leave beyond the returned k (hence they are underscores).


def removeDuplicates(nums):
    k = 0
    for num in nums:
        if nums[k] != num:
            k = k+1
            nums[k] = num


    return k + 1


#nums = [0,0,1,1,1,2,2,3,3,4,4,4,7,7,8]
nums = [1,1,2]
#nums = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))







