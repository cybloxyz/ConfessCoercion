import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import PIL as pil
from PIL import Image, ImageTk
import random
import requests
import subprocess


root = tk.Tk()
root.title("💖 JADI GINI...")
root.geometry("700x900")
root.resizable(True, True)
root.configure(bg="#f0f4ff")

def keluar_total():
    root.destroy()  # Ini akan nutup root + semua Toplevel

# Cegah root ditutup dengan tombol ✕
def cegah_tutup_root():
    messagebox.showinfo("itu..", "gatau nih kenapa gamau keluar")

root.protocol("WM_DELETE_WINDOW", cegah_tutup_root)

def buka_projek_lain():
    subprocess.Popen(["python", "caesarcipher.py"])

def makasi():
    halaman = tk.Toplevel(root)
    halaman.title("makasih aja ya?..")
    halaman.geometry("700x900")

    label = tk.Label(halaman, text="iya..gapapa, sama-sama..", font=("Quicksand", 14))
    label.pack(pady=40)

    btn_kembali = tk.Button(halaman, text="makasih ya..", command=makasii)
    btn_kembali.pack()

def makasii():
    halaman = tk.Toplevel(root)
    halaman.title("makasih aja ya?..")
    halaman.geometry("700x900")

    label = tk.Label(halaman, text="kok masih disini?..", font=("Quicksand", 14))
    label.pack(pady=40)

    btn_kembali = tk.Button(halaman, text="ngga kok..", command=makasiii)
    btn_kembali.pack()

def makasiii():
    halaman = tk.Toplevel(root)
    halaman.title("makasih aja ya?..")
    halaman.geometry("700x900")

    label = tk.Label(halaman, text="gapapa kok, lanjut aja", font=("Quicksand", 14))
    label.pack(pady=40)

    btn_kembali = tk.Button(halaman, text="makasih ya..", command=makasi)
    btn_kembali.pack()

def sama():
    halaman = tk.Toplevel(root)
    halaman.title(" ")
    halaman.geometry("700x900")

    img_lop = [
        "maksa/a.png",
        "maksa/b.png",
        "maksa/c.png",
        "maksa/d.png",
        "maksa/e.png",
        "maksa/f.png",
        "maksa/g.png",
        "maksa/f.png",
        "maksa/e.png",
        "maksa/d.png",
        "maksa/c.png",
        "maksa/b.png",
        "maksa/a.png"
    ]

    label = tk.Label(halaman, text="I GOT YOU AOWKAKKSAKSKA 🩷 ", font=("Quicksand", 14))
    label.pack(pady=40)

    btn_kembali = tk.Button(halaman, text="🩷🩷🩷", command=keluar_total)
    btn_kembali.pack()

    current_indeks = [0]

    def lop():
        current_indeks[0] += 1
        if current_indeks[0] >= len(img_lop):
           current_indeks[0] = 0

        pat = img_lop[current_indeks[0]]
        imgg = Image.open(pat).resize((220, 480), Image.Resampling.LANCZOS)
        photos = ImageTk.PhotoImage(imgg)

        # Update gambar di canvas
        canvas.itemconfig(image_id, image=photos)
        canvas.image = photos  # simpan referensinya supaya tidak kehapus

        # Panggil lagi fungsi ini setelah 2000 ms (2 detik)
        root.after(100, lop)
    
    # Buat canvas
    canvas = tk.Canvas(halaman, width=250, height=520, bg="#ffbbe8", highlightthickness=0)
    canvas.pack(pady=75)

    # Tempatkan gambar awal kosong
    image_id = canvas.create_image(125, 260, image=None)

    lop()

def paksa():
    kirim_telegram("yeee disukain balikk(eh emang pakai hati?)")
    sama()

def ga():
    halaman = tk.Toplevel(root)
    halaman.title("ngga ya..")
    halaman.geometry("700x900")

    label = tk.Label(halaman, text="iya gapapa kok", font=("Quicksand", 14))
    label.pack(pady=40)

    btn_kembali = tk.Button(halaman, text="iya..", command=gaa)
    btn_kembali.pack()

def gaa():
    halaman = tk.Toplevel(root)
    halaman.title("ngga ya..")
    halaman.geometry("700x900")

    label = tk.Label(halaman, text="seriuss, gapapa kok", font=("Quicksand", 14))
    label.pack(pady=40)

    btn_kembali = tk.Button(halaman, text="iya...", command=gaaa)
    btn_kembali.pack()

def gaaa():
    halaman = tk.Toplevel(root)
    halaman.title("ngga ya..")
    halaman.geometry("700x900")

    label = tk.Label(halaman, text="iyaa...seriuss, gapapa kok..", font=("Quicksand", 14))
    label.pack(pady=40)

    btn_kembali = tk.Button(halaman, text="iya....", command=ga)
    btn_kembali.pack()

qts = [
    "you know right, feel free to be honest..",
    "take your time, i'll wait",
    "you are cool, as always",
    "i'll never regret for choosing you",
    "you have no idea how i admire you"
]

def update_qts():
    teks.set(random.choice(qts))

# Daftar gambar
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

def ganti_gambar():
    global current_index
    current_index += 1
    if current_index >= len(img_paths):
       current_index = 0

    path = img_paths[current_index]
    img = Image.open(path).resize((220, 220), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)

    # Update gambar di canvas
    canvas.itemconfig(image_id, image=photo)
    canvas.image = photo  # simpan referensinya supaya tidak kehapus

    # Panggil lagi fungsi ini setelah 2000 ms (2 detik)
    root.after(300, ganti_gambar)

# Buat canvas
canvas = tk.Canvas(root, width=250, height=300, bg="#1e1f20", highlightthickness=0)
canvas.pack(pady=30)

# Tempatkan gambar awal kosong
image_id = canvas.create_image(125, 125, image=None)

font_title = ("Baufra", 24, "bold")
font_label = ("TeX Gyre Termes", 28, "bold")

isi = tk.Label(root, text="kalau menurut kamu gimana?...", font=font_label, bg="#f0f4ff").pack()

frame_buttons = tk.Frame(root, bg="#f0f4ff")
frame_buttons.pack(pady=10)

font_label = ("Quicksand", 18, "")

btn_respect = tk.Button(frame_buttons, text="🔐 makasii", font=font_label, bg="#7ac4f5", fg="black", command=makasi)
btn_respect.grid(row=0, column=0, padx=5)

btn_terima = tk.Button(frame_buttons, text="🩷 sama dong!", font=font_label, bg="#f16d6d", fg="black", command=paksa)
btn_terima.grid(row=0, column=1, padx=5)

btn_g = tk.Button(frame_buttons, text="💔 sorry ya..", font=font_label, bg="#5c5959", fg="black", command=ga)
btn_g.grid(row=0, column=2, padx=5)

teks = tk.StringVar()
label = tk.Label(root, textvariable=teks, wraplength=250, font=("Comic Sans MS", 18), justify="center", bg = "#f0f4ff").pack(pady=(30, 18))

# Pesan yang bisa di-copy
pesan = """
edit pesan kamu disini
"""

text_box = tk.Text(root, height=8, width=45, font=("C059", 12), wrap="word")
text_box.insert("1.0", pesan)
text_box.config(state="disabled")  # 🔒 kunci teks
text_box.pack(padx=20, pady=20)

def copy_ke_clipboard():
    root.clipboard_clear()
    root.clipboard_append(pesan)
    root.update()  # biar clipboard keisi

button = tk.Button(root, text="💌 Copy Pesan", font=("Quicksand", 14), bg="#ffd6e0", fg="#b0004b", command=copy_ke_clipboard)
button.pack()

tk.Button(root, text="terjemahin 💬", command=buka_projek_lain).pack()


TELEGRAM_TOKEN = "token API chatbot dari telegram"
CHAT_ID = "id telegram kamu"

def kirim_telegram(pesan):
    url = f"https://api.telegram.org/bot<token API chatbot>/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": pesan
    }
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Gagal kirim notif Telegram:", e)

update_qts()

ganti_gambar()

root.mainloop()

