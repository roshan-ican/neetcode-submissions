class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s, t) {
        
        if(!s || !t) return ""

        let neededChars = {}
        for(let char of t){
            neededChars[char] = (neededChars[char] || 0) + 1
        }

        let l = 0
        let minLen = Infinity
        let minStart = 0
        let requiredCount = Object.keys(neededChars).length
        let formed = 0 
        let windowsCount = {}

        for (let r = 0; r < s.length; r++) {
            let char = s[r]
            windowsCount[char] = (windowsCount[char] || 0) + 1

            if(neededChars[char] && windowsCount[char] === neededChars[char]){
                formed++
            }
            while(formed === requiredCount){
                if(r - l + 1  < minLen){
                    minLen = r - l + 1
                    minStart = l
                }
                let leftChar = s[l]
                windowsCount[leftChar]--

                if(neededChars[leftChar] && windowsCount[leftChar] < neededChars[leftChar]){
                    formed--
                }
                l++
            }
        }
        return minLen === Infinity ? "" : s.substring(minStart, minStart + minLen)
    }
}
