class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvasWidth = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turnLeft)
        self.canvas.bind_all('<KeyPress-Right>', self.turnRight)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        paddlePosition = self.canvas.coords(self.id)
        if paddlePosition[0] <= 0:
            self.x = 0
        elif paddlePosition[2] >= self.canvasWidth:
            self.x = 0

    def turnLeft(self, evt):
        self.x = -2

    def turnRight(self, evt):
        self.x = 2


