from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import models
from perlin_noise import PerlinNoise
app = Ursina(borderless = False)
window.title = 'Minceraft'

# Choosing between blocks
def update():
    global block_pick

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['5']: block_pick = 5
    if held_keys['6']: block_pick = 6
    if held_keys['7']: block_pick = 7

# types of objects, textures and sounds
Grass_texture = load_texture('assets/grass_texture_2.png')
Stone_texture = load_texture('assets/stone1.png')
dirt_texture = load_texture('assets/dirt.png')
brik_texture = load_texture('assets/Brick.png')
Obsidian_texture = load_texture('assets/Obsidian.png')
Diamond_block_texture = load_texture('assets/Diamond_block.png')
sky_texture = load_texture('assets/skyblock3.png')
arm_texture = load_texture('assets/armreal.png')
inventory2 = load_texture('assets/inventory_inside.png')
Diamond_pickaxe_texture = load_texture('assets/pickaxereal.png')
oak_texture = load_texture('assets/oak_block.png')
inventory_bar = load_texture('assets/inventorybar.png')
punch_sound = Audio('assets/assets_punch_sound',loop = False, autoplay = False)
block_pick = 1

# class defining the sky
class Sky(Entity):
    def __init__(self):
        super(Sky, self).__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True)

# class defining the hand
class Hand(Entity):
    def __init__(self):
        super(Hand, self).__init__(
            parent = camera.ui,
            model = 'cube',
            texture = arm_texture,
            position = Vec2(0.9,-0.4))

    def active(self):
        self.position = Vec2(0.3,-0.5)

    def passive(self):
        self.position = Vec2(0.5,-0.7)

# class for diamond pickaxe
class Diamondpickaxe(Entity):
    def __init__(self):
        super(Diamondpickaxe, self).__init__(
            parent=camera.ui,
            model='cube',
            texture=Diamond_pickaxe_texture,
            position=Vec2(0.7, -0.4))
    if held_keys['8']:
        Diamondpickaxe.visible = True
        Hand.visible = False

# class for inventory
class Inventory(Entity):
    def __init__(self):
        super(Inventory, self).__init__(
            parent = camera.ui,
            model = 'cube',
            texture = inventory_bar,
            position = Vec2(-0.3,-0.2))

# class defining Terrain
class Voxel(Button):
    def __init__(self, position =(1,2,3), texture = Grass_texture) :
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9, 1)),
            )



# defining how to destroy the blocks, defining when the sound plays and when blocks are placed
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = Grass_texture)
                if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, texture = Stone_texture)
                if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal, texture=brik_texture)
                if block_pick == 5: voxel = Voxel(position=self.position + mouse.normal, texture=Obsidian_texture)
                if block_pick == 6: voxel = Voxel(position=self.position + mouse.normal, texture=oak_texture)
                if block_pick == 7: voxel = Voxel(position=self.position + mouse.normal, texture=Diamond_block_texture)
            if key == 'right mouse down':
                destroy(self)

# the radius of the terrain
for z in range(25):
    for x in range(25):
        voxel = Voxel(position = (x,0,z))
player = FirstPersonController()
sky = Sky()
hand = Hand()
inventory = Inventory()
dpickaxe = Diamondpickaxe()
app.run()