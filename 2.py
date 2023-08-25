import arcade

column_space = 20
row_space = 20
left = 110
up = 110
size = 9

arcade.open_window ( 400 , 400 , "Complex Loop - Box")
arcade.set_background_color (arcade.color.WHITE)
arcade.start_render ()

for row in range ( 10 ) :
    for column in range ( 10 ) :
        x = column * column_space + left
        y = row * row_space + up
        if row % 2 == 0 :
            if column % 2 == 0 :
                arcade.draw_rectangle_filled ( x , y , size , size , arcade.color.RED , 45 )
            else :
                arcade.draw_rectangle_filled ( x , y , size , size , arcade.color.BLUE , 45 )
        
        else :
            if column % 2 == 0 :
                arcade.draw_rectangle_filled ( x , y , size , size , arcade.color.BLUE , 45 )
            else :
                arcade.draw_rectangle_filled ( x , y , size , size , arcade.color.RED , 45 )

arcade.finish_render ()
arcade.run ()