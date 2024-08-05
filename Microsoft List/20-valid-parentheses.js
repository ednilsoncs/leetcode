//https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=e86ew7id

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  
  const pilhaAberto = []
  if(s.length === 1){
    return false
  }

  for(let i = 0 ; i < s.length; i= i+1){
    const value = s[i]
    switch(value){
      case '(':
        pilhaAberto.push(value)
         break

      case '[':
        pilhaAberto.push(value)
          break

      case '{':
        pilhaAberto.push(value)
          break 
          
      case ')':
        if(pilhaAberto[pilhaAberto.length-1] === '('){
          pilhaAberto.pop()
        }else{
          return false
        }
          break
   
      case ']':
        if(pilhaAberto[pilhaAberto.length-1] === '['){
          pilhaAberto.pop()
        }else{
          return false
        }
          break
   
      case '}':
        if(pilhaAberto[pilhaAberto.length-1] === '{'){
          pilhaAberto.pop()
        }else{
          return false
        }
          break       
    }
  }
  
  return !!!pilhaAberto.length
};

