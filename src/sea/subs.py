import loader
import utils

#for i in xrange(2):
    #water_trail['emitters'][i]['offsetRangeX'] = 0
    #water_trail['emitters'][i]['offsetRangeY'] = 0
    #water_trail['emitters'][i]['offsetRangeZ'] = 0
    #water_trail['emitters'][i]['offsetX'] = {'keys':[], 'stepped':True}
    #water_trail['emitters'][i]['offsetY'] = {'keys':[], 'stepped':True}
    #water_trail['emitters'][i]['offsetZ'] = {'keys':[], 'stepped':True}

    #time_end = water_trail['emitters'][i]['emitterLifetime']
    #rate = water_trail['emitters'][i]['emissionRate']

    #steps = int(time_end * rate)

    #coils = 4

    #radius = bounds[0] / 3

    #for j in xrange(steps):
        #o = random.randint(0, 1)
        ## o = i

        #d = 1

        #a = float(j) / steps
        #water_trail['emitters'][i]['offsetX']['keys'].append([time_end * a, radius * math.cos(o * math.pi + d * a * math.pi * 2 * coils)])
        #water_trail['emitters'][i]['offsetZ']['keys'].append([time_end * a, radius * math.sin(o * math.pi + d * a * math.pi * 2 * coils)])

    ##water_trail['emitters'][i]['gravity'] = 1
    #water_trail['emitters'][i]['velocity'] = float(boat['navigation']['move_speed']) / 2

    #water_trail['emitters'][i]['velocityY'] = 1
    #water_trail['emitters'][i]['velocityZ'] = 0.25

    #water_trail['emitters'][i]['drag'] = 0.9887

def run():
    pa_base = utils.pa_media_dir()

    t1_sub_path = "/pa/units/sea/attack_sub/attack_sub.json"
    t2_sub_path = "/pa/units/sea/nuclear_sub/nuclear_sub.json"

    print(pa_base)

    pass

