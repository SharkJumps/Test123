# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Chise", color="#3C932A")


# The game starts here.

define config.name = _('Old School High School')

define gui.show_name = True

define config.version = "1.0"

define gui.about = _("Created by PyTom.\n\nHigh school backgrounds by Mugenjohncel.")
# label start:
#
#     show chise1
#     c "Hello world!"
#
#
#     scene bg 1
#
#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.
#
#     show eileen happy
#
#     # These display lines of dialogue.
#
#     e "You've created a new Ren'Py game."
#
#     e "Once you add a story, pictures, and music, you can release it to the world!"
#
#     # This ends the game.
#
#     return
