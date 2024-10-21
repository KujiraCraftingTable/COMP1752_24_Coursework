import tkinter as tk

from main import Pet, Interaction, Game


confirm_click_count = 0
mode_click_count = 0
back_click_count = 0

def confirm_clicked():
    global confirm_click_count
    confirm_click_count += 1
    click_times("Confirm", confirm_click_count)

def mode_clicked():
    global mode_click_count
    mode_click_count += 1
    click_times("Mode", mode_click_count)
    
def back_clicked():
    global back_click_count
    back_click_count += 1
    click_times("Back", back_click_count)

def click_times(button_name, count):
    if count == 1:
        print(f"Clicked {button_name} Button ({count} time)")
    else:
        print(f"Clicked {button_name} Button ({count} times)")

#Window config
window = tk.Tk()
window.geometry("300x50")
window.title("Test App")

#Image config
background_image = tk.PhotoImage(file="path_to_your_image.png")
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1) 

#Button config
confirm_btn = tk.Button(window, text="Confirm", command=confirm_clicked)
confirm_btn.grid(column=0, row=0)

mode_btn = tk.Button(window, text="Mode", command=mode_clicked)
mode_btn.grid(column=1, row=0)

back_btn = tk.Button(window, text="Back", command=back_clicked)
back_btn.grid(column=2, row=0)


window.mainloop()