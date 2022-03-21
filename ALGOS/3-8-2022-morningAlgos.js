/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

// Step 1: Make a function that takes in 2 parameters
// Create an empty string for the output
// Array length = 1 or 0? Return arr[0] or empty string
// Loop through the array
  // Push stuff into my output from the array
  // Push separator into my output from the array
// Return output

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */

// function join(arr1, separator) {
//   for(var i=0; i<arr1.length; i++){
//     return arr1[i] + separator1 + arr1[i + 1]
//   }
// }
// console.log(join)

/**
 * - Time: O(n) linear.
 * - Space: O(n) linear.
 */
 function join(arr, separator = ", ") {
  let joined = "";

  if (!arr.length) {
    return joined;
  }

  // less than arr.length - 1 to stop before last
  for (let i = 0; i < arr.length - 1; i++) {
    joined += arr[i] + separator;
  }
  return joined + arr[arr.length - 1];
}

//-------------------------------------------------------------------------------------------------------------------------


/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

const str1 = " there's no free lunch - gotta pay yer way. ";
const expected6 = "TNFL-GPYW";

const str2 = "Live from New York, it's Saturday Night! ";
const expected7 = "LFNYISN";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @returns {string} The given str converted into an acronym.
 */

// How to do it with .split
// Create a function that takes in a string
// Create an empty output
// Split on " "
// Loop through the resulting array
  // Pass the string[0].upper() into output

// Different method
// Create a function that takes in a string
// Create empty output
// Loop through input string
  // if index == 0 && string[index] != " ", push string[index] into output
  // if current letter is a space, pass string[i + 1].upper() to output
// Return my output

/**
 * - Time: O(n) linear because the nested loops increment i, so every iteration
 *    of nested loops reduces iterations of outer loop.
 * - Space: O(n) linear.
 */
 function acronymize(wordsStr) {
  let acronym = "";
  const len = wordsStr.length;

  for (let i = 0; i < len; i++) {
    while (wordsStr[i] === " " && i < len) {
      i++; // skip spaces, handles multiple spaces
    }
    // upperCase it now while we are already looping
    // to avoid upperCase having to loop over our output to upperCase
    acronym += wordsStr[i].toUpperCase();

    while (wordsStr[i] !== " " && i < len) {
      i++; // skip rest of word
    }
  }
  return acronym;
}