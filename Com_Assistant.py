import tkinter as tk
import getpass
import webbrowser
import vlc
import random
import subprocess

class ComputerAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Computer Assistant")
        self.root.config(bg="#1E90FF")  
        self.instance = vlc.Instance()  
        self.player = None

        self.create_widgets()

    def create_widgets(self):
        
        self.label_welcome = tk.Label(self.root, text="Welcome to Computer Assistant", font=("Helvetica", 20), bg="#1E90FF", fg="white", pady=20)
        self.label_welcome.pack(fill=tk.X)
        
        
        self.start_button = tk.Button(self.root, text="Start", command=self.start_chat, bg="#32CD32", fg="white", font=("Helvetica", 14))
        self.start_button.pack(pady=20)

    def start_chat(self):
        
        self.chat_window = tk.Toplevel(self.root)
        self.chat_window.config(bg="#1E90FF")
        self.chat_window.title("Computer Assistant")
        
        
        self.username = getpass.getuser()
        self.display_message(f"Hello {self.username}\nWelcome!!!\nI Can't Understand Your Language. So, You Have To Use Some Commands\nType /command For Listing Out the Commands")

        
        self.entry = tk.Entry(self.chat_window, width="50", bg="#4682B4", fg="white", font=("Helvetica", 12))
        self.entry.pack()
        
        
        self.ask_button = tk.Button(self.chat_window, text="Ask", command=self.handle_query, bg="#FFD700", fg="black", font=("Helvetica", 12))
        self.ask_button.pack()
        
        
        self.new_win_button = tk.Button(self.chat_window, text="New Window", command=self.start_chat, bg="#FFD700", fg="black", font=("Helvetica", 12))
        self.new_win_button.pack()

    def display_message(self, message):
        
        label_message = tk.Label(self.chat_window, text=message, bg="#87CEEB", fg="black", width="60", anchor="w", padx=10, pady=5)
        label_message.pack(anchor="nw")

    def handle_query(self):
        command = self.entry.get()
        
        if command == "/developedby":
            self.display_message("/developedby")
            self.display_message("Visit My Inventor")
            web_page = "https://mahmud5658.github.io/abdullah_portfolio/"
            webbrowser.open_new(web_page)

        elif command == "/command":
            self.display_message("You can ask me the questions\nin the format of commands\n1. Ask /howiwasmade\n2. Ask /youtube\n3. Ask /google\n"
                "4. Ask /chatgpt\n5. Ask /mathsolve\n6. Ask /play_music\n7. /stop_music\n8. /open_code\n9. /developedby")

        elif command == "/mathsolve":
            self.display_message("/mathsolve")
            self.display_message("Hope You Are Enjoying/Enjoyed The Math Solver")
            self.open_math_solver()

        elif command == "/howiwasmade":
            self.display_message("/howiwasmade")
            self.display_message("I was built using python and tkinter. tkinter is a built-in module in python\nIt is used to develop "
                "Graphical User Interface(s)(GUIs).")

        elif command == "/youtube":
            self.display_message("/youtube")
            self.display_message("Go to Youtube")
            web_page = "https://www.youtube.com/"
            webbrowser.open_new(web_page)

        elif command == "/chatgpt":
            self.display_message("/chatgpt")
            self.display_message("Go to chatGpt")
            web_page = "https://chatgpt.com/?oai-dm=1"
            webbrowser.open_new(web_page)

        elif command == "/google":
            self.display_message("/google")
            self.display_message("Go to Google")
            web_page = "https://www.google.com/"
            webbrowser.open_new(web_page)

        elif command == "/play_music":
            self.display_message("/play_song")
            self.display_message("Enjoy the music!")
            self.play_random_music()

        elif command == "/stop_music":
            self.display_message("/stop_music")
            self.display_message("Music stopped!")
            self.stop_song()

        elif command == "/open_code":
            self.display_message("/open_code")
            self.display_message("Opening Visual Studio Code...")
            subprocess.Popen(["code"])

        else:
            self.display_message(command)
            self.display_message("I Can't Understand. Please Use The Commands For Providing You The Information\n"
                "Use /command To Know The Commands")

    def open_math_solver(self):
        self.math_solver_window = tk.Toplevel(self.root)
        self.math_solver_window.config(bg="#1E90FF")
        self.math_solver_window.title("Computer Assistant(MathSolver)")
        self.math_solver_window.geometry("300x150")

        self.msg = tk.Label(self.math_solver_window, text="Enter A Mathematical Equation Here", bg="#87CEEB", fg="black")
        self.msg.pack()
        self.msg = tk.Label(self.math_solver_window, text="Like 2+3, 15*20+(12/2)%10 & ..... ", bg="#87CEEB", fg="black")
        self.msg.pack()
        self.ent = tk.Entry(self.math_solver_window, width="20", bg="#4682B4", fg="white")
        self.ent.pack()
        self.sol = tk.Button(self.math_solver_window, text="Solve", bg="#FFD700", fg="black", command=self.evaluate_expression)
        self.sol.pack()

    def evaluate_expression(self):
        try:
            calc = round(eval(self.ent.get()), 2)
            self.result = tk.Label(self.math_solver_window, text=f"       Result is {calc}      ", bg="#FFD700", fg="black")
            self.result.place(x=110, y=100)
        except Exception as e:
            self.result = tk.Label(self.math_solver_window, text="Error: Invalid expression", bg="#FFD700", fg="black")
            self.result.place(x=110, y=100)

    def play_random_music(self):
        music = [
            "/media/abdullah/Mahmud/song1.mp3",
            "/media/abdullah/Mahmud/song2.mp3",
            "/media/abdullah/Mahmud/song3.mp3",
        ]
        rand_music = random.choice(music)
        self.play_music(rand_music)

    def play_music(self, selected_music):
        media_path = selected_music
        self.player = self.instance.media_player_new()
        media = self.instance.media_new(media_path)
        self.player.set_media(media)
        self.player.play()

    def stop_song(self):
        if self.player:
            self.player.stop()
            self.player = None

def main():
    window = tk.Tk()
    window.geometry("500x400")
    ComputerAssistant(window)
    window.mainloop()

if __name__ == "__main__":
    main()
