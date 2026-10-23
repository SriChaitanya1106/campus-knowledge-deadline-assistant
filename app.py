from pathlib import Path
#step - 1: 
# take a keyword for searching from the user
# verify the keyword
print("=== Campus Knowledge & Deadline Assistant ===")
keyword = input("Enter a keyword: ")
clean_name = keyword.strip()
if clean_name == "":
    print("please enter a keyword: ")
elif clean_name.lower() == "exit":
    print("Goodbye!")
else:
    print("you entered:",clean_name)

#step - 2:
#finding all .txt files inside your documents folder using Python's pathlib module.
document_folder = Path(__file__).parent / "documents"
text_files = document_folder.glob("*.txt")
for file in text_files:
    print(file.name)