import tkinter as tk
from tkinter import messagebox

# --------- DATA ----------
rooms = {}

# --------- FUNCTIONS ----------
def add_room():
    r = room_no.get()
    t = room_type.get()
    if r == "" or t == "":
        messagebox.showerror("Error", "Please fill all fields")
        return
    rooms[r] = {"type": t, "booked": False, "customer": ""}
    messagebox.showinfo("Success", "Room Added Successfully")

def check_in():
    r = room_no.get()
    n = cust_name.get()
    if r in rooms and not rooms[r]["booked"]:
        rooms[r]["booked"] = True
        rooms[r]["customer"] = n
        messagebox.showinfo("Success", "Check-In Successful")
    else:
        messagebox.showerror("Error", "Room not available")

def check_out():
    r = room_no.get()
    if r in rooms and rooms[r]["booked"]:
        rooms[r]["booked"] = False
        rooms[r]["customer"] = ""
        messagebox.showinfo("Success", "Check-Out Successful")
    else:
        messagebox.showerror("Error", "Room already empty")

def view_rooms():
    text.delete("1.0", tk.END)
    for r in rooms:
        status = "Booked" if rooms[r]["booked"] else "Available"
        cust = rooms[r]["customer"] if rooms[r]["customer"] else "-"
        text.insert(tk.END, f"Room {r} | {rooms[r]['type']} | {status} | {cust}\n")

# --------- GUI ----------
root = tk.Tk()
root.title("Hotel Management System")
root.geometry("520x550")
root.config(bg="#f4f6f7")

# Header
tk.Label(
    root,
    text="HOTEL MANAGEMENT SYSTEM",
    font=("Arial", 18, "bold"),
    bg="#2c3e50",
    fg="white",
    pady=15
).pack(fill="x")

# Main Frame
frame = tk.Frame(root, bg="#f4f6f7")
frame.pack(pady=15)

def label(text):
    return tk.Label(frame, text=text, bg="#f4f6f7", font=("Arial", 11))

label("Room Number").grid(row=0, column=0, sticky="w", padx=10, pady=5)
room_no = tk.Entry(frame, width=25)
room_no.grid(row=0, column=1)

label("Room Type").grid(row=1, column=0, sticky="w", padx=10, pady=5)
room_type = tk.Entry(frame, width=25)
room_type.grid(row=1, column=1)

label("Customer Name").grid(row=2, column=0, sticky="w", padx=10, pady=5)
cust_name = tk.Entry(frame, width=25)
cust_name.grid(row=2, column=1)

# Buttons
btn_frame = tk.Frame(root, bg="#f4f6f7")
btn_frame.pack(pady=10)

def btn(text, cmd, color):
    return tk.Button(
        btn_frame,
        text=text,
        command=cmd,
        bg=color,
        fg="white",
        width=15,
        font=("Arial", 10, "bold")
    )

btn("Add Room", add_room, "#27ae60").grid(row=0, column=0, padx=5, pady=5)
btn("Check In", check_in, "#2980b9").grid(row=0, column=1, padx=5)
btn("Check Out", check_out, "#c0392b").grid(row=0, column=2, padx=5)
btn("View Rooms", view_rooms, "#8e44ad").grid(row=0, column=3, padx=5)

# Output Box
text = tk.Text(root, height=10, width=60, font=("Consolas", 10))
text.pack(pady=15)

root.mainloop()
