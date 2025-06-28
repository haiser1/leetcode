class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if not strs:
        #     return ""

        # prefix = []
        # for chars in zip(*strs):
        #     if len(set(chars)) == 1:  # Semua karakter dalam kolom harus sama
        #         prefix.append(chars[0])
        #     else:
        #         break  # Berhenti jika ada perbedaan

        # return "".join(prefix)

        if not strs:
            return ""

        strs.sort()  # Sortir daftar string
        first, last = strs[0], strs[-1]  # Bandingkan string pertama dan terakhir
        i = 0

        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        return first[:i]
        