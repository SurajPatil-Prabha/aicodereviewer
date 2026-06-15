from reviewer import CodeReviewer

reviewer = CodeReviewer()

file_name = "sample.py"

print("\n===== AI CODE REVIEWER =====\n")

print(reviewer.syntax_check(file_name))

print("\n===== CODE METRICS =====")
print("Total Lines:", reviewer.metrics(file_name))

print("\n===== PYLINT REPORT =====\n")
print(reviewer.review(file_name))