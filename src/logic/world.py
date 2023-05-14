from ..graphics import *
from ..constants import *
from ..map import maps

from .humans import *

class World:
    def __init__(self, game, map_num: int):
        self.sprites = []
        self.game = game
        self.map_num = map_num
        self.position = [0, 0] # Map position on the screen, top-left point
        self.timer = 0 # hyvää koodia, made for spawning in new humans

        drawWorld(self.game, self.map_num, world_pos = self.position)
        self.WORLD_SIZE = maps[self.map_num][0]
        self.spawn_humans()
    
    def spawn_humans(self):
        self.humans = []
        # Spawns in humans on sidewalks, randomising their positions slightly
        for y_pos, horizontal_stripe in enumerate(maps[self.map_num], -1):
            if y_pos == -1:
                # First line of list is map size (yes its weird)
                pass

            else:    
                for x_pos, vertical_point in enumerate(horizontal_stripe):
                    if x_pos == 0: # they dont spawn on top of you
                        pass
                    elif vertical_point[0:2] == "sw":
                        if int(vertical_point[2]) < 7:
                            if random.random() < 0.5:
                                randint = random.randint(1, 1000000)
                                self.humans.append((randint, Human(self.game, human1_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 40 + 30*random.random()], random.choice([-1, 1]), randint)))
                                if random.random() < 0.01:
                                    randint = random.randint(1, 1000000)
                                    self.humans.append((randint, K_Car(self.game, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 200 + 30*random.random()], -1, randint)))
                                else: 
                                    randint = random.randint(1, 1000000)
                                    self.humans.append((randint, Car(self.game, car1_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 200 + 30*random.random()], -1, randint)))
                            if random.random() < 0.1:
                                if random.random() < 0.5:
                                    randint = random.randint(1, 1000000)
                                    self.humans.append((randint, Fan(self.game, fan1_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 40 + 30*random.random()], randint)))
                                else:
                                    randint = random.randint(1, 1000000)
                                    self.humans.append((randint, Fan(self.game, fan2_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 40 + 30*random.random()], randint)))

                        else:
                            if random.random() < 0.5:
                                randint = random.randint(1, 1000000)
                                self.humans.append((randint, Human(self.game, human1_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 320 + 30*random.random()], random.choice([-1, 1]), randint)))
                                randint = random.randint(1, 1000000)
                                self.humans.append((randint, Car(self.game, car2_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 150 + 30*random.random()], 1, randint)))
                            if random.random() < 0.1:
                                if random.random() < 0.5:
                                    randint = random.randint(1, 1000000)
                                    self.humans.append((randint, Fan(self.game, fan1_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 40 + 30*random.random()], randint)))
                                else:
                                    randint = random.randint(1, 1000000)
                                    self.humans.append((randint, Fan(self.game, fan2_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 320 + 30*random.random()], randint)))

    def spawn_on_sides(self):
        for y_pos, horizontal_stripe in enumerate(maps[self.map_num], -1):
            if y_pos == -1:
                # First line of list is map size (yes its weird)
                pass

            else:    
                for x_pos, vertical_point in enumerate(horizontal_stripe):
                    if vertical_point[0:2] == "sw" and x_pos == 0 :
                        if int(vertical_point[2]) < 7:
                            if random.random() < 0.0015:
                                randint = random.randint(1, 1000000)
                                self.humans.append((randint, Human(self.game, human1_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 40 + 30*random.random()], random.choice([-1, 1]), randint)))
                            if random.random() < 0.0005:
                                if random.random() < 0.5:
                                    randint = random.randint(1, 1000000)
                                    self.humans.append((randint, Fan(self.game, fan1_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 40 + 30*random.random()], randint)))
                                else:
                                    randint = random.randint(1, 1000000)
                                    self.humans.append((randint, Fan(self.game, fan2_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 40 + 30*random.random()], randint)))

                        else:
                            if random.random() < 0.0015:
                                randint = random.randint(1, 1000000)
                                self.humans.append((randint, Human(self.game, human1_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 320 + 30*random.random()], random.choice([-1, 1]), randint)))
                            if random.random() < 0.005:
                                randint = random.randint(1, 1000000)
                                self.humans.append((randint, Car(self.game, car2_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 150 + 30*random.random()], 1, randint)))
                            if random.random() < 0.0005:
                                if random.random() < 0.5:
                                    randint = random.randint(1, 1000000)
                                    self.humans.append((randint, Fan(self.game, fan1_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 40 + 30*random.random()], randint)))
                                else:
                                    randint = random.randint(1, 1000000)
                                    self.humans.append((randint, Fan(self.game, fan2_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 320 + 30*random.random()], randint)))

                        if vertical_point[0:2] == "sw" and x_pos == self.WORLD_SIZE[0]-TILE_SIZE[0]:
                            if random.random() < 0.0015:
                                randint = random.randint(1, 1000000)
                                self.humans.append((randint, Human(self.game, human1_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 40 + 30*random.random()], random.choice([-1, 1]), randint)))
                            if random.random() < 0.005:
                                if random.random() < 0.01:
                                    randint = random.randint(1, 1000000)
                                    self.humans.append((randint, K_Car(self.game, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 200 + 30*random.random()], -1, randint)))
                                else:  
                                    randint = random.randint(1, 1000000)
                                    self.humans.append((randint, Car(self.game, car1_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 200 + 30*random.random()], -1, randint)))
                            if random.random() < 0.0005:
                                if random.random() < 0.5:
                                    randint = random.randint(1, 1000000)
                                    self.humans.append((randint, Fan(self.game, fan1_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 40 + 30*random.random()], randint)))
                                else:
                                    randint = random.randint(1, 1000000)
                                    self.humans.append((randint, Fan(self.game, fan2_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 40 + 30*random.random()], randint)))
                        else:
                            if random.random() < 0.0015:
                                randint = random.randint(1, 1000000)
                                self.humans.append((randint, Human(self.game, human1_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 320 + 30*random.random()], random.choice([-1, 1]), randint)))
                            if random.random() < 0.0005:
                                if random.random() < 0.5:
                                    randint = random.randint(1, 1000000)
                                    self.humans.append((randint, Fan(self.game, fan1_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 40 + 30*random.random()], randint)))
                                else:
                                    randint = random.randint(1, 1000000)
                                    self.humans.append((randint, Fan(self.game, fan2_tex, [TILE_SIZE[0]*x_pos + 100*random.random(), TILE_SIZE[1]*y_pos + 320 + 30*random.random()], randint)))


    def tick(self):
        drawWorld(self.game, self.map_num, world_pos = self.position)
        self.WORLD_SIZE = maps[self.map_num][0]
        for human in self.humans:
            human[1].tick()
        if self.timer > 50:
            self.spawn_on_sides()
        else:
            self.timer += 1
        self.spawn_kaarija()

    def spawn_kaarija(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                randint = random.randint(1, 1000000)
                self.humans.append((randint, K_Car(self.game, [1100, TILE_SIZE[1]*0 + 200 + 30*random.random()], -1, randint)))

