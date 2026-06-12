class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isSubsequence(s, t) {
        // get the count of the s
        // get the count of the t
        let sLike = []
        let i = 0
        for(let j = 0; j < t.length; j++){
            if(t[j] === s[i]){
                sLike.push(t[j])
                i++
            }else{
                continue
            }
        }
        let res = sLike.join('')
        return res === s ? true : false
    }
}
