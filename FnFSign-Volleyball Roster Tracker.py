# FnFSign - Volleyball Roster Tracker
# This script creates a GUI application to submit volleyball team rosters to an Excel file.
# It uses the Tkinter library for the GUI and openpyxl for Excel file manipulation.
import tkinter as tk
from tkinter import *

import openpyxl
import os

# Setting up excell
file_path = "tournament_rosters.xlsx"
if not os.path.exists(file_path):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["Tournament Name", "Division", "Team Name", "Player Names"])
    workbook.save(file_path)

# 
def submit_team():
    tournament = entry_tournament.get()
    division = entry_division.get()
    team_name = entry_team.get()
    players = entry_players.get("1.0", END).strip()

    if not tournament or not division or not team_name or not players:
        result_label.config(text="Please fill out all fields.", fg="red")
        return

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    sheet.append([tournament, division, team_name, players])
    workbook.save(file_path)

    result_label.config(text="Team submitted!", fg="green")
    entry_team.delete(0, END)
    entry_players.delete("1.0", END)

# GUI
window = Tk()
window.title("FnFSign – Team Roster Submission")
window.geometry("500x500")

Label(window, text="Tournament Name").pack()
entry_tournament = Entry(window, width=50)
entry_tournament.pack()

Label(window, text="Division (e.g., Co-Ed, Men's)").pack()
entry_division = Entry(window, width=50)
entry_division.pack()

Label(window, text="Team Name").pack()
entry_team = Entry(window, width=50)
entry_team.pack()

Label(window, text="Player Names (one line each)").pack()
entry_players = Text(window, width=50, height=10)
entry_players.pack()

submit_btn = Button(window, text="Submit Team", command=submit_team)
submit_btn.pack(pady=10)

result_label = Label(window, text="")
result_label.pack()

window.mainloop()

# This code creates a simple GUI application using Tkinter for submitting team rosters to an Excel file.
