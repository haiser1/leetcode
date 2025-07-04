func singleNumber(nums []int) int {
    m := make(map[int]int)
    for _, val := range nums{
        m[val]++
    }

    for i, val := range m{
        if val == 1{
            return i
        }
    }

    return 0
}