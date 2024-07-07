import os
import tkinter as tk
from tkinter import ttk, scrolledtext, font as tkfont

# Function to build dictionary from TXT file
def build_dictionary(file_path):
    word_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if '=' in line:
                english_word, bangla_meanings = line.split('=', 1)
                bangla_meanings = bangla_meanings.strip()
                if ',' in bangla_meanings:
                    meanings_list = [meaning.strip() for meaning in bangla_meanings.split(',')]
                else:
                    meanings_list = [bangla_meanings]
                word_dict[english_word.strip().lower()] = meanings_list
    return word_dict

# Function to get meaning of a word from dictionary
def get_meaning(word, word_dict):
    meanings = word_dict.get(word.lower(), ['Meaning not found'])
    return ', '.join(meanings)

# Function to handle button click event
def search_meaning():
    input_text = input_entry.get("1.0", tk.END).strip()
    
    # Define characters to remove
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~’1234567890–|‘©“”'''
    
    # Remove punctuation and special characters
    cleaned_text = ''.join([char for char in input_text if char not in punctuation])

    words = cleaned_text.split()
    
    results_text.delete("1.0", tk.END)  # Clear previous results
    
    results = [(word, get_meaning(word, word_dict)) for word in words]
    
    for word, meaning in results:
        results_text.insert(tk.END, f"{word}: {meaning}\n")
        results_text.tag_configure(word, font=('Helvetica', 30, 'bold'), foreground='blue')  # Change font size and color
        results_text.tag_add(word, f"{results_text.index(tk.END)} - {len(meaning) + 2} chars linestart", f"{results_text.index(tk.END)} linestart + {len(word)} chars")

# Create GUI window
root = tk.Tk()
root.title("English to Bangla Dictionary")

# Create a frame for input and output
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Label and text area for user input
input_label = ttk.Label(frame, text="Enter words separated by spaces:")
input_label.grid(row=0, column=0, sticky=tk.W)

input_entry = scrolledtext.ScrolledText(frame, width=80, height=10)
input_entry.grid(row=1, column=0, sticky=tk.W)

# Button to trigger search
search_button = ttk.Button(frame, text="Search", command=search_meaning)
search_button.grid(row=2, column=0, sticky=tk.W)

# Text area for displaying results
results_text = scrolledtext.ScrolledText(frame, width=120, height=20)
results_text.grid(row=3, column=0, columnspan=2, sticky=tk.W)

# Configure font and color for results_text
results_text.configure(font=tkfont.Font(family='Helvetica', size=50))
results_text.tag_configure('default', font=('Helvetica', 50))  # Default tag configuration

# Define the file path (adjust as needed)
file_path = r"C:\Users\style\Desktop\Movies Subtitles English\dictionary words storing\Over 50000 Unigw bangla to english Dictionary words.txt"

# Check if file exists
if os.path.exists(file_path):
    # Build the dictionary from the TXT file
    word_dict = build_dictionary(file_path)
else:
    tk.messagebox.showerror("File Not Found", f"File not found: {file_path}")
    root.destroy()

# Start the GUI main loop
root.mainloop()
