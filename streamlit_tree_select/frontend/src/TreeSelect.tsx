import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"
import CheckboxTree from 'react-checkbox-tree';


class TreeSelect extends StreamlitComponentBase {
  public state = {
    checked: [],
    expanded: [],
    checked_changed: false,
    expanded_changed: false,
  };


  public render = (): ReactNode => {

    const nodes = this.props.args['nodes']
    const checkModel = this.props.args['check_model']
    const checked = this.props.args['checked']
    const direction = this.props.args['direction']
    const disabled = this.props.args['disabled']
    const expandDisabled = this.props.args['expand_disabled']
    const expandOnClick = this.props.args['expand_on_click']
    const expanded = this.props.args['expanded']
    const noCascade = this.props.args['no_cascade']
    const onlyLeafCheckboxes = this.props.args['only_leaf_checkboxes']
    const showExpandAll = this.props.args['show_expand_all']

    if (!this.state.checked_changed) {
      this.state.checked = checked;
    };

    if (!this.state.expanded_changed){
      this.state.expanded = expanded;
    }

    return (<CheckboxTree
      icons={{
        check: <span className="rct-icon rct-icon-check" />,
        uncheck: <span className="rct-icon rct-icon-uncheck" />,
        halfCheck: <span className="rct-icon rct-icon-half-check" />,
        expandClose: <span className="rct-icon rct-icon-expand-close" />,
        expandOpen: <span className="rct-icon rct-icon-expand-open" />,
        expandAll: <span className="rct-icon rct-icon-expand-all" />,
        collapseAll: <span className="rct-icon rct-icon-collapse-all" />,
        parentClose: <span className="rct-icon rct-icon-parent-close" />,
        parentOpen: <span className="rct-icon rct-icon-parent-open" />,
        leaf: <span className="rct-icon rct-icon-leaf" />,
      }}
      nodes={nodes}
      checkModel={checkModel}
      direction={direction}
      disabled={disabled}
      expandDisabled={expandDisabled}
      expandOnClick={expandOnClick}
      noCascade={noCascade}
      onlyLeafCheckboxes={onlyLeafCheckboxes}
      showExpandAll={showExpandAll}
      checked={this.state.checked}
      expanded={this.state.expanded}
      onCheck={(checked) => { this.setState({ checked }); Streamlit.setComponentValue({'checked': checked, 'expanded': this.state.expanded}); this.state.checked_changed = true; }}
      onExpand={(expanded) => {this.setState({ expanded }); Streamlit.setComponentValue({ 'checked': this.state.checked, 'expanded': expanded}); this.state.expanded_changed = true;}}
    />)
  }


}


// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(TreeSelect)
