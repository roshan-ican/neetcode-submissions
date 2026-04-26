class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        
        let n = s.length
     
        let seen = new Set()
        let l = 0
        let ans = 0
        for(let r =0; r < n; r++){
            while(seen.has(s[r])){
                seen.delete(s[l])
                l++
            }
        seen.add(s[r])
        ans = Math.max(ans, r - l + 1)
           
        }
        return ans

    }
}
