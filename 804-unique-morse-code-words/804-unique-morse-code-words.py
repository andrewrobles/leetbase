class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        english_morse = {}
        for e, m in zip(english, morse):
            english_morse[e] = m
        transformations = set()
        for word in words:
            curr = ''
            for letter in word:
                curr += english_morse[letter]
            transformations.add(curr)
        return len(transformations)
                
            
            
        