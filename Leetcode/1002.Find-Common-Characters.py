class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_chars = []
        first_word_chars = set(words[0])
        for char in first_word_chars:
            min_count = min(word.count(char) for word in words)
            common_chars.extend([char] * min_count) 
        return common_chars
