func singleNumber(nums []int) int {
    // sifat xor, setiap angka yang di-XOR dengan dirinya sendiri akan menjadi nol
    // setiap angka yang di-XOR dengan nol tetap tidak berubah
    result := 0
    for _, val := range nums{
        result ^= val
    }

    return result
}