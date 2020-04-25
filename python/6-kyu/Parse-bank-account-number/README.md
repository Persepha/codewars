# Parse bank account number (6 kyu)
[Parse bank account number codewars link](https://www.codewars.com/kata/597eeb0136f4ae84f9000001)

### Details
Returns the bank account number parsed from specified string.

You work for a bank, which has recently purchased an ingenious machine to assist in reading letters and faxes sent in by branch offices.
The machine scans the paper documents, and produces a string with a bank account that looks like this:
```python
 _     _  _     _  _  _  _  _
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
```
Each string contains an account number written using pipes and underscores.
Each account number should have at least one digit, all of which should be in the range 0-9.

Your task is to write a function that can take bank account string and parse it into actual account numbers.
```python
 @param {string} bankAccount
 @return {number}
```
Examples:
```python
   '    _  _     _  _  _  _  _ \n'+
   '  | _| _||_||_ |_   ||_||_|\n'+     => 123456789
   '  ||_  _|  | _||_|  ||_| _|\n'

   ' _  _  _  _  _  _  _  _  _ \n'+
   '| | _| _|| ||_ |_   ||_||_|\n'+     => 23056789
   '|_||_  _||_| _||_|  ||_| _|\n',

   ' _  _  _  _  _  _  _  _  _ \n'+
   '|_| _| _||_||_ |_ |_||_||_|\n'+     => 823856989
   '|_||_  _||_| _||_| _||_| _|\n',
```