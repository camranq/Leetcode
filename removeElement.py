def removeElement(nums, val):
    readPtr = 0
    writePtr = 0

    while readPtr < len(nums):
        if nums[readPtr] != val:
            nums[writePtr] = nums[readPtr] #Retain element
            writePtr += 1
        readPtr += 1

    print(nums)
    return nums

removeElement([1, 2, 2, 3, 2], 2)