import arcade

JUMP_SPEED = 8
GRAVITY = 0.35

class Level_7(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        self.flag = True
        self.flag_2 = True
        self.flag_3 = False
        self.flag_4 = True
        self.flag_5 = True
        self.flag_6 = False
        self.flag_7 = False
        self.flag_8 = True
        self.flag_9 = False
        self.flag_10 = False
        self.flag_11 = False
        self.flag_12 = False
        self.lifes = 3
        self.score = 0 
        self.score_2 = 1
        self.x = 100
        self.y = 154
        self.cx_ca = 0
        self.MOVEMENT_SPEED = 2.6

        self.camera_sprites = arcade.Camera(800, 600)
        self.camera_gui = arcade.Camera(800, 600)
    def setup(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.platforms_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.flags_list = arcade.SpriteList()
        self.flags_list2 = arcade.SpriteList()
        self.flags_list3 = arcade.SpriteList()
        self.mole_list = arcade.SpriteList()
        self.brown_circle_list = arcade.SpriteList()
        self.mouse_list = arcade.SpriteList()
        self.ferret_list = arcade.SpriteList()

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

        for x in range(33, 3683, 64):
            grass_sprite = arcade.Sprite("./Resources/Images/grass.png", 0.5)
            grass_sprite.center_x = x
            grass_sprite.center_y = 90
            self.platforms_list.append(grass_sprite)
        for x in range(1055, 1248, 64):
            grass_sprite = arcade.Sprite("./Resources/Images/grass.png", 0.5)
            grass_sprite.center_x = x
            grass_sprite.center_y = 154
            self.platforms_list.append(grass_sprite)
        for x in range(2164, 2357, 64):
            grass_sprite = arcade.Sprite("./Resources/Images/grass.png", 0.5)
            grass_sprite.center_x = x
            grass_sprite.center_y = 154
            self.platforms_list.append(grass_sprite)
        for x in range(3362, 3555, 64):
            grass_sprite = arcade.Sprite("./Resources/Images/grass.png", 0.5)
            grass_sprite.center_x = x
            grass_sprite.center_y = 154
            self.platforms_list.append(grass_sprite)
        
        for x in range(3745, 4992, 64):
            snow_grass = arcade.Sprite("./Resources/Images/snow_grass.png", 0.92)
            snow_grass.center_x = x
            snow_grass.center_y = 90
            self.platforms_list.append(snow_grass)
        for x in range(3745, 4992, 64):
            snow_ground = arcade.Sprite("./Resources/Images/snow_ground.png", 0.92)
            snow_ground.center_x = x
            snow_ground.center_y = 26
            self.platforms_list.append(snow_ground)

        for x in range(33, 3683, 64):
            ground_sprite = arcade.Sprite("./Resources/Images/ground.png", 0.5)
            ground_sprite.center_x = x
            ground_sprite.center_y = 26
            self.platforms_list.append(ground_sprite)
        for i in range(0, 321, 64):
            ground_sprite = arcade.Sprite("./Resources/Images/ground.png", 0.5)
            ground_sprite.center_x = -31 - i
            ground_sprite.center_y = 26 - i
            self.platforms_list.append(ground_sprite)
        for i in range(0, 321, 64):
            ground_sprite = arcade.Sprite("./Resources/Images/ground.png", 0.5)
            ground_sprite.center_x = -31 - i
            ground_sprite.center_y = -38 - i
            self.platforms_list.append(ground_sprite)
        for i in range(0, 321, 64):
            ground_sprite = arcade.Sprite("./Resources/Images/ground.png", 0.5)
            ground_sprite.center_x = 33 - i
            ground_sprite.center_y = -38 - i
            self.platforms_list.append(ground_sprite)
        for i in range(0, 449, 64):
            ground_sprite = arcade.Sprite("./Resources/Images/ground.png", 0.5)
            ground_sprite.center_x = 5025 + i
            ground_sprite.center_y = 90 + i
            self.platforms_list.append(ground_sprite)
        for i in range(0, 449, 64):
            ground_sprite = arcade.Sprite("./Resources/Images/ground.png", 0.5)
            ground_sprite.center_x = 5025 + i
            ground_sprite.center_y = 26 + i
            self.platforms_list.append(ground_sprite)
        for i in range(0, 449, 64):
            ground_sprite = arcade.Sprite("./Resources/Images/ground.png", 0.5)
            ground_sprite.center_x = 5089 + i
            ground_sprite.center_y = 26 + i
            self.platforms_list.append(ground_sprite)
        for x in range(1311, 2101, 64):
            ground_sprite = arcade.Sprite("./Resources/Images/ground.png", 0.5)
            ground_sprite.center_x = x
            ground_sprite.center_y = -38
            self.platforms_list.append(ground_sprite)
        for x in range(1311, 2101, 64):
            ground_sprite = arcade.Sprite("./Resources/Images/ground.png", 0.5)
            ground_sprite.center_x = x
            ground_sprite.center_y = -102
            self.platforms_list.append(ground_sprite)
        for x in range(1311, 2101, 64):
            ground_sprite = arcade.Sprite("./Resources/Images/ground.png", 0.5)
            ground_sprite.center_x = x
            ground_sprite.center_y = -166
            self.platforms_list.append(ground_sprite)
        for x in range(1375, 2101, 64):
            ground_sprite = arcade.Sprite("./Resources/Images/ground.png", 0.5)
            ground_sprite.center_x = x
            ground_sprite.center_y = 90
            self.platforms_list.append(ground_sprite)
        
        for x in range(200, 941, 64):
            coin_sprite = arcade.Sprite("./Resources/Images/gold.png", 0.5)
            coin_sprite.center_x = x
            coin_sprite.center_y = 144
            self.coin_list.append(coin_sprite)
        for x in range(1119, 1248, 64):
            coin_sprite = arcade.Sprite("./Resources/Images/gold.png", 0.5)
            coin_sprite.center_x = x
            coin_sprite.center_y = 218
            self.coin_list.append(coin_sprite)
        for x in range(2228, 2357, 64):
            coin_sprite = arcade.Sprite("./Resources/Images/gold.png", 0.5)
            coin_sprite.center_x = x
            coin_sprite.center_y = 218
            self.coin_list.append(coin_sprite)
        for x in range(3426, 3555, 64):
            coin_sprite = arcade.Sprite("./Resources/Images/gold.png", 0.5)
            coin_sprite.center_x = x
            coin_sprite.center_y = 218
            self.coin_list.append(coin_sprite)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.platforms_list, gravity_constant = GRAVITY)

        grass_hill_sprite = arcade.Sprite("./Resources/Images/grass_hill.png", 0.5)
        grass_hill_sprite.center_x = 991
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resources/Images/grasshill.png", 0.5)
        grass_hill_sprite.center_x = 1311
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resources/Images/grass_hill.png", 0.5)
        grass_hill_sprite.center_x = 2120
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resources/Images/grasshill.png", 0.5)
        grass_hill_sprite.center_x = 2420
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resources/Images/grass_hill.png", 0.5)
        grass_hill_sprite.center_x = 3298
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resources/Images/grasshill.png", 0.5)
        grass_hill_sprite.center_x = 3618
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        for i in range(0, 321, 64):
            grass_hill_sprite = arcade.Sprite("./Resources/Images/grass_hill.png", 0.5)
            grass_hill_sprite.center_x = -31 - i
            grass_hill_sprite.center_y = 90 - i
            self.platforms_list.append(grass_hill_sprite)
        for i in range(0, 385, 64):
            grass_hill_sprite = arcade.Sprite("./Resources/Images/grass_hill.png", 0.5)
            grass_hill_sprite.center_x = 5025 + i
            grass_hill_sprite.center_y = 154 + i
            self.platforms_list.append(grass_hill_sprite)

        self.FLAG = arcade.Sprite("./Resources/Images/flagRed.png", 0.5)
        self.FLAG.center_x = 1061
        self.FLAG.center_y = 218
        self.flags_list.append(self.FLAG)
        Flag = arcade.Sprite("./Resources/Images/flagRed1.png", 0.5)
        Flag.center_x = 1061
        Flag.center_y = 218
        self.flags_list.append(Flag)
        self.FLAG2 = arcade.Sprite("./Resources/Images/flagRed.png", 0.5)
        self.FLAG2.center_x = 2190
        self.FLAG2.center_y = 218
        self.flags_list2.append(self.FLAG2)
        Flag2 = arcade.Sprite("./Resources/Images/flagRed1.png", 0.5)
        Flag2.center_x = 2190
        Flag2.center_y = 218
        self.flags_list2.append(Flag2)
        self.FLAG3 = arcade.Sprite("./Resources/Images/flagRed.png", 0.5)
        self.FLAG3.center_x = 3367
        self.FLAG3.center_y = 218
        self.flags_list3.append(self.FLAG3)
        Flag3 = arcade.Sprite("./Resources/Images/flagRed1.png", 0.5)
        Flag3.center_x = 3367
        Flag3.center_y = 218
        self.flags_list3.append(Flag3)

        self.exit_sprite = arcade.Sprite("./Resources/Images/exit.png", 0.5)
        self.exit_sprite.center_x = 4917
        self.exit_sprite.center_y = 154

        self.mole_sprite = arcade.Sprite('./Resources/Images/mole.png', 0.5, angle = 90)
        self.mole_sprite.center_x = 1459
        self.mole_sprite.center_y = -960
        mole_sprite_2 = arcade.Sprite('./Resources/Images/mole_2.png', 0.5, angle = -8)
        mole_sprite_2.center_x = 1952
        mole_sprite_2.center_y = 168
        self.mole_list.append(self.mole_sprite)
        self.mole_list.append(mole_sprite_2)

        mouse_sprite = arcade.Sprite("./Resources/Images/mouse.png", 0.9)
        mouse_sprite.center_x = 2540
        mouse_sprite.center_y = 210
        mouse_sprite_2 = arcade.Sprite("./Resources/Images/mouse_2.png", 0.9)
        mouse_sprite_2.center_x = 3161
        mouse_sprite_2.center_y = 210
        self.mouse_list.append(mouse_sprite_2)
        self.mouse_list.append(mouse_sprite)

        ferret_sprite = arcade.Sprite("./Resources/Images/ferret.png", 0.6)
        ferret_sprite.center_x = 3783
        ferret_sprite.center_y = 168
        ferret_sprite_2 = arcade.Sprite("./Resources/Images/ferret_2.png", 0.6)
        ferret_sprite_2.center_x = 4800
        ferret_sprite_2.center_y = 168
        self.ferret_list.append(ferret_sprite_2)
        self.ferret_list.append(ferret_sprite)

        for i in range(0, 71, 10):
            brown_circle_sprite = arcade.Sprite("./Resources/Images/brown_circle.png", 0.04)
            brown_circle_sprite.center_x = 1459 + i
            brown_circle_sprite.center_y = 100
            self.brown_circle_list.append(brown_circle_sprite)
        for i in range(0, 71, 10):
            brown_circle_sprite = arcade.Sprite("./Resources/Images/brown_circle.png", 0.04)
            brown_circle_sprite.center_x = 1459 + i
            brown_circle_sprite.center_y = 100
            self.brown_circle_list.append(brown_circle_sprite)
        for i in range(0, 71, 10):
            brown_circle_sprite = arcade.Sprite("./Resources/Images/brown_circle.png", 0.04)
            brown_circle_sprite.center_x = 1459 + i
            brown_circle_sprite.center_y = 80
            self.brown_circle_list.append(brown_circle_sprite)
        for i in range(0, 71, 10):
            brown_circle_sprite = arcade.Sprite("./Resources/Images/brown_circle.png", 0.04)
            brown_circle_sprite.center_x = 1459 + i
            brown_circle_sprite.center_y = 80
            self.brown_circle_list.append(brown_circle_sprite)
        for i in range(0, 71, 10):
            brown_circle_sprite = arcade.Sprite("./Resources/Images/brown_circle.png", 0.04)
            brown_circle_sprite.center_x = 1459 + i
            brown_circle_sprite.center_y = 60
            self.brown_circle_list.append(brown_circle_sprite)
        for i in range(0, 71, 10):
            brown_circle_sprite = arcade.Sprite("./Resources/Images/brown_circle.png", 0.04)
            brown_circle_sprite.center_x = 1459 + i
            brown_circle_sprite.center_y = 60
            self.brown_circle_list.append(brown_circle_sprite)
        for i in range(0, 71, 10):
            brown_circle_sprite = arcade.Sprite("./Resources/Images/brown_circle.png", 0.04)
            brown_circle_sprite.center_x = 1459 + i
            brown_circle_sprite.center_y = 100
            self.brown_circle_list.append(brown_circle_sprite)
        for i in range(0, 71, 10):
            brown_circle_sprite = arcade.Sprite("./Resources/Images/brown_circle.png", 0.04)
            brown_circle_sprite.center_x = 1459 + i
            brown_circle_sprite.center_y = 100
            self.brown_circle_list.append(brown_circle_sprite)
        for i in range(0, 71, 10):
            brown_circle_sprite = arcade.Sprite("./Resources/Images/brown_circle.png", 0.04)
            brown_circle_sprite.center_x = 1459 + i
            brown_circle_sprite.center_y = 80
            self.brown_circle_list.append(brown_circle_sprite)
        for i in range(0, 71, 10):
            brown_circle_sprite = arcade.Sprite("./Resources/Images/brown_circle.png", 0.04)
            brown_circle_sprite.center_x = 1459 + i
            brown_circle_sprite.center_y = 80
            self.brown_circle_list.append(brown_circle_sprite)
        for i in range(0, 71, 10):
            brown_circle_sprite = arcade.Sprite("./Resources/Images/brown_circle.png", 0.04)
            brown_circle_sprite.center_x = 1459 + i
            brown_circle_sprite.center_y = 60
            self.brown_circle_list.append(brown_circle_sprite)
        for i in range(0, 71, 10):
            brown_circle_sprite = arcade.Sprite("./Resources/Images/brown_circle.png", 0.04)
            brown_circle_sprite.center_x = 1459 + i
            brown_circle_sprite.center_y = 60
            self.brown_circle_list.append(brown_circle_sprite)
    def on_draw(self):
        arcade.start_render()
        self.camera_sprites.use()
        self.flags_list[0].draw()
        self.flags_list2[0].draw()
        self.flags_list3[0].draw()
        self.player_sprite.draw()
        self.mole_list[0].draw()
        self.ferret_list[0].draw()
        if self.brown_circle_list[48].center_y > 40: self.brown_circle_list.draw()
        self.mouse_list[0].draw()
        self.platforms_list.draw()
        self.coin_list.draw()
        arcade.draw_text(f'Money: {self.score}    Lifes: {self.lifes}', -380 + self.player_sprite.center_x, 250 + self.player_sprite.center_y, arcade.color.BLACK, 20)
        self.exit_sprite.draw()
        self.camera_gui.use()
    def update(self, delta_time):
        self.set_update_rate(1/110)
        self.physics_engine.update()
        self.player_sprite.update_animation()
        self.platforms_list.update()
        self.mole_list.update()
        self.coin_list.update()
        self.scroll_to_player()

        if self.lifes == 0:
            self.game_over()

        if self.player_sprite.center_x <= -130:
            self.close()
            from level_6 import Level_6
        elif self.player_sprite.center_x >= 5079:
            self.close()
            from level_8 import Level_8

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 10
        
        if self.player_sprite.center_x >= 1089 and self.player_sprite.center_x < 2198 and self.flag_4:
            self.FLAG.remove_from_sprite_lists()
            self.x = 1189
            self.y = 218
        elif self.player_sprite.center_x >= 2198 and self.player_sprite.center_x < 3395 and self.flag_5:
            self.FLAG2.remove_from_sprite_lists()
            self.x = 2698
            self.y = 218
            self.flag_4 = False
        elif self.player_sprite.center_x >= 3395:
            self.FLAG3.remove_from_sprite_lists()
            self.x = 3228
            self.y = 218
            self.flag_5 = False
        
        if self.flag_9: 
            if self.flag:
                for i in range(0, 4):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x -= 0.2
                for i in range(4, 8):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x += 0.2
                for i in range(8, 12):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x -= 1
                for i in range(12, 16):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x += 1
                for i in range(16, 20):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x -= 0.4
                for i in range(20, 24):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x += 0.4
                for i in range(24, 28):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x -= 1.2
                for i in range(28, 32):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x += 1.2
                for i in range(32, 36):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x -= 0.6
                for i in range(36, 40):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x += 0.6
                for i in range(40, 44):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x -= 1.4
                for i in range(44, 48):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x += 1.4
            elif not self.flag and self.flag_2:
                for i in range(48, 52):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x -= 0.2
                for i in range(52, 56):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x += 0.2
                for i in range(56, 60):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x -= 1
                for i in range(60, 64):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x += 1
                for i in range(64, 68):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x -= 0.4
                for i in range(68, 72):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x += 0.4
                for i in range(72, 76):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x -= 1.2
                for i in range(76, 80):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x += 1.2
                for i in range(80, 84):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x -= 0.6
                for i in range(84, 88):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x += 0.6
                for i in range(88, 92):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x -= 1.4
                for i in range(92, 96):
                    self.brown_circle_list[i].center_y += 2
                    self.brown_circle_list[i].center_x += 1.4

                if self.brown_circle_list[0].center_x >= 1400:
                    for i in range(0, 4):
                        self.brown_circle_list[i].center_x -= 2
                    for i in range(4, 8):
                        self.brown_circle_list[i].center_x += 2
                    for i in range(8, 12):
                        self.brown_circle_list[i].center_x -= 2
                    for i in range(12, 16):
                        self.brown_circle_list[i].center_x += 2
                    for i in range(16, 20):
                        self.brown_circle_list[i].center_x -= 2
                    for i in range(20, 24):
                        self.brown_circle_list[i].center_x += 2
                    for i in range(24, 28):
                        self.brown_circle_list[i].center_x -= 2
                    for i in range(28, 32):
                        self.brown_circle_list[i].center_x += 2
                    for i in range(32, 36):
                        self.brown_circle_list[i].center_x -= 2
                    for i in range(36, 40):
                        self.brown_circle_list[i].center_x += 2
                    for i in range(40, 44):
                        self.brown_circle_list[i].center_x -= 2
                    for i in range(44, 48):
                        self.brown_circle_list[i].center_x += 2
                else: 
                    for i in range(0, 4):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x -= 0.8
                    for i in range(4, 8):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x += 0.8
                    for i in range(8, 12):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x -= 0.8
                    for i in range(12, 16):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x += 0.8
                    for i in range(16, 20):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x -= 0.8
                    for i in range(20, 24):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x += 0.8
                    for i in range(24, 28):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x -= 0.8
                    for i in range(28, 32):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x += 0.8
                    for i in range(32, 36):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x -= 0.8
                    for i in range(36, 40):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x += 0.8
                    for i in range(40, 44):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x -= 0.8
                    for i in range(44, 48):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x += 0.8
            elif not self.flag and not self.flag_2:
                if self.brown_circle_list[48].center_x >= 1400:
                    for i in range(48, 52):
                        self.brown_circle_list[i].center_x -= 2
                    for i in range(52, 56):
                        self.brown_circle_list[i].center_x += 2
                    for i in range(56, 60):
                        self.brown_circle_list[i].center_x -= 2
                    for i in range(60, 64):
                        self.brown_circle_list[i].center_x += 2
                    for i in range(64, 68):
                        self.brown_circle_list[i].center_x -= 2
                    for i in range(68, 72):
                        self.brown_circle_list[i].center_x += 2
                    for i in range(72, 76):
                        self.brown_circle_list[i].center_x -= 2
                    for i in range(76, 80):
                        self.brown_circle_list[i].center_x += 2
                    for i in range(80, 84):
                        self.brown_circle_list[i].center_x -= 2
                    for i in range(84, 88):
                        self.brown_circle_list[i].center_x += 2
                    for i in range(88, 92):
                        self.brown_circle_list[i].center_x -= 2
                    for i in range(92, 96):
                        self.brown_circle_list[i].center_x += 2
                else:
                    for i in range(48, 52):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x -= 0.8
                    for i in range(52, 56):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x += 0.8
                    for i in range(56, 60):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x -= 0.8
                    for i in range(60, 64):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x += 0.8
                    for i in range(64, 68):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x -= 0.8
                    for i in range(68, 72):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x += 0.8
                    for i in range(72, 76):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x -= 0.8
                    for i in range(76, 80):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x += 0.8
                    for i in range(80, 84):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x -= 0.8
                    for i in range(84, 88):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x += 0.8
                    for i in range(88, 92):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x -= 0.8
                    for i in range(92, 96):
                        self.brown_circle_list[i].center_y -= 2
                        self.brown_circle_list[i].center_x += 0.8

            if self.brown_circle_list[0].center_y >= 400:
                self.flag = False
            if self.brown_circle_list[48].center_y >= 400:
                self.flag_2 = False
            
            if self.mole_sprite.center_y <= 270 and self.flag_8: 
                self.mole_sprite.center_y += 2
                self.cx_ca += 1
                if self.cx_ca < 750:
                    self.mole_sprite.change_angle = -0.1
                    self.mole_sprite.center_x += 0.1
                else:
                    self.mole_sprite.change_angle = 0
            else:
                if self.mole_list[0].center_y > 168:
                    self.mole_list[0].center_y -= 2
                    self.mole_sprite.change_angle = -0.4
                else:
                    self.mole_sprite.change_angle = 0
                self.flag_8 = False

        if self.player_sprite.center_x >= 1247:
            self.flag_9 = True

        if self.mole_list[0].collides_with_sprite(self.player_sprite) and self.flag_10 != 'kill':       
            if self.flag_8:
                self.player_sprite.change_y = 10
            else:
                self.lifes -= 1
                self.player_sprite.center_x = self.x
                self.player_sprite.center_y = self.y
        
        if self.flag_3 == False and not self.flag_8 and self.mole_list[0].center_x < 1952:
            self.mole_list[0].center_x += 3
        elif self.flag_3 == False and not self.flag_8 and self.mole_list[0].center_x >= 1952.599999999944:
            self.mole_list[0].remove_from_sprite_lists()
            self.flag_3 = True
        if self.flag_3 == True:
            flag = self.mole_list[0].center_x - self.player_sprite.center_x
            if (flag <= 200 and flag >= 0) and self.mole_list[0].center_x > 1755:
                self.flag_6 = True
            elif self.mole_list[0].center_x <= 1755:
                self.flag_6 = False
            if (flag <= 200 and flag >= 0) and self.mole_list[0].center_x <= 1755 and self.mole_list[0].center_x > 1459:
                self.flag_7 = True
            elif self.mole_list[0].center_x <= 1459:
                self.flag_7 = "false"
            if self.flag_6:
                self.mole_list[0].center_x -= 3
            if self.flag_7 == True:
                self.mole_list[0].center_x -= 3
            elif self.flag_7 == 'false':
                self.mole_sprite = arcade.Sprite('./Resources/Images/mole.png', 0.5, angle = 8)
                self.mole_sprite.center_x = 1459
                self.mole_sprite.center_y = 168
                self.mole_list.insert(0, self.mole_sprite)
                self.flag_10 = True
                self.flag_3 = 'kill'

        if self.flag_10 == True:
            if self.mole_list[0].center_x < 1952:
                self.mole_list[0].center_x += 3
            elif self.mole_list[0].center_x >= 1952:
                self.mole_list[0].remove_from_sprite_lists()
                self.flag_10 = 'kill'
                self.mole_list[0].center_x = 1952
        elif self.flag_10 == 'kill':
            self.mole_list[0].center_y -= 0.05
        
        if self.flag_11 == False and self.mouse_list[0].center_x > 2540:
            self.mouse_list[0].center_x -= 3
        elif self.flag_11 == False and self.mouse_list[0].center_x == 2540:
            self.mouse_list[0].remove_from_sprite_lists()
            self.flag_11 = True
            self.mouse_list[0].center_x = 2540
        if self.flag_11 == True and self.mouse_list[0].center_x < 3161:
            self.mouse_list[0].center_x += 3
        elif self.flag_11 == True and self.mouse_list[0].center_x == 3161:
            mouse_sprite_2 = arcade.Sprite("./Resources/Images/mouse_2.png", 0.9)
            mouse_sprite_2.center_x = 3161
            mouse_sprite_2.center_y = 210
            self.mouse_list.insert(0, mouse_sprite_2)
            self.flag_11 = False
        
        if self.mouse_list[0].collides_with_sprite(self.player_sprite):
            if self.player_sprite.center_y >= 210:
                self.player_sprite.change_y = 8
            else:
                self.lifes -= 1
                self.player_sprite.center_x = self.x
                self.player_sprite.center_y = self.y
        
        if self.player_sprite.center_x > 4200 and self.flag_12 == False:
            self.ferret_list[0].center_y = (self.player_sprite.center_x - self.ferret_list[0].center_x) / 10 + 160
            if self.ferret_list[0].center_y >= 130:
                self.flag_12 = True
        elif self.flag_12 == True:
            if self.ferret_list[0].center_y < 168:
                self.ferret_list[0].center_y += 3
            else:
                self.flag_12 = 'kill'
        elif self.flag_12 == 'kill' or self.flag_12 == 'KILL':
            if self.flag_12 == 'kill' and self.ferret_list[0].center_x > 3783:
                self.ferret_list[0].center_x -= 3
            elif self.flag_12 == 'kill' and self.ferret_list[0].center_x == 3783:
                self.ferret_list[0].remove_from_sprite_lists()
                self.flag_12 = 'KILL'
                self.ferret_list[0].center_x = 3783
            if self.flag_12 == 'KILL' and self.ferret_list[0].center_x < 4800:
                self.ferret_list[0].center_x += 3
            elif self.flag_12 == 'KILL' and self.ferret_list[0].center_x == 4800:
                ferret_sprite_2 = arcade.Sprite("./Resources/Images/ferret_2.png", 0.6)
                ferret_sprite_2.center_x = 4800
                ferret_sprite_2.center_y = 168
                self.ferret_list.insert(0, ferret_sprite_2)
                self.flag_12 = 'kill'
        
        if self.ferret_list[0].collides_with_sprite(self.player_sprite):
            if self.player_sprite.center_y >= 210:
                self.player_sprite.change_y = 8
            else:
                self.lifes -= 1
                self.player_sprite.center_x = self.x
                self.player_sprite.center_y = self.y
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
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -self.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = self.MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def scroll_to_player(self):
        position = self.player_sprite.center_x - self.width / 2, \
            self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, 0.1)
        
window = Level_7(800, 600, "Super Game")
window.setup()
arcade.run()
