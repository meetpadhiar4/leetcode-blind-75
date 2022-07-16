def characterReplacement(s: str, k: int) -> int:
    d = defaultdict(int)
    max_val, max_len = 0, 1
    left = 0
    for right in range(len(s)):
        d[s[right]] += 1
        max_val = max(max_val, d[s[right]])
        while (right - left + 1) - max_val > k:
            d[s[left]] -= 1
            max_val = max(max_val, d[s[left]])
            left += 1
        max_len = max(max_len, right - left + 1)
            
    return max_len