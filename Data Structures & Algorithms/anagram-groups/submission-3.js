class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(arr) {
        let g = {}
        for(let i=0; i < arr.length; i++ ){
            let w = arr[i]
            let s = w.split("").sort().join()

            if(g[s]){
                g[s].push(w)
            }else{
                g[s] = [w]
            }
        }
        return Object.values(g)
    }
}
