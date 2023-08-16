from code.DataParsing import DataParsing as DataParsing
from code.DataAnalytics import DataAnalytics as Analytics


MocuDataParsing = DataParsing('input_raw_data.txt', 'debug')
MocuAnalytics   = Analytics(MocuDataParsing, 'debug')

#MocuDataParsing = DataParsing('input_raw_data.txt', 'release')
#MocuAnalytics   = Analytics(MocuDataParsing, 'release')
#MocuAnalitics.ShowLastPairs(100);