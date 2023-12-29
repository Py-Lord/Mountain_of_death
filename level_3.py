import arcade

MOVEMENT_SPEED = 2.1
JUMP_SPEED = 8
GRAVITY = 0.35

class Level_3(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        self.flag = False
        self.flag_2 = False
        self.flag_3 = False
        self.flag_4 = True
        self.flag_5 = True
        self.lifes = 3
        self.score = 0 
        self.score_2 = 1
        self.score_3 = 1
        self.score_4 = 1
        self.x = 100
        self.y = 164

        self.camera_sprites = arcade.Camera(800, 600)
        self.camera_gui = arcade.Camera(800, 600)
    def setup(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.platforms_list = arcade.SpriteList()
        self.bug_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.flags_list = arcade.SpriteList()
        self.flags_list2 = arcade.SpriteList()
        self.flags_list3 = arcade.SpriteList()
        self.spider_list = arcade.SpriteList()
        self.ant_list = arcade.SpriteList()

        for i in range(0, 577, 64):
            coin_sprite = arcade.Sprite("./Resources/Images/gold.png", 0.5)
            coin_sprite.center_x = 450 + i
            coin_sprite.center_y = 144
            self.coin_list.append(coin_sprite)

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

        for x in range(33, 4962, 64):
            grass_sprite = arcade.Sprite("./Resources/Images/grass.png", 0.5)
            grass_sprite.center_x = x
            grass_sprite.center_y = 90
            self.platforms_list.append(grass_sprite)
        for x in range(1155, 1348, 64):
            grass_sprite = arcade.Sprite("./Resources/Images/grass.png", 0.5)
            grass_sprite.center_x = x
            grass_sprite.center_y = 154
            self.platforms_list.append(grass_sprite)
        for x in range(2164, 2357, 64):
            grass_sprite = arcade.Sprite("./Resources/Images/grass.png", 0.5)
            grass_sprite.center_x = x
            grass_sprite.center_y = 154
            self.platforms_list.append(grass_sprite)
        for x in range(3205, 3398, 64):
            grass_sprite = arcade.Sprite("./Resources/Images/grass.png", 0.5)
            grass_sprite.center_x = x
            grass_sprite.center_y = 154
            self.platforms_list.append(grass_sprite)

        for x in range(33, 4962, 64):
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
        
        for i in range(0, 577, 64):
            coin_sprite = arcade.Sprite("./Resources/Images/gold.png", 0.5)
            coin_sprite.center_x = 450 + i
            coin_sprite.center_y = 144
            self.coin_list.append(coin_sprite)
        for x in range(4501, 4822, 64):
            coin_sprite = arcade.Sprite("./Resources/Images/gold.png", 0.5)
            coin_sprite.center_x = x
            coin_sprite.center_y = 144
            self.coin_list.append(coin_sprite)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.platforms_list, gravity_constant=GRAVITY)
        
        self.bug_sprite = arcade.Sprite("./Resources/Images/bug_2.png", 0.3)
        self.bug_sprite.center_x = 2011
        self.bug_sprite.center_y = 155
        bug_2_sprite = arcade.Sprite("./Resources/Images/bug.png", 0.3)
        bug_2_sprite.center_x = 1510
        bug_2_sprite.center_y = 155
        self.bug_list.append(self.bug_sprite)
        self.bug_list.append(bug_2_sprite)

        self.spider_sprite = arcade.Sprite("./Resources/Images/spider_2.png", 0.9)
        self.spider_sprite.center_x = 2540
        self.spider_sprite.center_y = 164
        spider_2_sprite = arcade.Sprite("./Resources/Images/spider.png", 0.9)
        spider_2_sprite.center_x = 3041
        spider_2_sprite.center_y = 164
        self.spider_list.append(self.spider_sprite)
        self.spider_list.append(spider_2_sprite)

        self.ant_sprite = arcade.Sprite("./Resources/Images/ant2.png", 0.25)
        self.ant_sprite.center_x = 3576
        self.ant_sprite.center_y = 155
        ant_2_sprite = arcade.Sprite("./Resources/Images/ant2_2.png", 0.25)
        ant_2_sprite.center_x = 4275
        ant_2_sprite.center_y = 155
        self.ant_list.append(self.ant_sprite)
        self.ant_list.append(ant_2_sprite)

        grass_hill_sprite = arcade.Sprite("./Resources/Images/grass_hill.png", 0.5)
        grass_hill_sprite.center_x = 1091
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resources/Images/grasshill.png", 0.5)
        grass_hill_sprite.center_x = 1411
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resources/Images/grass_hill.png", 0.5)
        grass_hill_sprite.center_x = 2100
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resources/Images/grasshill.png", 0.5)
        grass_hill_sprite.center_x = 2420
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resources/Images/grass_hill.png", 0.5)
        grass_hill_sprite.center_x = 3141
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resources/Images/grasshill.png", 0.5)
        grass_hill_sprite.center_x = 3461
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
        self.FLAG.center_x = 1161
        self.FLAG.center_y = 218
        self.flags_list.append(self.FLAG)
        Flag = arcade.Sprite("./Resources/Images/flagRed1.png", 0.5)
        Flag.center_x = 1161
        Flag.center_y = 218
        self.flags_list.append(Flag)
        self.FLAG2 = arcade.Sprite("./Resources/Images/flagRed.png", 0.5)
        self.FLAG2.center_x = 2170
        self.FLAG2.center_y = 218
        self.flags_list2.append(self.FLAG2)
        Flag2 = arcade.Sprite("./Resources/Images/flagRed1.png", 0.5)
        Flag2.center_x = 2170
        Flag2.center_y = 218
        self.flags_list2.append(Flag2)
        self.FLAG3 = arcade.Sprite("./Resources/Images/flagRed.png", 0.5)
        self.FLAG3.center_x = 3210
        self.FLAG3.center_y = 218
        self.flags_list3.append(self.FLAG3)
        Flag3 = arcade.Sprite("./Resources/Images/flagRed1.png", 0.5)
        Flag3.center_x = 3210
        Flag3.center_y = 218
        self.flags_list3.append(Flag3)

        self.exit_sprite = arcade.Sprite("./Resources/Images/exit.png", 0.5)
        self.exit_sprite.center_x = 4917
        self.exit_sprite.center_y = 154
    def on_draw(self):
        arcade.start_render()
        self.camera_sprites.use()
        self.flags_list[0].draw()
        self.flags_list2[0].draw()
        self.flags_list3[0].draw()
        self.player_sprite.draw()
        self.platforms_list.draw()
        self.coin_list.draw()
        if self.flag_3 == False or self.flag_3 == True: self.ant_list[0].draw()
        if self.flag_2 == False or self.flag_2 == True: self.spider_list[0].draw()
        if self.flag == False or self.flag == True: self.bug_list[0].draw()
        arcade.draw_text(f'Money: {self.score}    Lifes: {self.lifes}', -380 + self.player_sprite.center_x, 250 + self.player_sprite.center_y, arcade.color.BLACK, 20)
        self.exit_sprite.draw()
        self.camera_gui.use()
    def update(self, delta_time):
        self.set_update_rate(1/110)
        self.player_sprite.update_animation()
        self.physics_engine.update()
        self.platforms_list.update()
        self.coin_list.update()
        self.scroll_to_player()

        if self.player_sprite.center_x <= -130:
            self.close()
            from level_2 import Level_2
        
        if self.player_sprite.center_x >= 5079:
            self.close()
            from level_4 import Level_4 

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 5

        if self.flag == False and self.bug_list[0].center_x > 1510:
            self.bug_list[0].center_x = self.bug_list[0].center_x - 3
        elif self.flag == False and self.bug_list[0].center_x == 1510:
            self.flag = True
            self.bug_sprite.remove_from_sprite_lists()
            self.bug_list[0].center_x = 1510
        if self.flag == True and self.bug_list[0].center_x >= 1510 and self.bug_list[0].center_x < 2011:
            self.bug_list[0].center_x = self.bug_list[0].center_x + 3
        elif self.flag == True and self.bug_list[0].center_x == 2011:
            self.bug_sprite = arcade.Sprite("./Resources/Images/bug_2.png", 0.3)
            self.bug_sprite.center_x = 2011
            self.bug_sprite.center_y = 155
            self.bug_list.insert(0, self.bug_sprite)
            self.flag = False

        if self.player_sprite.collides_with_sprite(self.bug_list[0]) and self.player_sprite.center_y >= 218 and self.score_2 == 1:
            self.score_2 += 1
            self.player_sprite.change_y = 8
        elif self.player_sprite.collides_with_sprite(self.bug_list[0]) and self.player_sprite.center_y >= 218 and self.flag != 'Kill' and self.score_2 == 2:
            self.flag = 'Kill'
            self.player_sprite.change_y = 8
            coin_sprite = arcade.Sprite("./Resources/Images/gold.png", 0.5)
            coin_sprite.center_x = self.bug_list[0].center_x + 80 
            coin_sprite.center_y = 144 
            self.coin_list.append(coin_sprite)
            coin_sprite = arcade.Sprite("./Resources/Images/gold.png", 0.5)
            coin_sprite.center_x = self.bug_list[0].center_x + 100 
            coin_sprite.center_y = 144
            self.coin_list.append(coin_sprite)
        elif self.player_sprite.collides_with_sprite(self.bug_list[0]) and self.player_sprite.center_y < 218 and (self.flag == True or self.flag == False):
            self.lifes -= 1
            self.player_sprite.center_x = self.x
            self.player_sprite.center_y = self.y
        
        if self.flag_2 == False and self.spider_list[0].center_x > 2540:
            self.spider_list[0].center_x = self.spider_list[0].center_x - 3
        elif self.flag_2 == False and self.spider_list[0].center_x == 2540:
            self.flag_2 = True
            self.spider_sprite.remove_from_sprite_lists()
            self.spider_list[0].center_x = 2540
        if self.flag_2 == True and self.spider_list[0].center_x >= 2540 and self.spider_list[0].center_x < 3041:
            self.spider_list[0].center_x = self.spider_list[0].center_x + 3
        elif self.flag_2 == True and self.spider_list[0].center_x == 3041:
            self.spider_sprite = arcade.Sprite("./Resources/Images/spider_2.png", 0.9)
            self.spider_sprite.center_x = 3041
            self.spider_sprite.center_y = 164
            self.spider_list.insert(0, self.spider_sprite)
            self.flag_2 = False
        
        if self.player_sprite.collides_with_sprite(self.spider_list[0]) and self.player_sprite.center_y >= 220 and self.score_3 == 1:
            self.score_3 += 1
            self.player_sprite.change_y = 8
        elif self.player_sprite.collides_with_sprite(self.spider_list[0]) and self.player_sprite.center_y >= 220 and self.flag_2 != 'Kill' and self.score_3 == 2:
            self.flag_2 = 'Kill'
            self.player_sprite.change_y = 8
            coin_sprite = arcade.Sprite("./Resources/Images/gold.png", 0.5)
            coin_sprite.center_x = self.spider_list[0].center_x + 80 
            coin_sprite.center_y = 144 
            self.coin_list.append(coin_sprite)
            coin_sprite = arcade.Sprite("./Resources/Images/gold.png", 0.5)
            coin_sprite.center_x = self.spider_list[0].center_x + 100 
            coin_sprite.center_y = 144
            self.coin_list.append(coin_sprite)
        elif self.player_sprite.collides_with_sprite(self.spider_list[0]) and self.player_sprite.center_y < 220 and (self.flag_2 == True or self.flag_2 == False):
            self.lifes -= 1
            self.player_sprite.center_x = self.x
            self.player_sprite.center_y = self.y

        if self.flag_3 == False and self.ant_list[0].center_x > 3576:
            self.ant_list[0].center_x = self.ant_list[0].center_x - 3
        elif self.flag_3 == False and self.ant_list[0].center_x == 3576:
            self.flag_3 = True
            self.ant_sprite.remove_from_sprite_lists()
            self.ant_list[0].center_x = 3576
        if self.flag_3 == True and self.ant_list[0].center_x >= 3576 and self.ant_list[0].center_x < 4275:
            self.ant_list[0].center_x = self.ant_list[0].center_x + 3
        elif self.flag_3 == True and self.ant_list[0].center_x == 4275:
            self.ant_sprite = arcade.Sprite("./Resources/Images/ant2.png", 0.25)
            self.ant_sprite.center_x = 4275
            self.ant_sprite.center_y = 155
            self.ant_list.insert(0, self.ant_sprite)
            self.flag_3 = False

        if self.player_sprite.collides_with_sprite(self.ant_list[0]) and self.player_sprite.center_y >= 218 and self.score_4 == 1:
            self.score_4 += 1
            self.player_sprite.change_y = 8
        elif self.player_sprite.collides_with_sprite(self.ant_list[0]) and self.player_sprite.center_y >= 218 and self.flag_3 != 'Kill' and self.score_4 == 2:
            self.flag_3 = 'Kill'
            self.player_sprite.change_y = 8
            coin_sprite = arcade.Sprite("./Resources/Images/gold.png", 0.5)
            coin_sprite.center_x = self.ant_list[0].center_x + 80 
            coin_sprite.center_y = 144 
            self.coin_list.append(coin_sprite)
            coin_sprite = arcade.Sprite("./Resources/Images/gold.png", 0.5)
            coin_sprite.center_x = self.ant_list[0].center_x + 100 
            coin_sprite.center_y = 144
            self.coin_list.append(coin_sprite)
        elif self.player_sprite.collides_with_sprite(self.ant_list[0]) and self.player_sprite.center_y < 218 and (self.flag_3 == True or self.flag_3 == False):
            self.lifes -= 1
            self.player_sprite.center_x = self.x
            self.player_sprite.center_y = self.y    
        
        if self.player_sprite.center_x >= 1161 and self.player_sprite.center_x < 2130 and self.flag_4:
            self.FLAG.remove_from_sprite_lists()
            self.x = 1189
            self.y = 218
        elif self.player_sprite.center_x >= 2170 and self.player_sprite.center_x < 3228 and self.flag_5:
            self.FLAG2.remove_from_sprite_lists()
            self.x = 2198
            self.y = 218
            self.flag_4 = False
        elif self.player_sprite.center_x >= 3228:
            self.JUMP_SPEED = 8
            self.FLAG3.remove_from_sprite_lists()
            self.x = 3228
            self.y = 218
            self.flag_5 = False
        
        if self.lifes == 0:
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
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def scroll_to_player(self):
        position = self.player_sprite.center_x - self.width / 2, \
            self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, 0.1)
        
window = Level_3(800, 600, "Super Game")
window.setup()
arcade.run()