/* 
  Given an array of strings
  return a sum to represent how many times each array item is found (a frequency table)
  Useful methods:
    Object.hasOwnProperty("keyName")
      - returns true or false if the object has the key or not
    Python: key in dict
*/

const arr1 = ["a", "a", "a"];
const expected1 = {
  a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

const arr4 = ["hello", "world", "hello", "World"];
// const expected8 = {
    hello: 2,
    world: 1,
    World: 1
}

/**
 * - Time: O(n) linear.
 * - Space: O(n) linear.
 */
 function frequencyTableBuilder(arr) {
  const freqTable = {};

  for (let i = 0; i < arr.length; i++) {
    const str = arr[i];

    if (freqTable.hasOwnProperty(str) === false) {
      // first occurrence found
      freqTable[str] = 1;
    } else {
      freqTable[str]++;
    }
  }
  return freqTable;
}

/**
 * Have the function run through the array and set each index as a new key
 * When it reaches a new index check if that key already exists, if so increase it's value by 1
 * Else insert as a new key
 */
x[arr[i]] = value
x+=({key:[i], value:1})


/* 
result = {}
counter = 0
loop through array
  add key to result


  
returning dictionary

{a,b,c,d}
result.a=0
*/









/*-----------------------------*/
/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */
function frequencyTableBuilder(arr) {

}

/**
 * Finds the only number that occurs odd times in the given odd-lengthed array.
 * - Time: O(2n) -> O(n) linear.
 * - Space: O(n) linear.
 * @param {number[]} nums Odd-lengthed.
 * @returns {number} The number that occurs odd times.
 */
 function oddOccurrencesInArray(nums) {
  const freqTable = {};

  for (const n of nums) {
    if (freqTable.hasOwnProperty(n)) {
      freqTable[n]++;
    } else {
      freqTable[n] = 1;
    }
  }

  for (const key in freqTable) {
    if (freqTable[key] % 2 !== 0) {
      return +key; // + converts the string key back to int.
    }
  }

  // The spec guaranteed there will be a solution so no other return is needed.
}



// -----------------------------------------------------------------------------------------------------------------------------




/* 
Given a non-empty array of odd length containing ints where every int but one
has a matching pair (another int that is the same)
return the only int that has no matching pair.
*/

const nums1 = [1];
const expected4 = 1;

const nums2 = [5, 4, 5];
const expected5 = 4;

const nums3 = [5, 4, 3, 4, 3, 4, 5];
const expected6 = 4; // there is a pair of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expected7 = 1;

function oddOccurrencesInArray(nums) {
    
}