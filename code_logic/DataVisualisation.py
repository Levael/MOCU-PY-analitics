import matplotlib.pyplot as chart

#chart.style.use('Solarize_Light2')
#chart.rcParams["figure.facecolor"] = "dimgray"
##chart.rcParams["axes.facecolor"] = "whitesmoke"


class DataVisualisation:
    def __init__(self, analysis_object, mode='release'):
        self._oculus_trials_total_times = analysis_object.oculus_trials_total_times
        self._moog_trials_total_times = analysis_object.moog_trials_total_times
        self._raw_data = analysis_object.parsed_raw_data



    def DrawMoogAndOculusTotalTrialsTimes(self):
        chart.figure('Oculus & Moog trials total times')

        # oculus chart
        chart.subplot(2, 1, 1)
        chart.title('Oculus')
        #chart.xlabel('frames')
        #chart.ylabel(y_axis_name)
        x_axis = range(1, len(self._oculus_trials_total_times)+1)
        y_axis = self._oculus_trials_total_times
        chart.scatter(x_axis, y_axis, s=1)

        # moog chart
        chart.subplot(2, 1, 2)
        chart.title('Moog')
        # chart.xlabel('frames')
        # chart.ylabel(y_axis_name)
        x_axis = range(1, len(self._moog_trials_total_times) + 1)
        y_axis = self._moog_trials_total_times
        chart.scatter(x_axis, y_axis, s=1)

        chart.subplots_adjust(left=0.035, right=0.98, top=0.96, bottom=0.03)
        chart.show()
        

    def DrawRawData(self):
        chart.figure('Time Manager Test. Number of points: ' + str(len(self._raw_data["time_stamps"])))
        
        x_axis = self._raw_data["time_stamps"]
        y_axis = self._raw_data["custom_values"]
        
        #print(f"{min(x_axis)} - {max(x_axis)}; {min(y_axis)} - {max(y_axis)}")
        #print(x_axis[-5:])

        #print(x_axis)
        #print(y_axis)

        #chart.xlim([min(x_axis), max(x_axis)])
        #chart.ylim([min(y_axis), max(y_axis)])

        colors = []
        color_border = 3    # max Y value = red

        for y_value in y_axis:
            if y_value > color_border:          color = (1, 0, 0)   # red
            elif y_value > 0 and y_value < 0.5: color = (0, 0.6, 0)   # green
            
            else:
                red_channel = y_value / color_border
                blue_channel = 1 - red_channel
                color = (red_channel, 0, blue_channel)  # red / blue gradient
            colors.append(color)
        
        #colors = ['red' if value < 0.5 else 'orange' if value >= 0.5 and value < 0.93 else "green" if value >= 0.93 and value <= 1.07 else "magenta" if value > 1.07 else "black" for value in y_axis]
        chart.scatter(x_axis, y_axis, s=1, c=colors)

        chart.subplots_adjust(left=0.035, right=0.98, top=0.96, bottom=0.03)
        chart.show()


    def MakePointedChart(self, data, number_of_charts = 1, index_in_figure = 1, chart_name = "", y_axis_name = ""):
        chart.subplot(1, number_of_charts, index_in_figure)
        chart.title('Total time: ' + str(round(sum(data), 2)) + 'ms')
        chart.xlabel('frames')
        chart.ylabel(y_axis_name)

        x_axis = range(1, len(data)+1)
        y_axis = data

        print(data)

        chart.scatter(x_axis, y_axis, s=1)
        

    def DrawChartAsAxes (self, data):
        chart.figure('')
        self.MakeChartAsAxes(data)
        #chart.title('Test')
        chart.xlabel('number of trials')
        chart.ylabel('trial total time')
        chart.show()


    def DrawCharts (self, data):
        list_of_trials = data

        chart.figure('Charts of ' + str(len(list_of_trials)) + ' last trials')

        for sub_chart in list_of_trials:
            self.MakeChartAsAxes(
                sub_chart,
                len(list_of_trials),
                list_of_trials.index(sub_chart)+1,
                '',
                'delay between frames (ms)')

        chart.tight_layout()
        chart.show()