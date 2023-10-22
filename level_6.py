import arcade

JUMP_SPEED = 8
GRAVITY = 0.35

class Level_6(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        self.flag = False
        self.flag_2 = False
        self.flag_3 = False
        self.flag_4 = True
        self.flag_5 = True
        self.flag_6 = False
        self.flag_7 = True
        self.flag_9 = 'q'
        self.lifes = 3
        self.score = 0 
        self.score_2 = 1
        self.x = 100
        self.y = 154
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
        self.scorpion_list = arcade.SpriteList()
        self.snail_list = arcade.SpriteList()
        self.shell_list = arcade.SpriteList()
        self.bogomol_list = arcade.SpriteList()

        self.player_sprite = arcade.AnimatedWalkingSprite() 
        self.player_sprite.center_x = self.x 
        self.player_sprite.center_y = self.y
        self.player_sprite.stand_right_textures = [arcade.load_texture("./Resource/Images/Person.png")]
        self.player_sprite.stand_left_textures = [arcade.load_texture("./Resource/Images/Person.png", mirrored=True)]  
        self.player_sprite.walk_right_textures = [
            arcade.load_texture("./Resource/Images/walk.png"), 
            arcade.load_texture("./Resource/Images/walk1.png"), 
            arcade.load_texture("./Resource/Images/walk2.png"), 
            arcade.load_texture("./Resource/Images/walk3.png"), 
            arcade.load_texture("./Resource/Images/walk4.png"),
            arcade.load_texture("./Resource/Images/walk5.png"), 
            arcade.load_texture("./Resource/Images/walk6.png"), 
            arcade.load_texture("./Resource/Images/walk7.png")]
        self.player_sprite.walk_left_textures = [
            arcade.load_texture("./Resource/Images/walk.png", mirrored=True), 
            arcade.load_texture("./Resource/Images/walk1.png", mirrored=True), 
            arcade.load_texture("./Resource/Images/walk2.png", mirrored=True), 
            arcade.load_texture("./Resource/Images/walk3.png", mirrored=True), 
            arcade.load_texture("./Resource/Images/walk4.png", mirrored=True),
            arcade.load_texture("./Resource/Images/walk5.png", mirrored=True), 
            arcade.load_texture("./Resource/Images/walk6.png", mirrored=True), 
            arcade.load_texture("./Resource/Images/walk7.png", mirrored=True)]  
        self.player_sprite.texture = self.player_sprite.stand_right_textures[0] 
        self.player_sprite.texture = self.player_sprite.stand_left_textures[0]
        self.player_sprite.scale = 0.5

        for x in range(33, 4962, 64):
            grass_sprite = arcade.Sprite("./Resource/Images/grass.png", 0.5)
            grass_sprite.center_x = x
            grass_sprite.center_y = 90
            self.platforms_list.append(grass_sprite)
        for x in range(1055, 1248, 64):
            grass_sprite = arcade.Sprite("./Resource/Images/grass.png", 0.5)
            grass_sprite.center_x = x
            grass_sprite.center_y = 154
            self.platforms_list.append(grass_sprite)
        for x in range(2164, 2357, 64):
            grass_sprite = arcade.Sprite("./Resource/Images/grass.png", 0.5)
            grass_sprite.center_x = x
            grass_sprite.center_y = 154
            self.platforms_list.append(grass_sprite)
        for x in range(3362, 3555, 64):
            grass_sprite = arcade.Sprite("./Resource/Images/grass.png", 0.5)
            grass_sprite.center_x = x
            grass_sprite.center_y = 154
            self.platforms_list.append(grass_sprite)

        for x in range(33, 4962, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = x
            ground_sprite.center_y = 26
            self.platforms_list.append(ground_sprite)
        for i in range(0, 321, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = -31 - i
            ground_sprite.center_y = 26 - i
            self.platforms_list.append(ground_sprite)
        for i in range(0, 321, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = -31 - i
            ground_sprite.center_y = -38 - i
            self.platforms_list.append(ground_sprite)
        for i in range(0, 321, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = 33 - i
            ground_sprite.center_y = -38 - i
            self.platforms_list.append(ground_sprite)
        for i in range(0, 449, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = 5025 + i
            ground_sprite.center_y = 90 + i
            self.platforms_list.append(ground_sprite)
        for i in range(0, 449, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = 5025 + i
            ground_sprite.center_y = 26 + i
            self.platforms_list.append(ground_sprite)
        for i in range(0, 449, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = 5089 + i
            ground_sprite.center_y = 26 + i
            self.platforms_list.append(ground_sprite)
        
        for x in range(200, 941, 64):
            coin_sprite = arcade.Sprite("./Resource/Images/gold.png", 0.5)
            coin_sprite.center_x = x
            coin_sprite.center_y = 144
            self.coin_list.append(coin_sprite)
        for x in range(1119, 1248, 64):
            coin_sprite = arcade.Sprite("./Resource/Images/gold.png", 0.5)
            coin_sprite.center_x = x
            coin_sprite.center_y = 218
            self.coin_list.append(coin_sprite)
        for x in range(2228, 2357, 64):
            coin_sprite = arcade.Sprite("./Resource/Images/gold.png", 0.5)
            coin_sprite.center_x = x
            coin_sprite.center_y = 218
            self.coin_list.append(coin_sprite)
        for x in range(3426, 3555, 64):
            coin_sprite = arcade.Sprite("./Resource/Images/gold.png", 0.5)
            coin_sprite.center_x = x
            coin_sprite.center_y = 218
            self.coin_list.append(coin_sprite)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.platforms_list, gravity_constant = GRAVITY)

        grass_hill_sprite = arcade.Sprite("./Resource/Images/grass_hill.png", 0.5)
        grass_hill_sprite.center_x = 991
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resource/Images/grasshill.png", 0.5)
        grass_hill_sprite.center_x = 1311
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resource/Images/grass_hill.png", 0.5)
        grass_hill_sprite.center_x = 2100
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resource/Images/grasshill.png", 0.5)
        grass_hill_sprite.center_x = 2420
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resource/Images/grass_hill.png", 0.5)
        grass_hill_sprite.center_x = 3298
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resource/Images/grasshill.png", 0.5)
        grass_hill_sprite.center_x = 3618
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        for i in range(0, 321, 64):
            grass_hill_sprite = arcade.Sprite("./Resource/Images/grass_hill.png", 0.5)
            grass_hill_sprite.center_x = -31 - i
            grass_hill_sprite.center_y = 90 - i
            self.platforms_list.append(grass_hill_sprite)
        for i in range(0, 385, 64):
            grass_hill_sprite = arcade.Sprite("./Resource/Images/grass_hill.png", 0.5)
            grass_hill_sprite.center_x = 5025 + i
            grass_hill_sprite.center_y = 154 + i
            self.platforms_list.append(grass_hill_sprite)

        self.FLAG = arcade.Sprite("./Resource/Images/flagRed.png", 0.5)
        self.FLAG.center_x = 1061
        self.FLAG.center_y = 218
        self.flags_list.append(self.FLAG)
        Flag = arcade.Sprite("./Resource/Images/flagRed1.png", 0.5)
        Flag.center_x = 1061
        Flag.center_y = 218
        self.flags_list.append(Flag)
        self.FLAG2 = arcade.Sprite("./Resource/Images/flagRed.png", 0.5)
        self.FLAG2.center_x = 2170
        self.FLAG2.center_y = 218
        self.flags_list2.append(self.FLAG2)
        Flag2 = arcade.Sprite("./Resource/Images/flagRed1.png", 0.5)
        Flag2.center_x = 2170
        Flag2.center_y = 218
        self.flags_list2.append(Flag2)
        self.FLAG3 = arcade.Sprite("./Resource/Images/flagRed.png", 0.5)
        self.FLAG3.center_x = 3367
        self.FLAG3.center_y = 218
        self.flags_list3.append(self.FLAG3)
        Flag3 = arcade.Sprite("./Resource/Images/flagRed1.png", 0.5)
        Flag3.center_x = 3367
        Flag3.center_y = 218
        self.flags_list3.append(Flag3)

        self.exit_sprite = arcade.Sprite("./Resource/Images/exit.png", 0.5)
        self.exit_sprite.center_x = 4917
        self.exit_sprite.center_y = 154

        self.scorpion_sprite = arcade.Sprite("./Resource/Images/scorpion_2.png", 0.3)
        self.scorpion_sprite.center_x = 1960
        self.scorpion_sprite.center_y = 180
        scorpion_sprite = arcade.Sprite("./Resource/Images/scorpion.png", 0.3)
        scorpion_sprite.center_x = 1450
        scorpion_sprite.center_y = 180
        self.scorpion_list.append(self.scorpion_sprite)
        self.scorpion_list.append(scorpion_sprite)

        self.snail_sprite = arcade.Sprite("./Resource/Images/snail.png", 0.2)
        self.snail_sprite.center_x = 2534
        self.snail_sprite.center_y = 174
        snail_sprite = arcade.Sprite("./Resource/Images/snail_2.png", 0.2)
        snail_sprite.center_x = 3182
        snail_sprite.center_y = 174
        self.snail_list.append(self.snail_sprite)
        self.snail_list.append(snail_sprite)

        self.shell_sprite = arcade.Sprite("./Resource/Images/shell.png", 0.2)
        self.shell_sprite.center_x = 2534
        self.shell_sprite.center_y = 500
        shell_sprite_2 = arcade.Sprite("./Resource/Images/shell_2.png", 0.2)
        shell_sprite_2.center_x = 2534
        shell_sprite_2.center_y = 174
        self.shell_list.append(self.shell_sprite)
        self.shell_list.append(shell_sprite_2)

        self.bogomol_sprite = arcade.Sprite("./Resource/Images/bogomol.png", 0.4)
        self.bogomol_sprite.center_x = 3820
        self.bogomol_sprite.center_y = 270
        bogomol_sprite_2 = arcade.Sprite("./Resource/Images/bogomol_2.png", 0.4)
        bogomol_sprite_2.center_x = 4700
        bogomol_sprite_2.center_y = 270
        self.bogomol_list.append(self.bogomol_sprite)
        self.bogomol_list.append(bogomol_sprite_2)
    def on_draw(self):
        arcade.start_render()
        self.camera_sprites.use()
        self.flags_list[0].draw()
        self.flags_list2[0].draw()
        self.flags_list3[0].draw()
        self.player_sprite.draw()
        self.platforms_list.draw()
        self.coin_list.draw()
        if self.flag == False or self.flag == True: self.scorpion_list[0].draw()
        if (self.flag_2 == False or self.flag_2 == True) and self.flag_7: self.snail_list[0].draw()
        else: self.shell_list[0].draw()
        if self.flag_3 == False or self.flag_3 == True: self.bogomol_list[0].draw()
        arcade.draw_text(f'Money: {self.score}    Lifes: {self.lifes}', -380 + self.player_sprite.center_x, 250 + self.player_sprite.center_y, arcade.color.BLACK, 20)
        self.exit_sprite.draw()
        self.camera_gui.use()
    def update(self, delta_time):
        self.set_update_rate(1/110)
        self.physics_engine.update()
        self.player_sprite.update_animation()
        self.platforms_list.update()
        self.shell_list.update()
        self.coin_list.update()
        self.scroll_to_player()

        if self.lifes == 0:
            self.game_over()

        if self.player_sprite.center_x <= -130:
            self.close()
            from level_5 import Level_5
        elif self.player_sprite.center_x >= 5079:
            self.close()
            from level_7 import Level_7

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
    
        if self.flag == False and self.scorpion_list[0].center_x > 1558:
            if self.scorpion_list[0].center_y == 185: self.flag_6 = False
            if self.scorpion_list[0].center_x - self.player_sprite.center_x <= 200 and self.scorpion_list[0].center_x - self.player_sprite.center_x >= 0: self.flag_6 = True
            if self.scorpion_list[0].center_x == 1960 or self.scorpion_list[0].center_x == 1759:
                self.scorpion_centerx = self.scorpion_list[0].center_x - 200
                self.scorpion_center_x = self.scorpion_list[0].center_x - 100
            if self.flag_6:
                if self.scorpion_list[0].center_x >= self.scorpion_center_x:
                    self.scorpion_list[0].center_y += 5
                    self.scorpion_list[0].center_x -= 3
                elif self.scorpion_list[0].center_x < self.scorpion_center_x and self.scorpion_list[0].center_x >= self.scorpion_centerx:
                    self.scorpion_list[0].center_y -= 5
                    self.scorpion_list[0].center_x -= 3
        elif self.flag == False and self.scorpion_list[0].center_x == 1558:
            self.flag = True
            self.scorpion_sprite.remove_from_sprite_lists()
            self.scorpion_list[0].center_x = 1558
        if self.flag == True and self.scorpion_list[0].center_x >= 1450 and self.scorpion_list[0].center_x < 1960:
            self.scorpion_list[0].center_x += 3
        elif self.flag == True and self.scorpion_list[0].center_x == 1960:
            self.scorpion_sprite = arcade.Sprite("./Resource/Images/scorpion_2.png", 0.3)
            self.scorpion_sprite.center_x = 1960
            self.scorpion_sprite.center_y = 180
            self.scorpion_list.insert(0, self.scorpion_sprite)
            self.flag = False
        if self.player_sprite.collides_with_sprite(self.scorpion_list[0]):
            self.player_sprite.center_x = self.x
            self.player_sprite.center_y = self.y
            self.lifes -= 1
        
        if self.flag_7:
            if self.flag_2 == False and self.snail_list[0].center_x > 2534:
                self.snail_list[0].center_x = self.snail_list[0].center_x - 1
            elif self.flag_2 == False and self.snail_list[0].center_x == 2534:
                self.flag_2 = True
                self.snail_sprite.remove_from_sprite_lists()
                self.snail_list[0].center_x = 2534
            if self.flag_2 == True and self.snail_list[0].center_x >= 2534 and self.snail_list[0].center_x < 3182:
                self.snail_list[0].center_x = self.snail_list[0].center_x + 1
            elif self.flag_2 == True and self.snail_list[0].center_x == 3182:
                self.snail_sprite = arcade.Sprite("./Resource/Images/snail.png", 0.2)
                self.snail_sprite.center_x = 3182
                self.snail_sprite.center_y = 174
                self.snail_list.insert(0, self.snail_sprite)
                self.flag_2 = False
        else:
            if self.flag_2 == False and self.shell_list[0].center_x > 2534:
                self.shell_list[0].center_x -= 3
                self.shell_list[0].change_angle = 5
            elif self.flag_2 == False and self.shell_list[0].center_x == 2534:
                self.flag_2 = True
                self.shell_sprite.remove_from_sprite_lists()
                self.shell_list[0].center_x = 2534
            if self.flag_2 == True and self.shell_list[0].center_x >= 2534 and self.shell_list[0].center_x < 3182:
                self.shell_list[0].center_x += 3
                self.shell_list[0].change_angle = 5
            elif self.flag_2 == True and self.shell_list[0].center_x == 3182:
                self.shell_sprite = arcade.Sprite("./Resource/Images/shell.png", 0.2)
                self.shell_sprite.center_x = 3182
                self.shell_sprite.center_y = 174
                self.shell_list.insert(0, self.shell_sprite)
                self.flag_2 = False
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
                self.flag_7 = True
                self.flag_9 = 'q'
                self.snail_list[0].center_y = 174
                    
        if self.player_sprite.collides_with_sprite(self.snail_list[0]) and self.player_sprite.center_y >= 184:
            self.player_sprite.change_y = 8
            self.flag_7 = False
            self.snail_list[0].center_y = 0
            if self.snail_list[0].center_x % 3 == 0: self.shell_list[0].center_x = self.snail_list[0].center_x - 1
            elif (self.snail_list[0].center_x + 1) % 3 == 0: self.shell_list[0].center_x = self.snail_list[0].center_x
            elif (self.snail_list[0].center_x + 2) % 3 == 0: self.shell_list[0].center_x = self.snail_list[0].center_x + 1
            self.shell_list[0].center_y = 174
            self.flag_8 = self.shell_list[0].center_x
        elif self.player_sprite.collides_with_sprite(self.snail_list[0]) and self.player_sprite.center_y < 184:
            self.lifes -= 1
            self.player_sprite.center_x = self.x 
            self.player_sprite.center_y = self.y 
        
        if self.flag_3 == False and self.bogomol_list[0].center_x > 3820:
            self.bogomol_list[0].center_x = self.bogomol_list[0].center_x - 4
        elif self.flag_3 == False and self.bogomol_list[0].center_x == 3820:
            self.flag_3 = True
            self.bogomol_sprite.remove_from_sprite_lists()
            self.bogomol_list[0].center_x = 3820
        if self.flag_3 == True and self.bogomol_list[0].center_x >= 3820 and self.bogomol_list[0].center_x < 4700:
            self.bogomol_list[0].center_x = self.bogomol_list[0].center_x + 2
        elif self.flag_3 == True and self.bogomol_list[0].center_x == 4700:
            self.bogomol_sprite = arcade.Sprite("./Resource/Images/bogomol.png", 0.4)
            self.bogomol_sprite.center_x = 4700
            self.bogomol_sprite.center_y = 270
            self.bogomol_list.insert(0, self.bogomol_sprite)
            self.flag_3 = False

        if self.player_sprite.collides_with_sprite(self.bogomol_list[0]) and self.player_sprite.center_y >= 184:
            if self.flag_3:
                self.player_sprite.change_y = 15
            else:
                self.lifes -= 1
                self.player_sprite.center_x = self.x
                self.player_sprite.center_y = self.y
        elif self.player_sprite.collides_with_sprite(self.bogomol_list[0]) and self.player_sprite.center_y < 184:
            self.lifes -= 1
            self.player_sprite.center_x = self.x 
            self.player_sprite.center_y = self.y
    def game_over(self):
        arcade.close_window()
        arcade.open_window(800, 600, 'Game Over')
        arcade.start_render()
        arcade.set_background_color(arcade.color.BLACK)
        game_over = arcade.load_texture('./Resource/Images/game_over.png')
        game_over.draw_sized(400, 300, 400, 300)
        game_over_sound =  arcade.load_sound('./Resource/Sound effects/game-over.mp3')
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
window = Level_6(800, 600, "Super Game")
window.setup()
arcade.run()