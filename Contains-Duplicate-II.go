func containsNearbyDuplicate(nums []int, k int) bool {
    indexMap := make(map[int]int) // Map untuk melacak indeks terakhir dari setiap elemen

    for i, val := range nums {
        if prevIndex, exists := indexMap[val]; exists {
            if i-prevIndex <= k { // Periksa apakah jarak indeks <= k
                return true
            }
        }
        indexMap[val] = i // Perbarui indeks terakhir elemen
    }

    return false // Tidak ditemukan elemen yang memenuhi kondisi
}