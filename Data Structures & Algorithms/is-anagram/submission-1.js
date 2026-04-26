class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        
    let sSort = s.split("").sort().join()
    let tSort = t.split("").sort().join()

    return true ? sSort === tSort : false
    }
}
