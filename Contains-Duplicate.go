func containsDuplicate(nums []int) bool {
    seen := make(map[int]bool)

    for _, val := range nums{
        if seen[val]{
            return true
        }
        seen[val] = true
    }

    return false

    // freq := make(map[int]int)

    // for _, val := range nums{
    //     freq[val]++
    // }

    // for _, val := range freq{
    //     if val > 1{
    //         return true
    //     }
    // }
    // return false
}