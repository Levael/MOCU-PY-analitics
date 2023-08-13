import matplotlib.pyplot as chart


class DataAnalitics:
    def __init__(self, data_object, mode = 'release'):
        self._mode = mode
        self._data = data_object.parsedData
        self._number_of_pairs = data_object.number_of_pairs
        self._number_of_corrupted_pairs = data_object.number_of_corrupted_pairs
        self._cpu_freq = 10_000     # tick per ms
        self._divergent_trials = []
        self._config = {
            'moog_markers':     [1, 'moog'],
            'oculus_markers':   [2, 'oculus']
        }


        if (self._mode == 'debug'):
            print('DataAnalitics.	', 'Number of oculus trials', len(self.GetOculusTrials()))
            print('DataAnalitics.	', 'Number of moog halftrials', len(self.GetMoogHalfTrials()))
            #print('DataAnalitics.	', 'Oculus trials', self.GetOculusTrials())
            #print('DataAnalitics.	', 'Moog halftrials', self.GetMoogHalfTrials())


    def GetOculusTrials(self):
        trials = [[]]
        trials_index = 0

        # starts from 1 to have excess to previous item (zero)
        for i in range(1, self._number_of_pairs):
            # treat only to oculus points
            if not(self._data[i]['custom_value'] in self._config['oculus_markers']):
                continue

            try:
                delay = (self._data[i]['time_stamp'] - self._data[i-1]['time_stamp']) / self._cpu_freq
            except:
                #print(self._data[i])
                delay = -1

            # throw away obviously not trial (happens in first trial with big delay)
            if delay > 100:
                trials_index += 1
                trials.append([])
                trials[trials_index].append(delay)
                continue

            trials[trials_index].append(delay)

        return trials


    def GetMoogHalfTrials(self):
        half_trials = [[]]
        half_trials_index = 0

        # starts from 1 to have excess to previous item (zero)
        for i in range(1, self._number_of_pairs):
            # treat only to moog points
            if not(self._data[i]['custom_value'] in self._config['moog_markers']):
                continue

            try:
                delay = (self._data[i]['time_stamp'] - self._data[i-1]['time_stamp']) / self._cpu_freq
            except:
                print(self._data[i])
                delay = -1
            

            # throw away obviously not trial (happens in first trial with big delay)
            if delay > 200:
                half_trials_index += 1
                half_trials.append([])
                half_trials[half_trials_index].append(delay)
                continue

            half_trials[half_trials_index].append(delay)

        return half_trials