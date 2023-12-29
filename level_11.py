import arcade
from arcade.experimental.lights import Light, LightLayer

JUMP_SPEED = 8
GRAVITY = 0.35
MOVEMENT_SPEED = 2.6

class Ball(arcade.Sprite):
    def follow_sprite(self, player_sprite):
        if self.center_y < player_sprite.center_y:
            self.center_y += min(2, player_sprite.center_y - self.center_y)
        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(2, self.center_y - player_sprite.center_y)

        if self.center_x < player_sprite.center_x:
            self.center_x += min(2, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(2, self.center_x - player_sprite.center_x)

class Level_11(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.flag = False
        self.flag_2 = False
        self.flag_3 = False
        self.flag_4 = False
        self.flag_5 = False
        self.flag_6 = False
        self.flag_7 = False 
        self.flag_8 = False
        self.flag_9 = False
        self.flag_10 = False
        self.flag_11 = False
        self.flag_12 = False
        self.flag_13 = False
        self.flag_14 = False
        self.flag_15 = False
        self.flag_16 = False
        self.flag_17 = False
        self.flag_18 = False
        self.flag_19 = False
        self.flag_20 = False
        self.flag_21 = False
        self.flag_22 = False
        self.flag_23 = False
        self.flag_24 = False
        self.flag_25 = False
        self.flag_26 = False
        self.flag_27 = False
        self.flag_28 = False
        self.flag_29 = False
        self.flag_30 = False
        self.flag_31 = False
        self.flag_32 = False
        self.flag_33 = False
        self.flag_34 = False
        self.flag_35 = False
        self.lifes = 3
        self.score = 0 
        self.score_2 = 1
        self.x = 100
        self.y = 100
        self.random_list = [1250, 1314, 1378, 1442, 1506, 1570, 1634, 1698, 1762, 1826, 1890, 1954]
        self.random_list_2 = [600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150]
        self.random_list_3 = [2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850]
        self.emitter = None

        self.camera_sprites = arcade.Camera(800, 600)
        self.camera_gui = arcade.Camera(800, 600)
    def setup(self):
        self.light_layer = LightLayer(800, 600)
        self.light_layer.set_background_color(arcade.color.BLACK)

        self.platforms_list = arcade.SpriteList()
        self.torch_list = arcade.SpriteList()
        self.obstacles_list = arcade.SpriteList()
        self.obstacles_list_2 = arcade.SpriteList()
        self.obstacles_list_3 = arcade.SpriteList()
        self.obstacles_list_4 = arcade.SpriteList()
        self.list = arcade.SpriteList()
        self.button_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()

        self.player_sprite = arcade.AnimatedWalkingSprite() 
        self.player_sprite.center_x = self.x 
        self.player_sprite.center_y = self.y
        self.player_sprite.stand_right_textures = [arcade.load_texture("./Resources/Images/Person.png")]
        self.player_sprite.stand_left_textures = [arcade.load_texture("./Resources/Images/Person.png", mirrored=True)]  
        self.player_sprite.walk_right_textures = [
            arcade.load_texture("./Resources/Images/walk.png"), 
            arcade.load_texture("./Resources/Images/walk1.png"), 
            arcade.load_texture("./Resources/Images/walk2.png"), 
            arcade.load_texture("./Resources/Images/walk3.png"), 
            arcade.load_texture("./Resources/Images/walk4.png"),
            arcade.load_texture("./Resources/Images/walk5.png"), 
            arcade.load_texture("./Resources/Images/walk6.png"), 
            arcade.load_texture("./Resources/Images/walk7.png")]
        self.player_sprite.walk_left_textures = [
            arcade.load_texture("./Resources/Images/walk.png", mirrored=True), 
            arcade.load_texture("./Resources/Images/walk1.png", mirrored=True), 
            arcade.load_texture("./Resources/Images/walk2.png", mirrored=True), 
            arcade.load_texture("./Resources/Images/walk3.png", mirrored=True), 
            arcade.load_texture("./Resources/Images/walk4.png", mirrored=True),
            arcade.load_texture("./Resources/Images/walk5.png", mirrored=True), 
            arcade.load_texture("./Resources/Images/walk6.png", mirrored=True), 
            arcade.load_texture("./Resources/Images/walk7.png", mirrored=True)]  
        self.player_sprite.texture = self.player_sprite.stand_right_textures[0] 
        self.player_sprite.texture = self.player_sprite.stand_left_textures[0]
        self.player_sprite.scale = 0.5

        for x in range(33, 401, 64):
            snow_grass = arcade.Sprite("./Resources/Images/snow_grass.png", 0.92)
            snow_grass.center_x = x
            snow_grass.center_y = 90
            self.platforms_list.append(snow_grass)
        for x in range(33,  401, 64):
            snow_ground = arcade.Sprite("./Resources/Images/snow_ground.png", 0.92)
            snow_ground.center_x = x
            snow_ground.center_y = 26
            self.platforms_list.append(snow_ground)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.platforms_list, gravity_constant = GRAVITY) 

        self.exit_sprite = arcade.Sprite("./Resources/Images/exit.png", 0.5)
        self.exit_sprite.center_x = 4917
        self.exit_sprite.center_y = 154

        for y in range(250, 2100, 64):
            wall_sprite = arcade.Sprite("./Resources/Images/wall.png", 0.5)
            wall_sprite.center_x = 400
            wall_sprite.center_y = y
            self.platforms_list.append(wall_sprite)
        for y in range(251, 387, 64):
            wall_sprite = arcade.Sprite("./Resources/Images/wall.png", 0.5)
            wall_sprite.center_x = 726
            wall_sprite.center_y = y
            self.platforms_list.append(wall_sprite)
        for y in range(251, 387, 64):
            wall_sprite = arcade.Sprite("./Resources/Images/wall.png", 0.5)
            wall_sprite.center_x = 1150
            wall_sprite.center_y = y
            self.platforms_list.append(wall_sprite)
        for y in range(251, 387, 64):
            wall_sprite = arcade.Sprite("./Resources/Images/wall.png", 0.5)
            wall_sprite.center_x = 1778
            wall_sprite.center_y = y
            self.platforms_list.append(wall_sprite)
        for y in range(251, 387, 64):
            wall_sprite = arcade.Sprite("./Resources/Images/wall.png", 0.5)
            wall_sprite.center_x = 2742
            wall_sprite.center_y = y
            self.platforms_list.append(wall_sprite)
        for y in range(251, 387, 64):
            wall_sprite = arcade.Sprite("./Resources/Images/wall.png", 0.5)
            wall_sprite.center_x = 3254
            wall_sprite.center_y = y
            self.platforms_list.append(wall_sprite)
        for y in range(187, 2100, 64):
            wall_sprite = arcade.Sprite("./Resources/Images/wall.png", 0.5)
            wall_sprite.center_x = 3816
            wall_sprite.center_y = y
            self.platforms_list.append(wall_sprite)
        for y in range(608, 775, 64):
            wall_sprite = arcade.Sprite("./Resources/Images/wall.png", 0.5)
            wall_sprite.center_x = 1123
            wall_sprite.center_y = y
            self.platforms_list.append(wall_sprite)
        for y in range(942, 1106, 64):
            wall_sprite = arcade.Sprite("./Resources/Images/wall.png", 0.5)
            wall_sprite.center_x = 3095
            wall_sprite.center_y = y
            self.platforms_list.append(wall_sprite)
        for x in range(380, 3900, 64):
            wall_sprite = arcade.Sprite("./Resources/Images/wall.png", 0.5)
            wall_sprite.center_x = x
            wall_sprite.center_y = 443
            self.platforms_list.append(wall_sprite)
        for x in range(380, 3900, 64):
            wall_sprite = arcade.Sprite("./Resources/Images/wall.png", 0.5)
            wall_sprite.center_x = x
            wall_sprite.center_y = 774
            self.platforms_list.append(wall_sprite)
        for x in range(380, 3900, 64):
            wall_sprite = arcade.Sprite("./Resources/Images/wall.png", 0.5)
            wall_sprite.center_x = x
            wall_sprite.center_y = 1105
            self.platforms_list.append(wall_sprite)
        for x in range(380, 3900, 64):
            wall_sprite = arcade.Sprite("./Resources/Images/wall.png", 0.5)
            wall_sprite.center_x = x
            wall_sprite.center_y = 1430
            self.platforms_list.append(wall_sprite)
        for x in range(380, 3900, 64):
            wall_sprite = arcade.Sprite("./Resources/Images/wall.png", 0.5)
            wall_sprite.center_x = x
            wall_sprite.center_y = 1755
            self.platforms_list.append(wall_sprite)
        for x in range(380, 3900, 64):
            wall_sprite = arcade.Sprite("./Resources/Images/wall.png", 0.5)
            wall_sprite.center_x = x
            wall_sprite.center_y = 2080
            self.platforms_list.append(wall_sprite)
        
        torch_sprite = arcade.Sprite("./Resources/Images/torch.png", 0.5, angle = 90)
        torch_sprite.center_x = 360
        torch_sprite.center_y = 235
        self.torch_list.append(torch_sprite)

        light = Light(150, 235, 400, arcade.csscolor.WHITE, 'soft')
        self.light_layer.add(light)

        for x in range(400, 3800, 64):
            wood_boards = arcade.Sprite("./Resources/Images/wood_boards.png", 0.9)
            wood_boards.center_x = x
            wood_boards.center_y = 57
            self.platforms_list.append(wood_boards)
        
        self.hallway = arcade.Sprite("./Resources/Images/hallway.png", 0.3)
        self.hallway.center_x = 563
        self.hallway.center_y = 268
        self.the_secret_room = arcade.Sprite("./Resources/Images/the_secret_room.png", 0.3)
        self.the_secret_room.center_x = 938
        self.the_secret_room.center_y = 268
        self.bathroom = arcade.Sprite("./Resources/Images/bathroom.png", 0.444)
        self.bathroom.center_x = 1464
        self.bathroom.center_y = 268
        self.bedroom = arcade.Sprite("./Resources/Images/bedroom.png", 0.3)
        self.bedroom.center_x = 2260
        self.bedroom.center_y = 268
        self.kitchen = arcade.Sprite("./Resources/Images/kitchen.png", 0.32)
        self.kitchen.center_x = 2998
        self.kitchen.center_y = 268
        self.living_room = arcade.Sprite("./Resources/Images/living_room.png", 0.356)
        self.living_room.center_x = 3535
        self.living_room.center_y = 268
        self.the_mysterious_room = arcade.Sprite("./Resources/Images/the_mysterious_room.png", 0.3)
        self.the_mysterious_room.center_x = 762
        self.the_mysterious_room.center_y = 608
        self.the_mysterious_room_2 = arcade.Sprite("./Resources/Images/the_mysterious_room.png", 0.3)
        self.the_mysterious_room_2.center_x = 3455
        self.the_mysterious_room_2.center_y = 940
        self.background = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background.center_x = 1605
        self.background.center_y = 608
        self.background_2 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_2.center_x = 2505
        self.background_2.center_y = 608
        self.background_3 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_3.center_x = 3400
        self.background_3.center_y = 608
        self.background_4 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_4.center_x = 2670
        self.background_4.center_y = 940
        self.background_5 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_5.center_x = 1770
        self.background_5.center_y = 940
        self.background_6 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_6.center_x = 870
        self.background_6.center_y = 940
        self.background_7 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_7.center_x = 870
        self.background_7.center_y = 1270
        self.background_8 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_8.center_x = 1770
        self.background_8.center_y = 1270
        self.background_9 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_9.center_x = 2670
        self.background_9.center_y = 1270
        self.background_10 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_10.center_x = 3400
        self.background_10.center_y = 1270
        self.background_11 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_11.center_x = 3350
        self.background_11.center_y = 1610
        self.background_12 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_12.center_x = 2500
        self.background_12.center_y = 1610
        self.background_13 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_13.center_x = 1700
        self.background_13.center_y = 1610
        self.background_14 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_14.center_x = 850
        self.background_14.center_y = 1610
        self.background_15 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_15.center_x = 850
        self.background_15.center_y = 1937
        self.background_16 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_16.center_x = 1700
        self.background_16.center_y = 1937
        self.background_17 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_17.center_x = 2500
        self.background_17.center_y = 1937
        self.background_18 = arcade.Sprite("./Resources/Images/background.png", 0.6)
        self.background_18.center_x = 3350
        self.background_18.center_y = 1937
        
        for _ in range(6): 
            random = __import__('random').choice(self.random_list)
            box = arcade.Sprite("./Resources/Images/box.png", 0.5)
            box.center_x = random
            box.center_y = 505
            self.obstacles_list.append(box)
            self.random_list.remove(random)
        for x in self.random_list:
            box = arcade.Sprite("./Resources/Images/box.png", 0.5)
            box.center_x = x
            box.center_y = 505
            self.platforms_list.append(box)
        
        for _ in range(6):
            random = __import__('random').choice(self.random_list_2)
            spike = arcade.Sprite("./Resources/Images/spike.png", 1)
            spike.center_x = random
            spike.center_y = 1400
            self.obstacles_list_2.append(spike)
            self.random_list_2.remove(random)
        
        for _ in range(6):
            spike = arcade.Sprite("./Resources/Images/spike.png", 1, angle = -90)
            spike.center_x = 2400
            spike.center_y = 1250
            self.obstacles_list_3.append(spike)

        for _ in range(6):
            random = __import__('random').choice(self.random_list_3)
            spike = arcade.Sprite("./Resources/Images/spike.png", 1, angle = 180)
            spike.center_x = random
            spike.center_y = 1173
            self.obstacles_list_4.append(spike)
            self.random_list_3.remove(random)

        for x in range(2300, 3005, 64):
            box = arcade.Sprite("./Resources/Images/box.png", 0.5)
            box.center_x = x
            box.center_y = 710
            self.list.append(box)

        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 3330
        box.center_y = 539
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 3490
        box.center_y = 620
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 3630
        box.center_y = 539
        self.platforms_list.append(box)
    
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 2950
        box.center_y = 850
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 2800
        box.center_y = 940
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 2650
        box.center_y = 850
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 2460
        box.center_y = 880
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 2300
        box.center_y = 960
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 2155
        box.center_y = 880
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 1965
        box.center_y = 880
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 1815
        box.center_y = 960
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 1670
        box.center_y = 880
        self.platforms_list.append(box)

        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 2950
        box.center_y = 850
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 2800
        box.center_y = 940
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 2650
        box.center_y = 850
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 2460
        box.center_y = 880
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 2300
        box.center_y = 960
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 2155
        box.center_y = 880
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 1965
        box.center_y = 880
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 1815
        box.center_y = 960
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 1670
        box.center_y = 880
        self.platforms_list.append(box)

        self.box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box.center_x = 2900
        self.box.center_y = 1490
        self.platforms_list.append(self.box)
        self.box2 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box2.center_x = 2900
        self.box2.center_y = 1547
        self.platforms_list.append(self.box2)
        self.box3 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box3.center_x = 2730
        self.box3.center_y = 1610
        self.platforms_list.append(self.box3)
        self.box4 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box4.center_x = 2580
        self.box4.center_y = 1570
        self.platforms_list.append(self.box4)
        self.box5 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box5.center_x = 2410
        self.box5.center_y = 1490
        self.platforms_list.append(self.box5)
        self.box6 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box6.center_x = 2410
        self.box6.center_y = 1547
        self.platforms_list.append(self.box6)
        self.box7 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box7.center_x = 2250
        self.box7.center_y = 1600
        self.platforms_list.append(self.box7)
        self.box8 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box8.center_x = 2186
        self.box8.center_y = 1600
        self.platforms_list.append(self.box8)
        self.box9 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box9.center_x = 2122
        self.box9.center_y = 1600
        self.platforms_list.append(self.box9)
        self.box10 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box10.center_x = 1950
        self.box10.center_y = 1490
        self.platforms_list.append(self.box10)
        self.box11 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box11.center_x = 1950
        self.box11.center_y = 1547
        self.platforms_list.append(self.box11)
        self.box12 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box12.center_x = 1750
        self.box12.center_y = 1490
        self.platforms_list.append(self.box12)
        self.box13 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box13.center_x = 1560
        self.box13.center_y = 1490
        self.platforms_list.append(self.box13)
        self.box14 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box14.center_x = 1380
        self.box14.center_y = 1490
        self.platforms_list.append(self.box14)
        self.box15 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box15.center_x = 1200
        self.box15.center_y = 1490
        self.platforms_list.append(self.box15)
        self.box16 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box16.center_x = 950
        self.box16.center_y = 1485
        self.platforms_list.append(self.box16)
        self.box17 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box17.center_x = 950
        self.box17.center_y = 1530
        self.platforms_list.append(self.box17)
        self.box18 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box18.center_x = 750
        self.box18.center_y = 1485
        self.platforms_list.append(self.box18)
        self.box19 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box19.center_x = 750
        self.box19.center_y = 1530
        self.platforms_list.append(self.box19)
        self.box20 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box20.center_x = 550
        self.box20.center_y = 1485
        self.platforms_list.append(self.box20)
        self.box21 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box21.center_x = 550
        self.box21.center_y = 1530
        self.platforms_list.append(self.box21)
        self.box22 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box22.center_x = 650
        self.box22.center_y = 1630
        self.platforms_list.append(self.box22)
        self.box23 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box23.center_x = 1600
        self.box23.center_y = 2020
        self.platforms_list.append(self.box23)
        self.box24 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box24.center_x = 1800
        self.box24.center_y = 2020
        self.platforms_list.append(self.box24)
        self.box25 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box25.center_x = 1800
        self.box25.center_y = 1956
        self.platforms_list.append(self.box25)
        self.box26 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box26.center_x = 2000
        self.box26.center_y = 1820
        self.platforms_list.append(self.box26)
        self.box27 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box27.center_x = 2150
        self.box27.center_y = 1820
        self.platforms_list.append(self.box27)
        self.box28 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box28.center_x = 2150
        self.box28.center_y = 1884
        self.platforms_list.append(self.box28)
        self.box29 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box29.center_x = 2300
        self.box29.center_y = 1820
        self.platforms_list.append(self.box29)
        self.box30 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box30.center_x = 2450
        self.box30.center_y = 1820
        self.platforms_list.append(self.box30)
        self.box31 = arcade.Sprite("./Resources/Images/box.png", 0.5)
        self.box31.center_x = 2450
        self.box31.center_y = 1884
        self.platforms_list.append(self.box31)
        self.box32 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box32.center_x = 2620
        self.box32.center_y = 1810
        self.platforms_list.append(self.box32)
        self.box33 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box33.center_x = 2620
        self.box33.center_y = 1850
        self.platforms_list.append(self.box33)
        self.box34 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box34.center_x = 2820
        self.box34.center_y = 1810
        self.platforms_list.append(self.box34)
        self.box35 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box35.center_x = 2820
        self.box35.center_y = 1850
        self.platforms_list.append(self.box35)
        self.box36 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box36.center_x = 3020
        self.box36.center_y = 1810
        self.platforms_list.append(self.box36)
        self.box37 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box37.center_x = 3020
        self.box37.center_y = 1850
        self.platforms_list.append(self.box37)
        self.box38 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box38.center_x = 3220
        self.box38.center_y = 1810
        self.platforms_list.append(self.box38)
        self.box39 = arcade.Sprite("./Resources/Images/box.png", 0.4)
        self.box39.center_x = 3220
        self.box39.center_y = 1850
        self.platforms_list.append(self.box39)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 770
        box.center_y = 880
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 1520
        box.center_y = 850
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 1370
        box.center_y = 880
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 920
        box.center_y = 880
        self.platforms_list.append(box)
        box = arcade.Sprite("./Resources/Images/box.png", 0.5)
        box.center_x = 620
        box.center_y = 880
        self.platforms_list.append(box)

        button = arcade.Sprite("./Resources/Images/button.png", 0.5)
        button.center_x = 3333
        button.center_y = 1161
        button_2 = arcade.Sprite("./Resources/Images/button_2.png", 0.5)
        button_2.center_x = 3333
        button_2.center_y = 1161
        self.button_list.append(button)
        self.button_list.append(button_2)

        ball = Ball("./Resources/Images/ball.png", 0.5)
        ball.center_x = 3500
        ball.center_y = 1750
        self.ball_list.append(ball)
        ball = Ball("./Resources/Images/ball.png", 0.5)
        ball.center_x = 3650
        ball.center_y = 1750
        self.ball_list.append(ball)
        ball = Ball("./Resources/Images/ball.png", 0.5)
        ball.center_x = 3800
        ball.center_y = 1490
        self.ball_list.append(ball)
        ball = Ball("./Resources/Images/ball.png", 0.5)
        ball.center_x = 2490
        ball.center_y = 1750
        self.ball_list.append(ball)
        ball = Ball("./Resources/Images/ball.png", 0.5)
        ball.center_x = 2900
        ball.center_y = 1490
        self.ball_list.append(ball)
        ball = Ball("./Resources/Images/ball.png", 0.5)
        ball.center_x = 1750
        ball.center_y = 1415
        self.ball_list.append(ball)
        ball = Ball("./Resources/Images/ball.png", 0.5)
        ball.center_x = 1560
        ball.center_y = 1415
        self.ball_list.append(ball)
        ball = Ball("./Resources/Images/ball.png", 0.5)
        ball.center_x = 1495
        ball.center_y = 1415
        self.ball_list.append(ball)
        ball = Ball("./Resources/Images/ball.png", 0.5)
        ball.center_x = 1380
        ball.center_y = 1415
        self.ball_list.append(ball)
        ball = Ball("./Resources/Images/ball.png", 0.5)
        ball.center_x = 1200
        ball.center_y = 1415
        self.ball_list.append(ball)

        self.robot = arcade.AnimatedTimeBasedSprite()
        for i in range(8):
            texture = arcade.load_texture(f"./Resources/Images/robot_walk{i}.png")
            self.robot.append_texture(texture)
            frame = arcade.AnimationKeyframe(i, 200, texture)
            self.robot.frames.append(frame) 
        self.robot.center_x = 1000
        self.robot.center_y = 1850

        self.robot_2 = arcade.Sprite("./Resources/Images/robot.png", 1)
        self.robot_2.center_x = 1000
        self.robot_2.center_y = 1850
    def on_draw(self):
        arcade.start_render()
        self.camera_sprites.use()
        with self.light_layer:
            self.hallway.draw()
            self.the_secret_room.draw()
            self.bathroom.draw()
            self.bedroom.draw()
            self.kitchen.draw()
            self.living_room.draw()
            self.the_mysterious_room.draw()
            self.the_mysterious_room_2.draw()
            self.background.draw()
            self.background_2.draw()
            self.background_3.draw()
            self.background_4.draw()
            self.background_5.draw()
            self.background_6.draw()
            self.background_7.draw()
            self.background_8.draw()
            self.background_9.draw()
            self.background_10.draw()
            self.background_11.draw()
            self.background_12.draw()
            self.background_13.draw()
            self.background_14.draw()
            self.background_15.draw()
            self.background_16.draw()
            self.background_17.draw()
            self.background_18.draw()
            self.player_sprite.draw()
            self.obstacles_list.draw()
            self.obstacles_list_2.draw()
            self.obstacles_list_3.draw()
            if self.player_sprite.center_x >= 2350: self.obstacles_list_4[0].draw()
            if self.player_sprite.center_x >= 2400: self.obstacles_list_4[1].draw()
            if self.player_sprite.center_x >= 2450: self.obstacles_list_4[2].draw()
            if self.player_sprite.center_x >= 2500: self.obstacles_list_4[3].draw()
            if self.player_sprite.center_x >= 2550: self.obstacles_list_4[4].draw()
            if self.player_sprite.center_x >= 2600: self.obstacles_list_4[5].draw()
            self.button_list[0].draw()
            if self.emitter: self.emitter.draw()
            self.ball_list.draw()
            if self.flag_35: self.robot.draw()
            else: self.robot_2.draw()
            self.platforms_list.draw()
            self.list.draw()
        self.light_layer.draw(ambient_color = (10, 10, 10))
        self.torch_list.draw()
        arcade.draw_text(f'Money: {self.score}    Lifes: {self.lifes}', -380 + self.player_sprite.center_x, 250 + self.player_sprite.center_y, arcade.color.BLACK, 20)
        self.exit_sprite.draw()
        self.camera_gui.use()
    def update(self, delta_time):
        self.set_update_rate(1/110)
        self.physics_engine.update()
        self.robot.update_animation()
        self.player_sprite.update_animation()
        self.platforms_list.update()
        if self.emitter: self.emitter.update()
        self.scroll_to_player()
        
        if self.player_sprite.center_x <= 3400 and self.player_sprite.center_x > 2480:
            for ball in self.ball_list[:3]:
                ball.follow_sprite(self.player_sprite) 
                if self.player_sprite.collides_with_sprite(ball):
                    ball.center_x = 10000
                    self.lifes -= 0.5
                if (ball.collides_with_sprite(self.box) or ball.collides_with_sprite(self.box2) or ball.collides_with_sprite(self.box3) or
                ball.collides_with_sprite(self.box4) or ball.collides_with_sprite(self.box5) or ball.collides_with_sprite(self.box6)):
                    if not self.flag_33:
                        ball.center_x = 10000
                        self.flag_33 = True
                else:
                    self.flag_33 = False
        if self.player_sprite.center_x <= 2480 and self.player_sprite.center_x > 1850 or self.flag_34:
            for ball in self.ball_list[3:5]:
                ball.follow_sprite(self.player_sprite)
                if self.player_sprite.collides_with_sprite(ball):
                    ball.center_x = 10000
                    self.lifes -= 0.5
                if (ball.collides_with_sprite(self.box3) or ball.collides_with_sprite(self.box4) or ball.collides_with_sprite(self.box5)
                or ball.collides_with_sprite(self.box6)) or ball.collides_with_sprite(self.box7) or ball.collides_with_sprite(self.box8):
                    if not self.flag_33:
                        ball.center_x = 10000
                        self.flag_33 = True
                else:
                    self.flag_33 = False
            self.flag_34 = True
        if self.player_sprite.center_x <= 1840:
            ball = self.ball_list[5]
            ball.follow_sprite(self.player_sprite)
            if self.player_sprite.collides_with_sprite(ball):
                ball.center_x = 10000
                self.lifes -= 0.5
        if self.player_sprite.center_x <= 1655:
            ball = self.ball_list[6]
            ball.follow_sprite(self.player_sprite)
            if self.player_sprite.collides_with_sprite(ball):
                ball.center_x = 10000
                self.lifes -= 0.5
        if self.player_sprite.center_x <= 1485:
            ball = self.ball_list[7]
            ball.follow_sprite(self.player_sprite)
            if self.player_sprite.collides_with_sprite(ball):
                ball.center_x = 10000
                self.lifes -= 0.5
        if self.player_sprite.center_x <= 1315:
            ball = self.ball_list[8]
            ball.follow_sprite(self.player_sprite)
            if self.player_sprite.collides_with_sprite(ball):
                ball.center_x = 10000
                self.lifes -= 0.5
        if self.player_sprite.center_x <= 1150:
            ball = self.ball_list[9]
            ball.follow_sprite(self.player_sprite)
            if self.player_sprite.collides_with_sprite(ball):
                ball.center_x = 10000
                self.lifes -= 0.5
        
        if self.lifes == 0:
            self.game_over()
        
        if self.player_sprite.center_x >= 450 and not self.flag:
            light = Light(600, 300, 600, arcade.csscolor.WHITE, 'soft')
            self.light_layer.add(light)
            self.flag = True
        if self.player_sprite.center_x >= 1200 and not self.flag_2:
            light = Light(1400, 300, 600, arcade.csscolor.WHITE, 'soft')
            self.light_layer.add(light)
            self.flag_2 = True
        if self.player_sprite.center_x >= 1900 and not self.flag_3:
            light = Light(2260, 300, 800, arcade.csscolor.WHITE, 'soft')
            self.light_layer.add(light)
            self.flag_3 = True
        if self.player_sprite.center_x >= 2800 and not self.flag_4:
            light = Light(2998, 300, 600, arcade.csscolor.WHITE, 'soft')
            self.light_layer.add(light)
            self.flag_4 = True
        if self.player_sprite.center_x >= 3300 and not self.flag_5:
            light = Light(3535, 300, 600, arcade.csscolor.WHITE, 'soft')
            self.light_layer.add(light)
            self.flag_5 = True
        if self.player_sprite.center_y >= 900 and not self.flag_9:
            light = Light(3400, 1000, 10000, arcade.csscolor.WHITE, 'soft')
            self.light_layer.add(light)
            self.flag_9 = True
        
        if self.flag_6 == False and self.player_sprite.center_x >= 890 and self.player_sprite.center_x <= 980:
            self.start_time = __import__('time').time()
            self.flag_6 = True
        if self.flag_6 == True and (self.player_sprite.center_x < 890 or self.player_sprite.center_x > 980):
            self.flag_6 = False
        if self.flag_6 == True and __import__('time').time() - self.start_time >= 3:
            self.player_sprite.center_x = 760
            self.player_sprite.center_y = 500
            self.flag_6 = 'kill'
        if self.flag_6 == 'kill':
            light = Light(760, 609, 600, arcade.csscolor.WHITE, 'soft')
            self.light_layer.add(light)
            self.flag_6 = 'KILL'
        
        if self.flag_7 == False and self.player_sprite.center_x >= 3650 and self.player_sprite.center_x <= 3700:
            self.start_time = __import__('time').time()
            self.flag_7 = True
        if self.flag_7 == True and (self.player_sprite.center_x < 3650 or self.player_sprite.center_x > 3700):
            self.flag_7 = False
        if self.flag_7 == True and __import__('time').time() - self.start_time >= 3:
            self.player_sprite.center_x = 3655
            self.player_sprite.center_y = 1000
            self.flag_7 = 'kill'
        if self.flag_7 == 'kill':
            light = Light(760, 609, 600, arcade.csscolor.WHITE, 'soft')
            self.light_layer.add(light)
            self.flag_7 = 'KILL'
        
        if self.player_sprite.center_x >= self.list[0].center_x - 30:
            self.flag_8 = True
        if self.flag_8:
            if self.list[0].center_y >= 505:
                self.list[0].center_y -= 3
            if self.list[1].center_y >= 505 and self.list[0].center_y <= 650:
                self.list[1].center_y -= 3
            if self.list[2].center_y >= 505 and self.list[1].center_y <= 650:
                self.list[2].center_y -= 3
            if self.list[3].center_y >= 505 and self.list[2].center_y <= 650:
                self.list[3].center_y -= 3
            if self.list[4].center_y >= 505 and self.list[3].center_y <= 650:
                self.list[4].center_y -= 3
            if self.list[5].center_y >= 505 and self.list[4].center_y <= 650:
                self.list[5].center_y -= 3
            if self.list[6].center_y >= 505 and self.list[5].center_y <= 650:
                self.list[6].center_y -= 3
            if self.list[7].center_y >= 505 and self.list[6].center_y <= 650:
                self.list[7].center_y -= 3
            if self.list[8].center_y >= 505 and self.list[7].center_y <= 650:
                self.list[8].center_y -= 3
            if self.list[9].center_y >= 505 and self.list[8].center_y <= 650:
                self.list[9].center_y -= 3
            if self.list[10].center_y >= 505 and self.list[9].center_y <= 650:
                self.list[10].center_y -= 3
            if self.list[11].center_y >= 505 and self.list[10].center_y <= 650:
                self.list[11].center_y -= 3
        
        box_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.obstacles_list)
        for box in box_hit_list:
            self.player_sprite.center_x = 760
            self.lifes -= 0.5
            box.remove_from_sprite_lists()
        
        if not self.flag_10 and self.platforms_list[-4].center_y < 970:
            self.platforms_list[-4].center_y += 1
        elif not self.flag_10 and self.platforms_list[-4].center_y == 970:
            self.flag_10 = True
        elif self.flag_10 and self.platforms_list[-4].center_y > 850:
            self.platforms_list[-4].center_y -= 1
        elif self.flag_10 and self.platforms_list[-4].center_y == 850:
            self.flag_10 = False 

        if not self.flag_11 and self.platforms_list[-3].center_x > 1220:
            self.platforms_list[-3].center_x -= 1
        elif not self.flag_11 and self.platforms_list[-3].center_x == 1220:
            self.flag_11 = True
        elif self.flag_11 and self.platforms_list[-3].center_x < 1370:
            self.platforms_list[-3].center_x += 1
        elif self.flag_11 and self.platforms_list[-3].center_x == 1370:
            self.flag_11 = False 

        if not self.flag_12 and self.platforms_list[-2].center_x < 1070:
            self.platforms_list[-2].center_x += 1
        elif not self.flag_12 and self.platforms_list[-2].center_x == 1070:
            self.flag_12 = True
        elif self.flag_12 and self.platforms_list[-2].center_x > 920:
            self.platforms_list[-2].center_x -= 1
        elif self.flag_12 and self.platforms_list[-2].center_x == 920:
            self.flag_12 = False 
        
        if not self.flag_13 and self.platforms_list[-1].center_x > 470:
            self.platforms_list[-1].center_x -= 1
            self.platforms_list[-1].center_y += 1
        elif not self.flag_13 and self.platforms_list[-1].center_x == 470:
            self.flag_13 = True
        elif self.flag_13 and self.platforms_list[-1].center_x < 620:
            self.platforms_list[-1].center_x += 1
            self.platforms_list[-1].center_y -= 1
        elif self.flag_13 and self.platforms_list[-1].center_x == 620:
            self.flag_13 = False 
        
        if self.player_sprite.center_x >= self.obstacles_list_2[0].center_x:
            self.flag_14 = True
        if self.player_sprite.center_x >= self.obstacles_list_2[1].center_x:
            self.flag_15 = True
        if self.player_sprite.center_x >= self.obstacles_list_2[2].center_x:
            self.flag_16 = True
        if self.player_sprite.center_x >= self.obstacles_list_2[3].center_x:
            self.flag_17 = True
        if self.player_sprite.center_x >= self.obstacles_list_2[4].center_x:
            self.flag_18 = True
        if self.player_sprite.center_x >= self.obstacles_list_2[5].center_x:
            self.flag_19 = True
        
        if self.flag_14 and self.obstacles_list_2[0].center_y > 1100:
            self.obstacles_list_2[0].center_y -= 3
        if self.flag_15 and self.obstacles_list_2[1].center_y > 1100:
            self.obstacles_list_2[1].center_y -= 3
        if self.flag_16 and self.obstacles_list_2[2].center_y > 1100:
            self.obstacles_list_2[2].center_y -= 3
        if self.flag_17 and self.obstacles_list_2[3].center_y > 1100:
            self.obstacles_list_2[3].center_y -= 3
        if self.flag_18 and self.obstacles_list_2[4].center_y > 1100:
            self.obstacles_list_2[4].center_y -= 3
        if self.flag_19 and self.obstacles_list_2[5].center_y > 1100:
            self.obstacles_list_2[5].center_y -= 3
        
        if not self.flag_20 and self.player_sprite.center_x >= 1300 and self.player_sprite.center_y >= 1100:
            self.flag_20 = True
            self.obstacles_list_3[0].center_y = self.player_sprite.center_y
        if not self.flag_21 and self.player_sprite.center_x >= 1350 and self.player_sprite.center_y >= 1100:
            self.flag_21 = True
            self.obstacles_list_3[1].center_y = self.player_sprite.center_y
        if not self.flag_22 and self.player_sprite.center_x >= 1400 and self.player_sprite.center_y >= 1100:
            self.flag_22 = True
            self.obstacles_list_3[2].center_y = self.player_sprite.center_y
        if not self.flag_23 and self.player_sprite.center_x >= 1450 and self.player_sprite.center_y >= 1100:
            self.flag_23 = True
            self.obstacles_list_3[3].center_y = self.player_sprite.center_y
        if not self.flag_24 and self.player_sprite.center_x >= 1500 and self.player_sprite.center_y >= 1100:
            self.flag_24 = True
            self.obstacles_list_3[4].center_y = self.player_sprite.center_y
        if not self.flag_25 and self.player_sprite.center_x >= 1550 and self.player_sprite.center_y >= 1100:
            self.flag_25 = True
            self.obstacles_list_3[5].center_y = self.player_sprite.center_y
        
        if self.flag_20:
            self.obstacles_list_3[0].center_x -= 2
        if self.flag_21:
            self.obstacles_list_3[1].center_x -= 2
        if self.flag_22:
            self.obstacles_list_3[2].center_x -= 2
        if self.flag_23:
            self.obstacles_list_3[3].center_x -= 2
        if self.flag_24:
            self.obstacles_list_3[4].center_x -= 2
        if self.flag_25:  
            self.obstacles_list_3[5].center_x -= 2
        
        if self.player_sprite.collides_with_sprite(self.button_list[0]) and self.flag_32 == False:
            self.button_list[0].remove_from_sprite_lists()
            self.flag_32 = True 
        if self.flag_32 == True:
            self.emitter = arcade.Emitter(
                center_xy = (3440, 1250),
                emit_controller = arcade.EmitBurst(10000),
                particle_factory = lambda emitter: arcade.LifetimeParticle(
                    filename_or_texture = "./Resources/Images/ball.png",
                    change_xy = arcade.rand_in_circle((0, 0), 2),
                    lifetime = 50,
                    scale = 0.3,
                    alpha = 15
                )
            )
            self.flag_32 = 'kill'
        
        if self.player_sprite.center_x >= 750:
            self.flag_35 = True
        if self.flag_35:
            self.robot.center_x += 2.4
        if self.player_sprite.center_x >= 1450 and self.box23.center_y >= 1820:
            self.box23.center_y -= 5
        if self.player_sprite.center_x >= 1600 and self.box24.center_y >= 1820:
            self.box24.center_y -= 2.2
        if self.box24.center_y <= 1820 and self.box25.center_y >= 1881:
            self.box25.center_y -= 2.2
    def game_over(self):
        arcade.close_window()
        arcade.open_window(800, 600, 'Game Over')
        arcade.start_render()
        arcade.set_background_color(arcade.color.BLACK)
        game_over = arcade.load_texture('./Resources/Images/game_over.png')
        game_over.draw_sized(400, 300, 400, 300)
        game_over_sound =  arcade.load_sound('./Resources/Sound effects/game-over.mp3')
        arcade.play_sound(game_over_sound, volume = 2)
        arcade.finish_render()
        arcade.run()
    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        if key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def scroll_to_player(self):
        position = self.player_sprite.center_x - self.width / 2, \
            self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, 0.1)
        
window = Level_11(800, 600, "Super Game")
window.setup()
arcade.run()
