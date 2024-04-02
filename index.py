import pygetwindow as gw
import time
import win32gui
import win32con
import win32api

import mouse
import keyboard

class AltSwitcherV3():
    target_window_name = "Roblox"
    hotkey = "ctrl"
    keybinds = ['e', 'q', 'a', 's', 'd', 'z', 'c', 't', 'y', 'g', 'h', 'u', 'j', 'i', 'k', 'o', 'l',]

    windows = []

    def __init__(self):
        # Get all windows with the target name
        self.windows = self.get_windows_by_name(self.target_window_name)
        self.windows = [window for window in self.windows if window.title.strip().lower() == self.target_window_name.lower()]

        # Sorting windows
        main_window = self.windows.pop(0)
        self.windows.reverse()
        self.windows.insert(0, main_window)

        accounts_number = len(self.windows)
        print(f"{accounts_number} Roblox accounts have been discovered")
        if accounts_number > len(self.keybinds):
            print(f"Unfortunately AltSwitcherV3 only supports keybinds for up to {len(self.keybinds)} accounts! Please contact me so that I can add more :D (Your computer is a beast btw)")
            print("Please close some of your alts and then re-run this program (otherwise it'll probably throw an error at some point)")
        else:
            print("You may use the following keybinds (in order) to quickly switch between your accounts:")
            output_string = ''

            for x in range(accounts_number):
                output_string += self.keybinds[x].capitalize()
                if x < accounts_number - 1:
                    output_string += ', '

            if accounts_number > 1:
                output_string = output_string.rsplit(', ', 1)
                output_string = ' and '.join(output_string)

            print(output_string)
            print('Have fun :D')

        for i, window in enumerate(self.windows):
            keyboard.add_hotkey(f"{self.hotkey}+{self.keybinds[i]}", lambda idx=i: self.switch_window(idx))
            
            

    def switch_window(self, idx):
        hwnd = self.windows[idx]._hWnd
        self.focus_window(hwnd)

    def get_windows_by_name(self, window_name):
        windows = gw.getWindowsWithTitle(window_name)
        return windows
    
    def focus_window(self, hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        self.restore_window_behavior(hwnd)
        self.simulate_mouse_click(hwnd)

    def restore_window_behavior(self, hwnd):
        time.sleep(0.001)
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    def simulate_mouse_click(self, hwnd):
        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0] + 10
        y = rect[1] + 10
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


print("|| AltSwitcherV3 for Roblox is now running... ||")

AltSwitcherV3()
keyboard.wait()