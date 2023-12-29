import arcade

JUMP_SPEED = 8
GRAVITY = 0.35

class Level_8(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        self.flag = False
        self.flag_2 = False
        self.flag_3 = False
        self.flag_4 = True
        self.flag_5 = True
        self.flag_6 = True
        self.flag_7 = False
        self.flag_9 = 'q'
        self.flag_10 = False
        self.flag_11 = True
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
        self.rabbit_list = arcade.SpriteList()
        self.hedgehog_list = arcade.SpriteList()
        self.shell_list = arcade.SpriteList()
        self.fox_list = arcade.SpriteList()

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

        for x in range(33, 2485, 64):
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

        for x in range(33, 2485, 64):
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
        
        for x in range(3681, 4992, 64):
            snow_grass = arcade.Sprite("./Resources/Images/snow_grass.png", 0.92)
            snow_grass.center_x = x
            snow_grass.center_y = 90
            self.platforms_list.append(snow_grass)
        for x in range(3681, 4992, 64):
            snow_ground = arcade.Sprite("./Resources/Images/snow_ground.png", 0.92)
            snow_ground.center_x = x
            snow_ground.center_y = 26
            self.platforms_list.append(snow_ground)
        for x in range(2485, 3299, 64):
            snow_grass = arcade.Sprite("./Resources/Images/snow_grass.png", 0.92)
            snow_grass.center_x = x
            snow_grass.center_y = 90
            self.platforms_list.append(snow_grass)
        for x in range(2485, 3299, 64):
            snow_ground = arcade.Sprite("./Resources/Images/snow_ground.png", 0.92)
            snow_ground.center_x = x
            snow_ground.center_y = 26
            self.platforms_list.append(snow_ground)
        for x in range(3363, 3618, 64):
            snow_ground = arcade.Sprite("./Resources/Images/snow_ground.png", 0.92)
            snow_ground.center_x = x
            snow_ground.center_y = 90
            self.platforms_list.append(snow_ground)
        for x in range(3299, 3682, 64):
            snow_ground = arcade.Sprite("./Resources/Images/snow_ground.png", 0.92)
            snow_ground.center_x = x
            snow_ground.center_y = 26
            self.platforms_list.append(snow_ground)
        for x in range(3362, 3555, 64):
            snow_grass = arcade.Sprite("./Resources/Images/snow_grass.png", 0.92)
            snow_grass.center_x = x
            snow_grass.center_y = 154
            self.platforms_list.append(snow_grass)
        
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
        snow_hill = arcade.Sprite("./Resources/Images/snow_hill.png", 0.92)
        snow_hill.center_x = 3298
        snow_hill.center_y = 154
        self.platforms_list.append(snow_hill)
        snow_hill = arcade.Sprite("./Resources/Images/snowhill.png", 0.92)
        snow_hill.center_x = 3618
        snow_hill.center_y = 154
        self.platforms_list.append(snow_hill)
        snow_hill = arcade.Sprite("./Resources/Images/snow_hill_1.png", 0.92)
        snow_hill.center_x = 3617
        snow_hill.center_y = 90
        self.platforms_list.append(snow_hill)
        snow_hill = arcade.Sprite("./Resources/Images/snow_hill_2.png", 0.92)
        snow_hill.center_x = 3299
        snow_hill.center_y = 90
        self.platforms_list.append(snow_hill)
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

        rabbit_sprite = arcade.Sprite("./Resources/Images/rabbit.png", 0.5, angle = 45)
        rabbit_sprite.center_x = 2056
        rabbit_sprite.center_y = 70
        rabbit_sprite_2 = arcade.Sprite("./Resources/Images/rabbit_2.png", 0.4)
        rabbit_sprite_2.center_x = 1780
        rabbit_sprite_2.center_y = 168
        rabbit_sprite_3 = arcade.Sprite("./Resources/Images/rabbit_3.png", 0.4)
        rabbit_sprite_3.center_x = 1376
        rabbit_sprite_3.center_y = 168
        self.rabbit_list.append(rabbit_sprite)
        self.rabbit_list.append(rabbit_sprite_2)
        self.rabbit_list.append(rabbit_sprite_3)

        hedgehog_sprite = arcade.Sprite("./Resources/Images/hedgehog_2.png", 0.3)
        hedgehog_sprite.center_x = 3188
        hedgehog_sprite.center_y = 180
        hedgehog_sprite_2 = arcade.Sprite("./Resources/Images/hedgehog.png", 0.3)
        hedgehog_sprite_2.center_x = 2528
        hedgehog_sprite_2.center_y = 180
        self.hedgehog_list.append(hedgehog_sprite)
        self.hedgehog_list.append(hedgehog_sprite_2)

        shell_sprite = arcade.Sprite("./Resources/Images/hedgehog_shell.png", 0.2)
        shell_sprite.center_x = 2528
        shell_sprite.center_y = 500
        shell_sprite_2 = arcade.Sprite("./Resources/Images/hedgehog_shell_2.png", 0.2)
        shell_sprite_2.center_x = 2528
        shell_sprite_2.center_y = 174
        self.shell_list.append(shell_sprite)
        self.shell_list.append(shell_sprite_2)

        fox_sprite = arcade.Sprite("./Resources/Images/fox_2.png", 0.44)
        fox_sprite.center_x = 4700
        fox_sprite.center_y = 60
        fox_sprite_2 = arcade.Sprite("./Resources/Images/fox.png", 0.44)
        fox_sprite_2.center_x = 3761
        fox_sprite_2.center_y = 106
        self.fox_list.append(fox_sprite)
        self.fox_list.append(fox_sprite_2)
    def on_draw(self):
        arcade.start_render()
        self.camera_sprites.use()
        self.flags_list[0].draw()
        self.flags_list2[0].draw()
        self.flags_list3[0].draw()
        self.player_sprite.draw()
        self.rabbit_list[0].draw()
        if (self.flag_7 or not self.flag_7) and self.flag_6: self.hedgehog_list[0].draw()
        else: self.shell_list[0].draw()
        self.fox_list[0].draw()
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
        self.rabbit_list.update()
        self.shell_list.update()
        self.coin_list.update()
        self.scroll_to_player()

        if self.lifes == 0:
            self.game_over()

        if self.player_sprite.center_x <= -130:
            self.close()
            from level_7 import Level_7
        elif self.player_sprite.center_x >= 5079:
            self.close()
            from level_9 import Level_9

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
        
        if self.flag:
            if self.flag_3 == False:
                self.rabbit_list[0].center_x -= 1.5
                self.rabbit_list[0].center_y += 1.5
                self.rabbit_list[0].change_angle = 0.15
            elif self.flag_3 == True and self.rabbit_list[0].center_y > 174:
                self.rabbit_list[0].center_x -= 1.5
                self.rabbit_list[0].center_y -= 1.5
            elif self.flag_3 == True and self.rabbit_list[0].center_y <= 174:
                self.rabbit_list[0].remove_from_sprite_lists()
                self.flag_3 = 'kill'
            elif self.flag_3 == 'kill':
                if not self.flag_2 and self.rabbit_list[0].center_x > 1376:
                    self.rabbit_list[0].center_x -= 4
                elif not self.flag_2 and self.rabbit_list[0].center_x == 1376:
                    self.rabbit_list[0].remove_from_sprite_lists()
                    self.flag_2 = True
                    self.rabbit_list[0].center_x = 1376
                if self.flag_2 and self.rabbit_list[0].center_x < 2056:
                    self.rabbit_list[0].center_x += 4
                elif self.flag_2 and self.rabbit_list[0].center_x == 2056:
                    rabbit_sprite_2 = arcade.Sprite("./Resources/Images/rabbit_2.png", 0.4)
                    rabbit_sprite_2.center_x = 2056
                    rabbit_sprite_2.center_y = 168
                    self.rabbit_list.insert(0, rabbit_sprite_2)
                    self.flag_2 = False
        if self.rabbit_list[0].collides_with_sprite(self.player_sprite):
            if self.player_sprite.center_y >= 210:
                self.player_sprite.change_y = 8
            else:
                self.lifes -= 1
                self.player_sprite.center_x = self.x
                self.player_sprite.center_y = self.y
        
        if self.player_sprite.center_x >= 1700:
            self.flag = True
        
        if self.rabbit_list[0].center_y >= 250:
            self.flag_3 = True
            self.rabbit_list[0].change_angle = 0

        if self.flag_6:
            if self.flag_7 == False and self.hedgehog_list[0].center_x > 2528:
                self.hedgehog_list[0].center_x -= 2
            elif self.flag_7 == False and self.hedgehog_list[0].center_x == 2528:
                self.flag_7 = True
                self.hedgehog_list[0].remove_from_sprite_lists()
                self.hedgehog_list[0].center_x = 2528
            if self.flag_7 == True and self.hedgehog_list[0].center_x >= 2528 and self.hedgehog_list[0].center_x < 3188:
                self.hedgehog_list[0].center_x += 2
            elif self.flag_7 == True and self.hedgehog_list[0].center_x == 3188:
                hedgehog_sprite = arcade.Sprite("./Resources/Images/hedgehog_2.png", 0.3)
                hedgehog_sprite.center_x = 3188
                hedgehog_sprite.center_y = 174
                self.hedgehog_list.insert(0, hedgehog_sprite)
                self.flag_7 = False
        else:
            if self.flag_7 == False and self.shell_list[0].center_x > 2528:
                self.shell_list[0].center_x -= 3
                self.shell_list[0].change_angle = 5
            elif self.flag_7 == False and self.shell_list[0].center_x == 2528:
                self.flag_7 = True
                self.shell_list[0].remove_from_sprite_lists()
                self.shell_list[0].center_x = 2528
            if self.flag_7 == True and self.shell_list[0].center_x >= 2528 and self.shell_list[0].center_x < 3188:
                self.shell_list[0].center_x += 3
                self.shell_list[0].change_angle = 5
            elif self.flag_7 == True and self.shell_list[0].center_x == 3188:
                shell_sprite = arcade.Sprite("./Resources/Images/hedgehog_shell.png", 0.2)
                shell_sprite.center_x = 3188
                shell_sprite.center_y = 174
                self.shell_list.insert(0, shell_sprite)
                self.flag_7 = False
            if self.player_sprite.collides_with_sprite(self.shell_list[0]) and self.player_sprite.center_y >= 184:
                self.player_sprite.change_y = 8
            elif self.player_sprite.collides_with_sprite(self.shell_list[0]) and self.player_sprite.center_y < 184:
                self.lifes -= 1
                self.player_sprite.center_x = self.x 
                self.player_sprite.center_y = self.y
            if self.shell_list[0].center_x == self.flag_8 and self.flag_9 == 'q': self.flag_9 = 'qq' 
            elif self.shell_list[0].center_x == self.flag_8 and self.flag_9 == 'qq': self.flag_9 = 'qqq'
            elif self.shell_list[0].center_x == self.flag_8 and self.flag_9 == 'qqq': self.flag_9 = 'qqqq'
            elif self.shell_list[0].center_x == self.flag_8 and self.flag_9 == 'qqqq':    
                self.flag_6 = True
                self.flag_9 = 'q'
                self.hedgehog_list[0].center_y = 174
                    
        if self.player_sprite.collides_with_sprite(self.hedgehog_list[0]) and self.player_sprite.center_y >= 184:
            self.player_sprite.change_y = 8
            self.flag_6 = False
            self.hedgehog_list[0].center_y = 0
            if self.hedgehog_list[0].center_x % 3 == 0: self.shell_list[0].center_x = self.hedgehog_list[0].center_x - 1
            elif (self.hedgehog_list[0].center_x + 1) % 3 == 0: self.shell_list[0].center_x = self.hedgehog_list[0].center_x
            elif (self.hedgehog_list[0].center_x + 2) % 3 == 0: self.shell_list[0].center_x = self.hedgehog_list[0].center_x + 1
            self.shell_list[0].center_y = 174
            self.flag_8 = self.shell_list[0].center_x
        elif self.player_sprite.collides_with_sprite(self.hedgehog_list[0]) and self.player_sprite.center_y < 184:
            self.lifes -= 1
            self.player_sprite.center_x = self.x 
            self.player_sprite.center_y = self.y 
        
        if self.flag_10:
            if self.flag_11 and self.fox_list[0].center_x >= 4450:
                self.fox_list[0].center_x -= 3
                self.fox_list[0].center_y += 2
            elif self.flag_11 and self.fox_list[0].center_x >= 4200:
                self.fox_list[0].center_x -= 3
                self.fox_list[0].center_y -= 2
            elif self.flag_11 and self.fox_list[0].center_x >= 3950:
                self.fox_list[0].center_x -= 3
                self.fox_list[0].center_y += 2
            elif self.flag_11 and self.fox_list[0].center_x > 3761:
                self.fox_list[0].center_x -= 3
                self.fox_list[0].center_y -= 2
            elif self.flag_11 and self.fox_list[0].center_x == 3761:
                self.fox_list[0].remove_from_sprite_lists()
                self.fox_list[0].center_x = 3761
                self.flag_11 = False
            elif not self.flag_11 and self.fox_list[0].center_x <= 3950:
                self.fox_list[0].center_x += 3
                self.fox_list[0].center_y += 2
            elif not self.flag_11 and self.fox_list[0].center_x <= 4200:
                self.fox_list[0].center_x += 3
                self.fox_list[0].center_y -= 2
            elif not self.flag_11 and self.fox_list[0].center_x <= 4450:
                self.fox_list[0].center_x += 3
                self.fox_list[0].center_y += 2
            elif not self.flag_11 and self.fox_list[0].center_x < 4700:
                self.fox_list[0].center_x += 3
                self.fox_list[0].center_y -= 2
            elif not self.flag_11 and self.fox_list[0].center_x == 4700:
                fox_sprite = arcade.Sprite("./Resources/Images/fox_2.png", 0.44)
                fox_sprite.center_x = 4700
                fox_sprite.center_y = 60
                self.fox_list.insert(0, fox_sprite)
                self.flag_11 = True

        if self.player_sprite.center_x >= 4400:
            self.flag_10 = True
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
        
window = Level_8(800, 600, "Super Game")
window.setup()
arcade.run()
