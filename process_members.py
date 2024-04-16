import pandas as pd
import csv

institution = "Central_South_University"
substring = ["Metallurgy and Environment", "Metallurgical and Environment"]
csv_files = f"institution_members_{institution}.csv"
df = pd.read_csv(csv_files)
print(df.head(5))

for col in df.columns:
    print(col)

df.drop(df.columns[[2]], axis=1, inplace=True)
print(df.head(5))

for col in df.columns:
    print(col)

department_list = sorted(df["department"].unique().astype(str))
department_list = pd.DataFrame(department_list)
print(department_list.head(5))

department_list.to_csv(f"institution_department_{institution}.csv", index=False, encoding='UTF-8')

targeted_department = df[df["department"].str.contains("|".join(substring), case=False, na=False)]

print(targeted_department.head(5))
targeted_department.to_csv(f"institution_targeted-department_{institution}.csv", index=False, encoding='UTF-8', sep=" ")
# with open(f"institution_department_{institution}.csv", 'w', encoding='UTF-8') as csvfile:
# 	csvwriter = csv.writer(csvfile)
# 	# csvwriter.writerows(department_list)
#     for department in range(len(department_list)):
#         csvwriter.writerow(department)
