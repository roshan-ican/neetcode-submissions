class Solution {
    /**
     * @param {string} s    
     * @return {number}
     */
    lengthOfLastWord(s) {
        let string = s.trim().split(" ")
        let lastWord = string.at(-1)
        return lastWord.length
    }
}
