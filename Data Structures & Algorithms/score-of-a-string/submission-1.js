class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    scoreOfString(s) {
        // split the each character in like 2
        // and then we like get the difference and add to the final
        // Stop at s.length - 1 so s[i + 1] never looks out of bounds!
        let res = 0
        for (let i = 0; i < s.length - 1; i++) {
            let sum = Math.abs(s.charCodeAt(i) - s.charCodeAt(i+1))
            res+=sum
        }
        return res
    }
}
