class Solution:
  def lengthOfLongestSubstring(s: str) -> int:
      char_set = set()
      left = 0
      max_len = 0
      for right in range(len(s)):
          while s[right] in char_set:
              char_set.remove(s[left])
              left += 1
          curr_len = right - left + 1
          max_len = max(max_len, curr_len)
          char_set.add(s[right])
            
      return max_len
