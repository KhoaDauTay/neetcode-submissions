class Solution:
    # len#<>
    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            encode_i = str(len(i)) + "#" + i
            result += encode_i
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # tìm vị trí '#' tiếp theo
            j = i
            while s[j] != "#":
                j += 1

            # đọc length
            length = int(s[i:j])

            # đọc đúng length ký tự sau '#'
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # nhảy đến string tiếp theo
            i = j + 1 + length
        return result

            