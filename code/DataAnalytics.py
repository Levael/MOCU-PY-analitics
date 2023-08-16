import matplotlib.pyplot as chart


class DataAnalytics:
    def __init__(self, data_object, mode = 'release'):
        self._mode = mode
        self._data = data_object.parsedData
        self._number_of_pairs = data_object.number_of_pairs
        self._number_of_corrupted_pairs = data_object.number_of_corrupted_pairs
        self._cpu_freq = 10_000     # tick per ms
        self._config = {
            'moog_markers':     [1, 'moog'],
            'oculus_markers':   [2, 'oculus'],

            'moog_divergent_value': 100,
            'oculus_divergent_value': 500
        }
        self._oculus_trials = []
        self._moog_trials = []
        self._divergent_oculus_trials = []
        self._divergent_moog_trials = []


        if (self._mode == 'debug'):
            print('DataAnalitics:	', 'Number of oculus trials', len(self.GetOculusTrials()))
            print('DataAnalitics:	', 'Number of moog halftrials', len(self.GetMoogHalfTrials()))
            #print('DataAnalitics:	', 'Oculus trials', self.GetOculusTrials())
            #print('DataAnalitics:	', 'Moog halftrials', self.GetMoogHalfTrials())


    def GetOculusTrials(self):
        trials = [[]]
        trials_index = 0

        # starts from 1 to have excess to previous item (zero)
        for i in range(self._number_of_pairs):
            # treat only to oculus points
            if not(self._data[i]['custom_value'] in self._config['oculus_markers']):
                continue

            self._oculus_trials.append(self._data[i])

            if len(self._oculus_trials) < 2:
                continue

            try:
                delay = (self._oculus_trials[-1]['time_stamp'] - self._oculus_trials[-2]['time_stamp']) / self._cpu_freq
            except:
                #print(self._data[i])
                delay = -1

            # throw away obviously not trial (happens in first trial with big delay)
            if delay > self._config['oculus_divergent_value']:
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
        for i in range(self._number_of_pairs):
            # treat only to moog points
            if not(self._data[i]['custom_value'] in self._config['moog_markers']):
                continue

            self._moog_trials.append(self._data[i])

            if len(self._moog_trials) < 2:
                continue

            try:
                delay = (self._moog_trials[-1]['time_stamp'] - self._moog_trials[-2]['time_stamp']) / self._cpu_freq
            except:
                print(self._data[i])
                delay = -1
            

            # throw away obviously not trial (happens in first trial with big delay)
            if delay > self._config['moog_divergent_value']:
                half_trials_index += 1
                half_trials.append([])
                half_trials[half_trials_index].append(delay)
                continue

            half_trials[half_trials_index].append(delay)

        return half_trials