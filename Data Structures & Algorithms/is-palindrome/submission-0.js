class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
          let str = s.replace(/[^a-z0-9]/gi, "").toLowerCase();
  if (str === str.split("").reverse().join("")) {
    return true;
  }
  return false;


    }
}
