class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 10
        heap = [1]
        seen = set(heap)  # Untuk menghindari duplikasi
        factors = [2, 3, 5]
        
        for _ in range(n):  # Lakukan iterasi n kali
            # Ambil bilangan terkecil dari heap
            ugly = heapq.heappop(heap)
            
            # Tambahkan faktor baru ke heap
            for factor in factors:
                new_ugly = ugly * factor
                if new_ugly not in seen:
                    heapq.heappush(heap, new_ugly)
                    seen.add(new_ugly)
        
        return ugly
        