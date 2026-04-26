class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length) return false  // Quick check first
        const _s ={}
        const _t = {}

        for(let w of s){
           _s[w] = (_s[w] || 0) + 1 
        }
        for(let w of t){
            _t[w] = (_t[w] || 0) + 1
        }
        for(let key in _s){
            if(_s[key] !== _t[key]) return false
        }
        return true
    }
}
