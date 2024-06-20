import tkinter as tk
from tkinter import PhotoImage
from moviepy.editor import VideoFileClip
from PIL import Image, ImageTk
import numpy as np
import threading
import queue
import pygame

pygame.mixer.init()

# Load the audio sound
audio_sound = pygame.mixer.Sound(r"audio.mp3")

class VideoPlayerApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Amusement")
        self.setup_main_window()

    def setup_main_window(self):
        image_path = r"cover page.png"
        bg_image = PhotoImage(file=image_path)
        self.bg_width = bg_image.width()
        self.bg_height = bg_image.height()

        self.center_window(self.master, self.bg_width, self.bg_height)

        background_label = tk.Label(self.master, image=bg_image)
        background_label.image = bg_image
        background_label.place(relheight=1, relwidth=1)

        text_label = tk.Label(self.master, text='Welcome to AMUSEMENT park', font=('Helvetica', 48, 'bold italic'), bg="white")
        text_label.place(relx=0.5, rely=0.3, anchor='center')

        self.button = tk.Button(self.master, text="Click to enter!!", command=self.on_button_click, width=20, height=2, font=('Georgia', 16), bg='white', fg='black')
        self.button.place(relx=0.5, rely=0.5, anchor='center')

    def on_button_click(self):
        audio_sound.play()
        self.button.place_forget()

        self.video_path = "gate1.mp4"
        self.clip = VideoFileClip(self.video_path)
        self.frame_iter = self.clip.iter_frames()

        self.canvas = tk.Canvas(self.master, width=self.bg_width, height=self.bg_height)
        self.canvas.place(relx=0.5, rely=0.5, anchor='center')

        self.update_frame()

    def update_frame(self):
        try:
            frame = next(self.frame_iter)
            pil_image = Image.fromarray(np.uint8(frame))
            resized_frame = pil_image.resize((self.bg_width, self.bg_height))
            self.frame_image = ImageTk.PhotoImage(resized_frame)
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.frame_image)
            self.master.after(30, self.update_frame)
        except StopIteration:
            self.frame_iter = self.clip.iter_frames()
            self.master.after(0, self.display_switches)

    def display_switches(self):
        self.switch_window = tk.Toplevel(self.master)
        self.switch_window.title("Switches and Images")

        switch_window_width = self.bg_width
        switch_window_height = self.bg_height

        self.center_window(self.switch_window, switch_window_width, switch_window_height)

        self.switches = []
        self.image_labels = []
        self.frame_queues = {}

        def toggle_switch(switch_number):
            switch = self.switches[switch_number - 1]
            if switch['bg'] == 'red':
                switch.config(bg='green', text=f"Switch {switch_number} on")
                threading.Thread(target=self.play_video, args=(switch_number,)).start()
            else:
                switch.config(bg='red', text=f"Switch {switch_number} off")
                self.stop_video(switch_number)

        def turn_on_all_switches():
            for i in range(16):
                switch = self.switches[i]
                switch.config(bg='green', text=f"Switch {i + 1} on")
            threading.Thread(target=self.play_popup_video).start()

        def turn_off_all_switches():
            for i in range(16):
                switch = self.switches[i]
                switch.config(bg='red', text=f"Switch {i + 1} off")
            self.stop_single_video()

        frame = tk.Frame(self.switch_window)
        frame.pack()

        switch_frame = tk.Frame(frame, width=switch_window_width // 2, height=switch_window_height)
        switch_frame.pack(side="left", padx=10, pady=10)

        for i in range(4):
            for j in range(4):
                switch_number = i * 4 + j + 1
                switch = tk.Button(switch_frame, text=f"Switch {switch_number} off", bg="red", width=10, height=5, command=lambda num=switch_number: toggle_switch(num))
                switch.grid(row=i, column=j, padx=5, pady=5)
                self.switches.append(switch)

        turn_on_button = tk.Button(switch_frame, text="Turn ON All Switches", command=turn_on_all_switches)
        turn_on_button.grid(row=4, column=0, columnspan=2, pady=10)

        turn_off_button = tk.Button(switch_frame, text="Turn OFF All Switches", command=turn_off_all_switches)
        turn_off_button.grid(row=4, column=2, columnspan=2, pady=10)

        self.image_frame = tk.Frame(frame, width=switch_window_width // 2, height=switch_window_height)
        self.image_frame.pack(side="right", padx=10, pady=10)

        for i in range(4):
            for j in range(4):
                image_number = i * 4 + j + 1
                image_path = f"image_{image_number}.png"
                image = PhotoImage(file=image_path)
                label = tk.Label(self.image_frame, image=image)
                label.image = image
                label.grid(row=i, column=j, padx=5, pady=5)
                self.image_labels.append(label)

    def play_video(self, switch_number):
        video_path = f"video_{switch_number}.mp4"
        video_clip = VideoFileClip(video_path)
        frame_queue = queue.Queue()
        self.frame_queues[switch_number] = frame_queue
        threading.Thread(target=self.enqueue_frames, args=(video_clip, frame_queue)).start()
        self.show_video_popup(switch_number)

    def enqueue_frames(self, video_clip, frame_queue):
        for frame in video_clip.iter_frames():
            frame_queue.put(frame)
        frame_queue.put(None)

    def stop_video(self, switch_number):
        if switch_number in self.frame_queues:
            del self.frame_queues[switch_number]
        image_label = self.image_labels[switch_number - 1]
        image_path = f"image_{switch_number}.png"
        image = PhotoImage(file=image_path)
        image_label.config(image=image)
        image_label.image = image

    def show_video_popup(self, switch_number):
        self.popup_window = tk.Toplevel(self.switch_window)
        self.popup_window.title(f"Video_{switch_number}")
        self.center_window(self.popup_window, self.bg_width, self.bg_height)
        
        self.popup_canvas = tk.Canvas(self.popup_window, width=self.bg_width, height=self.bg_height)
        self.popup_canvas.pack()
        
        self.update_video_frame(switch_number)

        self.popup_window.after(2000, self.popup_window.destroy)  # Close after 2 seconds

    def update_video_frame(self, switch_number):
        if switch_number in self.frame_queues:
            frame_queue = self.frame_queues[switch_number]
            try:
                frame = frame_queue.get_nowait()
                if frame is None:
                    self.popup_window.destroy()
                    return
                pil_image = Image.fromarray(np.uint8(frame))
                resized_frame = pil_image.resize((self.bg_width, self.bg_height))
                frame_image = ImageTk.PhotoImage(resized_frame)
                if self.popup_canvas.winfo_exists():
                    self.popup_canvas.create_image(0, 0, anchor=tk.NW, image=frame_image)
                    self.popup_canvas.image = frame_image
                    self.popup_window.after(30, lambda: self.update_video_frame(switch_number))
            except queue.Empty:
                self.popup_window.after(30, lambda: self.update_video_frame(switch_number))
        else:
            self.popup_window.after(30, lambda: self.update_video_frame(switch_number))

    def play_popup_video(self):
        self.popup_window = tk.Toplevel(self.master)
        self.popup_window.title("Cover Page Video")
        self.center_window(self.popup_window, self.bg_width, self.bg_height)
        
        self.popup_canvas = tk.Canvas(self.popup_window, width=self.bg_width, height=self.bg_height)
        self.popup_canvas.pack()
        
        self.popup_clip = VideoFileClip("cover page.mp4")
        self.popup_frame_iter = self.popup_clip.iter_frames()
        self.update_popup_frame()

    def update_popup_frame(self):
        try:
            frame = next(self.popup_frame_iter)
            pil_image = Image.fromarray(np.uint8(frame))
            resized_frame = pil_image.resize((self.bg_width, self.bg_height))
            frame_image = ImageTk.PhotoImage(resized_frame)
            if self.popup_canvas.winfo_exists():
                self.popup_canvas.create_image(0, 0, anchor=tk.NW, image=frame_image)
                self.popup_canvas.image = frame_image
                self.popup_window.after(30, self.update_popup_frame)
        except StopIteration:
            self.popup_frame_iter = self.popup_clip.iter_frames()
            self.popup_window.after(0, self.popup_window.destroy)
            self.show_original_window()

    def show_original_window(self):
        self.switch_window.deiconify()  # Show the original switches and images grid window
        for switch in self.switches:
            switch.config(bg='green', text=switch.cget('text').replace('off', 'on'))

    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f'{width}x{height}+{x}+{y}')

if _name_ == "_main_":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
