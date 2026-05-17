class Solution {
    /**
     * @param {number} n
     * @return {boolean}
     */
    confusingNumber(n) {

        const map = {
            '0' : '0',
            '1' : '1',
            '6' : '9',
            '8' : '8',
            '1' : '1',
            '9' : '6'
        }

        let rotated = ''
        for(const ch of String(n)){
            if(!(ch in map)){
                return false
            }
            rotated += map[ch]
        }
        rotated = rotated.split('').reverse().join('')
        return parseInt(rotated) !== n
    }
}
