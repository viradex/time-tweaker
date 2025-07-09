import os
import time
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

def browse():
    path = filedialog.askopenfilename() or filedialog.askdirectory()
    if path:
        path_var.set(path)

def apply_time():
    path = path_var.get().strip()
    date_str = date_var.get().strip()
    time_str = time_var.get().strip()

    if not Path(path).exists():
        messagebox.showerror("Error", "File or folder does not exist.")
        return

    try:
        month, day, year = [int(x) for x in date_str.split("/")]
        hour, minute = [int(x) for x in time_str.split(":")]
        dt = datetime(year, month, day, hour, minute, 0)
        final = time.mktime(dt.timetuple())
        os.utime(path, (final, final))
        messagebox.showinfo("Success", f"Time successfully updated for:\n{path}")
    except OverflowError:
        messagebox.showerror("Error", "Date is out of range! Must be after 01/01/1970.")
    except ValueError:
        messagebox.showerror("Error", "Invalid date/time format or value.")

# --- UI Setup ---
root = tk.Tk()
root.title("Time Tweaker")
root.geometry("420x300")
root.resizable(False, False)

root.iconbitmap("./assets/app.ico")

tk.Label(root, text="TIME TWEAKER", font=("Arial", 16, "bold")).pack(pady=(10, 5))
tk.Label(root, text="Update file/folder modification time").pack(pady=(0, 10))

path_var = tk.StringVar()
date_var = tk.StringVar()
time_var = tk.StringVar()

tk.Label(root, text="File or Folder Path:").pack(anchor="w", padx=15)
tk.Entry(root, textvariable=path_var, width=50).pack(padx=15)
tk.Button(root, text="Browse", command=browse).pack(pady=5)

tk.Label(root, text="Date (MM/DD/YYYY):").pack(anchor="w", padx=15, pady=(10, 0))
tk.Entry(root, textvariable=date_var, width=25).pack(padx=15)

tk.Label(root, text="Time (HH:MM, 24-hour):").pack(anchor="w", padx=15, pady=(10, 0))
tk.Entry(root, textvariable=time_var, width=25).pack(padx=15)

tk.Button(root, text="Apply Time", command=apply_time, bg="#4CAF50", fg="white").pack(pady=10)

root.mainloop()
