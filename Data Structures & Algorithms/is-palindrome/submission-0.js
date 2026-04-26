class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
    let newStr = s.toLowerCase().replace(/[^0-9a-z]/g, "")
    let start = 0
    let end = newStr.length - 1
    
    while(start < end){
        if(newStr[start] !== newStr[end]){
            return false
        } else {
            start++
            end--
        }
            
    }
    return true
    }
}
