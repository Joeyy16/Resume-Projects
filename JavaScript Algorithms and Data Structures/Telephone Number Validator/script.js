// a regular expression (regex) to determine whether the input string is a valid telephone number. A regular expression is a pattern that can be used to match certain strings. In this case, the regular expression re is designed to match strings that match several formats
var re = /^([+]?1[\s]?)?((?:[(](?:[2-9]1[02-9]|[2-9][02-8][0-9])[)][\s]?)|(?:(?:[2-9]1[02-9]|[2-9][02-8][0-9])[\s.-]?)){1}([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2}[\s.-]?){1}([0-9]{4}){1}$/;

// An optional + symbol followed by an optional 1 and an optional space (([+]?1[\s]?)?)
// An optional area code in parentheses, or the first three digits of the telephone number, followed by an optional space or punctuation (((?:[(](?:[2-9]1[02-9]|[2-9][02-8][0-9])[)][\s]?)|(?:(?:[2-9]1[02-9]|[2-9][02-8][0-9])[\s.-]?)){1})
// The next three digits of the telephone number, followed by an optional space or punctuation (([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2}[\s.-]?){1})
// The last four digits of the telephone number (([0-9]{4}){1})


// Function called telephoneCheck that takes a string as an argument and returns a boolean indicating whether the string is a valid telephone number.
function telephoneCheck(str) {
  return re.test(str); // The telephoneCheck function uses the test method of the re regex to check if the input string matches the pattern. If the input string matches the pattern, the test method returns true. If the input string does not match the pattern, the test method returns false.
}

// Calling function with arguement
telephoneCheck("555-555-5555");
