class Solution {
    /**
     * @param {number[]} arr
     * @return {number[]}
     */
    replaceElements(arr) {
        let result = new Array(arr.length).fill(-1)
        for(let i = 0; i < arr.length -1; i++){
            let cMax = arr[i + 1]

            for(let j = i + 1; j < arr.length; j++){
                if(arr[j] > cMax){
                    cMax = arr[j]
                }
            }
            result[i] = cMax
        }
        return result
    }
}
