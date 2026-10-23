print("=== Campus Knowledge & Deadline Assistant ===")
keyword = input("Enter a keyword: ")
clean_name = keyword.strip()
if clean_name == "":
    print("please enter a keyword: ")
elif clean_name.lower() == "exit":
    print("Goodbye!")
else:
    print("you entered: ",clean_name)
