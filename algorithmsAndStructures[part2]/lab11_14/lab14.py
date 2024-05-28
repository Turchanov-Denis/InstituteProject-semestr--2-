def get_substring_rk(text: str, pattern: str) -> list[int]:
    result = []

    alphabet_size = 256
    mod = 9973

    pattern_hash = ord(pattern[0]) % mod
    text_hash = ord(text[0]) % mod

    first_index_hash = 1

    for i in range(1, len(pattern)):
        pattern_hash *= alphabet_size
        pattern_hash += ord(pattern[i])
        pattern_hash %= mod

        text_hash *= alphabet_size
        text_hash += ord(text[i])
        text_hash %= mod

        first_index_hash *= alphabet_size
        first_index_hash %= mod

    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash and compare_text(text, i, pattern):
            result.append(i)

        if i == len(text) - len(pattern):
            break

        text_hash -= (ord(text[i]) * first_index_hash) % mod
        text_hash += mod
        text_hash *= alphabet_size
        text_hash += ord(text[i + len(pattern)])
        text_hash %= mod

    return result

def compare_text(text: str, index: int, pattern: str) -> bool:
    for i in range(len(pattern)):
        if pattern[i] != text[index + i]:
            return False
    return True

if __name__=="__main__":
    print(get_substring_rk('ibababacsbadcba', 'ba'))