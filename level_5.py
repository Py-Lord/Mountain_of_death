import arcade

MOVEMENT_SPEED = 2.1
JUMP_SPEED = 8
GRAVITY = 0.35

class Level_5(arcade.Window):
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
        self.x = 100
        self.y = 154

        self.camera_sprites = arcade.Camera(800, 600)
        self.camera_gui = arcade.Camera(800, 600)
    def setup(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.platforms_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.flags_list = arcade.SpriteList()
        self.flags_list2 = arcade.SpriteList()
        self.flags_list3 = arcade.SpriteList()
        self.frog_list = arcade.SpriteList()
        self.grasshopper_list = arcade.SpriteList()
        self.lizard_list = arcade.SpriteList()

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
        for x in range(3705, 3898, 64):
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
        for x in range(3769, 3898, 64):
            coin_sprite = arcade.Sprite("./Resource/Images/gold.png", 0.5)
            coin_sprite.center_x = x
            coin_sprite.center_y = 218
            self.coin_list.append(coin_sprite)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.platforms_list, gravity_constant=GRAVITY)

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
        grass_hill_sprite.center_x = 3641
        grass_hill_sprite.center_y = 154
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resource/Images/grasshill.png", 0.5)
        grass_hill_sprite.center_x = 3961
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
        self.FLAG3.center_x = 3710
        self.FLAG3.center_y = 218
        self.flags_list3.append(self.FLAG3)
        Flag3 = arcade.Sprite("./Resource/Images/flagRed1.png", 0.5)
        Flag3.center_x = 3710
        Flag3.center_y = 218
        self.flags_list3.append(Flag3)

        self.exit_sprite = arcade.Sprite("./Resource/Images/exit.png", 0.5)
        self.exit_sprite.center_x = 4917
        self.exit_sprite.center_y = 154

        self.grasshopper_sprite = arcade.Sprite("./Resource/Images/grasshopper_2.png", 0.2, angle = -368)
        self.grasshopper_sprite.center_x = 1894
        self.grasshopper_sprite.center_y = 164
        grasshopper_2_sprite = arcade.Sprite("./Resource/Images/grasshopper.png", 0.2, angle = 8)
        grasshopper_2_sprite.center_x = 1492
        grasshopper_2_sprite.center_y = 164
        self.grasshopper_list.append(self.grasshopper_sprite)
        self.grasshopper_list.append(grasshopper_2_sprite)

        self.lizard_sprite = arcade.Sprite("./Resource/Images/lizard.png", 0.5)
        self.lizard_sprite.center_x = 2655
        self.lizard_sprite.center_y = 164
        lizard_2_sprite = arcade.Sprite("./Resource/Images/lizard_2.png", 0.5)
        lizard_2_sprite.center_x = 3395
        lizard_2_sprite.center_y = 164
        self.lizard_list.append(self.lizard_sprite)
        self.lizard_list.append(lizard_2_sprite)

        self.frog_sprite = arcade.Sprite("./Resource/Images/frog.png", 1)
        self.frog_sprite.center_x = 4100
        self.frog_sprite.center_y = 174
        frog_2_sprite = arcade.Sprite("./Resource/Images/frog2.png", 1)
        frog_2_sprite.center_x = 4601
        frog_2_sprite.center_y = 174
        self.frog_list.append(self.frog_sprite)
        self.frog_list.append(frog_2_sprite)
    def on_draw(self):
        arcade.start_render()
        self.camera_sprites.use()
        self.flags_list[0].draw()
        self.flags_list2[0].draw()
        self.flags_list3[0].draw()
        self.player_sprite.draw()
        self.platforms_list.draw()
        self.coin_list.draw()
        if self.flag_3 == True or self.flag_3 == False: self.frog_list[0].draw()
        if self.flag_2 == True or self.flag_2 == False: self.lizard_list[0].draw()
        if self.flag == True or self.flag == False: self.grasshopper_list[0].draw()
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
        
        if self.lifes == 0:
            self.game_over()

        if self.player_sprite.center_x <= -130:
            self.close()
            from level_4 import Level_4
        elif self.player_sprite.center_x >= 5079:
            self.close()
            from level_6 import Level_6

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 10
        
        if self.player_sprite.center_x >= 1089 and self.player_sprite.center_x < 2198 and self.flag_4:
            self.FLAG.remove_from_sprite_lists()
            self.x = 1189
            self.y = 218
        elif self.player_sprite.center_x >= 2198 and self.player_sprite.center_x < 3738 and self.flag_5:
            self.FLAG2.remove_from_sprite_lists()
            self.x = 2698
            self.y = 218
            self.flag_4 = False
        elif self.player_sprite.center_x >= 3738:
            self.JUMP_SPEED = 8
            self.FLAG3.remove_from_sprite_lists()
            self.x = 3228
            self.y = 218
            self.flag_5 = False
        
        if self.flag == False and self.grasshopper_list[0].center_x > 1492:
            if self.grasshopper_list[0].center_x <= 1894 and self.grasshopper_list[0].center_x >= 1693:
                self.grasshopper_list[0].center_y += 5
                self.grasshopper_list[0].center_x -= 3
            elif self.grasshopper_list[0].center_x < 1693:
                self.grasshopper_list[0].center_y -= 5
                self.grasshopper_list[0].center_x -= 3
        elif self.flag == False and self.grasshopper_list[0].center_x == 1492:
            self.flag = True
            self.grasshopper_sprite.remove_from_sprite_lists()
            self.grasshopper_list[0].center_x = 1492
            self.grasshopper_list[0].center_y = 164
        if self.flag == True and self.grasshopper_list[0].center_x >= 1492 and self.grasshopper_list[0].center_x < 1894:
            if self.grasshopper_list[0].center_x <= 1696 and self.grasshopper_list[0].center_x >= 1492:
                self.grasshopper_list[0].center_y += 5
                self.grasshopper_list[0].center_x += 3
            elif self.grasshopper_list[0].center_x >= 1696:
                self.grasshopper_list[0].center_y -= 5
                self.grasshopper_list[0].center_x += 3
        elif self.flag == True and self.grasshopper_list[0].center_x == 1894:
            self.grasshopper_sprite = arcade.Sprite("./Resource/Images/grasshopper_2.png", 0.2)
            self.grasshopper_sprite.center_x = 1894
            self.grasshopper_sprite.center_y = 164
            self.grasshopper_list.insert(0, self.grasshopper_sprite)
            self.flag = False

        if self.player_sprite.collides_with_sprite(self.grasshopper_list[0]):
            self.player_sprite.change_y = 20
            self.lifes -= 0.1 #self.life.remove_from_sprites_lists() #self.lifes -= 2
        
        if self.flag_2 == False and self.lizard_list[0].center_x > 2655:
            self.lizard_list[0].center_x = self.lizard_list[0].center_x - 4
        elif self.flag_2 == False and self.lizard_list[0].center_x == 2655:
            self.flag_2 = True
            self.lizard_sprite.remove_from_sprite_lists()
            self.lizard_list[0].center_x = 2655
        if self.flag_2 == True and self.lizard_list[0].center_x >= 2655 and self.lizard_list[0].center_x < 3395:
            self.lizard_list[0].center_x = self.lizard_list[0].center_x + 4
        elif self.flag_2 == True and self.lizard_list[0].center_x == 3395:
            self.lizard_sprite = arcade.Sprite("./Resource/Images/lizard.png", 0.5)
            self.lizard_sprite.center_x = 3395
            self.lizard_sprite.center_y = 164
            self.lizard_list.insert(0, self.lizard_sprite)
            self.flag_2 = False
        
        if self.player_sprite.collides_with_sprite(self.lizard_list[0]):
            self.player_sprite.change_y = 20
            self.lifes -= 0.1 #self.life.remove_from_sprites_lists() #self.lifes -= 2
        
        if self.flag_3 == False and self.frog_list[0].center_x > 4100:
            if self.frog_list[0].center_x <= 4601 and self.frog_list[0].center_x >= 4477:
                self.frog_list[0].center_y += 5
                self.frog_list[0].center_x -= 3
            elif self.frog_list[0].center_x < 4477 and self.frog_list[0].center_x >= 4349:
                self.frog_list[0].center_y -= 5
                self.frog_list[0].center_x -= 3
            if self.frog_list[0].center_x <= 4349 and self.frog_list[0].center_x >= 4224:
                self.frog_list[0].center_y += 5
                self.frog_list[0].center_x -= 3
            elif self.frog_list[0].center_x < 4224:
                self.frog_list[0].center_y -= 5
                self.frog_list[0].center_x -= 3
        elif self.flag_3 == False and self.frog_list[0].center_x == 4100:
            self.flag_3 = True
            self.frog_sprite.remove_from_sprite_lists()
            self.frog_list[0].center_x = 4100
            self.frog_list[0].center_y = 164
        if self.flag_3 == True and self.frog_list[0].center_x >= 4100 and self.frog_list[0].center_x < 4601:
            if self.frog_list[0].center_x <= 4224 and self.frog_list[0].center_x >= 4100:
                self.frog_list[0].center_y += 5
                self.frog_list[0].center_x += 3
            elif self.frog_list[0].center_x > 4224 and self.frog_list[0].center_x < 4349:
                self.frog_list[0].center_y -= 5
                self.frog_list[0].center_x += 3
            if self.frog_list[0].center_x >= 4349 and self.frog_list[0].center_x <= 4473:
                self.frog_list[0].center_y += 5
                self.frog_list[0].center_x += 3
            elif self.frog_list[0].center_x > 4473:
                self.frog_list[0].center_y -= 5
                self.frog_list[0].center_x += 3
        elif self.flag_3 == True and self.frog_list[0].center_x == 4601:
            self.frog_sprite = arcade.Sprite("./Resource/Images/frog.png", 1)
            self.frog_sprite.center_x = 4601
            self.frog_sprite.center_y = 174
            self.frog_list.insert(0, self.frog_sprite)
            self.flag_3 = False
        
        if self.player_sprite.collides_with_sprite(self.frog_list[0]):
            self.player_sprite.change_y = 15
            self.lifes -= 0.05 #self.life.remove_from_sprites_lists() #self.lifes -= 1
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
window = Level_5(800, 600, "Super Game")
window.setup()
arcade.run()
