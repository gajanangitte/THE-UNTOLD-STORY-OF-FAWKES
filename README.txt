#######################################################################################################################################
#######################################################################################################################################
################################################ A Harry Potter Game ##################################################################
################################# Made using Python, Pygame, Doryen and Dawnlike library #############################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################

  No copyright infringement intended
  ALL RIGHTS RESERVED WITH WARNER BROS. AND J K ROWLING
NOTE: THIS IN NOT A ROGUELIKE
  
_______________SPECIAL THANKS TO_______________________________________________________________________________
 1. ROGUEBASIN
 2. MICHEAL COATES who designed his super-awesome lectures on game-programming,
 3. JUKEDROP
 4. 8ICONS.COM
 5. JKR for composing the Wizarding World
 
 You play as Fawkes the Phoenix and you have to save Harry James Potter.
 Gear up through levels and randomly generated rooms to experience a new thrill every time you enter the game.
 Reach the end and retrieve Harry Potter. Pick him up(you'll know how) and return to the spawing portal of level 1.
 
 To play just open main_game.py file and run it.....CHEERS
 
--------------------------------------------|| You don't need to read this ||---------------------------------------------------------
 |This is like my 3rd game and I exponential growth in my GAmeDEv basic skills. This project was originally designed                |
 |as an entry submission                                                                                                            |   
 |for SDSLabs, IIT Roorkee. It took me like 60 hours spread over 14 days in total to make this and it has been a hell of a journey. |
 --------------------------------------------|| You don't need to read this ||---------------------------------------------------------
 
 What follows is the code-info of the game as directed by Micheal(guruji)...HAve fun Playing and more fun while reading xD
 

                (                           )
          ) )( (                           ( ) )( (
       ( ( ( )  ) )                     ( (   (  ) )(
      ) )     ,,\\\                     ///,,       ) (
   (  ((    (\\\\//                     \\////)      )
    ) )    (-(__//                       \\__)-)     (
   (((   ((-(__||                         ||__)-))    ) )
  ) )   ((-(-(_||           ```\__        ||_)-)-))   ((
  ((   ((-(-(/(/\\        ''; 9.- `      //\)\)-)-))    )
   )   (-(-(/(/(/\\      '';;;;-\~      //\)\)\)-)-)   (   )
(  (   ((-(-(/(/(/\======,:;:;:;:,======/\)\)\)-)-))   )
    )  '(((-(/(/(/(//////:%%%%%%%:\\\\\\)\)\)\)-)))`  ( (
   ((   '((-(/(/(/('uuuu:WWWWWWWWW:uuuu`)\)\)\)-))`    )
     ))  '((-(/(/(/('|||:wwwwwwwww:|||')\)\)\)-))`    ((
  (   ((   '((((/(/('uuu:WWWWWWWWW:uuu`)\)\))))`     ))
        ))   '':::UUUUUU:wwwwwwwww:UUUUUU:::``     ((   )
          ((      '''''''\uuuuuuuu/``````         ))
            ))            `JJJJJJJJJ`           ((
             ((            LLLLLLLLLLL         ))
               ))         ///|||||||\\\       ((
                 ))      (/(/(/(^)\)\)\)       ((
                   ((                           ))
                     ((                       ((
                       ( )( ))( ( ( ) )( ) (()

class struc_Tile:

    '''This class functions as a struct that tracks the data for each tile 
    within a map.

    Attributes:
        block_path (arg, bool) : True if tile prevents actors from moving 
            through it under normal circumstances.
        explored (bool): Initializes to FALSE, set to true if player
            has seen it before.

    '''
 #    ___  _     _           __
#   / _ \| |__ (_) ___  ___| |_ ___
#  | | | | '_ \| |/ _ \/ __| __/ __|
#  | |_| | |_) | |  __/ (__| |_\__ \
#   \___/|_.__// |\___|\___|\__|___/
#           |__/

class obj_Actor:

    '''The actor object represents every entity in the game.

    This object is anything that can appear or act within the game.  Each entity 
    is made up of components that control how these objects work.

    Attributes:
        x (arg, int): position on the x axis
        y (arg, int): position on the y axis
        name_object (arg, str) : name of the object type, "chair" or
            "goblin" for example.
        animation (arg, list): sequence of images that make up the object's
            spritesheet. Created within the struc_Assets class.
        animation_speed (arg, float): time in seconds it takes to loop through
            the object animation.

    Components:
        creature: any object that has health, and generally can fight.
        ai: set of instructions an obj_Actor can follow.
        container: objects that can hold an inventory.
        item: items are items that are able to be picked up and (usually) 
            usable.
    
    '''

class obj_Game:
    
    '''The obj_Game tracks game progress

    This is an object that stores all the information used by the game to 'keep 
    track' of progress.  It tracks maps, objects, and game history or record of 
    messages.

    Attributes:
        current_map (obj): whatever map is currently loaded.
        current_objects (list): list of objects for the current map.
        message_history (list): list of messages that have been pushed
            to the player over the course of a game.'''
  
    def get_image(self, column, row, width = constants.CELL_WIDTH,
                  height = constants.CELL_HEIGHT, scale = None):
        '''This method returns a single sprite.

        Args:
            column (str): Letter which gets converted into an integer, column in 
                the spritesheet to be loaded.
            row (int): row in the spritesheet to be loaded.
            width (int): individual sprite width in pixels
            height (int): individual sprite height in pixels
            scale ((width, height)) = If included, scales the sprites to a new 
                size.

        Returns:
            image_list (list): This method returns a single sprite contained 
                within a list loaded from the spritesheet property.
            

 class com_Creature:
    
    '''Creatures are actors that have health and can fight.

    Attributes:
        name_instance (arg, str): name of instance. "Bob" for example.
        max_hp (arg, int): max health of the creature.
        death_function (arg, function): function to be executed when hp reaches 0.
        current_hp (int): current health of the creature.

    '''
   def map_create():

    '''Creates the default map.

    Currently, the map this function creatures is a small room with 2 pillars 
    within it.  It is a testing map.

    Returns:
        new_map (array): This array is populated with struc_Tile objects.

    Effects:
        Calls map_make_fov on new_map to preemptively create the fov.

    '''
        '''Check the current map for creatures at specified location.

    This function looks at that location for any object that has a creature
    component and returns it.  Optional argument allows user to exclude an 
    object from the search, usually the Player

    Args:
        x (int): x map coord to check for creature
        y (int): y map coord to check for creature
        exclude_object(obj_Actor, optional): if an object is passed into this 
            function, this object will be ignored by the search.

    Returns: 
        target (obj_Actor): but only if found at the location specified in the 
            arguments and if not excluded.

    '''
    def draw_game():
    
    '''Main call for drawing the entirity of the game.

    This method is responsible for regularly drawing the whole game.  It starts
    by clearing the main surface, then draws elements of the screen from front
    to back.

    The order of operations is:
    1) Clear the screen
    2) Draw the map
    3) Draw the objects
    4) Draw the debug console
    5) Draw the messages console
    6) Update the display

    '''
    def draw_text(display_surface, text_to_display, font,
              coords, text_color, back_color = None, center = False):
    ''' Displays text on the desired surface. 

    Args:
        display_surface (pygame.Surface): the surface the text is to be
            displayed on.
        text_to_display (str): what is the text to be written
        font (pygame.font.Font): font object the text will be written using
        coords ((int, int)): where on the display_surface will the object be
            written, the text will be drawn from the upper left corner of the 
            text.
        text_color ((int, int, int)): (R, G, B) color code for the desired color
            of the text.
        back_color ((int, int, int), optional): (R, G, B) color code for the 
            background.  If not included, the background is transparent.

    '''
   def helper_text_objects(incoming_text, incoming_font, incoming_color, incoming_bg):

    '''Generates the text objects used for drawing text.

    This function is most often used in conjuction with the draw_text method.  
    It generates the text objects used by draw_text to actually display whatever
    string is called by the method.

    Args:
        incoming_text (str):
        incoming_font (pygame.font.Font):
        incoming_color ((int, int, int)):
        incoming_bg ((int, int, int), optional):

    Returns:
        Text_surface (pygame.Surface):
        Text_surface.get_rect() (pygame.Rect): 

    '''
    def menu_inventory():

    '''Opens up the inventory menu.

    The inventory menu allows the player to examine whatever items they are 
    currently holding.  Selecting an item will drop it.

    '''

    # SURFACE_MAIN is the display surface, a special surface that serves as the
    # root console of the whole game.  Anything that appears in the game must be
    # drawn to this console before it will appear.
   
   def game_message(game_msg, msg_color = constants.COLOUR_GREY):

    '''Adds message to the message history

    Args:
        game_msg (str): Message to be saved
        msg_color ((int, int, int), optional) = color of the message

    '''
    
    
