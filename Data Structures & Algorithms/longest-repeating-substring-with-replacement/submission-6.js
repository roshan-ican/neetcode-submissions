class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        let counter = {};
        let res = 0;
        let l = 0;
        for (let r = 0; r < s.length; r++) {
            if (s[r] in counter) {
                counter[s[r]] += 1;
            } else {
                counter[s[r]] = 1;
            }
            while (r - l + 1 - Math.max(...Object.values(counter)) > k) {
                counter[s[l]] -= 1;
                l += 1;
            }
            res = Math.max(res, r - l + 1);
        }
        return res;
    }
}
