import arcade

JUMP_SPEED = 8
GRAVITY = 0.35

class Level_9(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        self.flag = False
        self.flag_2 = False
        self.flag_3 = False
        self.flag_4 = True
        self.flag_5 = True
        self.flag_6 = False
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
        self.hog_list = arcade.SpriteList()
        self.wolf_list = arcade.SpriteList()
        self.eagle_list = arcade.SpriteList()

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

        for x in range(33, 5000, 64):
            snow_grass = arcade.Sprite("./Resources/Images/snow_grass.png", 0.92)
            snow_grass.center_x = x
            snow_grass.center_y = 90
            self.platforms_list.append(snow_grass)
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

        for x in range(33, 5000, 64):
            snow_ground = arcade.Sprite("./Resources/Images/snow_ground.png", 0.92)
            snow_ground.center_x = x
            snow_ground.center_y = 26
            self.platforms_list.append(snow_ground)
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

        hog_sprite = arcade.Sprite("./Resources/Images/hog.png", 0.4)
        hog_sprite.center_x = 1979
        hog_sprite.center_y = 194
        hog_sprite_2 = arcade.Sprite("./Resources/Images/hog_2.png", 0.4)
        hog_sprite_2.center_x = 1451
        hog_sprite_2.center_y = 194
        self.hog_list.append(hog_sprite)
        self.hog_list.append(hog_sprite_2)

        wolf_sprite = arcade.Sprite("./Resources/Images/wolf.png", 0.5)
        wolf_sprite.center_x = 3150
        wolf_sprite.center_y = 194
        wolf_sprite_2 = arcade.Sprite("./Resources/Images/wolf_2.png", 0.5)
        wolf_sprite_2.center_x = 2570
        wolf_sprite_2.center_y = 194
        self.wolf_list.append(wolf_sprite)
        self.wolf_list.append(wolf_sprite_2)

        eagle_sprite = arcade.Sprite("./Resources/Images/eagle_2.png", 0.4)
        eagle_sprite.center_x = 3700
        eagle_sprite.center_y = 500
        eagle_sprite_2 = arcade.Sprite("./Resources/Images/eagle.png", 0.4)
        eagle_sprite_2.center_x = 4702
        eagle_sprite_2.center_y = 500
        self.eagle_list.append(eagle_sprite)
        self.eagle_list.append(eagle_sprite_2)
    def on_draw(self):
        arcade.start_render()
        self.camera_sprites.use()
        self.flags_list[0].draw()
        self.flags_list2[0].draw()
        self.flags_list3[0].draw()
        self.player_sprite.draw()
        self.hog_list[0].draw()
        self.wolf_list[0].draw()
        self.eagle_list[0].draw()
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
        self.coin_list.update()
        self.scroll_to_player()
        
        if self.lifes == 0:
            self.game_over()

        if self.player_sprite.center_x <= -130:
            self.close()
            from level_8 import Level_8
        elif self.player_sprite.center_x >= 5079:
            self.close()
            #from level_10 import Level_10

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

        if self.player_sprite.collides_with_sprite(self.hog_list[0]) and self.player_sprite.center_y > 190:
            self.player_sprite.change_y = 8
        elif self.player_sprite.collides_with_sprite(self.hog_list[0]) and self.player_sprite.center_y <= 190:
            self.player_sprite.center_x = self.x
            self.player_sprite.center_y = self.y
            self.lifes -= 1
        
        if self.hog_list[0].center_x >= 1451 and self.hog_list[0].center_x <= 1979 and self.player_sprite.center_x > 1350:
            self.hog_list[0].center_x -= (self.hog_list[0].center_x - self.player_sprite.center_x) // 100
        if str(self.hog_list[0].center_x - self.player_sprite.center_x)[0] == '-' and not self.flag:
            center_x = self.hog_list[0].center_x
            self.hog_list[0].remove_from_sprite_lists()
            self.hog_list[0].center_x = center_x
            self.flag = True
        if str(self.hog_list[0].center_x - self.player_sprite.center_x)[0] != '-' and self.flag:
            hog_sprite = arcade.Sprite("./Resources/Images/hog.png", 0.4)
            hog_sprite.center_x = self.hog_list[0].center_x
            hog_sprite.center_y = 194
            self.hog_list.insert(0, hog_sprite)
            self.flag = False
        
        if self.player_sprite.collides_with_sprite(self.wolf_list[0]) and self.player_sprite.center_y > 190:
            self.player_sprite.change_y = 8
        elif self.player_sprite.collides_with_sprite(self.wolf_list[0]) and self.player_sprite.center_y <= 190:
            self.player_sprite.center_x = self.x
            self.player_sprite.center_y = self.y
            self.lifes -= 1
        
        if self.wolf_list[0].center_x >= 2570 and self.wolf_list[0].center_x <= 3150 and self.player_sprite.center_x > 2500:
            self.wolf_list[0].center_x -= (self.wolf_list[0].center_x - self.player_sprite.center_x) // 50
        if str(self.wolf_list[0].center_x - self.player_sprite.center_x)[0] == '-' and not self.flag_2:
            center_x = self.wolf_list[0].center_x
            self.wolf_list[0].remove_from_sprite_lists()
            self.wolf_list[0].center_x = center_x
            self.flag_2 = True
        if str(self.wolf_list[0].center_x - self.player_sprite.center_x)[0] != '-' and self.flag_2:
            wolf_sprite = arcade.Sprite("./Resources/Images/wolf.png", 0.5)
            wolf_sprite.center_x = self.wolf_list[0].center_x
            wolf_sprite.center_y = 194
            self.wolf_list.insert(0, wolf_sprite)
            self.flag_2 = False
        
        if not self.flag_3 and self.flag_6 and self.eagle_list[0].center_x < 4078:
            self.eagle_list[0].center_x += 3
            self.eagle_list[0].center_y -= 2
        elif not self.flag_3 and self.eagle_list[0].center_x >= 4078 and self.eagle_list[0].center_x < 4324:
            self.eagle_list[0].center_x += 3
        elif not self.flag_3 and self.eagle_list[0].center_x >= 4324 and self.eagle_list[0].center_x < 4702:
            self.eagle_list[0].center_x += 3
            self.eagle_list[0].center_y += 2
        elif not self.flag_3 and self.eagle_list[0].center_x == 4702:
            self.eagle_list[0].remove_from_sprite_lists()
            self.eagle_list[0].center_x = 4702
            self.flag_3 = True
        elif self.flag_3 and self.eagle_list[0].center_x > 4324:
            self.eagle_list[0].center_x -= 3
            self.eagle_list[0].center_y -= 2
        elif self.flag_3 and self.eagle_list[0].center_x > 4078 and self.eagle_list[0].center_x <= 4324:
            self.eagle_list[0].center_x -= 3
        elif self.flag_3 and self.eagle_list[0].center_x > 3700 and self.eagle_list[0].center_x <= 4078:
            self.eagle_list[0].center_x -= 3
            self.eagle_list[0].center_y += 2
        elif self.flag_3 and self.eagle_list[0].center_x == 3700:
            eagle_sprite = arcade.Sprite("./Resources/Images/eagle_2.png", 0.4)
            eagle_sprite.center_x = 3700
            eagle_sprite.center_y = 500
            self.eagle_list.insert(0, eagle_sprite)
            self.flag_3 = False
        if self.player_sprite.center_x > 3900:
            self.flag_6 = True
        
        if self.eagle_list[0].collides_with_sprite(self.player_sprite):
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
        
window = Level_9(800, 600, "Super Game")
window.setup()
arcade.run()
