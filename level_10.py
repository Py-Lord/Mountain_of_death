import arcade

JUMP_SPEED = 8
GRAVITY = 0.35
MOVEMENT_SPEED = 2.6

class Level_10(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        self.flag = False
        self.flag_2 = False
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
        self.snow_balls = arcade.SpriteList()
        self.snow_ball_list = arcade.SpriteList()

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

        for x in range(33, 2177, 64):
            snow_grass = arcade.Sprite("./Resource/Images/snow_grass.png", 0.92)
            snow_grass.center_x = x
            snow_grass.center_y = 90
            self.platforms_list.append(snow_grass)
        for x in range(3233, 5000, 64):
            snow_ground = arcade.Sprite("./Resource/Images/snow_grass.png", 0.92)
            snow_ground.center_x = x
            snow_ground.center_y = -934
            self.platforms_list.append(snow_ground)
        for x in range(33,  2177, 64):
            snow_ground = arcade.Sprite("./Resource/Images/snow_ground.png", 0.92)
            snow_ground.center_x = x
            snow_ground.center_y = 26
            self.platforms_list.append(snow_ground)

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

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.platforms_list, gravity_constant = GRAVITY)

        for i in range(0, 321, 64):
            grass_hill_sprite = arcade.Sprite("./Resource/Images/grass_hill.png", 0.5)
            grass_hill_sprite.center_x = -31 - i
            grass_hill_sprite.center_y = 90 - i
            self.platforms_list.append(grass_hill_sprite)
        for i in range(0, 321, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/grass_hill_1.png", 0.5)
            ground_sprite.center_x = -31 - i
            ground_sprite.center_y = 26 - i
            self.platforms_list.append(ground_sprite)

        for x in range(1000, 1321, 64):
            snowdrift_sprite = arcade.Sprite("./Resource/images/snowdrift.png", 0.92)
            snowdrift_sprite.center_x = x
            snowdrift_sprite.center_y = 154
            self.platforms_list.append(snowdrift_sprite)
        snowdrift_hill = arcade.Sprite("./Resource/images/snowdrift_hill.png", 0.92)
        snowdrift_hill.center_x = 936
        snowdrift_hill.center_y = 154
        self.platforms_list.append(snowdrift_hill) 
        snowdrift_hill = arcade.Sprite("./Resource/images/snowdrift_hill_2.png", 0.92)
        snowdrift_hill.center_x = 1384
        snowdrift_hill.center_y = 154
        self.platforms_list.append(snowdrift_hill)

        for i in range(0, 1000, 64):
            snow_hill = arcade.Sprite("./Resource/images/snowhill.png", 0.92)
            snow_hill.center_x = 2209 + i 
            snow_hill.center_y = 90 - i
            self.platforms_list.append(snow_hill) 
        for i in range(0, 1000, 64):
            snow_hill = arcade.Sprite("./Resource/images/snow_hill_1.png", 0.92)
            snow_hill.center_x = 2209 + i 
            snow_hill.center_y = 26 - i
            self.platforms_list.append(snow_hill) 
        for i in range(0, 1000, 64):
            snow_hill = arcade.Sprite("./Resource/images/snow_ground.png", 0.92)
            snow_hill.center_x = 2209 + i 
            snow_hill.center_y = -38 - i
            self.platforms_list.append(snow_hill) 

        self.exit_sprite = arcade.Sprite("./Resource/Images/exit.png", 0.5)
        self.exit_sprite.center_x = 4917
        self.exit_sprite.center_y = 154

        self.snowman = arcade.Sprite("./Resource/images/snowman.png", 0.5)
        self.snowman.center_x = 1160
        self.snowman.center_y = 284

        for i in range(120):
            snow_ball = arcade.Sprite("./Resource/images/snow_ball.png", 0.05)
            snow_ball.center_x = 1061
            snow_ball.center_y = 306
            self.snow_balls.append(snow_ball)
        
        self.snow_ball_big = arcade.Sprite("./Resource/images/snow_ball_big.png", 1.5)
        self.snow_ball_big.center_x = 2050
        self.snow_ball_big.center_y = 173
        snow_ball_half = arcade.Sprite("./Resource/images/snow_ball_half.png", 1.5, angle = 100)
        snow_ball_half.center_x = 4022
        snow_ball_half.center_y = -860
        snow_ball_half_2 = arcade.Sprite("./Resource/images/snow_ball_half.png", 1.5, angle = -460)
        snow_ball_half_2.center_x = 4164
        snow_ball_half_2.center_y = -860
        self.snow_ball_list.append(snow_ball_half)
        self.snow_ball_list.append(snow_ball_half_2)

        self.gem_sprite = arcade.Sprite("./Resource/images/gem.png", 0.3)
        self.gem_sprite.center_x = 4093
        self.gem_sprite.center_y = -860
    def on_draw(self):
        arcade.start_render()
        self.camera_sprites.use()
        self.player_sprite.draw()
        self.platforms_list.draw()
        self.snowman.draw()
        if len(self.snow_balls) > 8:
            self.snow_balls[0].draw()
            self.snow_balls[1].draw()
            self.snow_balls[2].draw()
            self.snow_balls[3].draw()
            self.snow_balls[4].draw()
            self.snow_balls[5].draw()
            self.snow_balls[6].draw()
            self.snow_balls[7].draw()
        if self.snow_ball_big.center_x != 4100: self.snow_ball_big.draw()
        else: 
            self.snow_ball_list.draw()
            self.gem_sprite.draw()
        arcade.draw_text(f'Money: {self.score}    Lifes: {self.lifes}', -380 + self.player_sprite.center_x, 250 + self.player_sprite.center_y, arcade.color.BLACK, 20)
        self.exit_sprite.draw()
        self.camera_gui.use()
    def update(self, delta_time):
        self.set_update_rate(1/110)
        self.physics_engine.update()
        self.player_sprite.update_animation()
        self.platforms_list.update()
        self.snow_ball_big.update()
        self.scroll_to_player()
        
        if self.lifes == 0:
            self.game_over()

        if self.player_sprite.center_x <= -130:
            self.close()
            from level_9 import Level_9
        elif self.player_sprite.center_x >= 5079:
            self.close()
            #from level_11 import Level_11
        
        if self.flag == True:
            if self.snow_balls[6].center_x >= self.player_sprite.center_x:
                self.snow_balls[6].center_x -= 1
                self.snow_balls[6].center_y -= 0.1
            else: self.snow_balls[6].center_y -= 1
            if self.snow_balls[7].center_x >= self.player_sprite.center_x:
                self.snow_balls[7].center_x -= 1
                self.snow_balls[7].center_y -= 0.2
            else: self.snow_balls[7].center_y -= 1
            if self.snow_balls[0].center_x >= self.player_sprite.center_x:
                self.snow_balls[0].center_x -= 1
                self.snow_balls[0].center_y -= 0.3
            else: self.snow_balls[0].center_y -= 1
            if self.snow_balls[1].center_x >= self.player_sprite.center_x:
                self.snow_balls[1].center_x -= 1
                self.snow_balls[1].center_y -= 0.4
            else: self.snow_balls[1].center_y -= 1
            if self.snow_balls[2].center_x >= self.player_sprite.center_x:
                self.snow_balls[2].center_x -= 1
                self.snow_balls[2].center_y -= 0.5
            else: self.snow_balls[2].center_y -= 1
            if self.snow_balls[3].center_x >= self.player_sprite.center_x:
                self.snow_balls[3].center_x -= 1
                self.snow_balls[3].center_y -= 0.6
            else: self.snow_balls[3].center_y -= 1
            if self.snow_balls[4].center_x >= self.player_sprite.center_x:
                self.snow_balls[4].center_x -= 1
                self.snow_balls[4].center_y -= 0.7
            else: self.snow_balls[4].center_y -= 1
            if self.snow_balls[5].center_x >= self.player_sprite.center_x:
                self.snow_balls[5].center_x -= 1
                self.snow_balls[5].center_y -= 0.8
            else: self.snow_balls[5].center_y -= 1

            if self.snow_balls[0].collides_with_sprite(self.player_sprite):
                self.lifes -= 0.3
                self.snow_balls[0].remove_from_sprite_lists()
            elif self.snow_balls[1].collides_with_sprite(self.player_sprite):
                self.lifes -= 0.3
                self.snow_balls[1].remove_from_sprite_lists()
            elif self.snow_balls[2].collides_with_sprite(self.player_sprite):
                self.lifes -= 0.3
                self.snow_balls[2].remove_from_sprite_lists()
            elif self.snow_balls[3].collides_with_sprite(self.player_sprite):
                self.lifes -= 0.3
                self.snow_balls[3].remove_from_sprite_lists()
            elif self.snow_balls[4].collides_with_sprite(self.player_sprite):
                self.lifes -= 0.3
                self.snow_balls[4].remove_from_sprite_lists()
            elif self.snow_balls[5].collides_with_sprite(self.player_sprite):
                self.lifes -= 0.3
                self.snow_balls[5].remove_from_sprite_lists()
            elif self.snow_balls[6].collides_with_sprite(self.player_sprite):
                self.lifes -= 0.3
                self.snow_balls[6].remove_from_sprite_lists()
            elif self.snow_balls[7].collides_with_sprite(self.player_sprite):
                self.lifes -= 0.3
                self.snow_balls[7].remove_from_sprite_lists()
            if self.snow_balls[0].center_y <= 120: self.snow_balls[0].remove_from_sprite_lists()
            elif self.snow_balls[1].center_y <= 120: self.snow_balls[1].remove_from_sprite_lists()
            elif self.snow_balls[2].center_y <= 120: self.snow_balls[2].remove_from_sprite_lists()
            elif self.snow_balls[3].center_y <= 120: self.snow_balls[3].remove_from_sprite_lists()
            elif self.snow_balls[4].center_y <= 120: self.snow_balls[4].remove_from_sprite_lists()
            elif self.snow_balls[5].center_y <= 120: self.snow_balls[5].remove_from_sprite_lists()
            elif self.snow_balls[6].center_y <= 120: self.snow_balls[6].remove_from_sprite_lists()
            elif self.snow_balls[7].center_y <= 120: self.snow_balls[7].remove_from_sprite_lists()
        if self.player_sprite.center_x >= 300:
            self.flag = True
        if len(self.snow_balls) <= 8:
            self.flag = 'kill'
        
        if self.player_sprite.collides_with_sprite(self.snowman) and self.flag == True:
            self.player_sprite.center_x = 100
            self.player_sprite.center_y = 164
        elif self.player_sprite.collides_with_sprite(self.snowman) and self.flag == 'kill' and self.player_sprite.center_y <= 395:
            self.player_sprite.change_y = 8
        elif self.player_sprite.collides_with_sprite(self.snowman) and self.flag == 'kill' and self.player_sprite.center_y > 395:
            self.platforms_list.append(self.snowman)
        if self.flag == 'kill' and self.snowman.center_y <= 1500 and self.player_sprite.center_y >= 154:
            self.snowman.center_y += 0.3
            self.snowman.center_x += 1
        
        if self.player_sprite.collides_with_sprite(self.snow_ball_big):
            self.player_sprite.change_y = 8
        if self.player_sprite.center_x >= 2300:
            self.flag_2 = True
        if self.flag_2:
            if self.snow_ball_big.center_x >= 2180 and self.snow_ball_big.center_x < 3215:
                self.snow_ball_big.center_x += 3
                self.snow_ball_big.center_y -= 3
                self.snow_ball_big.change_angle = -5
            elif self.snow_ball_big.center_x < 2180:
                self.snow_ball_big.center_x += 1
                self.snow_ball_big.change_angle = -2
            elif self.snow_ball_big.center_x >= 3215 and self.snow_ball_big.center_x < 3500:
                self.snow_ball_big.center_x += 2.5
                self.snow_ball_big.change_angle = -4
            elif self.snow_ball_big.center_x >= 3500 and self.snow_ball_big.center_x < 3650:
                self.snow_ball_big.center_x += 2
                self.snow_ball_big.change_angle = -3
            elif self.snow_ball_big.center_x >= 3650 and self.snow_ball_big.center_x < 3800:
                self.snow_ball_big.center_x += 1.5
                self.snow_ball_big.change_angle = -2
            elif self.snow_ball_big.center_x >= 3800 and self.snow_ball_big.center_x < 4000:
                self.snow_ball_big.center_x += 1
                self.snow_ball_big.change_angle = -1
            elif self.snow_ball_big.center_x >= 4000 and self.snow_ball_big.center_x < 4100:
                self.snow_ball_big.center_x += 0.5
                self.snow_ball_big.change_angle = -0.5
            else:
                self.snow_ball_big.center_y = -1000         
                self.snowman.center_y -= 1
                self.snowman.center_x += 1
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
        
window = Level_10(800, 600, "Super Game")
window.setup()
arcade.run()
