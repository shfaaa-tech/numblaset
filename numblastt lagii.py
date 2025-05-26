# NumBlast/
# ├── numblastt lagii.py
# ├── assets/
# │   ├── awal.jpg
# │   ├── loading.jpg
# │   ├── choose player.jpg
# │   └── loading otw ke game.jpg
# |   └── awalan game.jpg
# |   └── 6.jpg
# |   └── 7.jpg
# |   └── 8.jpg
# |   └── 9.jpg
# |   └── 10.jpg
# └── README.md

import tkinter as tk
from PIL import Image, ImageTk
import os
import random

class NumBlastApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NumBlast!")
        self.geometry("1280x720")
        self.resizable(False, False)
        self.configure(bg="#ffcde1")
        self.current_frame = None
        self.assets_path = os.path.join(os.getcwd(), "assets")
        self.num_players = None
        self.switch_frame(IntroScreen)

    def switch_frame(self, frame_class):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.pack(fill="both", expand=True)

class IntroScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#ffcde1")
        img_path = os.path.join(master.assets_path, "awal.jpg")
        try: 
            img = Image.open(img_path)
            img = img.resize((1280, 720))
            self.photo_img = ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Gagal memuat gambar {img_path}: {e}")
            return

        canvas = tk.Canvas(self, width=1280, height=720)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_img)

        self.after(3000, lambda: master.switch_frame(LoadingScreen))
    def change_bg_image(self, filename):
        try:
            img_path = os.path.join(self.master.assets_path, filename)
            print("Mencoba buka gambar:", img_path)
            img = Image.open(img_path)
            img = img.resize((480, 320))
            self.photo_img = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_img)
            print("Berhasil ubah gambar latar.")
        except Exception as e:
            print(f"Gagal mengubah gambar latar: {e}")

class LoadingScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#bce8f1")
        img_path = os.path.join(master.assets_path, "loading.jpg")
        try: 
            img = Image.open(img_path)
            img = img.resize((1280, 720))
            self.photo_img = ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Gagal memuat gambar {img_path}: {e}")
            return
    
        canvas = tk.Canvas(self, width=1280, height=720)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_img)

        self.after(3000, lambda: master.switch_frame(PlayerSelectScreen))

class PlayerSelectScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width=1280, height=720, bg="#fdcfe0")
        self.master = master
        self.pack_propagate(False)
        img_path = os.path.join(master.assets_path, "choose player.jpg")
        print("Cek gambar:", img_path)
        
        try: 
            img = Image.open(img_path)
            img = img.resize((1280, 720), Image.Resampling.LANCZOS)
            self.photo_img = ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Gagal memuat gambar {img_path}: {e}")
            return
        
        self.canvas = tk.Canvas(self, width=1280, height=720, highlightthickness=0)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_img)

        tombol_info = {
            2: (260, 480, 360, 580),
            3: (460, 480, 560, 580),
            4: (660, 480, 760, 580),
            5: (860, 480, 960, 580),
        }

        for num, (x1, y1, x2, y2) in tombol_info.items():
            area = self.canvas.create_rectangle(x1, y1, x2, y2, outline="", fill="")
            self.canvas.tag_bind(area, "<Button-1>", lambda e, n=num: self.select_players(n))

        self.bg_label = tk.Label(self, image=self.photo_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label.lower()

        tombol_info = [(2, 320, 500, 90, 100), (3, 480, 500, 90, 100), (4, 645, 500, 90, 100), (5, 810, 500, 90, 100)]

    def select_players(self,num):
        self.master.num_players = num
        print(f"Jumlah pemain yang dipilih: {num}")
        self.master.switch_frame(PlayLoadingScreen)

class PlayLoadingScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width=1280, height=720, bg="#bce8f1")
        self.master = master
        self.pack_propagate(False)

        img_path = os.path.join(master.assets_path, "loading otw ke game.jpg")
        print("Cek gambar:", img_path)

        try:
            img = Image.open(img_path)
            img = img.resize((1280, 720), Image.Resampling.LANCZOS)
            self.photo_img = ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Gagal memuat gambar {img_path}: {e}")
            return
        
        canvas = tk.Canvas(self, width=1280, height=720, highlightthickness=0)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_img)

        self.play_area = canvas.create_rectangle(520, 395, 760, 445, outline="", fill="")
        canvas.tag_bind(self.play_area, "<Button-1>", lambda event: self.lets_play())
       
    def lets_play(self):
        print("Let's Play diklik!")
        self.master.switch_frame(GameAwalPlayScreen)

        canvas = tk.Canvas(self, width=1280, height=720)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_img)
    
        transparent_btn = tk.Button(self, text="Start", bg="#89CFF0", fg="white", font=("Helvetica", 14, "bold"), command=lambda: self.master.switch_frame(GameAwalPlayScreen))
        transparent_btn.place(x=530, y=610, width=220, height=60)

class GameAwalPlayScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(width=1280, height=720)
        self.pack_propagate(False)
        self.show_background("awalan game.jpg")

        self.canvas = tk.Canvas(self, width=1280, height=720, highlightthickness=0)
        self.canvas.pack()

        self.show_background("awalan game.jpg")

        self.next_area = self.canvas.create_rectangle(1035, 500, 1180, 600, outline="", fill="")
        self.canvas.tag_bind(self.next_area, "<Button-1>", lambda event: master.switch_frame(GameplayScreen))

        self.exit_area = self.canvas.create_rectangle(1035, 600, 1180, 700, outline="", fill="")
        self.canvas.tag_bind(self.exit_area, "<Button-1>", lambda event: master.quit)

    def show_background(self, filename):
        try:
            path = os.path.join(self.master.assets_path, filename)
            img = Image.open(path).resize((1280, 720), Image.Resampling.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)
        except Exception as e:
            print(f"[ERROR] Gagal memuat gambar '{filename}': {e}")

class GameplayScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width=1280, height=720)
        self.master = master
        self.pack_propagate(False)
        self.pack(fill="both", expand=False)

        self.canvas = tk.Canvas(self, width=1280, height=720, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.bg_image = None
        self.bg_image_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=None)

        self.input_entry = tk.Entry(self, font=("Helvetica", 24), justify="center", bg="#66c536", fg="#000")
        self.entry_window = self.canvas.create_window(640, 430, window=self.input_entry, width=300, height=55)

        self.submit_button = self.canvas.create_rectangle(580, 510, 700, 560, outline="", fill="")
        self.exit_button = self.canvas.create_rectangle(1080, 510, 1200, 560, outline="", fill="")

        self.canvas.tag_bind(self.submit_button, "<Button-1>", lambda e: self.tebak())
        self.canvas.tag_bind(self.exit_button, "<Button-1>", lambda e: self.master.destroy())

        self.angka_boom = random.randint(1, 100)
        self.batas_bawah = 1
        self.batas_atas = 100
        self.jumlah_pemain = master.num_players
        self.pemain_aktif = 1

        self.info_text = self.canvas.create_text(640, 100, text="", font=("Helvetica", 20), fill="white")
        self.update_info_text()

        self.show_background("6.jpg")

    def show_background(self, filename):
        try:
            path = os.path.join(self.master.assets_path, filename)
            img = Image.open(path).resize((1280, 720), Image.Resampling.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(img)
            self.canvas.itemconfig(self.bg_image_id, image=self.bg_image)
        except Exception as e:
            print(f"[ERROR] Tidak bisa load gambar '{filename}': {e}")

    def update_info_text(self):
        self.canvas.itemconfig(self.info_text, text=f"Giliran Pemain {self.pemain_aktif} | Tebak angka antara {self.batas_bawah} - {self.batas_atas}")

    def tebak(self):
        tebakan_str = self.input_entry.get()
        self.input_entry.config(state="disabled")
        self.canvas.itemconfigure(self.entry_window, state='hidden')
        self.canvas.itemconfigure(self.submit_button, state='hidden')
        self.canvas.itemconfigure(self.exit_button, state='hidden')

        if not tebakan_str.isdigit():
            self.show_background("9.jpg")
            self.after(2000, self.next_turn)
            return

        tebakan = int(tebakan_str)

        if tebakan < self.batas_bawah or tebakan > self.batas_atas:
            self.show_background("9.jpg")
            self.after(2000, self.next_turn)
            return

        if tebakan == self.angka_boom:
            self.show_background("10.jpg")
            self.after(3000, lambda: self.master.switch_frame(PlayerSelectScreen))
            return
        elif tebakan < self.angka_boom:
            self.batas_bawah = tebakan + 1
            self.show_background("8.jpg")
        else:
            self.batas_atas = tebakan - 1
            self.show_background("7.jpg")

        self.after(2000, self.next_turn)

    def next_turn(self):
        self.pemain_aktif = (self.pemain_aktif % self.jumlah_pemain) + 1
        self.input_entry.delete(0, tk.END)
        self.input_entry.config(state="normal")
        self.canvas.itemconfigure(self.entry_window, state='normal')
        self.canvas.itemconfigure(self.submit_button, state='normal')
        self.canvas.itemconfigure(self.exit_button, state='normal')
        self.update_info_text()
        self.show_background("6.jpg")

if __name__ == '__main__':
    app = NumBlastApp()
    app.mainloop()
