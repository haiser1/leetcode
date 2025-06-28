func singleNumber(nums []int) []int {
    m := make(map[int]int)

    for _, val := range nums{
        m[val]++
    }
    result := []int{}
    for key, val := range m{
        if val == 1{
            result = append(result, key)
        }
    }

    return result
    
}