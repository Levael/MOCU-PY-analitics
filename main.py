from code.DataParsing import DataParsing as DataParsing
from code.DataAnalytics import DataAnalytics as Analytics
from code.DataVisualisation import DataVisualisation as Visualisation

MocuDataParsing = DataParsing('input_raw_data.txt', 'debug')
MocuAnalytics = Analytics(MocuDataParsing, 'debug')
MocuVisualisation = Visualisation(MocuAnalytics, 'debug')

MocuVisualisation.DrawMoogAndOculusTotalTrialsTimes()

# MocuDataParsing = DataParsing('input_raw_data.txt', 'release')
# MocuAnalytics   = Analytics(MocuDataParsing, 'release')
# MocuAnalytics.ShowLastPairs(100);
