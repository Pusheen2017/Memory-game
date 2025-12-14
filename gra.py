import pygame, os, random;from enum import Enum;from pygame import color as color#importuje potrzebne moduły


#Memory game

class BUTTON(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4  
    STARTBUTTON = 5

ppos = {
    BUTTON.RED: (55,45),
    BUTTON.GREEN: (122,47),
    BUTTON.BLUE: (122,120),
    BUTTON.YELLOW: (55,120),
    BUTTON.STARTBUTTON: (80,105)
}

ppath = {
    BUTTON.RED: ("podświetlNaCzerwono.png"),
    BUTTON.GREEN: ("podświetlNaZielono.png"),
    BUTTON.BLUE: ("podświetlNaNiebiesko.png"),
    BUTTON.YELLOW: ("podświetlNaŻółto.png"),
    BUTTON.STARTBUTTON: ("startbutton.png")
}

class Gra:
    RandomSequence=list[BUTTON] #inicjalizuje listę globalną RandomSequence
    PlayerSequence=list[BUTTON]#inicjalizuje listę globalną PlayerSequence
         
    def __init__(self):
        self.RandomSequence = []
        self.PlayerSequence = []
        self.running = True #flaga działania programu
        self.started = False #flaga aktywnej gry
        self.ControlsActive=False
        self.screen = pygame.display.set_mode((286, 249)) #okno gry
        pygame.display.set_caption("Memory Game")
        self.clock = pygame.time.Clock()
        #img_path = os.path.join(os.path.dirname(__file__), "startbutton.png")
        #image = pygame.image.load(img_path).convert_alpha()
        #self.screen.blit(image, (0, 0))
        #pygame.display.flip()
        pygame.fastevent.init()
        #self.music()
       

    def drawBase(self):
        img_path = os.path.join(os.path.dirname(__file__), "memo.png")
        image = pygame.image.load(img_path).convert_alpha()
        self.screen.blit(image, (0, 0))
        #pygame.display.flip()
        
    def drawSelected(self, button: BUTTON):
        self.drawBase()
        img_path = os.path.join(os.path.dirname(__file__), ppath[button])
        image = pygame.image.load(img_path).convert_alpha()
        self.screen.blit(image, ppos[button])
        pygame.display.flip()

   
    def events(self):
        self.eventsWithTime0(1)
    
    def eventsWithTime0(self, sleepTime): #sprawdzanie przycisków na czas
        strartTime = pygame.time.get_ticks()
        while self.running and pygame.time.get_ticks() - strartTime < sleepTime:
            pygame.fastevent.init()
            event = pygame.fastevent.poll()
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def music(self):
        # losowanie niejednorazowe przy starcie — drukujemy każdą wartość
        #img_path = os.path.join(self.BASE_DIR, "memo.png")
        #image = pygame.image.load(img_path).convert_alpha()
        for _ in range(10):
            
            n = random.randint(1, 4) #RANDOM BUTTON
            b = BUTTON(n)
            self.RandomSequence.append(b)
            self.drawSelected(b)
            print(self.RandomSequence)
            pos = (int, int)

            self.eventsWithTime(1000)
        self.ControlsActive=True
    def eventsWithTime(self, sleepTime): #sprawdzanie przycisków na czas
        strartTime = pygame.time.get_ticks()
        
        while self.running and pygame.time.get_ticks() - strartTime < sleepTime:
            pygame.fastevent.init()
            event = pygame.fastevent.poll()
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_w:#Jeżeli klawisz w naciśnięty
                    print("Naciśnięto W")
                    self.PlayerSequence.append("red")
                    self.drawSelected(BUTTON.RED)
                elif event.key == pygame.K_d:
                    print("Naciśnięto D")
                    self.PlayerSequence.append("blue")
                    self.drawSelected(BUTTON.BLUE)
                elif event.key == pygame.K_a:
                    print("Naciśnięto A")
                    self.PlayerSequence.append("green")
                    self.drawSelected(BUTTON.GREEN)
                elif event.key == pygame.K_s:
                    print("Naciśnięto S")
                    self.PlayerSequence.append("yellow")
                    self.drawSelected(BUTTON.YELLOW)
    
    def CheckSequence(self,pos : int):
        return self.RandomSequence[pos] == self.PlayerSequence[pos]
            
    
    def eventsMouseStartClick(self):
        while self.running:
            pygame.fastevent.init()
            event = pygame.fastevent.poll()
            if event.type == pygame.QUIT: #zamknięto okno
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #klawisz escape
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONUP:  #klinięty przycisk i puszczony
                pos = pygame.mouse.get_pos() #współrzędne kursora (x,y)
                butonPos = ppos[BUTTON.STARTBUTTON]
 
                rect = pygame.Rect(butonPos[0], butonPos[1],91,29) #poprawić żeby nie wpisywać wymiarów ręcznie
                if rect.collidepoint(pos):
                    self.started = True
                    return
                    
                    
    #główna pętla programu
    def run(self):
        while self.running:
            if self.started: #gra uruchomiona
                self.music()#losowanie sekwencji
                if self.ControlsActive:
                    self.eventsWithTime0
                else:
                    pass
                
                self.started = False
                #główna pętla gry, losowanie sekwencji, sprawdzanie czy gracz dobrze powtórzył sekwencję
            else: #gra nie uruchomiona
                self.drawSelected(BUTTON.STARTBUTTON)
                #sprawdzać czy kliknięto start
                self.eventsMouseStartClick()
            
            self.clock.tick(60)
            #self.eventsWithTime(1000)
            #self.drawBase()
            self.events()  

if __name__ == "__main__":
    game = Gra()
    game.run()