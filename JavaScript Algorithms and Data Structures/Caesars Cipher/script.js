// The lookup table is an object with keys that are the uppercase letters of the alphabet, and values that are the corresponding letters of the alphabet shifted by 13 places. For example, the key A maps to the value N, the key B maps to the value O, and so on.
var lookup = {
  'A': 'N','B': 'O','C': 'P','D': 'Q',
  'E': 'R','F': 'S','G': 'T','H': 'U',
  'I': 'V','J': 'W','K': 'X','L': 'Y',
  'M': 'Z','N': 'A','O': 'B','P': 'C',
  'Q': 'D','R': 'E','S': 'F','T': 'G',
  'U': 'H','V': 'I','W': 'J','X': 'K',
  'Y': 'L','Z': 'M'
};

function rot13(encodedStr) {
  var codeArr = encodedStr.split("");  // The rot13 function starts by splitting the encoded string into an array of individual characters using the split method.
  var decodedArr = []; // Your Result goes here // It then initializes an empty array called decodedArr that will be used to store the decoded version of the encoded string.

  // The rot13 function then uses the map method to iterate over each character in the codeArr array. For each character, the function checks if the lookup table has a key with the same value as the character. If it does, it assigns the corresponding value from the lookup table to the letter variable. If the lookup table does not have a key with the same value as the character, the function does not modify the value of the letter variable.
  decodedArr = codeArr.map(function(letter) {
    if(lookup.hasOwnProperty(letter)) {
      letter = lookup[letter];
    }
    return letter;
  });

  // Finally, the rot13 function returns the decoded version of the encoded string by joining the elements of the decodedArr array together into a single string using the join method.
  return decodedArr.join(""); // Array to String
}
