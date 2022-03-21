function rotateStr(str, amnt) {
    var result = ""
    
    if(amnt>str.length){
      amnt=amnt-str.length
    }
    for(var i=str.length-amnt; i<str.length; i++){
        result += str[i]
      }
      for(var j=0; j<str.length-amnt; j++){
        result += str[j]
      }
    return result
}

console.log(rotateStr("Hello World", 13))