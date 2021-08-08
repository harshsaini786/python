import pandas as pd
import glob
path = './sample json/*.json'
files = glob.glob(path)
for file in files:
    f = open(file, 'r')
    jsonData = pd.read_json(f)
    jsonData.to_csv(f.name+".csv")
    f.close()
