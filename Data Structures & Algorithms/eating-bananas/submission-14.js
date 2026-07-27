class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let start = 0;
        let end = Math.max(...piles);
        let ans = end;

        while (start <= end) {
            let hours = 0;
            let k = Math.floor((start + end) / 2);
            for (let i = 0; i < piles.length; i++) {
                hours += Math.ceil(piles[i] / k);
            }
            if (hours <= h) {
                ans = k;
                end = k - 1;
            } else {
                start = k + 1;
            }
        }
        return ans;
    }
}
