/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

/*
PSEUDOCODE:
STEP 1: Iterate through string
STEP 2: Look for parentheses pairs
STEP 3: If there's an uneven number of parentheses, return false
STEP 4: If there's an even number of parentheses, return true
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
 function parensValid(str) {
    const parensStack = [];
  
    for (const char of str) {
      if (char === "(") {
        parensStack.push(char);
      } else if (char === ")") {
        if (parensStack.length === 0) {
          return false;
        } else {
          parensStack.pop();
        }
      }
    }
    return parensStack.length === 0;
  }



//----------------------------------------------------------------------------------------------------------------------



/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str5 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected5 = true;

const str6 = "D(i{a}l[ t]o)n{e";
const expected6 = false;

const str7 = "A(1)s[O (n]0{t) 0}k";
const expected7 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
 function bracesValid(str) {
    const stack = [];
    const closeToOpen = { ")": "(", "}": "{", "]": "[" };
  
    for (let i = 0; i < str.length; i++) {
      switch (str[i]) {
        case "(":
        case "{":
        case "[":
          stack.push(str[i]);
          break;
        case ")":
        case "}":
        case "]":
          if (closeToOpen[str[i]] === stack[stack.length - 1]) {
            stack.pop();
          } else {
            return false;
          }
          break;
        default:
          break;
      }
    }
    return stack.length === 0;
  }