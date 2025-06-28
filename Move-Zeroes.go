func moveZeroes(nums []int)  {
    // [0,1,0,3,12]
    // [1,0,3,12]
    // [1,3,12]
    n := len(nums) // 5
    lastNonZeroIndex := 0 // 1 + 1 + 1 = 3

    // Pindahkan semua elemen non-zero ke depan
    for i := 0; i < n; i++ {
        if nums[i] != 0 {
            nums[lastNonZeroIndex] = nums[i]
            lastNonZeroIndex++
        }
    }

    // Isi sisa array dengan nol
    // [1,3,12,0,0]
    for i := lastNonZeroIndex; i < n; i++ {
        nums[i] = 0
    }
}