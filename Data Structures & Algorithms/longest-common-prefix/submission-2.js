class Solution {
    /**
     * @param {string[]} strs
     * @return {string}
     */
    longestCommonPrefix(strs) {
        let res = "";

        let firstWord = strs[0];

        for (let j = 0; j < firstWord.length; j++) {
            let char = firstWord[j];

            for (let i = 1; i < strs.length; i++) {
                if (j >= strs[i].length || strs[i][j] !== char) {
                    return res;
                }
            }

            res += char;
        }
        return res;
    }
}
