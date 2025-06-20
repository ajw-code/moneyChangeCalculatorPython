I'm running the script moneyChangeCalculator.py from a Windows 11 Powershell terminal within a PyCharm 2025.1 environment. 
Python version is Python 3.13.3. Additional libraries that are needed to run the program are getopt and sys. 
If you do not have them installed on your environment, then a simple "pip install <library>" can be used. 
In order to run the script you can run the command in Powershell "python .\moneyChangeCalculator.py --help" to print out the usage options. 
I've also added an Easter egg for the program to calculate the cost of a haircut with ONLY the option "--shave_and_a_haircut". Try it! It's fun!

As for the program I've created a class that has local variables that store dollar values, coinage values, dollar amounts and coinage amounts.
I've implemented three methods within the class to calculate the number of dollars, calculate the coinage and one method to print out the results on the screen. 

For the rest of the program, I've implemented four helper functions. One function to print program usage, 
another to verify the numeric input is a valid dollar amount (no negative numbers, no fractions of a penny). 
The "get_number_of_digits_after_decimal" function is also a helper function that is used to count the number of digits after a decimal. 
This function is called in the "check_money_amount_in_dollars" function to verify that the number input does not contain fractions of a penny, i.e. 
more than two digits after the decimal. The final helper function is the parse_commandline function. I'm going old school with this command line parsing and
 using the getopts command line parser to parse input. There is a try, except wrapper around the getopts block to verify whether the input is purely numeric or not.

