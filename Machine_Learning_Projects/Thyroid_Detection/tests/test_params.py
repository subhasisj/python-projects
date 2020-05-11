class TobeSerialized:
    def __init__(self):
        self.params = {

        'XGBClassifier':{

                        'max_depth':[3,5,7,9,12,15,25],
                        'n_estimators': [10, 50, 100, 200],
                        'learning_rate': [0.5, 0.1, 0.01, 0.001],
                        'min_child_weight':[1,3,5,7]
                        },

        'RandomForestClassifier':{
                        "n_estimators": [10, 50, 100, 130],
                        "criterion": ['gini', 'entropy'],
                        "max_depth": range(2, 4, 1),
                        "max_features": ['auto', 'log2']
                        },

        'KNeighborsClassifier':{
                        "algorithm" : ['ball_tree', 'kd_tree', 'brute'],
                        "leaf_size" : [10,17,24,28,30,35],
                        "n_neighbors":[4,5,8,10,11],
                        "p":[1,2]
                    }
                }


test1 = TobeSerialized()
test2 = TobeSerialized()
# print('before')
before = test1.params
# print(test.params)

import jsonpickle
serialized1 = jsonpickle.encode(test1)
serialized2 = jsonpickle.encode(test2)

after = jsonpickle.decode(serialized1).params
assert before == after

keep_in_dict = {'model' :serialized1,
                'score':20 }
keep_in_dict2 = {'model' :serialized2,#jsonpickle.decode(serialized2),
                'score':40 }
# print('after')
# print(keep_in_dict['model'].params)

import pandas as pd
df1 = pd.DataFrame(keep_in_dict,index=[0])
df2 = pd.DataFrame(keep_in_dict2,index=[0])
df3 = pd.concat([df1,df2])

df3 = df3.sort_values('score',ascending=False).reset_index(drop=True)
print(df3)
print(df3.loc[1])
print(jsonpickle.decode(df3.loc[1]['model']).params)



