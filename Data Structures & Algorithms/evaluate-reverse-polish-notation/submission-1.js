class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        let operands = ["+", "-", "*", "/"]
        let stack = []
       
    for (const tok of tokens) {
      if (!operands.includes(tok)) {
        stack.push(Number(tok)); 
      } else {
          const right = stack.pop()
          const left = stack.pop()
          switch(tok){
              case '+':
                stack.push(left + right)
                break;
              case "-":
                stack.push(left - right)
                break;
              case "*":
                stack.push(left * right)
                break;
              case "/":
                stack.push(Math.trunc(left / right))
                break;
          }
      }

    }
    return stack[0]
    }
}
