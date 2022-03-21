/*
PSEUDOCODE:
STEP 1: Iterate through string
STEP 2: Look for parentheses pairs
STEP 3: If there's an uneven number of parentheses, return false
STEP 4: If there's an even number of parentheses, return true
*/

const str1 = "Y(3(p)p(3)r)s";
// const expected1 = true;

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
console.log(parensValid(str1))

const str5 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
// const expected5 = true;

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
  console.log(bracesValid(str5))


