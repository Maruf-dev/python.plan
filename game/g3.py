from tkinter import *
import random
import time

class Brick:
    def __init__(self, canvas, x, y, color, points):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y, x + 60, y + 20, fill=color, outline='white')
        self.points = points
        self.destroyed = False

    def destroy(self):
        self.canvas.delete(self.id)
        self.destroyed = True
        return self.points

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

        self.canvas.update()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def hit_brick(self, pos):
        for brick in self.game.bricks:
            if not brick.destroyed:
                brick_pos = self.canvas.coords(brick.id)
                if (pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2] and
                    pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]):
                    points = brick.destroy()
                    self.game.add_score(points)
                    return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:  # Top wall
            self.y = -self.y
        if pos[3] >= self.canvas_height:  # Bottom
            if self.game.lives > 0:
                self.game.lose_life()
                self.reset_position()
            else:
                self.hit_bottom = True
                self.game.game_over()
        if self.hit_paddle(pos):  # Paddle collision
            self.y = -self.y
        if self.hit_brick(pos):  # Brick collision
            self.y = -self.y
        if pos[0] <= 0 or pos[2] >= self.canvas_width:  # Side walls
            self.x = -self.x

    def reset_position(self):
        self.canvas.coords(self.id, 245, 100, 260, 115)
        starts = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(starts)
        self.y = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas.update()
        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<space>', self.stop)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0
            self.canvas.coords(self.id, 0, pos[1], pos[2]-pos[0], pos[3])
        if pos[2] >= self.canvas_width:
            self.x = 0
            self.canvas.coords(self.id, self.canvas_width-(pos[2]-pos[0]), pos[1],
                             self.canvas_width, pos[3])

    def turn_left(self, evt):
        self.x = -6

    def turn_right(self, evt):
        self.x = 6

    def stop(self, evt):
        self.x = 0

class Game:
    def __init__(self, tk, canvas):
        self.tk = tk
        self.canvas = canvas
        self.score = 0
        self.lives = 3
        self.level = 1
        self.paddle = Paddle(canvas, 'blue')
        self.ball = Ball(canvas, self.paddle, 'red', self)
        self.running = True

        # Initialize bricks
        self.bricks = []
        self.create_bricks()

        # Create displays
        self.score_display = canvas.create_text(50, 30, text=f"Score: {self.score}",
                                              font=("Arial", 16), fill="black")
        self.lives_display = canvas.create_text(450, 30, text=f"Lives: {self.lives}",
                                              font=("Arial", 16), fill="black")
        self.level_display = canvas.create_text(250, 30, text=f"Level: {self.level}",
                                              font=("Arial", 16), fill="black")

    def create_bricks(self):
        colors_and_points = [
            ('red', 30),
            ('orange', 20),
            ('yellow', 10),
            ('green', 5)
        ]

        for row, (color, points) in enumerate(colors_and_points):
            for col in range(8):
                x = col * 62 + 1
                y = row * 22 + 50
                self.bricks.append(Brick(self.canvas, x, y, color, points))

    def check_level_complete(self):
        if all(brick.destroyed for brick in self.bricks):
            self.level += 1
            self.canvas.itemconfig(self.level_display, text=f"Level: {self.level}")
            self.ball.reset_position()
            self.create_bricks()

    def add_score(self, points):
        self.score += points
        self.canvas.itemconfig(self.score_display, text=f"Score: {self.score}")
        self.check_level_complete()

    def lose_life(self):
        self.lives -= 1
        self.canvas.itemconfig(self.lives_display, text=f"Lives: {self.lives}")

    def game_over(self):
        self.running = False
        self.canvas.create_text(250, 200, text=f"Game Over\nFinal Score: {self.score}",
                              font=("Arial", 20), fill="red", justify="center")
        restart_button = Button(self.tk, text="Restart", command=self.restart)
        self.canvas.create_window(250, 250, window=restart_button)

    def restart(self):
        self.canvas.delete("all")
        self.__init__(self.tk, self.canvas)
        self.run()

    def run(self):
        while self.running:
            if self.running:
                self.ball.draw()
                self.paddle.draw()
                self.tk.update_idletasks()
                self.tk.update()
                time.sleep(0.01)

tk = Tk()
tk.title('Brick Breaker')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

game = Game(tk, canvas)
game.run()