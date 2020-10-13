import pandas as pd

data = pd.read_csv("lines.csv")
dct = {
    "name":data['1'].apply(lambda x: f'{x}'.lower()),
    "accept":data['2'].apply(lambda x: float(x.split('%')[0])),
    "level":data['3']
}
# newdata = pd.DataFrame({"name":data['1'],"accept":data['2'].apply(lambda x: [1, 2], axis=1),"level":data['3']})
data =  pd.DataFrame(dct)
# for x in newdata:
#     print(x["name"])
#     print(type(x["name"]))
#     x["name"] = x['name'].loewer()
#     x["accept"] = float(x['accept'])
newdata = data.sort_values(by=['accept'],ascending=False)
print(newdata.loc[0,['name']])
test = f"https://leetcode.com/problems/{ '-'.join(newdata.loc[0,['name']].values[0].split())}/"

print(newdata)
newdata.to_csv("./newdata")
print(test)