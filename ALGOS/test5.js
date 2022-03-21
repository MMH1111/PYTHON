const queue1 = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1];

function socialDistancingEnforcer(queue) {
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

const nums1 = [-2, 5, 7, 0, 3];

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