const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

  function join(arr, separator) {
    for(var i=0; i<arr.length; i++){
        return arr[i] + separator + arr[i + 1] + separator + arr[i + 2];
    }
  }
  console.log(join(arr1,separator1))