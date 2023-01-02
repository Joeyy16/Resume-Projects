// function called convertToRoman that takes a number as an argument and returns the Roman numeral representation of that number.
function convertToRoman(num) {
  var ref = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100], ['XC', 90], ['L', 50], ['XL', 40], ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]; // function starts by defining an array called ref that maps Roman numeral letters to their corresponding values.
  var res = []; // It then initializes an empty array called res that will be used to store the Roman numeral representation of the input number.
  ref.forEach(function(p) { // function then uses the forEach method to iterate over the ref array
    while (num >= p[1]) { // For each element in the ref array, the function uses a while loop to add the corresponding Roman numeral letter to the res array as many times as needed to represent the input number.
      res.push(p[0]);
      num -= p[1]; //  It then subtracts the corresponding value from the input number each time a letter is added to the res array.
    }
  });
  return res.join(''); // returns the Roman numeral representation of the input number by joining the elements of the res array together into a single string using the join method.
}
