func removeElement(nums []int, val int) int {
    // [0,1,2,2,3,0,4,2]
    // [0,1,3,0,4]
    // val = 2
    j := 0 // 1 + 1 + 1 + 1 + 1
    for i := 0; i < len(nums); i++{
        if nums[i] != val{
            nums[j] = nums[i]
            j++
        }
    }

    return j
}