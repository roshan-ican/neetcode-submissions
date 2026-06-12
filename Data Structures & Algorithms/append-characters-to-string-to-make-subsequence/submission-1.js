class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {number}
     */
    appendCharacters(s, t) {
        let j = 0;
        for (let i = 0; i < s.length; i++) {
            if (t[j] === s[i]) {
                j++;
                if(j === t.length) {
                    break;
                }
            }
        }
        return Math.abs(j - t.length)
    }
}
