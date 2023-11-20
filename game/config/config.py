class Config:
    SCALE = 1
    CAMERA_SCALE = 2
    TILE_SIZE = 16
    COL = 20
    ROW = 20
    SCREEN_WIDTH = TILE_SIZE * COL * SCALE
    SCREEN_HEIGHT = TILE_SIZE * ROW * SCALE 
    DEFAULT_LEVEL_SIZE = SCREEN_WIDTH;
    
    # Player
    PLAYER_START = (150, 120)
    PLAYER_ANIMATION_TIMER = 100
    PLAYER_SPRITE_SIZE = 64
    DEFAULT_PLAYER_LAYER = 2

    # ANIMATION
    DEFAULT_ELF_ANIMATION_PATH = "../assets/elf_pack/sword/elf_sword_color_3"
    DEFAULT_ELF_ANIMATIONS = {"idle": 6, "walk": 6, "attack": 6, "death": 6}

    DEFAULT_ANIMATIONS_LIST = ["walk", "idle"]

    # CONTROLS
    MOVEMENT_TYPE = "keyboard"