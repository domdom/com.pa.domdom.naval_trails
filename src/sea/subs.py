# from pa_tools lib
import loader
import utils

from decimal import Decimal

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

def sub_explosion(boat_name, boat):
    bounds = boat.get('mesh_bounds', [0, 10, 0])
    model = loader.loads('''{
        "spec": {
            "shader": "meshParticle_unit",
            "shape": "mesh",
            "facing": "emitterZ",
            "red" : 0,
            "green" : 0,
            "blue" : 0,
            "size": [[0.9, 1], [1, 0]],
            "papa": "/pa/units/sea/''' + boat_name + '/' + boat_name + '''.papa",
            "polyAdjustCenter": 5,
            "materialProperties": {
                "DiffuseTexture": "/pa/units/sea/''' + boat_name + '/' + boat_name + '''_diffuse.papa",
                "MaterialTexture": "/pa/units/sea/''' + boat_name + '/' + boat_name + '''_material.papa",
                "MaskTexture": "/pa/units/sea/''' + boat_name + '/' + boat_name + '''_mask.papa",
                "TeamColor_Primary": 0,
                "TeamColor_Secondary": 0
            }
        },
        "gravity": [[0, 0], [1, -20]],
        "drag": 0.95,
        "lifetime": 5,
        "emissionBursts": 1,
        "bLoop": false
    }''')


    base_water_ring = loader.loads('''{
      "spec": {
        "shader": "particle_add",
        "facing": "EmitterZ",
        "size": [[0, 0.3 ], [0.2, 0.5 ] , [0.4, 0.75 ], [0.6, 0.875], [1, 1]],
        "red": 0.15,
        "green": 0.8,
        "blue": 1.0,
        "alpha": [[0, 1 ], [0.3, 0.3 ], [0.5, 0.2 ], [1, 0 ]],
        "baseTexture": "/pa/effects/textures/particles/simpleExplosionRing.papa"
      },
      "delay" : 0.4,
      "sizeX": 40.0,
      "sizeRangeX": 20,
      "offsetZ": 1.5,
      "emissionBursts": 1,
      "rotationRange": 0.5,
      "lifetime": 2,
      "lifetimeRange" : 1,
      "emitterLifetime": 2,
      "bLoop": false,
      "sort": "NoSort"
    }''')

    rings = []

    for i in range(0, 3):
        ring = copy.deepcopy(base_water_ring)
        rings.append(ring)


    base_mist = loader.loads('''{
      "spec": {
        "shader": "particle_transparent",
        "size": [[0, 0], [0.15, 3.5], [0.5, 2], [1, 1]],
        "red": 0.7,
        "green": 0.7,
        "blue": 1.5,
        "alpha": [[0.0, 0.1], [1.0, 0]],
        "cameraPush" : 1,
        "baseTexture": "/pa/effects/textures/particles/softSmoke.papa"
      },
      "delay" : 0.4,
      "offsetRangeX" : 1,
      "offsetRangeY" : 1,
      "offsetZ" : 0,
      "velocityZ" : 1,
      "velocity" : 7,
      "drag" : 0.97,
      "sizeX": 3.5,
      "emissionBursts": 9,
      "lifetime": 3.5,
      "lifetimeRange" : 0.7,
      "emitterLifetime": 1.0,
      "useWorldSpace" : true,
      "bLoop": false
    }''')

    mists = []
    for i in range(1, 5):
        mist = copy.deepcopy(base_mist)
        mist['offsetRangeX'] = 4 * (i - 1) + 0.4
        mist['offsetRangeY'] = mist['offsetRangeX']
        mist['velocity'] = 10.0 / (i * 2)
        mist['velocity'] = 3.5 / (i * 2)
        mists.append(mist)

    base_splash = loader.loads('''{
      "spec": {
        "shader": "particle_transparent",
        "facing" : "velocity",
        "red": 1,
        "green": 1,
        "blue": 1,
        "alpha": [[0.5, 0.8], [1.0, 0]],
        "sizeX": [[0, 1 ], [1, 0.1 ]],
        "sizeY" : [[0, 1], [1, 0.1 ]],
        "cameraPush" : 1,
        "baseTexture": "/pa/effects/textures/particles/simpleSmoke.papa"
      },
      "delay" : 0.4,
      "type" : "SHELL",
      "offsetRangeX" : 0.1,
      "offsetRangeY" : 0.1,
      "offsetRangeZ" : 0.5,
      "useRadialVelocityDir" : true,
      "offsetAllowNegZ" : false,
      "velocity" : 8,
      "velocityRange" : 7,
      "gravity" : -5,
      "sizeX": 1.5,
      "sizeY": 5,
      "sizeRangeY" : 2,
      "emissionBursts": 80,
      "lifetime": 1.4,
      "emitterLifetime": 1.0,
      "useWorldSpace" : true,
      "bLoop": false
    }''')

    splash_white = copy.deepcopy(base_splash)
    splash_blue = copy.deepcopy(base_splash)

    splash_blue['spec']['red'] = 0.15
    splash_blue['spec']['green'] = 0.5
    splash_blue['spec']['blue'] = 1

    light = loader.loads('''{
      "spec": {
        "shape": "pointlight",
        "red": 3.0,
        "green": 2.0,
        "blue": 0.7,
        "alpha": [[0, 3], [0.25, 1], [1, 0]]
      },
      "gravity": [[0, 0], [1, -20]],
      "drag": 0.95,
      "sizeX": 60,
      "emissionBursts": 1,
      "lifetime": 5,
      "emitterLifetime": 0.5,
      "bLoop": false,
      "endDistance": 2000
    }''')
    base_fire = loader.loads('''{
      "spec": {
        "shader": "particle_clip",
        "shape": "mesh",
        "facing": "EmitterZ",
        "red": [[0, 100], [0.35, 30]],
        "green": [[0, 50], [0.35, 4]],
        "blue": [[0, 10], [0.35, 1]],
        "alpha": [[0, 1], [0.8, 0.5], [1, 0]],
        "size": [[0, 0], [0.1, 1], [0.2, 1.5], [0.3, 1.6], [1, 0]],
        "papa": "/pa/effects/fbx/particles/sphere_ico16seg.papa",
        "materialProperties": {
          "Texture": "/pa/effects/textures/particles/flat.papa"
        }
      },
      "gravity": [[0, 0], [1, -20]],
      "rotationRange" : 3.14,
      "rotationRateRange" : 3.14,
      "drag": 0.95,
      "offsetZ" : 0,
      "sizeX": 4,
      "lifetime": 2,
      "emissionBursts": 1,
      "bLoop": false,
      "endDistance": 2000
    }''')

    base_obscure = loader.loads('''{
      "spec": {
        "shader": "particle_clip",
        "shape": "mesh",
        "facing": "EmitterZ",
        "red": 0.1,
        "green": 0.1,
        "blue": 0.2,
        "alpha": [[0, 0.0], [0.3, 0.3], [1, 0]],
        "size": [[0, 0], [0.1, 1], [0.2, 1.5], [0.3, 1.6], [1, 0]],
        "papa": "/pa/effects/fbx/particles/sphere_ico16seg.papa",
        "materialProperties": {
          "Texture": "/pa/effects/textures/particles/fire_puff.papa"
        }
      },
      "gravity": [[0, 0], [1, -20]],
      "rotationRange" : 3.14,
      "rotationRateRange" : 1,
      "drag": 0.95,
      "offsetZ" : 0,
      "sizeX": 5,
      "lifetime": 2,
      "emissionBursts": 1,
      "bLoop": false,
      "endDistance": 2000
    }''')

    explosions = []
    for i in range(0, 3):
        fire = copy.deepcopy(base_fire)
        smoke = copy.deepcopy(base_obscure)

        scale = Decimal(1.0 - abs(i - 1) / 3.0)

        time_scale = Decimal(1.0 - abs(i - 1) / 2.0)

        fire['offsetRangeY'] = 1 * (i - 1)
        fire['offsetY'] = (i - 1) * bounds[1] / 3.0
        fire['delay'] = (i - 1) * 0.3
        smoke['delay'] = (i - 1) * 0.3 + 0.1

        fire['lifetime'] *= time_scale
        smoke['lifetime'] *= time_scale

        fire['sizeX'] *= scale
        smoke['sizeX'] *= scale

        smoke['type'] = 'EMITTER'
        smoke['linkIndex'] = i * 2

        explosions.append(fire)
        explosions.append(smoke)


    base_bubbles = loader.loads('''{
            "spec" : {
                "shader" : "particle_add",
                "red" : 1,
                "green" : 1,
                "blue" : 1,
                "alpha" : [[0, 1], [1, 0]],
                "baseTexture" : "/pa/effects/textures/particles/dot.papa",
                "dataChannelFormat" : "PositionAndColor"
            },
            "sizeX" : 0.3,
            "emitterLifetime" : 10,
            "type" : "EMITTER",
            "lifetime" : 1,
            "gravity" : 10,
            "drag" : 0.95,
            "bLoop" : false
        }''')

    base_bubbles['offsetRangeX'] = bounds[0] / 3
    base_bubbles['offsetRangeY'] = bounds[1] / 3
    base_bubbles['offsetRangeZ'] = bounds[2] / 3

    base_bubbles['linkIndex'] = len(explosions)


    return explosions + [model, base_bubbles, light, splash_white, splash_blue] + rings + mists


def run():
    pa_base = utils.pa_media_dir()


    t1_sub_path = "pa/units/sea/attack_sub/attack_sub.json"
    t2_sub_path = "pa/units/sea/nuclear_sub/nuclear_sub.json"


    trail_offsets = {}
    trail_offsets['attack_sub'] = (0, 8, 0)
    trail_offsets['nuclear_sub'] = (0, 17.5, -2)

    

    units = [t1_sub_path, t2_sub_path]

    patches = []

    for boat_path in units:

        boat = loader.load(os.path.join(pa_base, boat_path))

        boat_name = os.path.splitext(os.path.basename(boat_path))[0]


        offset_x = []
        offset_z = []

        bounds = boat.get('mesh_bounds', [0, 0, 0])

        print (boat_name, bounds)

        trail = base_spiral_trail()

        for bubble_spiral in trail['emitters']:
            time_end = float(bubble_spiral['emitterLifetime'])
            rate = float(bubble_spiral['emissionRate'])

            bubble_spiral['offsetX'] = {'keys': [], "stepped" : True}
            bubble_spiral['offsetZ'] = {'keys': [], "stepped" : True}

            steps = int(time_end * rate)

            coils = 4

            radius = bounds[0] / 4.5

            for j in range(steps):
                o = j % 2

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
            "destination" : "/mod/sea/''' + boat_name + '''/trail.pfx",
            "patch" : [
                {"op" : "replace", "path" : "", "value" : ''' + loader.dumps(trail) + '''}
            ]
        }'''))
        patches.append(loader.loads('''{
            "target" : "/pa/effects/specs/default_explosion.pfx",
            "destination" : "/mod/sea/''' + boat_name + '''/death.pfx",
            "patch" : [
                {"op" : "replace", "path" : "/emitters", "value" : ''' + loader.dumps(sub_explosion(boat_name, boat), indent=2) + '''}
            ]
        }'''))
        patches.append(loader.loads('''{
            "target" : "/''' + boat_path + '''",
            "patch" : [
                {"op" : "add", "path" : "/fx_offsets", "value" : [
                    {
                        "type" : "moving",
                        "bone" : "bone_root",
                        "filename" : "/mod/sea/''' + boat_name + '''/trail.pfx",
                        "offset" : ''' + loader.dumps(trail_offsets.get(boat_name, [0, bounds[1]/2, 0])) + '''
                    }
                ]
                },
                {"op" : "add", "path" : "/events/died/effect_spec", "value" : "/mod/sea/''' + boat_name + '''/death.pfx"},
                {"op" : "add", "path" : "/events/died/effect_scale", "value" : 1}
            ]
        }'''))

    # print(loader.dumps(patches))

    return patches



