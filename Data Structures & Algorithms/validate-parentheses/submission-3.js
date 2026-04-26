class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {


    const stack = [];
    const parens = { ')': '(', ']': '[', '}': '{' };

    for (let char of s) {
        if (['(', '[', '{'].includes(char)) {
        stack.push(char);
        } else {
        if (stack.pop() !== parens[char]) return false;
        }
    }

    return stack.length === 0;
}
}
