const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

  function join(arr, separator) {
    for(var i=0; i<arr.length; i++){
        return arr[i] + separator + arr[i + 1] + separator + arr[i + 2];
    }
  }
  console.log(join(arr1,separator1))

const str1 = "a x a";
// const expected1 = true;
const str2 = "racecar";
// const expected2 = true;
function isstringpal(str){
length = str.length
for (i=0; i<str.length/2; i++) {
    if(str[i] !== str[length-1-i]){
      return "false";
    }
    return "true"
  }
}  
console.log(isstringpal(str2))

const str5 = "what up, daddy-o?";
// const expected5 = "dad";
var longestPalindrome = function (s) {
  // Update the string to put hash "#" at the beginning, end and in between each character
  let updatedString = getUpdatedString(s);
  // Length of the array that will store the window of palindromic substring
  const length = 2 * s.length + 1;
  // Array to store the length of each palindrome centered at each element
  let p = new Array(length);
  p.fill(0);
  // Current center of the longest palindromic string
  let c = 0;
  // Right boundary of the longest palindromic string
  let r = 0;
  // Maximum length of the substring
  let maxLength = 0;
  // Position index
  let position = -1;
  for (let i = 0; i < length; i++) {
      // Mirror of the current index
      let mirror = 2 * c - i;
      // Check if the mirror is outside the left boundary of current longest palindrome
      if (i < r) {
          p[i] = Math.min(r - i, p[mirror]);
      }
      // Indices of the characters to be compared
      let a = i + (1 + p[i]);
      let b = i - (1 + p[i]);
      // Expand the window
      while (a < length && b >= 0 && updatedString[a] === updatedString[b]) {
          p[i]++;
          a++;
          b--;
      }
      // If the expanded palindrome is expanding beyond the right boundary of
      // the current longest palindrome, then update c and r
      if (i + p[i] > r) {
          c = i;
          r = i + p[i];
      }
      if (maxLength < p[i]) {
          maxLength = p[i];
          position = i;
      }
  }
  let offset = p[position];
  let result = "";
  for (let i = position - offset + 1; i <= position + offset - 1; i++) {
      if (updatedString[i] !== '#') {
          result += updatedString[i];
      }
  }
  return result;
};

function getUpdatedString(s) {
  let sb = "";
  for (let i = 0; i < s.length; i++) {
      sb += "#" + s[i];
  }
  sb += "#";
  return sb;
}
console.log(longestPalindrome(str5))