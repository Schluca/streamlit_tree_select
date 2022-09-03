# streamlit_tree_select
A simple and elegant checkbox tree for Streamlit. Build on [react-checkbox-tree](https://github.com/Socvest/streamlit-on-Hover-tabs).

<p align="center">
  <img src="./img/example.gif" alt="animated" />
</p>

### Installation

streamlit-tree-select is distributed via. [PyPi](https://pypi.org/project/streamlit-tree-select/):

```
pip install streamlit-tree-select
```



### Example
Using streamlit-tree-select is as simple as importing tree_select and passing a list of nodes.
``` python
import streamlit as st
from streamlit_tree_select import tree_select

st.title("🐙 Streamlit-tree-select")
st.subheader("A simple and elegant checkbox tree for Streamlit.")

# Create nodes to display
nodes = [
    {"label": "Folder A", "value": "folder_a"},
    {
        "label": "Folder B",
        "value": "folder_b",
        "children": [
            {"label": "Sub-folder A", "value": "sub_a"},
            {"label": "Sub-folder B", "value": "sub_b"},
            {"label": "Sub-folder C", "value": "sub_c"},
        ],
    },
    {
        "label": "Folder C",
        "value": "folder_c",
        "children": [
            {"label": "Sub-folder D", "value": "sub_d"},
            {
                "label": "Sub-folder E",
                "value": "sub_e",
                "children": [
                    {"label": "Sub-sub-folder A", "value": "sub_sub_a"},
                    {"label": "Sub-sub-folder B", "value": "sub_sub_b"},
                ],
            },
            {"label": "Sub-folder F", "value": "sub_f"},
        ],
    },
]

return_select = tree_select(nodes)
st.write(return_select)

```


