def tip(bill_amt, tip_per):
	return bill_amt * tip_per

def total_bill(tip_amt, bill_amt):
	return tip_amt + bill_amt

def split_bill(bill_amt, num_people):
	return bill_amt / num_people

def main():
	bill_amt= float(raw_input("How much was your bill? "))
	tip_amt = tip(bill_amt,.15)

	menu_choice = int(raw_input("What would you like to do? Select 1 to calculate tip or 2 to split the bill. "))

	if menu_choice == 1:
		print total_bill(tip_amt, bill_amt)
		prompt = raw_input("Would you like to split your bill? ").lower()
		if prompt == "yes":
			split = int(raw_input("How many ways to split the bill? "))
			print split_bill(bill_amt, split)
	else: 
		split_num = int(raw_input("How many ways to split the bill? "))
		print split_bill(bill_amt, split_num)


if __name__ == '__main__':
	main()