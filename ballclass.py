import random 

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 245, 100)
        startAngles = [-3, -2, -1, 1, 2, 3]
        random.shuffle(startAngles)
        self.x = startAngles[0]
        self.y = -3
        self.canvasHeight = self.canvas.winfo_height()
        self.canvasWidth = self.canvas.winfo_width()
        self.hitBottom = False

    def hitPaddle(self, ballPosition):
        paddlePosition = self.canvas.coords(self.paddle.id)
        if ballPosition[2] >= paddlePosition[0] and ballPosition[0] <= paddlePosition[2]:
            if ballPosition[3] >= paddlePosition[1] and ballPosition[3] <= paddlePosition[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        ballPosition = self.canvas.coords(self.id)
        if ballPosition[1] <= 0:
            self.y = 3
        if ballPosition[3] >= self.canvasHeight:
            self.hitBottom = True 
        if ballPosition[0] <= 0:
            self.x = 3
        if ballPosition[2] >= self.canvasWidth:
            self.x = -3
        if self.hitPaddle(ballPosition) == True:
            self.y = -3


