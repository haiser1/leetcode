func missingNumber(nums []int) int {
    // [3,0,1]
    n := len(nums) // 3
    expectedSum := n * (n + 1) / 2 // 6
    actualSum := 0 // 4

    for _, val := range nums{
        actualSum += val
    }

    return expectedSum - actualSum // 6 - 4 = 2
}