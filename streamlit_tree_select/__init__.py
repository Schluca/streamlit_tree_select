from __future__ import annotations

import os
from typing import Any
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
_RELEASE = True

if not _RELEASE:
    _tree_select = components.declare_component(
        # We give the component a simple, descriptive name ("streamlit_tree_select"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "streamlit_tree_select",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _tree_select = components.declare_component("streamlit_tree_select", path=build_dir)


# Create a wrapper function for the component.
def tree_select(nodes: list[dict[str, str, None | list[Any]]],
                check_model: str = "all",
                checked: None | list = None,
                direction: str = 'ltr',
                disabled: bool = False,
                expand_disabled: bool = False,
                expand_on_click: bool = False,
                expanded: None | list = None,
                no_cascade: bool = False,
                only_leaf_checkboxes: bool = False,
                show_expand_all: bool = False,
                key: None | str = None):
    """Create a new instance of "streamlit_tree_select".

    Parameters
    ----------
    nodes: list[dict[str, str, list[Any]]]
        A list containing tree nodes and their children.
        A need needs to include a label and a value. Furthermore, a list of children can be added.
        Further possible parameters:
            className (A class Name to add to the node, default None)
            disabled (Whether the node should be disabled, default False)
            showCheckbox (Whether the node should show a checkbox, default True)
            title (A custom title attribute for th node, default None)

    check_model: str, default 'all'
        Specifies which selected nodes should be returned. Possible inputs: "all", "leaf".

    checked: None | list, default None
        A list of selected nodes.

    direction: str, default 'ltr'
        Specify the direction of the component. Left-to-right ('ltr') or right-to-left ('rtl').

    disabled: bool, default False
        If True, the component will be disabled and cannot be used.

    expand_disabled: bool, default False
        If True, nodes cannot be expanded.

    expand_on_click: bool, default False
        If True, nodes will be expanded by clicking on the labels.

    expanded: None | list, default None
        A list of expanded node values.

    no_cascade: bool, default False
        If True, toggling a parent node will not cascade its check state to its children.

    only_leaf_checkboxes: bool, default False
        If True, checkboxes will only be shown for leaf nodes.

    show_expand_all: bool, default False
        If True buttons for expanding and collapsing all parent nodes will appear in the three.
    key

    Returns
    -------
    dict
        Returns a dictionary containing checked values (list), expanded nodes (list) and if any changes occurred (bool).
    """

    if checked is None:
        checked = []
    if expanded is None:
        expanded = []

    tree_select_value = _tree_select(nodes=nodes,
                                     check_model=check_model,
                                     checked=checked,
                                     direction=direction,
                                     disabled=disabled,
                                     expand_disabled=expand_disabled,
                                     expand_on_click=expand_on_click,
                                     expanded=expanded,
                                     no_cascade=no_cascade,
                                     only_leaf_checkboxes=only_leaf_checkboxes,
                                     show_expand_all=show_expand_all,
                                     key=key,
                                     default=[])

    return tree_select_value


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run streamlit_tree_select/__init__.py`
if not _RELEASE:
    import streamlit as st

    # Create an instance of our component with a constant `name` arg, and
    # print its output value.
    test_nodes = [{'value': '0',
                   'label': '0'},
                  {
                      'value': '1',
                      'label': '1',
                      'children': [
                          {
                              'value': '2',
                              'label': '2',
                              'children': [
                                  {'value': '3', 'label': '3'},
                                  {'value': '4', 'label': '4'},
                              ],
                          },
                          {'value': '5', 'label': '5'},
                      ],
                  }]

    tree_return = tree_select(test_nodes, check_model='all', checked=['1', '3'])
    st.write(tree_return)
