class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    isNumeric(val) {
        return !isNaN(val) && !isNaN(parseFloat(val));
    }

    evalRPN(tokens) {
        let stack = []

        for(let i = 0; i < tokens.length; i++){
            const num = tokens[i]
            if(this.isNumeric(num)){
                stack.push(num)
            }
            else{
                let one = Number(stack.pop())
                let two = Number(stack.pop())
                if(num==='+'){
                    stack.push(one + two)
                }
                else if(num==='-'){
                    stack.push(two - one)
                }
                else if(num === '*'){
                    stack.push(one * two)
                }else{

                    stack.push(Math.trunc(two/one))
                }
            }
        }
        return stack[0]
    }
}
