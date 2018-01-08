import pandas as pd
import pickle

tables = {}

# tables keeps track of each sheet in the excel doc
# turns each sheet into a separate dict based on the name of the sheet
lookup_table = pd.ExcelFile(sys.argv[1])
for name in lookup_table.sheet_names:
	tables[name] = lookup_table.parse(name)
	headers = list(tables[name])
	label = headers[1]
	tables[name] = tables[name].set_index(label).T.to_dict('list')

pickle_out = open(sys.argv[2], 'wb')
pickle.dump(tables, pickle_out)
pickle_out.close()