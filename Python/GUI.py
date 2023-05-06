import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1920x1080")
app.title("ENGG1100 GUI.py")


def drive_callback(value):
    if value > 1:
        text = "Forward: " + str(int(value))
    elif value < -1:
        text = "Reverse: " + str(int(value))
    else:
        text = "Neutral"
    drive_value.configure(text=int(value))
    output_console(text)

def pan_callback(value):
    if value > 1:
        text = "Right: " + str(int(value))
    elif value < -1:
        text = "Left: " + str(int(value))
    else:
        text = "Centre"
    pan_value.configure(text=int(value))
    output_console(text)

def tilt_callback(value):
    text = "Tilt: " + str(int(value))
    tilt_value.configure(text=int(value))
    output_console(text)

def output_console(text):
    result.delete(1.0, "end")
    result.insert("end", text)

# creating a frame
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=0, padx=0, fill="both", expand=True)

frame_2 = customtkinter.CTkFrame(master=frame_1, width=250, height=500)
frame_2.place(x=312.5, y=280, anchor="center")

frame_3 = customtkinter.CTkFrame(master=frame_1, width=550, height=500)
frame_3.place(x=755, y=280, anchor="center")

frame_4 = customtkinter.CTkFrame(master=frame_1, width=250, height=500)
frame_4.place(x=1215, y=280, anchor="center")

# creating a textbox (OUTPUT CONSOLE)
result = customtkinter.CTkTextbox(master=frame_1, width=550, height=250, font=customtkinter.CTkFont(size=25, weight="bold"))
result.place(x=755, y=750, anchor="center")

# creating an option menu (SELECT SERIAL)
serial = customtkinter.CTkOptionMenu(frame_1, values=["Option 1", "Option 2", "Option 3"])
serial.place(x=755, y=70, anchor="center")
serial.set("Select Serial")

# creating labels
drive_label = customtkinter.CTkLabel(master=frame_2, text="DRIVE", font=customtkinter.CTkFont(size=40, weight="bold"))
drive_label.place(x=125, y=380, anchor="center")

pan_label = customtkinter.CTkLabel(master=frame_3, text="PAN", font=customtkinter.CTkFont(size=40, weight="bold"))
pan_label.place(x=275, y=380, anchor="center")

tilt_label = customtkinter.CTkLabel(master=frame_4, text="TILT", font=customtkinter.CTkFont(size=40, weight="bold"))
tilt_label.place(x=125, y=380, anchor="center")

drive_speed_1 = customtkinter.CTkLabel(master=frame_2, text=" 100%", font=customtkinter.CTkFont(size=25, weight="bold"))
drive_speed_1.place(x=12, y=18)

drive_speed_2 = customtkinter.CTkLabel(master=frame_2, text="-100%", font=customtkinter.CTkFont(size=25, weight="bold"))
drive_speed_2.place(x=12, y=290)

pan_speed_1 = customtkinter.CTkLabel(master=frame_3, text="-90", font=customtkinter.CTkFont(size=25, weight="bold"))
pan_speed_1.place(x=115, y=120)

pan_speed_2 = customtkinter.CTkLabel(master=frame_3, text=" 90", font=customtkinter.CTkFont(size=25, weight="bold"))
pan_speed_2.place(x=385, y=120)

tilt_speed_1 = customtkinter.CTkLabel(master=frame_4, text=" 100%", font=customtkinter.CTkFont(size=25, weight="bold"))
tilt_speed_1.place(x=162, y=18)

tilt_speed_2 = customtkinter.CTkLabel(master=frame_4, text="   0%", font=customtkinter.CTkFont(size=25, weight="bold"))
tilt_speed_2.place(x=162, y=290)

# creating sliders
slider_1 = customtkinter.CTkSlider(master=frame_2, command=drive_callback, from_=-100, to=100, width=30, height=300, orientation="vertical")
slider_1.place(x=112.5, y=20)
slider_1.set(0)

slider_2 = customtkinter.CTkSlider(master=frame_3, command=pan_callback, from_=-90, to=90, width=300, height=30)
slider_2.place(x=125, y=165)
slider_2.set(0)

slider_3 = customtkinter.CTkSlider(master=frame_4, command=tilt_callback, from_=0, to=100, width=30, height=300, orientation="vertical")
slider_3.place(x=112.5, y=20)
slider_3.set(0)

# creating labels to show slider values
drive_value = customtkinter.CTkLabel(master=frame_2, text="0", font=customtkinter.CTkFont(size=25, weight="bold"))
drive_value.place(x=125, y=440, anchor="center")

pan_value = customtkinter.CTkLabel(master=frame_3, text="0", font=customtkinter.CTkFont(size=25, weight="bold"), justify="center")
pan_value.place(x=275, y=440, anchor="center")

tilt_value = customtkinter.CTkLabel(master=frame_4, text="0", font=customtkinter.CTkFont(size=25, weight="bold"))
tilt_value.place(x=125, y=440, anchor="center")


app.mainloop()
