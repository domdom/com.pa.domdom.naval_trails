# from pa_tools lib
import loader
import utils

# from python
import random
import math
import copy
import os

# the bubble spiral made by the sub engines
def base_spiral_trail():
    blue_bubbles = loader.loads("""
    {
        "description": "main particles - close to water color",
        "spec": {
            "shader": "particle_transparent",
            "size": [ [ 0, 1.5 ], [ 0.1, 0.5 ], [ 1, 0 ] ],
            "red": 0.15,
            "green": 0.5,
            "blue": 1.0,
            "alpha": [ [ 0, 0.4 ], [ 1, 0 ] ],
            "baseTexture": "/pa/effects/textures/particles/softdot.papa"
        },
        "velocityY": 100,
        "sizeX": 1.0,
        "sizeRangeX": 1,
        "emissionRate": 150,
        "lifetime": 1.4,
        "emitterLifetime": 2.0,
        "lifetimeRange": 5.0,
        "useWorldSpace": true,
        "killOnDeactivate": false,
        "bLoop": true,
        "endDistance": 1500
    }
    """)
    white_bubbles = loader.loads("""
    {
        "description": "adds some white dots",
        "spec": {
            "shader": "particle_transparent",
            "size": [ [ 0, 1 ], [ 0.1, 0.5 ], [ 1, 0 ] ],
            "red": 1,
            "green": 1,
            "blue": 1,
            "alpha": [ [ 0, 0.5 ], [ 1, 0 ] ],
            "baseTexture": "/pa/effects/textures/particles/dot.papa"
        },
        "velocityY": 100,
        "sizeX": 0.8,
        "emissionRate": 75,
        "lifetime": 1.4,
        "emitterLifetime": 2.0,
        "lifetimeRange": 5.0,
        "useWorldSpace": true,
        "killOnDeactivate": false,
        "bLoop": true,
        "endDistance": 1500
    }
    """)

    return copy.deepcopy({'emitters': [blue_bubbles, white_bubbles]})

# the bubbles floating up from the side of the sub
def base_random_bubbles():
    pass  



def run():
    pa_base = utils.pa_media_dir()


    t1_sub_path = "pa/units/sea/attack_sub/attack_sub.json"
    t2_sub_path = "pa/units/sea/nuclear_sub/nuclear_sub.json"

    t1_sub = loader.load(os.path.join(pa_base, t1_sub_path))
    t2_sub = loader.load(os.path.join(pa_base, t2_sub_path))

    

    units = [t1_sub, t2_sub]

    patches = []

    for boat in units:

        offset_x = []
        offset_z = []

        bounds = boat.get('mesh_bounds', [0, 0, 0])
        trail = base_spiral_trail()

        for bubble_spiral in trail['emitters']:
            time_end = float(bubble_spiral['emitterLifetime'])
            rate = float(bubble_spiral['emissionRate'])

            bubble_spiral['offsetX'] = {'keys': [], "stepped" : True}
            bubble_spiral['offsetZ'] = {'keys': [], "stepped" : True}

            steps = int(time_end * rate)

            coils = 4

            radius = bounds[0] / 3

            for j in range(steps):
                o = random.randint(0, 1)

                d = 1

                a = float(j) / steps
                bubble_spiral['offsetX']['keys'].append([time_end * a, radius * math.cos(o * math.pi + d * a * math.pi * 2 * coils)])
                bubble_spiral['offsetZ']['keys'].append([time_end * a, radius * math.sin(o * math.pi + d * a * math.pi * 2 * coils)])

            #bubble_spiral['gravity'] = 1
            bubble_spiral['velocity'] = float(boat['navigation']['move_speed']) / 2

            bubble_spiral['velocityY'] = 1
            bubble_spiral['velocityZ'] = 0.25

            bubble_spiral['drag'] = 0.9887
        patches.append(loader.loads('''{
            "target" : "/base/wake_trail.pfx",
            "destination" : "/mod/sea/''' + str(len(patches)) + '''.pfx",
            "patch" : [
                {"op" : "replace", "path" : "", "value" : ''' + loader.dumps(trail) + '''}
            ]
        }'''))

    patches.append(loader.loads('''{
            "target" : "/''' + t1_sub_path + '''",
            "patch" : [
                {"op" : "add", "path" : "/fx_offsets", "value" : ''' + patches[0]['destination'] + '''}
            ]
        }'''))
    patches.append(loader.loads('''{
            "target" : "/''' + t2_sub_path + '''",
            "patch" : [
                {"op" : "add", "path" : "/fx_offsets", "value" : ''' + patches[1]['destination'] + '''}
            ]
        }'''))

    print(loader.dumps(patches))

    return patches



