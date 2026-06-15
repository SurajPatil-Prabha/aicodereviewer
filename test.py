import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("AI Code Reviewer")
app.geometry("500x300")

label = ctk.CTkLabel(
    app,
    text="AI Code Reviewer",
    font=("Arial", 24)
)
label.pack(pady=40)

button = ctk.CTkButton(
    app,
    text="Working!"
)
button.pack()

app.mainloop()
