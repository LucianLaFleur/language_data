import tkinter as tk
from datetime import timedelta
from tkinter import ttk
import pygame

class CountdownApp:
    def __init__(self, master):
        self.bassline_audio = "bassline0032423.wav"
        self.three_stripeBass = "ThreeStripe_russianBass.wav"
        self.master = master
        self.master.title("Countdown Timer")
        self.master.geometry("600x300")  # Adjusted window size
        self.remaining_time_2min = timedelta(minutes=2)
        self.remaining_time_20min = timedelta(minutes=20)
        self.elapsed_time_stopwatch = timedelta()
        self.is_running_2min = False
        self.is_running_20min = False
        self.is_running_stopwatch = False  

        self.label_2min = tk.Label(text="2-Minute Countdown", font=('Helvetica', 18))
        self.label_2min.grid(row=0, column=0, columnspan=2)
        self.display_2min = tk.Label(font=('Helvetica', 24))
        self.display_2min.grid(row=1, column=0, columnspan=2)
        self.update_display_2min()
        self.display_2min.configure(bg="black", fg="lime green")
        self.start_pause_button_2min = tk.Button(text="Start 2min", command=lambda: self.toggle_timer_2min())
        self.start_pause_button_2min.grid(row=2, column=0, pady=5)
        self.reset_button_2min = tk.Button(text="Reset 2min", command=lambda: self.reset_timer_2min())
        self.reset_button_2min.grid(row=2, column=1, pady=5)

        self.label_20min = tk.Label(text="20-Minute Countdown", font=('Helvetica', 18))
        self.label_20min.grid(row=3, column=0, columnspan=2)
        self.display_20min = tk.Label(font=('Helvetica', 24))
        self.display_20min.grid(row=4, column=0, columnspan=2)
        self.update_display_20min()
        self.display_20min.configure(bg="black", fg="lime green")
        self.start_pause_button_20min = tk.Button(text="Start 20min", command=lambda: self.toggle_timer_20min())
        self.start_pause_button_20min.grid(row=5, column=0, pady=5)
        self.reset_button_20min = tk.Button(text="Reset 20min", command=lambda: self.reset_timer_20min())
        self.reset_button_20min.grid(row=5, column=1, pady=5)

        self.update_timers()

        self.label_stopwatch = tk.Label(text="Stopwatch", font=('Helvetica', 18))
        self.label_stopwatch.grid(row=0, column=2, columnspan=2)
        self.display_stopwatch = tk.Label(font=('Helvetica', 24))
        self.display_stopwatch.grid(row=1, column=2, columnspan=2)
        self.update_display_stopwatch()
        self.display_stopwatch.configure(bg="#416", fg="lime green")
        self.start_pause_button_stopwatch = tk.Button(text="Start Stopwatch", command=lambda: self.toggle_stopwatch())
        self.start_pause_button_stopwatch.grid(row=2, column=2, pady=5)
        self.reset_button_stopwatch = tk.Button(text="Reset Stopwatch", command=lambda: self.reset_stopwatch())
        self.reset_button_stopwatch.grid(row=2, column=3, pady=5)

    # Initialize Pygame for audio
        pygame.mixer.init()
    def play_audio(self, audio_file):
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

    def update_display_2min(self):
        minutes, seconds = divmod(self.remaining_time_2min.seconds, 60)
        time_format = '{:02d}:{:02d}'.format(minutes, seconds)
        # self.display_2min.config(text=time_format)
        self.display_2min.config(text=time_format)

    def update_display_20min(self):
        minutes, seconds = divmod(self.remaining_time_20min.seconds, 60)
        time_format = '{:02d}:{:02d}'.format(minutes, seconds)
        # self.display_20min.config(text=time_format)
        self.display_20min.config(text=time_format)

    def update_display_stopwatch(self):
        elapsed_time = str(self.elapsed_time_stopwatch).split(".")[0]  # Format: HH:MM:SS
        self.display_stopwatch.config(text=elapsed_time)

    def update_timers(self):
        if self.is_running_2min:
            self.remaining_time_2min -= timedelta(seconds=1)
            self.update_display_2min()
            if self.remaining_time_2min.total_seconds() <= 0:
                self.play_audio(self.bassline_audio)
                self.reset_timer_2min()
        if self.is_running_20min:
            self.remaining_time_20min -= timedelta(seconds=1)
            self.update_display_20min()
            if self.remaining_time_20min.total_seconds() <= 0:
                self.play_audio(self.three_stripeBass)
                self.reset_timer_20min()
        if self.is_running_stopwatch:
            self.elapsed_time_stopwatch += timedelta(seconds=1)
            self.update_display_stopwatch()
            if self.elapsed_time_stopwatch.total_seconds() % 1800 == 0:
                self.play_audio(self.three_stripeBass)
            elif self.elapsed_time_stopwatch.total_seconds() % 900 == 0:
                self.play_audio(self.bassline_audio)
            # self.elapsed_time_stopwatch
            
        self.master.after(1000, self.update_timers)

    def toggle_timer_2min(self):
        self.is_running_2min = not self.is_running_2min
        if self.is_running_2min:
            self.start_pause_button_2min.config(text="Pause 2min")
        else:
            self.start_pause_button_2min.config(text="Start 2min")
        self.update_display_2min()

    def reset_timer_2min(self):
        self.start_pause_button_2min.config(text="Start 2min")
        self.remaining_time_2min = timedelta(minutes=2)
        self.update_display_2min()

    def toggle_timer_20min(self):
        self.is_running_20min = not self.is_running_20min
        if self.is_running_20min:
            self.start_pause_button_20min.config(text="Pause 20min")
        else:
            self.start_pause_button_20min.config(text="Start 20min")

    def reset_timer_20min(self):
        self.start_pause_button_20min.config(text="Start 20min")
        self.remaining_time_20min = timedelta(minutes=20)
        self.update_display_20min()

    def toggle_stopwatch(self):
        self.is_running_stopwatch = not self.is_running_stopwatch
        if self.is_running_stopwatch:
            self.start_pause_button_stopwatch.config(text="Pause Stopwatch")
        else:
            self.start_pause_button_stopwatch.config(text="Start Stopwatch")

    def reset_stopwatch(self):
        self.is_running_stopwatch = False
        self.start_pause_button_stopwatch.config(text="Start Stopwatch")
        self.elapsed_time_stopwatch = timedelta()
        self.update_display_stopwatch()

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()
