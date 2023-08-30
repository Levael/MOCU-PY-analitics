class DataAnalytics:
    def __init__(self, data_object, mode='release'):
        self._mode = mode
        self._data = data_object.parsedData
        self._number_of_pairs = data_object.number_of_pairs
        self._number_of_corrupted_pairs = data_object.number_of_corrupted_pairs
        self._cpu_freq = 10_000  # tick per ms
        self._config = {
            'moog_markers':     [1, 'moog'],
            'oculus_markers':   [2, 'oculus'],

            'moog_divergent_value': 100,
            'oculus_divergent_value': 200
        }
        self._oculus_trials = []
        self._moog_trials = []
        
        self._oculus_pairs = []
        self._moog_pairs = []

        self._divergent_oculus_trials = []
        self._divergent_moog_trials = []
        
        self._filtered_oculus_trials = []
        self._filtered_moog_trials = []

        self._time_oculus_trials_delays = self.GetOculusTrials()
        self._time_moog_trials_delays = self.GetMoogHalfTrials()

        self.oculus_trials_total_times = self.GetOculusTotalTimeTrials()
        self.moog_trials_total_times = self.GetMoogTotalTimeTrials()
        
        self.parsed_raw_data = self.GetParsedRawData()

        if self._mode == 'debug':
            print('DataAnalytics:	', 'Number of oculus trials', len(self._time_oculus_trials_delays), ' / ',
                  len(self.oculus_trials_total_times))
            # print('DataAnalytics:	', 'Oculus trials total times', self._oculus_trials_total_times)

            print('DataAnalytics:	', 'Number of moog halftrials', len(self._time_moog_trials_delays), ' / ',
                  len(self.moog_trials_total_times))
            # print('DataAnalytics:	', 'Moog trials total times', self._moog_trials_total_times)
            # print('DataAnalytics:	', 'Oculus trials', self.GetOculusTrials())
            # print('DataAnalytics:	', 'Moog halftrials', self.GetMoogHalfTrials())


    def GetParsedRawData(self):
        listWithTimeStamps = []
        
        for timeStamp in self._data:
            listWithTimeStamps.append(timeStamp['time_stamp'])    # yeah yeah, I acsidentaly switched them, never mind

        return listWithTimeStamps


    def GetOculusTrials(self):
        trials = [[]]
        trials_index = 0

        # starts from 1 to have excess to previous item (zero)
        for i in range(self._number_of_pairs):
            # treat only to oculus points
            if not (self._data[i]['custom_value'] in self._config['oculus_markers']):
                continue

            
            self._oculus_pairs.append(self._data[i])

            if len(self._oculus_pairs) < 2:
                continue

            try:
                delay = (self._oculus_pairs[-1]['time_stamp'] - self._oculus_pairs[-2]['time_stamp']) / self._cpu_freq
            except:
                # print(self._data[i])
                delay = -1

            # throw away obviously not trial (happens in first trial with big delay)
            if delay > self._config['oculus_divergent_value']:
                trials_index += 1
                trials.append([])
                # todo here add moog and oculus separate trials
                # last point, not include
                # trials[trials_index].append(delay)
                continue

            trials[trials_index].append(delay)

        return trials

    def GetMoogHalfTrials(self):
        half_trials = [[]]
        half_trials_index = 0

        # starts from 1 to have excess to previous item (zero)
        for i in range(self._number_of_pairs):
            # treat only to moog points
            if not (self._data[i]['custom_value'] in self._config['moog_markers']):
                continue

            self._moog_pairs.append(self._data[i])

            if len(self._moog_pairs) < 2:
                continue

            try:
                delay = (self._moog_pairs[-1]['time_stamp'] - self._moog_pairs[-2]['time_stamp']) / self._cpu_freq
            except:
                print(self._data[i])
                delay = -1

            # throw away obviously not trial (happens in first trial with big delay)
            if delay > self._config['moog_divergent_value']:
                half_trials_index += 1
                half_trials.append([])
                # half_trials[half_trials_index].append(delay)
                continue

            #if delay <

            half_trials[half_trials_index].append(delay)

        return half_trials

    def GetMoogTotalTimeTrials(self):
        total_times = []

        for moog_trial_delays in self._time_moog_trials_delays:
            total_times.append(sum(moog_trial_delays))

        return total_times

    def GetOculusTotalTimeTrials(self):
        total_times = []

        for oculus_trial_delays in self._time_oculus_trials_delays:
            total_time = sum(oculus_trial_delays)
            total_times.append(total_time)

            #if total_time < 900 or total_time > 1100:
            #    self._divergent_oculus_trials.append(oculus_trial_delays)

        return total_times
