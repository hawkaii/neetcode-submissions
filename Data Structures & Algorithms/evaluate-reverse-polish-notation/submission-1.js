class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
          const stack = [];

  for (let c of tokens) {
    let a, b;
    console.log(c);
    switch (c) {
      case "+":
        a = parseInt(stack.pop());
        b = parseInt(stack.pop());
        stack.push(a + b);
        break;
      case "-":
        a = parseInt(stack.pop());
        b = parseInt(stack.pop());
        stack.push(b - a);
        break;
      case "*":
        a = parseInt(stack.pop());
        b = parseInt(stack.pop());
        stack.push(a * b);
        break;
      case "/":
        a = parseInt(stack.pop());
        b = parseInt(stack.pop());
        stack.push(Math.trunc(b / a));
        break;
      default:
        stack.push(c);
        break;
    }
  }

  return stack[0];

    }
}
