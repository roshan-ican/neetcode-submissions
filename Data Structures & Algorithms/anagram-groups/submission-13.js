class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const groups = {}
        
        for(let word of strs){
            const key = word.split("").sort().join("")
            if(key in groups){
                groups[key].push(word)
            }else{
                groups[key] = [word]
            }
        }
        
        return Object.values(groups)  // Returns array of arrays
        }
}
