func majorityElement(nums []int) int {
    freq := make(map[int]int)

    for _, num := range nums{
        freq[num]++
    }

    for key, val := range freq{
        if val > len(nums) / 2{
            return key
        }
    }

    return 0

    
}