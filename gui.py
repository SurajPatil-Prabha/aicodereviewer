import customtkinter as ctk
from tkinter import filedialog
from reviewer import CodeReviewer

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

reviewer = CodeReviewer()

app = ctk.CTk()
app.title("AI Code Reviewer")
app.geometry("900x600")

selected_file = ""


def choose_file():
    global selected_file

    selected_file = filedialog.askopenfilename(
        filetypes=[("Python Files", "*.py")]
    )

    file_label.configure(text=selected_file)


def review_code():
    if selected_file == "":
        output.delete("1.0", "end")
        output.insert("end", "Please select a Python file.")
        return

    syntax_result = reviewer.syntax_check(selected_file)
    line_count = reviewer.metrics(selected_file)
    pylint_report = reviewer.review(selected_file)

    report = f"""
===== AI CODE REVIEW REPORT =====

{syntax_result}

Total Lines: {line_count}

===== PYLINT REPORT =====

{pylint_report}
"""

    output.delete("1.0", "end")
    output.insert("end", report)


title = ctk.CTkLabel(
    app,
    text="AI Code Reviewer",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

select_btn = ctk.CTkButton(
    app,
    text="Select Python File",
    command=choose_file
)
select_btn.pack(pady=10)

file_label = ctk.CTkLabel(
    app,
    text="No file selected"
)
file_label.pack()

review_btn = ctk.CTkButton(
    app,
    text="Review Code",
    command=review_code
)
review_btn.pack(pady=10)

output = ctk.CTkTextbox(
    app,
    width=800,
    height=350
)
output.pack(pady=20)

app.mainloop()