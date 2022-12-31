/*
This code defines a function called convertToRoman that takes a number as an argument and returns the Roman numeral representation of that number.

The Roman numeral system uses a set of letters to represent different values. For example, the letter I represents the value 1, the letter V represents the value 5, and the letter X represents the value 10. The Roman numeral system also has rules for constructing larger numbers using these letters. For example, the Roman numeral IV represents the value 4 (5 - 1) and the Roman numeral IX represents the value 9 (10 - 1).

The convertToRoman function starts by defining an array called ref that maps Roman numeral letters to their corresponding values. It then initializes an empty array called res that will be used to store the Roman numeral representation of the input number.

The convertToRoman function then uses the forEach method to iterate over the ref array. For each element in the ref array, the function uses a while loop to add the corresponding Roman numeral letter to the res array as many times as needed to represent the input number. It then subtracts the corresponding value from the input number each time a letter is added to the res array.

Finally, the convertToRoman function returns the Roman numeral representation of the input number by joining the elements of the res array together into a single string using the join method.
*/

function convertToRoman(num) {
  var ref = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100], ['XC', 90], ['L', 50], ['XL', 40], ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]];
  var res = [];
  ref.forEach(function(p) {
    while (num >= p[1]) {
      res.push(p[0]);
      num -= p[1];
    }
  });
  return res.join('');
}
