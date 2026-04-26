class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        let arr = temperatures
        let res = Array(arr.length).fill(0);
        let stack = []
        for (let i = 0; i < arr.length; i++) {
            const t = arr[i]
            while(stack.length > 0 && t > stack[stack.length-1][0]){
                const [stackT, stackInd] = stack.pop()
                res[stackInd] = i - stackInd
            }
            stack.push([t, i])
        }
        return res
    }
}
