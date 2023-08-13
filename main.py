from DataParsing import DataParsing as DataParsing
from DataAnalitics import DataAnalitics as Analitics


MocuDataParsing = DataParsing('data_for_debug.txt', 'debug')
MocuAnalitics   = Analitics(MocuDataParsing, 'debug')

#MocuDataParsing = DataParsing('input_raw_data.txt', 'release')
#MocuAnalitics   = Analitics(MocuDataParsing, 'release')
#MocuAnalitics.ShowLastPairs(100);


### NOTES:
#   there is a problem with input file, data is corrupted.
#   also here not every wrong data is sorted and notised