def main():
	a = int(input("Give me a number: "))
	b = int(input("Give me another number: "))
	operator = input("what to do with the numbers? (a for add, m for multiply): ")

	if operator == "a":
		print(f"{a} + {b} = {a + b}")
	elif operator == "m":
		print(f"{a} * {b} = {a * b}")

if __name__ == "__main__":
	main()