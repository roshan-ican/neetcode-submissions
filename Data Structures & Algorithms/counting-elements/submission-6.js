class Solution {
    /**
     * @param {number[]} arr
     * @return {number}
     */
    countElements(arr) {
        // we need to have a map and see
        let count = {}
        let result = 0
        for(let i = 0; i < arr.length; i++){
            if(arr[i] in count){
                count[arr[i]] += 1
            }else{
                count[arr[i]] = 1
            }
        }
        for(const [key, value] of Object.entries(count)){
            if(Number(key) + 1 in count){
                result += value
            }
        }
        return result
    }
}
