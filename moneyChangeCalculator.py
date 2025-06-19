import getopt
import sys

##Implement a class to calculate dollar bills and change based on amount passed through to it
class calculate_bills_and_change:
#Initialize the for standard bills and standard change
    def __init__(self):
        #Initialize Bills
        self.hundred_dollar_amount = 100
        self.fifty_dollar_amount = 50
        self.twenty_dollar_amount = 20
        self.ten_dollar_amount = 10
        self.five_dollar_amount = 5
        self.one_dollar_amount = 1

        self.number_of_hundred_dollar_bills =0
        self.number_of_fifty_dollar_bills =0
        self.number_of_twenty_dollar_bills =0
        self.number_of_ten_dollar_bills =0
        self.number_of_five_dollar_bills =0
        self.number_of_one_dollar_bills =0

        #Initialize Change
        self.quarter_amount = 25
        self.dime_amount=10
        self.nickel_amount=5
        self.penny_amount=1

        self.number_of_quarters =0
        self.number_of_dimes =0
        self.number_of_nickels =0
        self.number_of_pennies =0

        self.running_total = 0

    #Method takes in amount in float format and then converts it to int format.
    #Method then performs division based algorithm to determine bill denominations
    def calculate_bills(self, amount):
        integer_amount = int(amount)

        self.number_of_hundred_dollar_bills = int(integer_amount/ self.hundred_dollar_amount)
        integer_amount = int(integer_amount - self.number_of_hundred_dollar_bills * self.hundred_dollar_amount)

        self.number_of_fifty_dollar_bills = int(integer_amount/ self.fifty_dollar_amount)
        integer_amount = int(integer_amount -self.number_of_fifty_dollar_bills*self.fifty_dollar_amount)

        self.number_of_twenty_dollar_bills = int(integer_amount/ self.twenty_dollar_amount)
        integer_amount=int(integer_amount - self.number_of_twenty_dollar_bills * self.twenty_dollar_amount)

        self.number_of_ten_dollar_bills = int(integer_amount/ self.ten_dollar_amount)
        integer_amount=int(integer_amount - self.number_of_ten_dollar_bills * self.ten_dollar_amount)

        self.number_of_five_dollar_bills = int(integer_amount/ self.five_dollar_amount)
        integer_amount=int(integer_amount - self.number_of_five_dollar_bills * self.five_dollar_amount)

        self.number_of_one_dollar_bills = int(integer_amount/ self.one_dollar_amount)


    #Calculate coinage
    def calculate_coinage(self, amount):
        #Convert to string and then extract the decimal to convert back to int
        decimal_string_index=1
        string_amount =str(amount)
        split_string_amount=string_amount.split(".")
        decimal_string_amount=split_string_amount[decimal_string_index]

        integer_decimal_amount=int(decimal_string_amount)

        self.number_of_quarters = int(integer_decimal_amount / self.quarter_amount)
        integer_decimal_amount=int(integer_decimal_amount - self.number_of_quarters * self.quarter_amount)

        self.number_of_dimes = int(integer_decimal_amount / self.dime_amount)
        integer_decimal_amount=int(integer_decimal_amount - self.number_of_dimes * self.dime_amount)

        self.number_of_nickels = int(integer_decimal_amount / self.nickel_amount)
        integer_decimal_amount=int(integer_decimal_amount - self.number_of_nickels * self.nickel_amount)

        self.number_of_pennies = int(integer_decimal_amount / self.penny_amount)
        integer_decimal_amount=int(integer_decimal_amount - self.number_of_pennies*self.penny_amount)


    #Method to print number of each denomimnation of coin
    def print_results(self):
        print("-"*40)
        print("-"+"The total number of bills and coins to dispense is: -")
        print("Bills:")
        print("Hundreds: "+ str(self.number_of_hundred_dollar_bills))
        print("Fifties: " + str(self.number_of_fifty_dollar_bills))
        print("Twenties: " + str(self.number_of_twenty_dollar_bills))
        print("Tens: " + str(self.number_of_ten_dollar_bills))
        print("Fives: " + str(self.number_of_five_dollar_bills))
        print("Ones: "+ str(self.number_of_one_dollar_bills))
        print("-"*40)
        print("Coins:")
        print("Quarters: "+ str(self.number_of_quarters))
        print("Dimes: " + str(self.number_of_dimes))
        print("Nickels: "+ str(self.number_of_nickels))
        print("Pennies: "+ str(self.number_of_pennies))
        print("-" * 40)
        print("Thanks for using this calculator! Bye!")



##Helper Functions
#Implement function to print program usage in order to modularize the code
def print_program_usage(version_number):
    usage_string = "Usage ./moneyChangeCalculator.py Options\n" \
                    "--moneyAmount=<moneyAmountInDollars>\t -m <moneyAmountInDollars>\n" \
                    "--help\t\t\t\t\t -h print this help \n"
    print(usage_string)

#The following function parses arguments from the command line and returns dollar amount


#The following function performs error checking on the input
def check_money_amount_in_dollars(amount):
    #Constant to set maximum number after of digits after decimal
    down_to_the_nearest_penny = 2


    if(amount>=0 and amount<0.1):
        print("Amount is $0.00. No change can be given")
        sys.exit()
    elif(amount <0):
        print("Amount {} is less than $0.00. No change can be given.".format(amount))
        sys.exit()
    elif(get_number_of_digits_after_decimal(amount)>down_to_the_nearest_penny):
        print("Amount {} has values that are fractions of a penny. It is an invalid amount.".format(amount))
        sys.exit()
    else:
        #The amount is valid
        return amount

#Get number of digits after input. Cannot be more than two digits
def get_number_of_digits_after_decimal(amount):
    amount_string = str(amount)
    if "." not in amount_string:
        return 0
    return len(amount_string.split(".")[-1])

#Helper function to parse commandline
def parse_commandline(version_number):
    options_string_slice_start = 1
    error_option_slice=1
    amount = 0
    Sacagawea_flag = False
    half_dollar_flag = False

    try:
        options, arguments = getopt.getopt(sys.argv[options_string_slice_start:], "hm:", ["help", "moneyAmountInDollars=", "shave_and_a_haircut"])
    except getopt.GetoptError as err:

        #Extract Option from err:
        error_sentence = str(err)
        error_sentence_split = error_sentence.split(' ')
        error_option = error_sentence_split[error_option_slice]

        #print help information and exit
        print("ERROR: input argument " + error_option + " not recognized. Program execution aborted.")
        print_program_usage(version_number)
        sys.exit(2)

    if(options ==[]):
        print("Error: required arguments missing. Program execution aborted.")
        print_program_usage(version_number)
        sys.exit()

    for option, argument in options:
        if (option=="--shave_and_a_haircut"):
            print("Two Bits!")
            sys.exit()
        elif ((option=="-h") or (option=="--help")):
            print_program_usage(version_number)
            sys.exit()
        elif ((option=="-m") or (option=="--moneyAmountInDollars")):
            amount = argument
            return float(amount)
        else:
            print_program_usage(version_number)
            print(argument)
            sys.exit()

        #Default case if all else fails
        return float(amount)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    version_number = "0.1"

    #initialize amount to float data type
    amount =0.00

    try:
        amount = parse_commandline(version_number)
    except ValueError:
        print("Error: input argument is not a number. Program execution aborted.")
        sys.exit()

    #Check Input for Errors:
    check_money_amount_in_dollars(amount)

    #Create class and then use helper methods
    bills_and_change = calculate_bills_and_change()
    bills_and_change.calculate_bills(amount)
    bills_and_change.calculate_coinage(amount)
    bills_and_change.print_results()




