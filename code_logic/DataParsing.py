import re	# regular expressions


class DataParsing:
	def __init__(self, file_path, mode):
		self._mode = mode
		self._rawData = self.GetRawData(file_path);

		self.parsedData = self.ParseData(self._rawData)
		self.number_of_pairs
		self.number_of_corrupted_pairs


		if (self._mode == 'debug'):
			print('DataParsing:	', 'Number of corrupted pairs: ', self.number_of_corrupted_pairs, ' / ', self.number_of_pairs)
			#print('DataParsing:	', 'self.parsedData: ', self.parsedData)


	def GetRawData(self, file_path):
		with open(file_path) as file:
			# [0]   - only one long line
			# ';'   - custom separator of pairs
			# [:-1] - last line is empty in txt files
			try:
				return file.readlines()[0].split(';')[:-1]
			except:
				print("File seems to be empty")
				return


	def ParseData(self, data):
		self.number_of_pairs = len(data)	# number of pairs
		self.number_of_corrupted_pairs = 0
		parsed_data = []

		for index in range(self.number_of_pairs):
			try:
				time_stamp, custom_value = data[index].split(',')
			except:
				self.number_of_corrupted_pairs += 1
				continue
			
			parsed_data.append({
				'time_stamp':	self.ExtractFloat(time_stamp),
				'custom_value':	self.ExtractFloat(custom_value)
			})

			if parsed_data[-1]['time_stamp'] == None:
				print(index, data[index], ' : ', data[index-1])
			
		return parsed_data


	def ExtractFloat(self, str):
		# find float number in string (from left to right (I guess))

		match = re.search(r'(\d+\.\d+|\d+)', str)
		return float(match.group()) if match else None