import copy
import numpy as np

def GraspRelease(cue_variable):
    cue = copy.deepcopy(cue_variable)
    try:
        if isinstance(cue,np.ndarray):
            cue = cue.tolist()
        assert isinstance(cue,list)
        for i,_ in enumerate(cue):
            if cue[i]=='End of sessions':
                cue[i]='set'
            if cue[i]=='close hands':
                cue[i]='grasp'
            if cue[i]=='imagine_extension':
                cue[i]='release'
            if cue[i]=='imagine_flexion':
                cue[i]='grasp'
            if cue[i]=='imagine_hands_closed':
                cue[i]='grasp'
            if cue[i]=='imagine_hands_open':
                cue[i]='release'
            if cue[i]=='imagine_set':
                cue[i]='set'
            if cue[i]=='open hands':
                cue[i]='release'
            if cue[i]=='flexion':
                cue[i]='grasp'
            if cue[i]=='extension':
                cue[i]='release'
            if cue[i]=='eye_close':
                cue[i]='set'
            if cue[i]=='still':
                cue[i]='set'
        return np.array(cue)
    except Exception as e:
        print(e)
        return None
