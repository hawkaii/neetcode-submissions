class MinStack {
      constructor() {
     this.stack = [];
  }

  /**
   * @param {number} val
   * @return {void}
   */
  push(val) {
    this.stack.push(val);
  }

  /**
   * @return {void}
   */
  pop() {
    if (this.stack.length > 0) {
      this.stack.pop();
    }
  }

  /**
   * @return {number}
   */
  top() {
    if (this.stack.length > 0) {
      return this.stack[this.stack.length - 1];
    }
  }

  /**
   * @return {number}
   */
  getMin() {
     const tmp = [];
        let mini = this.stack[this.stack.length - 1];

        while (this.stack.length > 0) {
            mini = Math.min(mini, this.stack[this.stack.length - 1]);
            tmp.push(this.stack.pop());
        }

        while (tmp.length > 0) {
            this.stack.push(tmp.pop());
        }

        return mini
  }

}
