import time, random, os, pygame
from ProcessGrabber import ProcessGrabber
def prGreen(s): print("\033[92m {}\033[00m".format(s))

class RouletteWheel():
    def __init__(self):
        self.processHandler = ProcessGrabber()
        self.processes = self.processHandler.processes
        
        self.processesToShow = 9
        self.center = self.processesToShow // 2
        
        
        pygame.init()
        pygame.mixer.init()
        self.channel = pygame.mixer.Channel(5)
        self.tick_sound = pygame.mixer.Sound("silent-short-click.mp3")
        
    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")
        
    @staticmethod
    def ease_in_out(i, end, startDelay, endDelay):
        if end <= 1:
            return endDelay

        i = max(0, min(i, end - 1))
        t = i / (end - 1)

        if t == 0:
            eased = 0.0
        else:
            eased = 2 ** (10 * (t - 1))

        return startDelay + (endDelay - startDelay) * eased


    def spin(self):
        spins = random.randint(len(self.processes) // 2, len(self.processes) * 2)
        startDelay = 0.06
        delay = startDelay
        endDelay = 0.70
        
        for step in range(spins):
            self.clear()
            print("🎰 Roulette Wheel\n")

            for i in range(self.processesToShow):
                self.channel.play(self.tick_sound)
                idx = (i - self.center) % len(self.processes)
                value = f"{self.processes[idx][1]} {self.processes[idx][0]}"

                if i == self.center:
                    prGreen(f">>> {value} <<<")
                else:
                    print(f"    {value}")

            self.processes.append(self.processes.pop(0))
            time.sleep(self.ease_in_out(step, spins, startDelay, endDelay))
            
   
        cooldown = 5
        for i in range(cooldown):
            self.clear()
            print("🎰 Roulette Wheel\n")
            print(f"🟢 Ball landed on: {self.processes[0]}. It will be terminated in: {cooldown - i} seconds")
            time.sleep(1)
        self.processHandler.terminateProcess(self.processes[0][0])
        
        
            
wheel = RouletteWheel()
while(1):
    wheel.spin()
