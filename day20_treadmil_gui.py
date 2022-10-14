import tkinter as ttk
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('treadmil-users.csv')


app = ttk.Tk()
app.geometry('600x300')
app.title('Treadmil Users Analysis')

# Radio Button
graphs = ttk.Variable(app)
values = {
    'Pair Plot': "sns.pairplot(data = data)",
    'Joint Plot': "sns.jointplot(data = data, x='{col1}', y='{col2}')",
    'Bar Plot': "sns.barplot(data = data, x='{col1}', y='{col2}')"
    
}
graphs.set(values['Pair Plot'])
y = 10
for key, value in values.items():
    ttk.Radiobutton(app, text = key, variable=graphs, value = value).place(x=10, y = y)
    y += 20

    ## Option Menu 1
    col1= ttk.Variable(app)
    values = ['Select']+list(data.columns)
    col1.set(values[0])
    ttk.Label(app,text = 'Column1').place(x=150,y=10)
    ttk.OptionMenu(app, *values).place(x= 150, y=40)

    ## Option Menu 2
    col2= ttk.Variable(app)
    col2.set(values[0])
    ttk.Label(app,text = 'Column2').place(x=150,y=80)
    ttk.OptionMenu(app, *values).place(x= 150, y=110)

## Option Menu 3
    col3= ttk.Variable(app)
    col3.set(values[0])
    ttk.Label(app,text = 'Column3').place(x=150,y=150)
    ttk.OptionMenu(app, *values).place(x= 150, y=180)


def show():
    print(graphs.get())
    print(col1.get())
    print(col2.get())
    print(col3.get())

ttk.Button(app, text='Show', command = show).place(x=400,y=10)    


app.mainloop()