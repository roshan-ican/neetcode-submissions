class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {

        const count = {}
        for(let n of nums){
            count[n] = (count[n] || 0) + 1
        }
        const buckets = Array(nums.length + 1).fill(null).map(() => [])
        // console.log(buckets, "__buckets_")
        for(let num in count){
            const freq = count[num]
            buckets[freq].push(num)
        }
    //    console.log(buckets, "__buckets_")
       const res = []
       for(let i = buckets.length -1; i >= 0; i--){
            for(let num of buckets[i]){
                res.push(num)
                if(res.length === k) return res
            }
       }
    //    console.log(res,"__a")
    }
}
