from code_logic.DataParsing import DataParsing as DataParsing
from code_logic.DataAnalytics import DataAnalytics as Analytics
from code_logic.DataVisualisation import DataVisualisation as Visualisation

#MocuDataParsing = DataParsing('input_raw_data.txt', 'debug')
#MocuAnalytics = Analytics(MocuDataParsing, 'debug')
#MocuVisualisation = Visualisation(MocuAnalytics, 'debug')

MocuDataParsing = DataParsing("C:\\Users\\Levael\\GitHub\\C#-tests\\C#-tests\\Tests\\Debug_log.txt", 'debug')   # "C:\\Users\\Levael\\GitHub\\MOCU-PY-analytics\\input_raw_data.txt"
MocuAnalytics = Analytics(MocuDataParsing, 'debug')
MocuVisualisation = Visualisation(MocuAnalytics, 'debug')

MocuVisualisation.DrawRawData()











#MocuVisualisation.DrawMoogAndOculusTotalTrialsTimes()
#MocuVisualisation.DrawRawData()

# MocuDataParsing = DataParsing('input_raw_data.txt', 'release')
# MocuAnalytics   = Analytics(MocuDataParsing, 'release')
# MocuAnalytics.ShowLastPairs(100);
