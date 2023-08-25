import random
import arcade


class Spaceship ( arcade.Sprite ) :
    def __init__ ( self , game ):
        super().__init__ ( ":resources:images/space_shooter/playerShip2_orange.png" )
        self.center_x = game.width // 2
        self.center_y = 40
        self.width = 48
        self.height = 48
        self.speed = 15

class Enemy ( arcade.Sprite ) :
    def __init__(self, game ):
        super().__init__ ( ":resources:images/space_shooter/playerShip1_blue.png" )
        self.center_x = random.randint ( 0 , game.width - 48 )
        self.center_y = game.height + 24
        self.angle = 180
        self.width = 48 
        self.height = 48 


class Game ( arcade.Window ) :

    def __init__ ( self ) :                                                                            # Introduction
        super().__init__( width= 1000 , height= 700 , title = "Intesllar" )
        arcade.set_background_color ( arcade.color.DARK_BLUE )
        self.background = arcade.load_texture ( ":resources:images/backgrounds/stars.png" )
        self.me = Spaceship ( self )
        self.enemy = Enemy ( self )

    def on_draw ( self ) :                                                                             # Show
        arcade.start_render ()
        arcade.draw_lrwh_rectangle_textured ( 0 , 0 , self.width , self.height , self.background )
        self.me.draw ()
        self.enemy.draw ()

    def on_key_press ( self , symbol : int , modifiers : int ) :                                       # Spaceship movement
        if symbol == 65363 :                                                                           # move to right
            self.me.center_x += self.me.speed
        
        elif symbol == 65361 :                                                                         # move to left
            self.me.center_x -= self.me.speed

    def on_update ( self , delta_time : float ) :                                                      # Enemy movement
        self.enemy.center_y -= 1
        

window = Game ()
arcade.run ()