import joblib
import os
import numpy as np

def get_length_subject_trials(path_to_dataset,subject):
    return len(os.listdir((path_to_dataset+subject+'/')))

def load_subject_trial(path_to_dataset,subject,trial):
    try:
        __a = ' '
        __path = path_to_dataset+subject+'/'+str(trial)+'.sav'
        __data = joblib.load(__path)
        assert isinstance(__data,dict)
        assert 'emg' in __data.keys()
        assert 'cue' in __data.keys()
        return __data
    except AssertionError as __a:
        # print(__a)
        __data = None
        return __data
    except FileNotFoundError as __a:
        # print(__a)
        __data = None
        return __data

def load_subject_data(path_to_dataset,subject):
    subject = subject
    __length = get_length_subject_trials(path_to_dataset,subject)
    __emg = 0
    __cue = 0
    for trial in range(1,__length+1):
        __data = load_subject_trial(path_to_dataset,subject,trial)
        if __data != None:
            if trial==1:
                __emg = __data['emg']
                __cue = __data['cue']
            else:
                __emg = np.vstack((__emg, __data['emg']))
                __cue += __data['cue']
    return __emg, np.array(__cue)

def load_all_subjects_data(path_to_dataset):
    __subjects = os.listdir(path_to_dataset)
    __emg = np.empty((0,1))
    __cue = 0

    for __s, __subject in enumerate(__subjects):
        if __s==0:
            __emg, __cue = load_subject_data(path_to_dataset, __subject)
        else:
            __data_emg, __data_cue = load_subject_data(path_to_dataset, __subject)
            try:
                assert isinstance(__data_emg,np.ndarray)
                assert __emg.shape[-1] == __data_emg.shape[-1]
                __emg = np.vstack((__emg,__data_emg))
                __cue = np.hstack((__cue,__data_cue))
            except AssertionError:
                pass    

    return __emg, __cue