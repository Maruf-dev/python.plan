from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle, color, game):
        self.canvas = canvas
        self.paddle = paddle
        self.game = game
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(starts)
        self.y = -3
        self.hit_bottom = False

        # Ensure canvas dimensions are fetched after update
        self.canvas.update()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:  # Top wall
            self.y = -self.y
        if pos[3] >= self.canvas_height:  # Bottom
            self.hit_bottom = True
            self.game.game_over()  # Call game over function
        if self.hit_paddle(pos):  # Paddle collision
            self.y = -self.y
        if pos[0] <= 0 or pos[2] >= self.canvas_width:  # Left & Right walls
            self.x = -self.x  # Fix: reverse X direction instead of Y

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas.update()  # Ensure correct canvas width
        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -4  # Increased speed for better responsiveness

    def turn_right(self, evt):
        self.x = 4  # Increased speed for better responsiveness

class Game:
    def __init__(self, tk, canvas):
        self.tk = tk
        self.canvas = canvas
        self.paddle = Paddle(canvas, 'blue')
        self.ball = Ball(canvas, self.paddle, 'red', self)
        self.running = True

    def game_over(self):
        self.running = False
        self.canvas.create_text(250, 200, text="Game Over", font=("Arial", 20), fill="red")
        restart_button = Button(self.tk, text="Restart", command=self.restart)
        self.canvas.create_window(250, 230, window=restart_button)

    def restart(self):
        self.canvas.delete("all")  # Clear the canvas
        self.__init__(self.tk, self.canvas)  # Restart the game logic
        self.run()

    def run(self):
        while self.running:
            self.ball.draw()
            self.paddle.draw()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)

tk = Tk()
tk.title('Bounce Game')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

game = Game(tk, canvas)
game.run()
