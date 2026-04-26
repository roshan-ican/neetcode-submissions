class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let groupedAnagrams = {}
        if(strs.length === 1 ){
            return [strs]
        }
        // if the reverse and forward are same then split them into sub arrays
        for(let i  = 0; i < strs.length; i++){
            const word = strs[i]
            const sortedWord = word.split("").sort().join()
     
            // frequencies[sortedWord] = (frequencies[sortedWord] || 0) + 1;
        if (groupedAnagrams[sortedWord]) {
            groupedAnagrams[sortedWord].push(word);
        } else {
            // If it's not in the object, create a new array with the current word
            groupedAnagrams[sortedWord] = [word];
        }
        }
        const result =Object.values(groupedAnagrams);
        return result

    }
}
