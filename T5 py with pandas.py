import pandas as pd

#df data frame holds data of csv file

df = pd.read_csv("students.csv")
print(df)  #display csv data

high_scores = df[df["Marks"] > 80]

print(high_scores)

print("Average Marks:", df["Marks"].mean())     # average

print("Max Marks:", df["Marks"].max())          # highest

print("Min Marks:", df["Marks"].min())          # lowest

