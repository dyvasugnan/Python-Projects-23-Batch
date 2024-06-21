import tkinter as tk
from tkinter import messagebox
import math
from moviepy.editor import VideoFileClip
import pygame
from PIL import Image, ImageTk


#paths
TITLE_PAGE_VIDEO = "C:\\Users\\Yennati\\Downloads\\TITLE_PAGE.mp4"
INSTRUCTION_PAGE_VIDEO = "C:\\Users\\Yennati\\Downloads\\ins video.mp4"
GRID_BACKGROUND = "C:\\Users\\Yennati\\Downloads\\grig_background.jpg"

#initialisations
noof_mums = 0
mumsCo_ord = []
playerCo_ord = [0,0]
reach = 5
prev = 0
steps = 0

#sound effcts
pygame.init()
pygame.mixer.init()
# Load the sound file
instruction_music = pygame.mixer.Sound("C:\\Users\\Yennati\\Downloads\\instruction_music.mp3")
frontpage_music = pygame.mixer.Sound("C:\\Users\\Yennati\\Downloads\\frontpage_music.mp3")

#front page video
def front_page():
    frontpage_music.play()
    # Path to the video file
    video_path = TITLE_PAGE_VIDEO
    # Load the video clip
    video_clip = VideoFileClip(video_path)
    # Play the video clip
    video_clip.preview()
    # Close the video clip preview window
    video_clip.close()
    instruction_page()

def instruction_page():
    # Path to the video file
    video_path = INSTRUCTION_PAGE_VIDEO
    # Load the video clip
    video_clip = VideoFileClip(video_path)
    # Play the video clip
    video_clip.preview()
    # Close the video clip preview window
    frontpage_music.stop()
    video_clip.close()
    instruction_music.play()

front_page()


def DisplayGameOver(steps, reach):
    root = tk.Tk()
    root.attributes('-fullscreen', True)

    label = tk.Label(root, text="Game Over!", font=("Helvetica", 60),bg= 'white')
    label.pack(expand=True)
    root.configure(bg='white')
    if reach != -1:
        steps_label = tk.Label(root, text="Steps taken: {}".format(steps), font=("Helvetica", 50),bg= 'white')
        steps_label.pack(expand=True)
    else:
        steps_label = tk.Label(root, text="Player can never be caught!!", font=("Helvetica", 50),bg= 'white')
        steps_label.pack(expand=True)

    # Create and add the exit button
    exit_button = tk.Button(root, text="Exit", command=root.destroy, width=5, height=1, font=("Helvetica", 50),bg= 'white')
    exit_button.pack(pady=30)
    root.mainloop()

def minCo_ord_to_player(playerCo_ord, mumsCo_ord):
    distances = []
    min_dist = float('inf')
    min_index = 0
    for mummy_position in range(0, len(mumsCo_ord)):
        distance = euclidean_distance(playerCo_ord[0], playerCo_ord[1], mumsCo_ord[mummy_position][0],mumsCo_ord[mummy_position][1])
        distances.append(distance)
        if min_dist > distance:
            min_dist = distance
            min_index = mummy_position
    return mumsCo_ord[min_index], distances


def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))


def PlayerMove(min_mumsCo_ord, playerCo_ord):
    mums_xCo_ord, mums_yCo_ord = min_mumsCo_ord[0], min_mumsCo_ord[1]
    player_xCo_ord, player_yCo_ord = playerCo_ord[0], playerCo_ord[1]
    if player_xCo_ord > mums_xCo_ord:
        player_xCo_ord += 1
    if player_yCo_ord > mums_yCo_ord:
        player_yCo_ord += 1
    if player_xCo_ord < mums_xCo_ord:
        player_xCo_ord -= 1
    if player_yCo_ord < mums_yCo_ord:
        player_yCo_ord -= 1
    playerCo_ord = [player_xCo_ord, player_yCo_ord]
    return playerCo_ord


def MummyMove(mumsCo_ord, playerCo_ord):
    for mummy_pos in range(0, len(mumsCo_ord)):
        mummy_xCo_ord, mummy_yCo_ord = mumsCo_ord[mummy_pos][0], mumsCo_ord[mummy_pos][1]
        player_xCo_ord, player_yCo_ord = playerCo_ord[0], playerCo_ord[1]
        if mummy_xCo_ord < player_xCo_ord:
            mummy_xCo_ord += 1
        if mummy_yCo_ord < player_yCo_ord:
            mummy_yCo_ord += 1
        if mummy_xCo_ord > player_xCo_ord:
            mummy_xCo_ord -= 1
        if mummy_yCo_ord > player_yCo_ord:
            mummy_yCo_ord -= 1
        mumsCo_ord[mummy_pos] = [mummy_xCo_ord, mummy_yCo_ord]
    return mumsCo_ord

def AverageDistances(distances):
    return sum(distances) / len(distances)


def NeverCondition(reach, prev, current):
    if current >= prev:
        reach -= 1
    return reach

def update_positions():
    global mumsCo_ord
    global playerCo_ord
    global reach
    global prev
    global steps
    width = root.winfo_width()
    height = root.winfo_height()

    cell_width = width / 16
    cell_height = height / 16

    origin_x = width / 2
    origin_y = height / 2

    if (playerCo_ord not in mumsCo_ord) or reach != 0:
        steps += 1
        min_mumsCo_ord, distances = minCo_ord_to_player(playerCo_ord, mumsCo_ord)
        current = AverageDistances(distances)
        reach = NeverCondition(reach, prev, current)
        prev = current
        playerCo_ord = PlayerMove(min_mumsCo_ord, playerCo_ord)
        MummyMove(mumsCo_ord, playerCo_ord)

    canvas.delete("player")
    player_x = origin_x + playerCo_ord[0] * cell_width
    player_y = origin_y - playerCo_ord[1] * cell_height
    canvas.create_image(player_x, player_y, anchor='center', image=player_img, tags="player")

    canvas.delete("mummy")
    for x, y in mumsCo_ord:
        mummy_x = origin_x + x * cell_width
        mummy_y = origin_y - y * cell_height
        canvas.create_image(mummy_x, mummy_y, anchor='center', image=mummy_img, tags="mummy")
        if (mummy_x == player_x and mummy_y == player_y) or reach == -1:
            root.destroy()
            DisplayGameOver(steps, reach)
    root.after(3000, update_positions)
def create_grid(event=None):
    global prev
    global reach
    global steps
    width = root.winfo_width()
    height = root.winfo_height()

    canvas.delete("grid_line")
    canvas.delete("origin_point")
    canvas.delete("player")
    canvas.delete("mummy")
    canvas.delete("background")

    resized_bg = bg_image.resize((width, height), Image.NEAREST)
    bg_img = ImageTk.PhotoImage(resized_bg)

    background = canvas.create_image(0, 0, anchor='nw', image=bg_img, tags="background")
    canvas.tag_lower(background)

    cell_width = width / 16
    cell_height = height / 16

    player_size = min(cell_width, cell_height) / 2 * 0.8
    mummy_size = min(cell_width, cell_height) / 2 * 0.8

    for i in range(1, 16):
        x = i * cell_width
        canvas.create_line(x, 0, x, height, tags="grid_line")

    for i in range(1, 16):
        y = i * cell_height
        canvas.create_line(0, y, width, y, tags="grid_line")

    origin_x = width / 2
    origin_y = height / 2
    canvas.create_oval(origin_x - 2, origin_y - 2, origin_x + 2, origin_y + 2, fill="red", tags="origin_point")

    canvas.create_image(origin_x, origin_y, anchor='center', image=player_img, tags="player")

    for x, y in mumsCo_ord:
        mummy_x = origin_x + x * cell_width
        mummy_y = origin_y - y * cell_height
        canvas.create_image(mummy_x, mummy_y, anchor='center', image=mummy_img, tags="mummy")
    canvas.bg_img = bg_img

def get_mummy_input():
    instruction_music.stop()
    global noof_mums
    input_window = tk.Toplevel(root)
    input_window.attributes('-fullscreen', True)
    input_window.title("Input Mummy Coordinates")

    # Set background image for input window
    width = input_window.winfo_screenwidth()
    height = input_window.winfo_screenheight()
    resized_bg = bg_image.resize((width, height), Image.NEAREST)
    bg_img = ImageTk.PhotoImage(resized_bg)

    canvas = tk.Canvas(input_window, width=width, height=height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor='nw', image=bg_img)

    label = tk.Label(canvas, text="Enter number of mummies:", font=("Arial", 24), bg='white')
    label_window = canvas.create_window(width / 2, height / 4, window=label)

    num_mummies_var = tk.StringVar()
    num_mummies_entry = tk.Entry(canvas, textvariable=num_mummies_var, font=("Arial", 24), bg='white')
    entry_window = canvas.create_window(width / 2, height / 3, window=num_mummies_entry)

    def on_confirm_num_mummies():
        try:
            noof_mums = int(num_mummies_var.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for the number of mummies.")
            return

        input_window.destroy()
        get_coordinates(noof_mums)

    confirm_button = tk.Button(canvas, text="Next", command=on_confirm_num_mummies, font=("Arial", 24), bg='white')
    button_window = canvas.create_window(width / 2, height / 2.5, window=confirm_button)

    canvas.bg_img = bg_img

def get_coordinates(noof_mums):
    global mumsCo_ord

    coord_window = tk.Toplevel(root)
    coord_window.attributes('-fullscreen', True)
    coord_window.title("Input Mummy Coordinates")

    width = coord_window.winfo_screenwidth()
    height = coord_window.winfo_screenheight()
    resized_bg = bg_image.resize((width, height), Image.NEAREST)
    bg_img = ImageTk.PhotoImage(resized_bg)

    canvas = tk.Canvas(coord_window, width=width, height=height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor='nw', image=bg_img)

    label = tk.Label(canvas, text=f"Enter coordinates for {noof_mums} mummies:", font=("Arial", 24), bg='white')
    label_window = canvas.create_window(width / 2, height / 20, window=label)

    coords_entries = []
    for i in range(noof_mums):
        frame = tk.Frame(canvas, bg='white')
        frame_window = canvas.create_window(width / 2, height / 10 + i * 40, window=frame)
        tk.Label(frame, text=f"Mummy {i + 1}:", font=("Arial", 18), bg='white').pack(side="left")
        coord_var = tk.StringVar()
        coord_entry = tk.Entry(frame, textvariable=coord_var, font=("Arial", 18), bg='white')
        coord_entry.pack(side="left")
        coords_entries.append(coord_var)

    def update_grid():
        global mumsCo_ord
        mumsCo_ord = []
        for i, coord_var in enumerate(coords_entries):
            try:
                x, y = map(int, coord_var.get().split(','))
                mumsCo_ord.append((x, y))
            except ValueError:
                messagebox.showerror("Error", f"Invalid input for mummy {i + 1}. Please enter coordinates as x, y.")
                return
        create_grid()
        coord_window.destroy()
        update_positions()


    confirm_button = tk.Button(canvas, text="Confirm", command=update_grid, font=("Arial", 24), bg='white')
    button_window = canvas.create_window(width / 2, height - 100, window=confirm_button)

    canvas.bg_img = bg_img

noof_mums = 0
mumsCo_ord = []

root = tk.Tk()
root.title("Coordinate Grid")
root.attributes('-fullscreen', True)

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

bg_image = Image.open("C:\\Users\\Yennati\\Downloads\\grig_background.jpg")
player_img = ImageTk.PhotoImage(Image.open("C:\\Users\\Yennati\\Downloads\\player_icon.jpg").resize((70,70)))
mummy_img = ImageTk.PhotoImage(Image.open("C:\\Users\\Yennati\\Downloads\\mummy_icon1.jpg").resize((70,70)))

canvas.bind("<Configure>", create_grid)

input_button = tk.Button(root, text="Set Mummies", command=get_mummy_input)
input_button.pack()

root.mainloop()
