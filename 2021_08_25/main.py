import pandas as pd
def answer_one():
    nobel_data = pd.read_csv('nobel.csv')
    return nobel_data.head()
answer_one()


def answer_two():
    gender_data = nobel_data['sex'].value_counts()
    birth_data = nobel_data['birth_country'].value_counts().head()
    return gender_data, birth_data
answer_two()

