class Config:
    SCALE = 1
    TILE_SIZE = 16
    COL = 20
    ROW = 20
    SCREEN_WIDTH = TILE_SIZE * COL * SCALE
    SCREEN_HEIGHT = TILE_SIZE * ROW * SCALE 
    PLAYER_START = (100, 50)
    PLAYER_ANIMATION_TIMER = 200

    DEFAULT_ELF_ANIMATION_PATH = "../assets/elf_pack/sword/elf_sword_color_3"
    DEFAULT_ELF_ANIMATIONS = {"idle": 6, "walk": 6, "attack": 6, "death": 6}