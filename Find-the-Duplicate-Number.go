func findDuplicate(nums []int) int {
    m := make(map[int]bool)

    for _, val := range nums{
        if _, exits := m[val]; exits{
            return val
        }
        m[val] = true
        
    }
    return 0
}