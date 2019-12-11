import plotly.graph_objects as go
import numpy as np
import pandas as pd
from collections import OrderedDict

table_books = 'dataset/Books.csv'
dfBooks = pd.read_csv(table_books)
np_dfBooks = np.array(dfBooks)

count = 0
parentList = {}
for x in np_dfBooks:
    if count != 0 and x[1] != 'Books' and x[1]!=np_dfBooks[np_dfBooks[:, 0] == x[4],1]:
        parentList.update({x[1]: np_dfBooks[np_dfBooks[:, 0] == x[4], 1]})
    else:
        parentList.update({x[1]: ''})
        print(count)
        print(x[1])
    if count == 3827:
        print(x[1])
        print(np_dfBooks[np_dfBooks[:, 0] == x[4], 1])
        break
    count = count + 1
print(parentList.keys())
print(parentList.values())

fig = go.Figure()
fig.add_trace(go.Sunburst(
    labels=list(parentList.keys()),
    parents=list(parentList.values()),
    domain=dict(column=0)
))
fig.update_layout(
    margin=dict(t=0, l=0, r=0, b=0)
)
fig.show()

#treemap
fig1 = go.Figure(go.Treemap(
    labels=list(parentList.keys()),
    parents=list(parentList.values()),
))

fig1.show()

