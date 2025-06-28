func twoSum(numbers []int, target int) []int {
   num_map := make(map[int]int)

    for i, val :=  range numbers{
        comp := target - val
        if j, found := num_map[comp]; found {
            return []int{j, i+1}
        }
        num_map[val] = i+1
    }
    return nil
}