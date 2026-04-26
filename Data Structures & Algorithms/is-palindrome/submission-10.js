class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let filtered = s.replace(/[^a-z0-9]/gi, '').toLowerCase();
        let start = 0
        let end = filtered.length - 1

        while(start < end){   
            if(filtered[start] !== filtered[end]){
                return false
            }
            start++
            end--
        }
        return true

    }
}
