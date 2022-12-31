/*
This code defines a function called checkCashRegister that takes three arguments: price, cash, and cid.

The price argument represents the price of an item. The cash argument represents the amount of money that a customer is paying for the item. The cid argument is an array of arrays representing the denominations of currency in a cash register and the corresponding amounts of each denomination. Each inner array has two elements: a string representing the name of the denomination and a number representing the amount of that denomination in the register.

The checkCashRegister function returns an object with two properties: status and change. The status property indicates the status of the transaction and can be one of three values: 'OPEN', 'CLOSED', or 'INSUFFICIENT_FUNDS'. The change property is an array of arrays representing the denominations of change to be given to the customer and the corresponding amounts of each denomination.

The checkCashRegister function starts by initializing the output object with a status property set to null and an empty change array. It then calculates the amount of change that the customer is owed by subtracting the price from the cash.

Next, the function uses the reduce method to iterate over the cid array and calculate the total amount of money in the register. It also creates an object called register that has properties corresponding to each denomination in the cid array and values representing the corresponding amounts of each denomination.

If the total amount of money in the register is equal to the amount of change owed to the customer, the function sets the status property of the output object to 'CLOSED' and the change property to the original cid array. If the total amount of money in the register is less than the amount of change owed to the customer, the function sets the status property of the output object to 'INSUFFICIENT_FUNDS' and returns the output object.

If the total amount of money in the register is greater than the amount of change owed to the customer, the function uses the reduce method to iterate over the denom array and calculate the change to be given to the customer. The denom array is an array of objects representing the different denominations of currency that can be used to give change. Each object has two properties: name, which is a string representing the name of the denomination, and val, which is a number representing the value of the denomination in dollars.

The function uses a while loop to iterate over the denom array and add up the amount of each denomination needed to give the customer the correct change. It then updates the change and register variables accordingly and pushes the denomination and amount of that denomination into the change_arr array.

Finally, the function sets the status property of the output object to 'OPEN' and the change property to the change_arr array, and returns the output object.
*/

var denom = [
	{ name: 'ONE HUNDRED', val: 100},
	{ name: 'TWENTY', val: 20},
	{ name: 'TEN', val: 10},
	{ name: 'FIVE', val: 5},
	{ name: 'ONE', val: 1},
	{ name: 'QUARTER', val: 0.25},
	{ name: 'DIME', val: 0.1},
	{ name: 'NICKEL', val: 0.05},
	{ name: 'PENNY', val: 0.01}
];

function checkCashRegister(price, cash, cid) {
 var output = {status: null, change: []};
 var change = cash - price;
 var register = cid.reduce(function(acc, curr) {
 acc.total += curr[1];
 acc[curr[0]] = curr[1];
 return acc;
 }, {total: 0});
 if(register.total === change) {
 output.status = 'CLOSED';
 output.change = cid;
 return output;
 }
 if(register.total < change) {
 output.status = 'INSUFFICIENT_FUNDS';
 return output;
 }
 var change_arr = denom.reduce(function(acc, curr) {
 var value = 0;
 while(register[curr.name] > 0 && change >= curr.val) {
 change -= curr.val;
 register[curr.name] -= curr.val;
 value += curr.val;
 change = Math.round(change * 100) / 100;
 }
 if(value > 0) {
 acc.push([ curr.name, value ]);
 }
 return acc;
 }, []);
 if(change_arr.length < 1 || change > 0) {
 output.status = 'INSUFFICIENT_FUNDS';
 return output;
 }
 output.status = 'OPEN';
 output.change = change_arr;
 return output;
}
