import numpy as np
import time

motorAction = {
    1:'set',2:'flexion',3:'extension',4:'open hands',5:'close hands'
}

motorImagery = {1:'imagine_set',2:'imagine_flexion',3:'imagine_extension',4:'imagine_hands_open',5:'imagine_hands_closed'
}

rest = {1:'eye_close',2:'still'
}

artifacts = {1:'neck',2:'right_leg',3:'left_leg',4:'shoulder'
}

motorPattern = [1,2,3,1,5,4,1]
cueClasses = ['m', 'r', 'a']

# noSessionIterations = int(input("Enter no of session iterations:"))
# trialPerClass = int(input("Enter no of trials per class:"))
# epochTime = float(input("Enter epoch time frame in seconds:"))

cue = []


def cue_generator(trialPerClass):
# DAQ = 0

# while DAQ != noSessionIterations:
    # DAQ += 1
    useTime = False
    cueClassChoice = np.random.choice(np.array(cueClasses))
    # print(cueClassChoice)   #for testing to be removed
    if cueClassChoice == 'm':
        for trial in range(trialPerClass):
            for i in motorPattern:
                for motor in [motorImagery,motorAction]:
                    cue.append(motor[i])
                    useTime = True
                    # print(cue)  #for testing to be removed
                    '''
                        TODO
                        1. pass cue variable to cue_display thread
                        2. wait for updatedCue flag response from cue_display thread
                    '''
                    # time.sleep(epochTime)
    elif cueClassChoice == 'r':
        for trial in range(trialPerClass):
            cueChoice = np.random.choice(list(rest.values()))
            cue.append(cueChoice)
            # print(cue)  #for testing to be removed
            '''
                TODO
                1. pass cue variable to cue_display thread
                2. wait for updatedCue flag response from cue_display thread
            '''
    else:
        for trial in range(trialPerClass):
            cueChoice = np.random.choice(list(artifacts.values()))
            cue.append(cueChoice)
            # print(cue)  #for testing to be removed
            '''
                TODOs
                1. pass cue variable to cue_display thread
                2. wait for updatedCue flag response from cue_display thread
            '''
    return cueClassChoice, cue, useTime