import tkinter as tk
from tkinter import ttk

# --- Functions ---
def greet():
    """
    This function is called when the button is clicked.
    It gets the text from the entry box and updates the greeting label.
    """
    # Get the name from the entry widget's text
    name = name_entry.get()
    
    # Update the greeting label's text
    # The f-string formats the greeting with the entered name
    greeting_label.config(text=f"Hello, {name}!")


# --- Main Application Window ---
# Create the main window instance
root = tk.Tk()
root.title("Simple Greeter")
root.geometry("300x150") # Set the window size (width x height)

# Use the themed widgets for a more modern look
style = ttk.Style(root)
style.theme_use("clam") # You can try other themes like 'alt', 'default', 'classic'

# Create a frame to hold all the other widgets
# The padding adds some space around the contents
main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.pack(fill="both", expand=True)


# --- Widgets ---
# 1. Label asking for the user's name
name_label = ttk.Label(main_frame, text="Enter your name:")
name_label.pack(pady=5) # pady adds vertical padding

# 2. Entry widget (text box) for user input
name_entry = ttk.Entry(main_frame, width=30)
name_entry.pack(pady=5)
name_entry.focus() # Place the cursor in the entry box on startup

# 3. Button that calls the greet() function when clicked
greet_button = ttk.Button(main_frame, text="Greet Me!", command=greet)
greet_button.pack(pady=10)

# 4. Label to display the final greeting (initially empty)
greeting_label = ttk.Label(main_frame, text="")
greeting_label.pack(pady=5)


# --- Start the Application ---
# The mainloop() method keeps the window open and listens for events
root.mainloop()