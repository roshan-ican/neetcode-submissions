class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const groupedAnagrams = {}
    
        if(strs.length === 1 ){
            return [strs]
        }

        for(let i = 0 ; i < strs.length; i++){
            let word = strs[i]
            let sort = word.split("").sort().join()
            // console.log(sort, "sort")
            if(groupedAnagrams[sort]){
                 groupedAnagrams[sort].push(word)
            } else{
                 groupedAnagrams[sort] = [word]
            }
        }
        return Object.values(groupedAnagrams)
    }
}
