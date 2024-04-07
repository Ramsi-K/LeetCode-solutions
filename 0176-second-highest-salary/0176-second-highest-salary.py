import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    max_salary = employee.salary.max()
    return pd.DataFrame([[employee.loc[employee.salary < max_salary, 'salary'].max()]], columns = ['SecondHighestSalary'])


    # second_highest_salary = employee.salary.sort_values(ascending=False).drop_duplicates().iloc[1] if len(employee.salary.unique()) > 1 else None
    # return pd.DataFrame({"SecondHighestSalary": [second_highest_salary]})