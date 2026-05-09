class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    
    isPalindrome(s) {
        function isAlphaNum(c) {
  return (
    (c >= "a" && c <= "z") || (c >= "A" && c <= "Z") || (c >= "0" && c <= "10")
  );
}
            let new_str = "";
  for (let i = 0; i < s.length; i++) {
    let c = s[i];
    if (isAlphaNum(c)) {
      new_str += c;
    }
  }
  new_str = new_str.toLowerCase();

  let l = new_str.length;

  for (let i = 0; i < l; i++) {
    if (i >= l / 2) {
      break;
    }
    if (new_str[i] !== new_str[l - 1 - i]) {
      return false;
    }
  }
  return true;


    }
}
