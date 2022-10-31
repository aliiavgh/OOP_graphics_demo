#Демо-версия проекта 1.0

import warnings
from xml.etree.ElementTree import PI 
import numpy as np
import pandas as pd 

warnings.filterwarnings('ignore')

import seaborn as sns
sns.set()

import matplotlib 
import matplotlib.pyplot as plt 
import matplotlib.ticker 

import plotly
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot, plot
from IPython.display import display, IFrame

init_notebook_mode(connected=True)

def plotly_depict_figure_as_iframe(fig, title="", width=800, height=500,
  plot_path='../../_static/plotly_htmls/'):

  fig_path_path = f"{plot_path}/{title}.html"
  plot(fig, filename=fig_path_path, show_link=False, auto_open=False);
  display(IFrame(fig_path_path, width=width, height=height))


BISHKEK = pd.read_csv('/home/hello/Documents/coding/ML/demo_ver.py/dataset1/data - Bishkek2.csv')
NARYN = pd.read_csv('/home/hello/Documents/coding/ML/demo_ver.py/dataset1/data - Naryn2.csv')
BATKEN = pd.read_csv('/home/hello/Documents/coding/ML/demo_ver.py/dataset1/data - Batken2.csv')
CHUY = pd.read_csv('/home/hello/Documents/coding/ML/demo_ver.py/dataset1/data - Chuy2.csv')
IK = pd.read_csv('/home/hello/Documents/coding/ML/demo_ver.py/dataset1/data - Issyk-Kul2.csv')
JA = pd.read_csv('/home/hello/Documents/coding/ML/demo_ver.py/dataset1/data - Jalal-Abad2.csv')
OSH = pd.read_csv('/home/hello/Documents/coding/ML/demo_ver.py/dataset1/data - Osh2.csv')
CITY_OSH = pd.read_csv('/home/hello/Documents/coding/ML/demo_ver.py/dataset1/data - cityOSH1.csv')
TALAS = pd.read_csv('/home/hello/Documents/coding/ML/demo_ver.py/dataset1/data - Talas1.csv')
KR = pd.read_csv('/home/hello/Documents/coding/ML/demo_ver.py/dataset1/data - Kyrgyzstan3.csv')


class DataMixin:
    def __init__(self, region, year): 
        self.region = eval(region)
        self.name_region = region.title()
        self.year = year


class StatisticsMen(DataMixin): 
    def graph(self): 
        return self.region[[x for x in self.region.columns if '[0]' in x]  + ["Наименование показателей"]].groupby("Наименование показателей").sum().plot()


class StatisticsWomen(DataMixin):
    def graph(self): 
        return self.region[[x for x in self.region.columns if '[1]' in x]  + ["Наименование показателей"]].groupby("Наименование показателей").sum().plot()


class Gender(DataMixin): 
    def gender_per(self): 
        identified = self.region.loc[31, 'total']
        men = round((self.region.loc[31, ' мужчины']/identified)*100)
        women = round((self.region.loc[31, 'женщины']/identified)*100)
        pie_ = self.region[[' мужчины'] + ['женщины']].loc[self.year-1990]
        print(f'В {self.name_region.title()} заболевших мужчин/женщин: {men}%/{women}%')
        return pie_.plot.pie(autopct='%1f', subplots=True, figsize=(15, 15))


class Registered(DataMixin): 
    def in_hospital(self): 
        registered = self.region.loc[(self.year-1990), 'Состоят на учете в леч.уч.']
        identified = self.region.loc[(self.year-1990), 'total']
        pie_ = self.region[['total'] + ['Состоят на учете в леч.уч.']].loc[self.year-1990]
        print(f'В {self.name_region}: {round((identified/registered)*100)}% заболевших были выявлены в {self.year} году')
        return pie_.plot.pie(autopct='%1f', subplots=True, figsize=(15, 15))


class Diseases(DataMixin): 
    def percent_men(self): 
        data = self.region.loc[(self.year-1990), '[0]Губы, полости рта и глотки':'[0]Прочих органов']
        return data.plot.pie(subplots=True, figsize=(15, 15))
    def percent_women(self): 
        data = self.region.loc[(self.year-1990), '[1]Губы, полости рта и глотки':'[1]Прочих органов']
        return data.plot.pie(autopct='%1f', subplots=True, figsize=(15, 15))


plt.show() 