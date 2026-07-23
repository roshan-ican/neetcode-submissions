class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        const n = temperatures.length
        const res = new Array(n).fill(0)
        const stack = []
        for(let i = 0 ;i < n; i++){
            let curr = temperatures[i]
            while (
                stack.length > 0 &&
                curr > temperatures[stack[stack.length - 1]]
            ) {
                const prevIndex = stack.pop();
                res[prevIndex] = i - prevIndex;
            }

            stack.push(i);
        }

      
       return res

    }
}
