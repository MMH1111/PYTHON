/* 
Given an array of ints representing a line of people where the space between
indexes is 1 foot, with 0 meaning no one is there and 1 meaning someone is in
that space,
return whether or not there is at least 6 feet separating every person.
Bonus: O(n) linear time (avoid nested loops that cause re-visiting indexes).
*/

const queue1 = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1];
const expected1 = false;

const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected2 = true;

const queue3 = [1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected3 = true;

const queue4 = [];
const expected4 = true;

const queue5 = [1];
const expected7 = true;

/*
 * Determines whether each occupied space in the line of people is separated by
 * 6 empty spaces.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<0|1>} queue
 * @returns {Boolean}
 */

/** PSEUDOCODE
 * run through the index until it hits a 1
 * start a count at 0 and add for every 0 until the next 1
 * if count is >=6 reset count to 0
 * if count is <6, insert 0 * (6 - count) at index - 1, set count to 0
 */
 function socialDistancingEnforcer(queue) {
    var one = false
    var count = 6
    for(var i = 0; i < queue.length; i++){
        if(queue[i] == 1 && count < 6){
        return false
        }
        if(queue[i] == 1 && count >= 6){
         count = 0
        }
        if(queue[i] == 0){
          count+=1
        }
      }
      return true
  }
  
  console.log(socialDistancingEnforcer(queue1))



// ======================================================================================




/* 
  Balance Index
  Here, a balance point is ON an index, not between indices.
  Return the balance index where sums are equal on either side
  (exclude its own value).
  
  Return -1 if none exist.
  
*/

const nums1 = [-2, 5, 7, 0, 3];
const expected5 = 2; // I believe it's returning 2, because 7, which is the balance point has an index of 2.

const nums2 = [9, 9];
const expected6 = -1;

/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */

function balanceIndex(nums) {
    for(var i=0; i<nums.length; i++){
        var leftcount = 0
        var rightcount = 0
        for(var left=0; left<i; left++){
            leftcount += nums[left]
        }
        for(var right=nums.length-1; right>i; right--){
            rightcount +=nums [right]
        }
        if(leftcount === rightcount){
            return i
        }
    }
    return -1
}
console.log(balanceIndex(nums1))