import tkinter as tk
from tkinter import messagebox

false = False
true = True

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char)- base + shift)% 26 + base)
        else:
            result += char
            
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def handle_encrypt():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        result = encrypt(text, shift)
        result_label.config(text=f"your encryption result : {result}")
    except ValueError:
        messagebox.showerror("seriously huh?", "enter the shift number first!")
        
def handle_decrypt():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        result = encrypt(text, shift)
        result_label.config(text=f"your decryption result : {result}")
        
    except ValueError:
        messagebox.showerror("seriously huh?", "enter the shift number first!")
        
def handle_copy():
    result = result_label.cget("text")
    if "result" in result:
        root.clipboard_clear()
        root.clipboard_append(result)
        root.update()
        messagebox.showinfo("Copied!", "result copied to clipboard  ✅")

root = tk.Tk()
root.title("🔒 SECRET MESSAGE")
root.geometry("450x300")
root.resizable(false, false)
root.configure(bg="#f0f4ff")

font_title = ("Helvetica", 14, "bold")
font_label = ("Helvetica", 11)
font_entry = ("Helvetica", 10)

tk.Label(root, text="enter your secret message: ", font=font_label, bg="#f0f4ff").pack(pady=(5, 5))
entry_text = tk.Entry(root, width=50, font=font_entry)
entry_text.pack(pady=(0, 10))

tk.Label(root, text="enter the shift number: ", font=font_label, bg="#f0f4ff").pack(pady=(5, 5))
entry_shift = tk.Entry(root, width=10, font=font_entry, justify='center')
entry_shift.pack(pady=10)

frame_buttons = tk.Frame(root, bg="#f0f4ff")
frame_buttons.pack(pady=10)

btn_encrypt = tk.Button(frame_buttons, text="🔐 encrypt!", font=font_label, bg="#c2e7ff", fg="black", command=handle_encrypt)
btn_encrypt.grid(row=0, column=0, padx=10)

btn_decrypt = tk.Button(frame_buttons, text="🔓 decrypt!", font=font_label, bg="#ffd6d6", fg="black", command=handle_decrypt)   
btn_decrypt.grid(row=0, column=1, padx=10)

result_label = tk.Label(root, text="Result will appears here", wraplength=380, font=("Courier New", 11), bg="#f0f4ff", fg="darkblue", justify="center")
result_label.pack(pady=15)

copy_btn = tk.Button(root, text="📋 copy result", font=font_label, bg="#feffba", fg="black", command=handle_copy, state="normal")
copy_btn.pack(pady=5)

root.mainloop()         