/*
This code defines a function called telephoneCheck that takes a string as an argument and returns a boolean indicating whether the string is a valid telephone number.

The telephoneCheck function uses a regular expression (regex) to determine whether the input string is a valid telephone number. A regular expression is a pattern that can be used to match certain strings. In this case, the regular expression re is designed to match strings that are in the following format:

An optional + symbol followed by an optional 1 and an optional space (([+]?1[\s]?)?)
An optional area code in parentheses, or the first three digits of the telephone number, followed by an optional space or punctuation (((?:[(](?:[2-9]1[02-9]|[2-9][02-8][0-9])[)][\s]?)|(?:(?:[2-9]1[02-9]|[2-9][02-8][0-9])[\s.-]?)){1})
The next three digits of the telephone number, followed by an optional space or punctuation (([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2}[\s.-]?){1})
The last four digits of the telephone number (([0-9]{4}){1})
The telephoneCheck function uses the test method of the re regex to check if the input string matches the pattern. If the input string matches the pattern, the test method returns true. If the input string does not match the pattern, the test method returns false.

The telephoneCheck function then returns the value returned by the test method. In this example, the function is called with the string "555-555-5555" as an argument, so it will return true if the string is a valid telephone number and false if it is not.
*/

var re = /^([+]?1[\s]?)?((?:[(](?:[2-9]1[02-9]|[2-9][02-8][0-9])[)][\s]?)|(?:(?:[2-9]1[02-9]|[2-9][02-8][0-9])[\s.-]?)){1}([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2}[\s.-]?){1}([0-9]{4}){1}$/;

function telephoneCheck(str) {
  return re.test(str);
}

telephoneCheck("555-555-5555");
