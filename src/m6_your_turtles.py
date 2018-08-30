"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Justin Ogasawara.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

Speed_Racer1 = rg.SimpleTurtle('turtle')
Speed_Racer1.pen = rg.Pen('blue', 3)
Speed_Racer1.speed = 10
Speed_Racer2 = rg.SimpleTurtle('turtle')
Speed_Racer2.pen = rg.Pen('red', 3)
Speed_Racer2.speed = 10
radius = 10
for k in range(20):

    Speed_Racer1.draw_circle(radius)
    Speed_Racer2.draw_circle(radius)
    Speed_Racer1.pen_up()
    Speed_Racer2.pen_up()
    Speed_Racer1.right(45)
    Speed_Racer2.right(135)
    Speed_Racer1.forward(8)
    Speed_Racer2.forward(8)
    Speed_Racer2.left(135)
    Speed_Racer1.left(45)
    Speed_Racer1.pen_down()
    Speed_Racer2.pen_down()
    radius = radius + 5

window.close_on_mouse_click()