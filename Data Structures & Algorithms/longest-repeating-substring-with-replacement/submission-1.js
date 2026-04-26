class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        let count = new Map();
        let maxFreq = 0;
        let left = 0;
        let res = 0;

        for (let right = 0; right < s.length; right++) {
            // Increment the count of the current character
            count.set(s[right], (count.get(s[right]) || 0) + 1);
            // Update maxFreq to the highest frequency in the current window
            maxFreq = Math.max(maxFreq, count.get(s[right]));

            // If the number of characters to replace exceeds k, shrink window
            while ((right - left + 1) - maxFreq > k) {
                // Decrement the count of the leftmost character
                count.set(s[left], count.get(s[left]) - 1);
                left++;
            }

            // Update result with the size of the current valid window
            res = Math.max(res, right - left + 1);
        }

        return res;
    }
}
