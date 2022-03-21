/*
Solution for 3-15-2022 Morning Algos
*/

// https://www.freecodecamp.org/news/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb/

function reverseString(str) {
    // Step 1. Create an empty string that will host the new created string
    var newString = "";
 
    // Step 2. Create the FOR loop
    /* The starting point of the loop will be (str.length - 1) which corresponds to the 
       last character of the string, "o"
       As long as i is greater than or equals 0, the loop will go on
       We decrement i after each iteration */
    for (var i = str.length - 1; i >= 0; i--) { 
        newString += str[i]; // or newString = newString + str[i];
    }
    /* Here hello's length equals 5
        For each iteration: i = str.length - 1 and newString = newString + str[i]
        First iteration:    i = 5 - 1 = 4,         newString = "" + "o" = "o"
        Second iteration:   i = 4 - 1 = 3,         newString = "o" + "l" = "ol"
        Third iteration:    i = 3 - 1 = 2,         newString = "ol" + "l" = "oll"
        Fourth iteration:   i = 2 - 1 = 1,         newString = "oll" + "e" = "olle"
        Fifth iteration:    i = 1 - 1 = 0,         newString = "olle" + "h" = "olleh"
    End of the FOR Loop*/
 
    // Step 3. Return the reversed string
    return newString; // "olleh"
}
 
reverseString('hello world');
console.log(reverseString('hello world'))

https://www.geeksforgeeks.org/reverse-string-preserving-space-positions/


function preserveSpace(str)
{
    let n = str.length;

    // Initialize two pointers
    // as two corners
    let start = 0;
    let end = n - 1;

    let Str = str.split('');

    // Move both pointers toward
    // each other
    while (start < end)
    {

        // If character at start or
        // end is space, ignore it
        if (Str[start] == ' ')
        {
            start++;
            continue;
        }
        else if (Str[end] == ' ')
        {
            end--;
            continue;
        }

        // If both are not spaces, do swap
        else
        {
            let temp = Str[start];
            Str[start] = Str[end];
            Str[end] = temp;
            start++;
            end--;
        }
    }
    document.write(Str.join(""));
}
 
let str = "internship at geeks for geeks";

preserveSpace(str);

/*
Solution for 3-15-2022 Morning Algos
*/
// https://megafauna.dev/remove-duplicate-array-values-javascript/#:~:text=%208%20Ways%20to%20Remove%20Duplicate%20Array%20Values,from%20an%20Array%20Using%20.forEach%20%28%29%0ADe-duplication...%20More%20
class ArrayMagic {
    constructor(array) {
      this.array = array;
  
      return this;
    }
  
    removeDuplicateValues() {
      return [ ...new Set(this.array) ];
    }
  }
  
  const letters = [ 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'x', 'z', 'z' ]
  
  const uniqueLetters = new ArrayMagic(letters).removeDuplicateValues()
  
  console.log(uniqueLetters) // Array(6) [ "a", "b", "c", "d", "x", "z" ]


  class ArrayMagic {
    constructor(array) {
      this.array = array;
  
      return this;
    }
  
    removeDuplicateValues() {
      return [ ...new Set(this.array) ];
    }
  }
  
  const letters = "abcABC"
  
  const uniqueLetters = new ArrayMagic(letters).removeDuplicateValues()
  
  console.log(uniqueLetters)



