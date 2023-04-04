import pandas as pd
import datetime

class NJCleaner:
    def __init__(self, path:str):
        self.data=pd.read_csv(path)

    def order_by_scheduled_time(self):
        self.data = self.data.sort_values('scheduled_time', ascending=True)
        return self.data

    def drop_columns_and_nan(self):
        self.data=self.data.drop(columns=['from', 'to'])
        self.data=self.data.drop())
        return self.data

    def convert_date_to_day(self):

        self.data['day']=[x.con for  x  in self.data['date']]
        return self.data
train=NJCleaner("HAZI/HAZI06/2018_03.csv")
train.order_by_scheduled_time()
train.drop_columns_and_nan()
train.convert_date_to_day()
print(train.data)
print("a")
print("a")
print("a")
print("a")
