import pygame, simpleGE, random

""" slide and catch pt. 1 & 2 """

class Pickle(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("pickle.png")
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        #move to top of screen
        self.y = 10
        
        #x random 0 - screen width
        self.x = random.randit(0, self.screenWidth)
        
        #dy is random minSpeed to maxSpeed
        self.dy = random.randit(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
        
class Burger(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("burger#7.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5

    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed        
        if self.isKeyPressed(pygame.L_RIGHT):
            self.x += self.moveSpeed
        
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)

class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time Left: 30"
        self.center = (500, 30)

        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("background2.png")
        
        self.numPickles = 5
        self.score = 0
        self.lblScore = LblScore()
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 30
        self.lblTime = LblTime()
        
        self.burger = Burger(self)
        #self.pickle = Pickle(self)
        
        self.pickles = []
        for i in range(self.numPickles):
            self.pickles.append(Pickle(self))
            
        self.sprites = [self.burger,
                        self.pickles,
                        self.lblScore,
                        self.lblTime]
        
    def process(self):
        for pickle in self.pickles:
            if coin.collidesWith(self.burger):
                coin.reset()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimerLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()

class Instructions(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("background2.png")
        self.reponse = "Feast!"
        
        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [
        "You are a diner meal!",
        "Move your arrow keys",
        "from left to right.",
        "Catch as many pickles",
        "as you can to put on your burger!",
        "Watch the time!",
        "",
        ]
        
        self.directions.center = (320, 240)
        self.directions.size = (500, 250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Feast"
        self.btnPlay.center = (150, 400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit!"
        self.btnQuit.center = (500, 400)
        
        
        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit]
        
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Feast"
            self.stop()
           
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
            
        
def main():
    
    keepGoing = True
    while keepGoing:
        instructions = Instructions()
        instructions.start()
        
        if instructions.response == "Feast":
            game = Game()
            game.start()
    #print(instructions.response)
        else:
            keepGoing = False
    

        
if __name__ == "__main__":
    main()