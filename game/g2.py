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
        self.speed_multiplier = 1.0  # New: for speed power-ups

        self.canvas.update()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                # New: Add score based on paddle hit
                self.game.add_score(10)
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x * self.speed_multiplier, self.y * self.speed_multiplier)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = -self.y
        if pos[3] >= self.canvas_height:
            if self.game.lives > 0:
                self.game.lose_life()
                self.reset_position()
            else:
                self.hit_bottom = True
                self.game.game_over()
        if self.hit_paddle(pos):
            self.y = -self.y
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = -self.x

    def reset_position(self):
        # New: Reset ball position after losing a life
        self.canvas.coords(self.id, 245, 100, 260, 115)
        starts = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(starts)
        self.y = -3

class PowerUp:
    def __init__(self, canvas, paddle, ball, game, type):
        self.canvas = canvas
        self.paddle = paddle
        self.ball = ball
        self.game = game
        self.type = type

        # Different colors for different power-ups
        colors = {
            'extend': 'green',
            'speed': 'yellow',
            'slow': 'purple'
        }

        self.id = canvas.create_oval(0, 0, 20, 20, fill=colors[type])
        # Random starting position
        x = random.randint(50, 450)
        self.canvas.move(self.id, x, 50)
        self.speed = 2
        self.active = True

    def draw(self):
        if self.active:
            self.canvas.move(self.id, 0, self.speed)
            pos = self.canvas.coords(self.id)

            # Check for paddle collision
            paddle_pos = self.canvas.coords(self.paddle.id)
            if (pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] and
                pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]):
                self.apply_power_up()
                self.active = False
                self.canvas.delete(self.id)

            # Remove if missed
            if pos[3] >= 400:
                self.active = False
                self.canvas.delete(self.id)

    def apply_power_up(self):
        if self.type == 'extend':
            self.paddle.extend()
            self.game.schedule_power_down('extend', 5000)
        elif self.type == 'speed':
            self.ball.speed_multiplier = 1.5
            self.game.schedule_power_down('speed', 5000)
        elif self.type == 'slow':
            self.ball.speed_multiplier = 0.7
            self.game.schedule_power_down('slow', 5000)

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas.update()
        self.canvas_width = self.canvas.winfo_width()
        self.normal_width = 100
        self.extended_width = 150

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<space>', self.stop)  # New: stop paddle movement

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

    def stop(self, evt):  # New: stop paddle
        self.x = 0

    def extend(self):  # New: extend paddle size
        pos = self.canvas.coords(self.id)
        width = pos[2] - pos[0]
        if width == self.normal_width:
            # Extend from the center
            center = (pos[0] + pos[2]) / 2
            self.canvas.coords(self.id,
                             center - self.extended_width/2, pos[1],
                             center + self.extended_width/2, pos[3])

    def normalize(self):  # New: return to normal size
        pos = self.canvas.coords(self.id)
        width = pos[2] - pos[0]
        if width == self.extended_width:
            # Return to normal size from the center
            center = (pos[0] + pos[2]) / 2
            self.canvas.coords(self.id,
                             center - self.normal_width/2, pos[1],
                             center + self.normal_width/2, pos[3])

class Game:
    def __init__(self, tk, canvas):
        self.tk = tk
        self.canvas = canvas
        self.score = 0
        self.lives = 3
        self.level = 1
        self.paddle = Paddle(canvas, 'blue')
        self.ball = Ball(canvas, self.paddle, 'red', self)
        self.power_ups = []
        self.running = True

        # Create score display
        self.score_display = canvas.create_text(50, 30, text=f"Score: {self.score}",
                                              font=("Arial", 16), fill="black")
        # Create lives display
        self.lives_display = canvas.create_text(450, 30, text=f"Lives: {self.lives}",
                                              font=("Arial", 16), fill="black")
        # Create level display
        self.level_display = canvas.create_text(250, 30, text=f"Level: {self.level}",
                                              font=("Arial", 16), fill="black")

        self.power_up_timer = 0
        self.scheduled_power_downs = []

    def add_score(self, points):
        self.score += points
        self.canvas.itemconfig(self.score_display, text=f"Score: {self.score}")

        # Level up every 100 points
        if self.score % 100 == 0:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.canvas.itemconfig(self.level_display, text=f"Level: {self.level}")
        self.ball.speed_multiplier += 0.1  # Increase speed slightly

    def lose_life(self):
        self.lives -= 1
        self.canvas.itemconfig(self.lives_display, text=f"Lives: {self.lives}")

    def game_over(self):
        self.running = False
        self.canvas.create_text(250, 200, text=f"Game Over\nFinal Score: {self.score}",
                              font=("Arial", 20), fill="red", justify="center")
        restart_button = Button(self.tk, text="Restart", command=self.restart)
        self.canvas.create_window(250, 250, window=restart_button)

    def schedule_power_down(self, power_type, delay):
        self.scheduled_power_downs.append({
            'type': power_type,
            'time': time.time() + (delay / 1000)  # Convert ms to seconds
        })

    def check_power_downs(self):
        current_time = time.time()
        remaining_power_downs = []

        for power_down in self.scheduled_power_downs:
            if current_time >= power_down['time']:
                if power_down['type'] == 'extend':
                    self.paddle.normalize()
                elif power_down['type'] in ['speed', 'slow']:
                    self.ball.speed_multiplier = 1.0
            else:
                remaining_power_downs.append(power_down)

        self.scheduled_power_downs = remaining_power_downs

    def spawn_power_up(self):
        if random.random() < 0.005:  # 0.5% chance each frame
            power_type = random.choice(['extend', 'speed', 'slow'])
            self.power_ups.append(PowerUp(self.canvas, self.paddle, self.ball, self, power_type))

    def restart(self):
        self.canvas.delete("all")
        self.__init__(self.tk, self.canvas)
        self.run()

    def run(self):
        while self.running:
            if self.running:
                self.ball.draw()
                self.paddle.draw()

                # Update power-ups
                self.spawn_power_up()
                for power_up in self.power_ups[:]:
                    if power_up.active:
                        power_up.draw()
                    else:
                        self.power_ups.remove(power_up)

                self.check_power_downs()

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