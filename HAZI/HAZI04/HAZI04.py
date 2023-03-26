import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''

def csv_to_df(input:str):
    df_data=pd.read_csv(input)
    return df_data

df_data=csv_to_df('\GitRepos\BEVADAT2022232\BEVADAT2022232\HAZI\HAZI04\StudentsPerformance.csv')

'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''
def capitalize_columns(df_data):
    df_data_capitalized=df_data.copy()
    df_data_capitalized.columns = [col if 'e' in col else col.upper() for col in df_data_capitalized.columns]
    return df_data_capitalized

'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''

def math_passed_count(df_data):
    new_df=df_data.copy()
    math_scores=new_df['math score']
    return sum(score >=50 for score in math_scores)

'''
Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''
def did_pre_course(df_data):
    df_did_pre_course=df_data.copy()
    df_did_pre_course=df_did_pre_course[df_did_pre_course['test preparation course'] != 'none' ]
    return df_did_pre_course

'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''

def average_scores(df_data):
    df_average_scores=df_data.copy()
    return df_average_scores.groupby(['parental level of education'])['math score','reading score','writing score'].mean()

'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''
def add_age(df_data):
    df_data_with_age=df_data.copy()
    np.random.seed(42)
    df_data_with_age['age']= [np.random.randint(18,67) for _ in range(len(df_data_with_age))]
    return df_data_with_age

'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''


def female_top_score(df_data):
    df_female=df_data.copy()
    df_female=df_female[df_female['gender']=='female']
    df_female['sum of points'] = df_female['math score'] + df_female['reading score'] + df_female['writing score']
    best_score_df=df_female.sort_values('sum of points', ascending=False)[:1]
    return (best_score_df['math score'],best_score_df['reading score'],best_score_df['writing score'])

'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''

def add_grade(df_data):
    df_data_with_grade=df_data.copy()
    df_data_with_grade['grade'] = pd.cut(df_data_with_grade[['math score', 'reading score', 'writing score']].sum(axis=1)/300,
                         bins=[0, 0.6, 0.7, 0.8, 0.9, 1],
                         labels=['F', 'D', 'C', 'B', 'A'])
    return df_data_with_grade

'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''

def math_bar_plot(df_data):
    new_df=df_data.copy()
    new_df=new_df.groupby(['gender'])['math score'].mean()
    fig, ax = plt.subplots()
    
    ax.bar(new_df.index, new_df.values)
    ax.set_title('Average Math Score by Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Math Score')

    for bars in ax.containers:
        ax.bar_label(bars)
    return fig

''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''

def writing_hist(df_data):
    new_df=df_data.copy()
    fig, ax = plt.subplots()
    
    ax.hist(new_df['writing score'],100)
    ax.set_title('Distribution of Writing Scores')
    ax.set_xlabel('Writing Score')
    ax.set_ylabel('Number of Students')

''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''

def ethnicity_pie_chart(df_data:pd.DataFrame):
    new_df=df_data.copy()
    numberPerGroup=new_df.groupby(['race/ethnicity'])['gender'].count()
    print(numberPerGroup)
    fig, ax = plt.subplots()
    ax.pie(numberPerGroup.values,labels=numberPerGroup.index,labeldistance=0.8, autopct='%1.1f%%')
    ax.set_title('Proportion of Students by Race/Ethnicity')
    return fig

ethnicity_pie_chart(df_data)
plt.show()