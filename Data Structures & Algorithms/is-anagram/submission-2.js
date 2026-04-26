class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length){
            return false
        }
        const count1 = {}
        const count2 = {}

        for(let i of s){
            count1[i] = (count1[i] || 0) + 1
        }
           for(let j of t){
            count2[j] = (count2[j] || 0) + 1
        }
        for(let key in count1){
            if(count1[key] !== count2[key]){
                return false
            }
        }
        return true
    }
}
