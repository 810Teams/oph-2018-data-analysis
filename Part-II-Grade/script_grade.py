"""
Data Generating Script
"""

import numpy, pandas
from random import choice
from math import floor

grades_db = {4: 'A', 3.5: 'B+', 3: 'B', 2.5: 'C+', 2: 'C', 1.5: 'D+', 1: 'D', 0.5: 'F', 0: 'F'}
grades = [4]*5 + [3.5] + [3] + [2] + [1.5] + [1] + [0]*2
titles = ['Name', 'Programming', 'Thai', 'English', 'Mathematics', 'Science', 'SocialStudies', 'Computer']

def main():
    """ Main function """
    # gen_sample()
    # gen_quiz()
    # solve()

def gen_sample():
    """ Generate Sample Dataset """
    df = dict()

    df['Name'] = ['?' for i in range(50)]
    df['Programming'] = ['X' for _ in range(50)]

    for i in titles[2::]:
        df[i] = [choice(grades) for _ in range(50)]

    # Calculation
    for i in range(50):
        df['Programming'][i] = grades_db[floor((df['English'][i] + df['Mathematics'][i]*2 + df['Computer'][i]*2)/5*2)/2]

    df = pandas.DataFrame(df, columns=titles)

    df.to_csv('sample.csv', index=False)

def gen_quiz():
    """ Generate Quiz Dataset """
    df = dict()

    df['Name'] = ['?' for i in range(10)]
    df['Programming'] = ['X' for _ in range(10)]

    for i in titles[2::]:
        df[i] = [choice(grades) for _ in range(10)]

    df = pandas.DataFrame(df, columns=titles)

    df.to_csv('quiz.csv', index=False)

def solve():
    """ Solve for the missing value """
    df = pandas.read_csv('quiz.csv')

    for i in range(10):
        df['Programming'][i] = grades_db[floor((df['English'][i] + df['Mathematics'][i]*2 + df['Computer'][i]*2)/5*2)/2]

    print(df[['Name', 'Programming', 'English', 'Mathematics', 'Computer']])

main()
