import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1920x1080")
app.title("ENGG1100 GUI.py")

def drive_callback(value):
    print(int(value))
    drive_value.configure(text=int(value))

def pan_callback(value):
    print(int(value))
    pan_value.configure(text=int(value))

def tilt_callback(value):
    print(int(value))
    tilt_value.configure(text=int(value))

# creating a frame
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=0, padx=0, fill="both", expand=True)

# creating labels
drive_label = customtkinter.CTkLabel(master=frame_1, text="DRIVE", font=('Arial', 40))
drive_label.pack(pady=10, padx=10)
drive_label.place(x=255, y=400)

pan_label = customtkinter.CTkLabel(master=frame_1, text="PAN", font=('Arial', 40))
pan_label.pack(pady=10, padx=10)
pan_label.place(x=715, y=400)

tilt_label = customtkinter.CTkLabel(master=frame_1, text="TILT", font=('Arial', 40))
tilt_label.pack(pady=10, padx=10)
tilt_label.place(x=1175, y=400)

drive_speed_1 = customtkinter.CTkLabel(master=frame_1, text=" 100%", font=('Arial', 25))
drive_speed_1.pack(pady=10, padx=10)
drive_speed_1.place(x=200, y=50)

drive_speed_2 = customtkinter.CTkLabel(master=frame_1, text="-100%", font=('Arial', 25))
drive_speed_2.pack(pady=10, padx=10)
drive_speed_2.place(x=200, y=320)

pan_speed_1 = customtkinter.CTkLabel(master=frame_1, text=" 90", font=('Arial', 25))
pan_speed_1.pack(pady=10, padx=10)
pan_speed_1.place(x=570, y=150)

pan_speed_2 = customtkinter.CTkLabel(master=frame_1, text="-90", font=('Arial', 25))
pan_speed_2.pack(pady=10, padx=10)
pan_speed_2.place(x=870, y=150)

tilt_speed_1 = customtkinter.CTkLabel(master=frame_1, text=" 100%", font=('Arial', 25))
tilt_speed_1.pack(pady=10, padx=10)
tilt_speed_1.place(x=1250, y=50)

tilt_speed_2 = customtkinter.CTkLabel(master=frame_1, text="   0%", font=('Arial', 25))
tilt_speed_2.pack(pady=10, padx=10)
tilt_speed_2.place(x=1250, y=320)

# creating sliders
slider_1 = customtkinter.CTkSlider(master=frame_1, command=drive_callback, from_=-100, to=100, width=30, height=300, orientation="vertical")
slider_1.pack(padx=0, pady=20)
slider_1.place(x=300, y=50)
slider_1.set(0)

slider_2 = customtkinter.CTkSlider(master=frame_1, command=pan_callback, from_=-90, to=90, width=300, height=30)
slider_2.pack(padx=0, pady=20)
slider_2.place(x=600, y=190)
slider_2.set(0)

slider_3 = customtkinter.CTkSlider(master=frame_1, command=tilt_callback, from_=0, to=100, width=30, height=300, orientation="vertical")
slider_3.pack(padx=0, pady=20)
slider_3.place(x=1200, y=50)
slider_3.set(0)

# creating labels to show slider values

drive_value = customtkinter.CTkLabel(master=frame_1, text="0", font=customtkinter.CTkFont(size=25, weight="bold"))
drive_value.pack(pady=10, padx=10)
drive_value.place(x=300, y=470)

pan_value = customtkinter.CTkLabel(master=frame_1, text="0", font=customtkinter.CTkFont(size=25, weight="bold"))
pan_value.pack(pady=10, padx=10)
pan_value.place(x=740, y=470)

tilt_value = customtkinter.CTkLabel(master=frame_1, text="0", font=customtkinter.CTkFont(size=25, weight="bold"))
tilt_value.pack(pady=10, padx=10)
tilt_value.place(x=1200, y=470)


app.mainloop()
