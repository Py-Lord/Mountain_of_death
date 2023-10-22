import arcade

MOVEMENT_SPEED = 2.1
JUMP_SPEED = 8
GRAVITY = 0.35

class Level(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        self.flag_5 = False
        self.flag_4 = True
        self.flag_3 = False
        self.flag_2 = False
        self.flag = False
        self.lifes = 3
        self.score = 0 
        self.score_2 = 1
        self.x = 100
        self.y = 164

        self.camera_sprites = arcade.Camera(800, 600)
        self.camera_gui = arcade.Camera(800, 600)
        
    def setup(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.music = arcade.Sound('./Resource/Sound effects/mario-game.mp3')
        self.main_sound = self.music.play()

        self.platforms_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bee_list = arcade.SpriteList()
        self.flags_list = arcade.SpriteList()
        self.flags_list2 = arcade.SpriteList()
        self.fly_list = arcade.SpriteList()
        self.fly_list2 = arcade.SpriteList()
        self.bird_list = arcade.SpriteList()

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

        for x in range(-286, 800, 64):
            grass_sprite = arcade.Sprite("./Resource/Images/grass.png", 0.5)
            grass_sprite.center_x = x
            grass_sprite.center_y = 90
            self.platforms_list.append(grass_sprite)
        for x in range(1440, 4385, 64):
            grass_sprite = arcade.Sprite("./Resource/Images/grass.png", 0.5)
            grass_sprite.center_x = x
            grass_sprite.center_y = 729
            self.platforms_list.append(grass_sprite)
        for x in range(2118, 2247, 64):
            grass_sprite = arcade.Sprite("./Resource/Images/grass.png", 0.5)
            grass_sprite.center_x = x
            grass_sprite.center_y = 793
            self.platforms_list.append(grass_sprite)
        for x in range(3040, 3233, 64):
            grass_sprite = arcade.Sprite("./Resource/Images/grass.png", 0.5)
            grass_sprite.center_x = x
            grass_sprite.center_y = 793
            self.platforms_list.append(grass_sprite)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.platforms_list, gravity_constant=GRAVITY)
        
        for x in range(-286, 867, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = x
            ground_sprite.center_y = 30
            self.platforms_list.append(ground_sprite)
        for i in range(0, 600, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = 801 + i
            ground_sprite.center_y = 89 + i
            self.platforms_list.append(ground_sprite)
        for i in range(0, 600, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = 865 + i
            ground_sprite.center_y = 89 + i
            self.platforms_list.append(ground_sprite)
        for i in range(0, 600, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = 929 + i
            ground_sprite.center_y = 89 + i
            self.platforms_list.append(ground_sprite)
        for x in range(1440, 4449, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = x
            ground_sprite.center_y = 665
            self.platforms_list.append(ground_sprite)
        for x in range(2057, 2314, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = x
            ground_sprite.center_y = 729
            self.platforms_list.append(ground_sprite)
        for x in range(2976, 3297, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = x
            ground_sprite.center_y = 729
            self.platforms_list.append(ground_sprite)
        for i in range(0, 514, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = 4448 + i
            ground_sprite.center_y = 729 + i
            self.platforms_list.append(ground_sprite)
        for i in range(0, 449, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = 4512 + i
            ground_sprite.center_y = 729 + i
            self.platforms_list.append(ground_sprite)
        for i in range(0, 449, 64):
            ground_sprite = arcade.Sprite("./Resource/Images/ground.png", 0.5)
            ground_sprite.center_x = 4512 + i
            ground_sprite.center_y = 665 + i
            self.platforms_list.append(ground_sprite)

        for y in range(154, 539, 64):
            wall_sprite = arcade.Sprite("./Resource/Images/wall.png", 0.5)
            wall_sprite.center_x = 33
            wall_sprite.center_y = y
            self.platforms_list.append(wall_sprite)

        for i in range(0, 577, 64):
            grass_hill_sprite = arcade.Sprite("./Resource/Images/grass_hill.png", 0.5)
            grass_hill_sprite.center_x = 801 + i
            grass_hill_sprite.center_y = 153 + i
            self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resource/Images/grass_hill.png", 0.5)
        grass_hill_sprite.center_x = 2054
        grass_hill_sprite.center_y = 793
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resource/Images/grasshill.png", 0.5)
        grass_hill_sprite.center_x = 2310
        grass_hill_sprite.center_y = 793
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resource/Images/grass_hill.png", 0.5)
        grass_hill_sprite.center_x = 2976
        grass_hill_sprite.center_y = 793
        self.platforms_list.append(grass_hill_sprite)
        grass_hill_sprite = arcade.Sprite("./Resource/Images/grasshill.png", 0.5)
        grass_hill_sprite.center_x = 3296
        grass_hill_sprite.center_y = 793
        self.platforms_list.append(grass_hill_sprite)
        for i in range(0, 449, 64):
            grass_hill_sprite = arcade.Sprite("./Resource/Images/grass_hill.png", 0.5)
            grass_hill_sprite.center_x = 4448 + i
            grass_hill_sprite.center_y = 793 + i
            self.platforms_list.append(grass_hill_sprite)
        
        for i in range(0, 600, 64):
            coin_sprite = arcade.Sprite("./Resource/Images/gold.png", 0.5)
            coin_sprite.center_x = 801 + i
            coin_sprite.center_y = 180 + i
            self.coin_list.append(coin_sprite)
        for i in range(0, 259, 64):
            coin_sprite = arcade.Sprite("./Resource/Images/gold.png", 0.5)
            coin_sprite.center_x = 450 + i
            coin_sprite.center_y = 144
            self.coin_list.append(coin_sprite)
        for i in range(3100, 3229, 64):
            coin_sprite = arcade.Sprite("./Resource/Images/gold.png", 0.5)
            coin_sprite.center_x = i
            coin_sprite.center_y = 857
            self.coin_list.append(coin_sprite)
        for i in range(4084, 4213, 64):
            coin_sprite = arcade.Sprite("./Resource/Images/gold.png", 0.5)
            coin_sprite.center_x = i
            coin_sprite.center_y = 788
            self.coin_list.append(coin_sprite)
            
        self.exit_sprite = arcade.Sprite("./Resource/Images/exit.png", 0.5)
        self.exit_sprite.center_x = 4346
        self.exit_sprite.center_y = 788

        self.bee_sprite = arcade.Sprite("./Resource/Images/bee.png", 0.5)
        self.bee_sprite.center_x = 1990
        self.bee_sprite.center_y = 788
        bee_2_sprite = arcade.Sprite("./Resource/Images/bee_2.png", 0.5)
        bee_2_sprite.center_x = 1460
        bee_2_sprite.center_y = 788
        self.bee_list.append(self.bee_sprite)
        self.bee_list.append(bee_2_sprite)

        self.fly_sprite = arcade.Sprite("./Resource/Images/fly.png", 0.5)
        self.fly_sprite.center_x = 2374
        self.fly_sprite.center_y = 788
        self.fly_list.append(self.fly_sprite)
        fly_2_sprite = arcade.Sprite("./Resource/Images/fly_2.png", 0.5)
        fly_2_sprite.center_x = 2612
        fly_2_sprite.center_y = 788
        self.fly_list.append(fly_2_sprite)
        self.fly = arcade.Sprite("./Resource/Images/fly_2.png", 0.5)
        self.fly.center_x = 2676
        self.fly.center_y = 788
        self.fly_list2.append(self.fly)
        fly2 = arcade.Sprite("./Resource/Images/fly.png", 0.5)
        fly2.center_x = 2914
        fly2.center_y = 788
        self.fly_list2.append(fly2)

        self.bird_sprite = arcade.Sprite("./Resource/Images/bird.png", 0.6) 
        self.bird_sprite.center_x = 3364
        self.bird_sprite.center_y = 800
        self.bird_list.append(self.bird_sprite)
        bird_2 = arcade.Sprite("./Resource/Images/bird_2.png", 0.6)
        bird_2.center_x = 4000
        bird_2.center_y = 800
        self.bird_list.append(bird_2)

        self.FLAG = arcade.Sprite("./Resource/Images/flagRed.png", 0.5)
        self.FLAG.center_x = 2118
        self.FLAG.center_y = 857
        self.flags_list.append(self.FLAG)
        Flag = arcade.Sprite("./Resource/Images/flagRed1.png", 0.5)
        Flag.center_x = 2118
        Flag.center_y = 857
        self.flags_list.append(Flag)
        self.FLAG2 = arcade.Sprite("./Resource/Images/flagRed.png", 0.5)
        self.FLAG2.center_x = 3040
        self.FLAG2.center_y = 857
        self.flags_list2.append(self.FLAG2)
        Flag2 = arcade.Sprite("./Resource/Images/flagRed1.png", 0.5)
        Flag2.center_x = 3040
        Flag2.center_y = 857
        self.flags_list2.append(Flag2)
    def on_draw(self):
        arcade.start_render()
        self.camera_sprites.use()
        arcade.draw_text(f'Money: {self.score}    Lifes: {self.lifes}', -380 + self.player_sprite.center_x, 250 + self.player_sprite.center_y, arcade.color.BLACK, 20)
        self.flags_list[0].draw()
        self.flags_list2[0].draw()
        if self.flag_5 == False or self.flag_5 == True: self.bird_list[0].draw()
        if self.flag == False or self.flag == True: self.bee_list[0].draw()
        if self.flag_2 == False or self.flag_2 == True: self.fly_list[0].draw()
        if self.flag_3 == False or self.flag_3 == True: self.fly_list2[0].draw()
        self.coin_list.draw()
        self.player_sprite.draw()
        self.platforms_list.draw()
        self.exit_sprite.draw()
        self.camera_gui.use()

    def update(self, delta_time):
        self.set_update_rate(1/110)
        self.player_sprite.update_animation()
        self.platforms_list.update()
        self.physics_engine.update()
        self.coin_list.update()
        self.scroll_to_player()

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 5
            self.coin_sound = arcade.load_sound('./Resource/Sound effects/money.mp3')
            arcade.play_sound(self.coin_sound, volume = 2)

        if self.player_sprite.center_x > 4512:
            self.close()
            from level_2 import Level_2

        if self.flag == False and self.bee_list[0].center_x > 1460:
            self.bee_list[0].center_x = self.bee_list[0].center_x - 2
        elif self.flag == False and self.bee_list[0].center_x == 1460:
            self.flag = True
            self.bee_sprite.remove_from_sprite_lists()
            self.bee_list[0].center_x = 1460
        if self.flag == True and self.bee_list[0].center_x >= 1460 and self.bee_list[0].center_x < 1990:
            self.bee_list[0].center_x = self.bee_list[0].center_x + 2
        elif self.flag == True and self.bee_list[0].center_x == 1990:
            self.bee_sprite = arcade.Sprite("./Resource/Images/bee.png", 0.5)
            self.bee_sprite.center_x = 1990
            self.bee_sprite.center_y = 788
            self.bee_list.insert(0, self.bee_sprite)
            self.flag = False

        if self.player_sprite.collides_with_sprite(self.bee_list[0]) and self.player_sprite.center_y >= 832 and self.flag != 'Kill':
            self.flag = 'Kill'
            self.player_sprite.change_y = 8
            coin_sprite = arcade.Sprite("./Resource/Images/gold.png", 0.5)
            coin_sprite.center_x = self.bee_list[0].center_x - 80 
            coin_sprite.center_y = 788 
            self.coin_list.append(coin_sprite)
        elif self.player_sprite.collides_with_sprite(self.bee_list[0]) and self.player_sprite.center_y < 832 and (self.flag == True or self.flag == False):
            self.lifes -= 1
            self.player_sprite.center_x = self.x
            self.player_sprite.center_y = self.y

        if self.player_sprite.center_x >= 2090 and self.player_sprite.center_x < 3012 and self.flag_4:
            self.FLAG.remove_from_sprite_lists()
            self.x = 2120
            self.y = 857
        elif self.player_sprite.center_x >= 3012:
            self.FLAG2.remove_from_sprite_lists()
            self.x = 3040
            self.y = 857
            self.flag_4 = False

        if self.lifes == 0:
            self.music.stop(self.main_sound)
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

        if self.flag_2 == False and self.fly_list[0].center_x > 2374:
            self.fly_list[0].center_x = self.fly_list[0].center_x - 2
        elif self.flag_2 == False and self.fly_list[0].center_x == 2374:
            self.flag_2 = True
            self.fly_sprite.remove_from_sprite_lists()
            self.fly_list[0].center_x = 2374
        if self.flag_2 == True and self.fly_list[0].center_x >= 2374 and self.fly_list[0].center_x < 2612:
            self.fly_list[0].center_x = self.fly_list[0].center_x + 2
        elif self.flag_2 == True and self.fly_list[0].center_x == 2612:
            self.fly_sprite = arcade.Sprite("./Resource/Images/fly.png", 0.5)
            self.fly_sprite.center_x = 2612
            self.fly_sprite.center_y = 788
            self.fly_list.insert(0, self.fly_sprite)
            self.flag_2 = False

        if self.flag_3 == False and self.fly_list2[0].center_x < 2914:
            self.fly_list2[0].center_x = self.fly_list2[0].center_x + 2
        elif self.flag_3 == False and self.fly_list2[0].center_x == 2914:
            self.flag_3 = True
            self.fly.remove_from_sprite_lists()
            self.fly_list2[0].center_x = 2914
        if self.flag_3 == True and self.fly_list2[0].center_x <= 2914 and self.fly_list2[0].center_x > 2676:
            self.fly_list2[0].center_x = self.fly_list2[0].center_x - 2
        elif self.flag_3 == True and self.fly_list2[0].center_x == 2676:
            self.fly = arcade.Sprite("./Resource/Images/fly_2.png", 0.5)
            self.fly.center_x = 2676
            self.fly.center_y = 788
            self.fly_list2.insert(0, self.fly)
            self.flag_3 = False
        
        if self.player_sprite.collides_with_sprite(self.fly_list[0]) and self.player_sprite.center_y >= 832 and self.flag_2 != 'Kill':
            self.flag_2 = 'Kill'
            self.player_sprite.change_y = 8
            coin_sprite = arcade.Sprite("./Resource/Images/gold.png", 0.5)
            coin_sprite.center_x = self.fly_list[0].center_x + 80 
            coin_sprite.center_y = 788 
            self.coin_list.append(coin_sprite)
        elif self.player_sprite.collides_with_sprite(self.fly_list[0]) and self.player_sprite.center_y < 832 and (self.flag_2 == True or self.flag_2 == False):
            self.lifes -= 1
            self.player_sprite.center_x = self.x
            self.player_sprite.center_y = self.y
                                                        
        if self.player_sprite.collides_with_sprite(self.fly_list2[0]) and self.player_sprite.center_y >= 832 and self.flag_3 != 'Kill':
            self.flag_3 = 'Kill'
            self.player_sprite.change_y = 8
            coin_sprite = arcade.Sprite("./Resource/Images/gold.png", 0.5)
            coin_sprite.center_x = self.fly_list2[0].center_x - 80 
            coin_sprite.center_y = 788 
            self.coin_list.append(coin_sprite)
        elif self.player_sprite.collides_with_sprite(self.fly_list2[0]) and self.player_sprite.center_y < 832 and (self.flag_3 == True or self.flag_3 == False):
            self.lifes -= 1
            self.player_sprite.center_x = self.x
            self.player_sprite.center_y = self.y
        
        if self.flag_5 == False and self.bird_list[0].center_x < 4000:
            self.bird_list[0].center_x = self.bird_list[0].center_x + 3
        elif self.flag_5 == False and self.bird_list[0].center_x == 4000:
            self.flag_5 = True
            self.bird_sprite.remove_from_sprite_lists()
            self.bird_list[0].center_x = 4000
        if self.flag_5 == True and self.bird_list[0].center_x <= 4000 and self.bird_list[0].center_x > 3364:
            self.bird_list[0].center_x = self.bird_list[0].center_x - 3
        elif self.flag_5 == True and self.bird_list[0].center_x == 3364:
            self.bird_sprite = arcade.Sprite("./Resource/Images/bird.png", 0.6)
            self.bird_sprite.center_x = 3364
            self.bird_sprite.center_y = 800
            self.bird_list.insert(0, self.bird_sprite)
            self.flag_5 = False

        if self.player_sprite.collides_with_sprite(self.bird_list[0]) and self.player_sprite.center_y >= 868 and self.score_2 == 1:
            self.score_2 += 1
            self.player_sprite.change_y = 8
        elif self.player_sprite.collides_with_sprite(self.bird_list[0]) and self.player_sprite.center_y >= 868 and self.flag_5 != 'Kill' and self.score_2 == 2:
            self.flag_5 = 'Kill'
            self.player_sprite.change_y = 8
            coin_sprite = arcade.Sprite("./Resource/Images/gold.png", 0.5)
            coin_sprite.center_x = self.bird_list[0].center_x + 80 
            coin_sprite.center_y = 788 
            self.coin_list.append(coin_sprite)
            coin_sprite = arcade.Sprite("./Resource/Images/gold.png", 0.5)
            coin_sprite.center_x = self.bird_list[0].center_x + 100 
            coin_sprite.center_y = 788 
            self.coin_list.append(coin_sprite)
        elif self.player_sprite.collides_with_sprite(self.bird_list[0]) and self.player_sprite.center_y < 868 and (self.flag_5 == True or self.flag_5 == False):
            self.lifes -= 1
            self.player_sprite.center_x = self.x
            self.player_sprite.center_y = self.y
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
                jump =  arcade.load_sound('./Resource/Sound effects/jump.mp3')
                arcade.play_sound(jump, volume = 2)
        elif key == arcade.key.LEFT:
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

    def on_resize(self, width, height):
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))
        
window = Level(800, 600, "Super Game")
window.setup()
arcade.run()