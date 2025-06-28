func majorityElement(nums []int) []int {
    freq := make(map[int]int)

    for _, num := range nums{
        freq[num]++
    }

    result := []int{}

    for key, val := range freq{
        if val > len(nums) / 3{
            result = append(result, key)
        }
    }

    return result
}