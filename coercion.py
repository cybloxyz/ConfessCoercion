import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import requests
import subprocess

#defdef
body = ("Quicksand", 14)
base = "700x900"

root = tk.Tk()
root.title("💖 UMM..")
root.geometry("700x900")
root.resizable(True, True)
root.configure(bg="#f0f4ff")

#copy
def copy_ke_clipboard():
    root.clipboard_clear()
    root.clipboard_append(letters)
    root.update() 

def total_close():
    root.destroy()
    
def prevent_close():
    messagebox.showinfo("so..", "i don't know why don't ask me!")
    
root.protocol("WM_DELETE_WINDOW", prevent_close)

def open_other():
    subprocess.Popen(["python", "cipherEn.py"])
    
    
#thank you 
def thanks():
    page = tk.Toplevel(root)
    page.title("only thanks?")
    page.geometry("700x900")
    
    label = tk.Label(page, text="it's ok..you're welcome..", font=("Quicksand", 14))
    label.pack(pady=40)
    
    back_btn = tk.Button(page, text="thanks", command=thankss)
    back_btn.pack()
    
def thankss():
    page = tk.Toplevel(root)
    page.title("btwthanks for that 'thanks'..")
    page.geometry("700x900")
    
    label = tk.Label(page, text="it is ok, trus me..:)", font=("Quicksand", 14))
    label.pack(pady=40)
    
    back_btn = tk.Button(page, text="yeah..", command=thanksss)
    back_btn.pack(pady=40)
    
def thanksss():
    page = tk.Toplevel(root)
    page.title("it's ok...you can go")
    page.geometry("700x900")
    
    label = tk.Label(page, text="it is ok, no problem just go if you want to..", font=("Quicksand", 14))
    label.pack()
    
    back_btn = tk.Button(page, text="yeah..i'll go", command=thankssss)
    back_btn.pack()
    
def thankssss():
    page = tk.Toplevel(root)
    page.title("you still here?")
    page.geometry("700x900")
    
    label = tk.Label(page, text="why are you still here?..", font=("Quicksand", 14))
    label.pack()    
    
    back_btn = tk.Button(page, text="no no..", command=thankss)
    back_btn.pack()
    
#NO
def no():
    page = tk.Toplevel(root)
    page.title("ok then")
    page.geometry(base)
    
    label = tk.Label(page, text="hmmm...okay", font=body)
    label.pack(pady=40)
    
    back_btn = tk.Button(page, text="yeah", command=noo)
    back_btn.pack()
    
def noo():
    page = tk.Toplevel(root)
    page.title("yea..i'm alright")
    page.geometry(base)
    
    label = tk.Label(page, text="it is ok, just go if you want to", font=body)
    label.pack(pady=40)
    
    back_btn = tk.Button(page, text="ok", command=nooo)
    back_btn.pack()
    
def nooo():
    page = tk.Toplevel(root)
    page.title("hmmm")
    page.geometry(base)
    
    label = tk.Label(page, text="hmmm..why still here?", font=body)
    label.pack(pady=40)
    
    back_btn = tk.Button(page, text="idk..omg", command=no)
    back_btn.pack()
    
#same here
def same():
    page = tk.Toplevel(root)
    page.title("<3")
    page.geometry(base)
    
    img_love = [
        "maksa/a.png", "maksa/b.png", "maksa/c.png", "maksa/d.png", "maksa/e.png", "maksa/f.png", "maksa/g.png",
        "maksa/f.png", "maksa/e.png", "maksa/d.png", "maksa/c.png", "maksa/b.png", "maksa/a.png"
    ]
    
    label = tk.Label(page, text="GOTCHA! <3", font=body)
    label.pack(pady=40)
    
    back_btn = tk.Button(page, text="🩷🩷🩷 caution, it will noticed directly to my telegram!", command=total_close)
    back_btn.pack()
    
    current_index = [0]
    
    def love():
        current_index[0] += 1
        if current_index[0] >= len(img_love):
            current_index[0] = 0
            
        pat = img_love[current_index[0]]
        imgg = Image.open(pat).resize((220, 480), Image.Resampling.LANCZOS)
        photos = ImageTk.PhotoImage(imgg)
        
        canvas.itemconfig(image_id, image=photos)
        canvas.image = photos
        
        root.after(100, love)
        
    canvas = tk.Canvas(page, width=250, height=520, bg="#ffbbe8", highlightthickness=0)
    canvas.pack(pady=75)
    
    image_id = canvas.create_image(125,260, image=None)
    
    love()
    
#coercion
def coercion():
    kirim_telegram("yay, same thing! omg is it perfect your plan? ummm don't forget also consider about heart btw :P")
    same()
    
# quotes
qts = [
    "you know right, feel free to be honest..",
    "take your time, i'll wait",
    "you are my favorite as always",
    "i'll never regret for this",
    "you have no idea about my feeling for you"
]

def update_qts():
    text.set(random.choice(qts))
    
# presentation

img_paths = [
     "maksa/l.png",
    "maksa/l.png",
    "maksa/me.png",
    "maksa/when.png",
    "maksa/i.png",
    "maksa/see.png",
    "maksa/you.png",
    "maksa/l.png",
    "maksa/dug.png",
    "maksa/l.png",
    "maksa/dug.png",
    "maksa/1.png",
    "maksa/2.png",
    "maksa/4.png",
    "maksa/5.png",
    "maksa/3.png",
    "maksa/7.png",
    "maksa/7.png",
    "maksa/6.png",
    "maksa/l.png",
    "maksa/dug.png",
    "maksa/l.png",
    "maksa/dug.png",
    "maksa/l.png"
]

current_index = 0

def change_pic():
    global current_index
    current_index += 1
    if current_index >= len(img_paths):
        current_index = 0
        
    path = img_paths[current_index]
    img = Image.open(path).resize((220, 220), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    
    canvas.itemconfig(image_id, image = photo)
    canvas.image = photo
    
    root.after(300, change_pic)
    
canvas = tk.Canvas(root, width=250, height=300, bg="#1e1f20", highlightthickness=0)
canvas.pack(pady=30)

image_id = canvas.create_image(125, 125, image=None)

font_title = ("Baufra", 24, "bold")
font_label = ("TeX Gyre Termes", 28, "bold")

isi = tk.Label(root, text="what do you think?...", font=font_label, bg="#f0f4ff")
isi.pack()

frame_buttons = tk.Frame(root, bg="#f0f4ff")
frame_buttons.pack(pady=10)

font_label = ("Quicksand", 18, "")

btn_resp =tk.Button(frame_buttons, text="🔐 thank you", font=font_label, bg="#7ac4f5", fg="black", command=thanks)
btn_resp.grid(row=0, column=0, padx=5)

btn_acc = tk.Button(frame_buttons, text="so do i 🩷", font=font_label, bg="#f16d6d", fg="black", command=coercion)
btn_acc.grid(row=0, column=1, padx=5)

btn_no =tk.Button(frame_buttons, text="💔 i am sorry", font=font_label, bg="#5c5959", fg="black", command=no)
btn_no.grid(row=0, column=2, padx=5)

text = tk.StringVar()
label = tk.Label(root, textvariable=text, wraplength=250, font=("Comic Sans MS", 18), justify="center", bg="#f0f4ff").pack(pady=(30, 18))

#message
letters = """
iy rkmumvellobc! drsc sc myxpocc ohkwzvo wocckqo
"""

#telegram bot
text_box = tk.Text(root, height=8, width=45, font=("C059", 12), wrap="word")
text_box.insert("1.0", letters)
text_box.config(state="disabled") 
text_box.pack(padx=20, pady=20)

button = tk.Button(root, text="💌 Copy message", font=("Quicksand", 14), bg="#ffd6e0", fg="#b0004b", command=copy_ke_clipboard)
button.pack()

tk.Button(root, text="translate it 💬", command=open_other).pack()

TELEGRAM_TOKEN = "YOUR TOKEN"
CHAT_ID = "YOUR CHAT ID"

def kirim_telegram(pesan):
    url = f"https://api.telegram.org/botXXXXXXXXXXXXXXXXXXXXXXX/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": pesan
    }
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("failed send notification:", e)

update_qts()

change_pic()

root.mainloop()


