import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

data1 = {
  "x": ["10", "100", "1000"],
  "y": ["7500", "50000", "500000"],
  "line": {"shape": "spline"},
  "marker": {"size": 8},
  "name": "Client-Server",
  "opacity": 1,
  "type": "scatter",
  "uid": "0f64ce"
}
data2 = {
  "x": ["10", "100", "1000"],
  "y": ["7500", "25000", "45455"],
  "line": {"shape": "spline"},
  "marker": {"size": 8},
  "name": "P2P - u = 300 Kbps",
  "type": "scatter",
  "uid": "f4418e"
}
data3 = {
  "x": ["10", "100", "1000"],
  "y": ["7500", "15000", "20548"],
  "line": {"shape": "spline"},
  "marker": {"size": 8},
  "name": "P2P - u = 700 Kbps",
  "type": "scatter",
  "uid": "6a2582"
}
data4 = {
  "x": ["10", "100", "1000"],
  "y": ["7500", "7500", "7500"],
  "line": {"shape": "spline"},
  "marker": {"size": 8},
  "name": "P2P - u = 2 Mbps",
  "type": "scatter",
  "uid": "b8625b"
}
layout = {
  "autosize": False,
  "bargap": 0.2,
  "bargroupgap": 0,
  "barmode": "group",
  "boxgap": 0.3,
  "boxgroupgap": 0.3,
  "boxmode": "overlay",
  "dragmode": "zoom",
  "font": {
    "color": "#444",
    "family": "\"Open sans\", verdana, arial, sans-serif",
    "size": 12
  },
  "height": 583,
  "hidesources": False,
  "hovermode": "x",
  "legend": {
    "x": 1.02,
    "y": 1,
    "bgcolor": "#fff",
    "bordercolor": "#444",
    "borderwidth": 0,
    "font": {
      "color": "",
      "family": "",
      "size": 0
    },
    "traceorder": "normal",
    "xanchor": "left",
    "yanchor": "top"
  },
  "margin": {
    "r": 80,
    "t": 100,
    "autoexpand": True,
    "b": 80,
    "l": 80,
    "pad": 0
  },
  "paper_bgcolor": "#fff",
  "plot_bgcolor": "#fff",
  "separators": ".,",
  "showlegend": True,
  "title": "Distribution of a 15Gbit file to N peers",
  "titlefont": {
    "color": "",
    "family": "",
    "size": 0
  },
  "width": 800,
  "xaxis": {
    "anchor": "y",
    "autorange": True,
    "autotick": False,
    "domain": [0, 1],
    "dtick": 1000,
    "exponentformat": "B",
    "gridcolor": "#eee",
    "gridwidth": 1,
    "linecolor": "#444",
    "linewidth": 1,
    "mirror": False,
    "nticks": 0,
    "overlaying": False,
    "position": 0,
    "range": [-45, 1055],
    "rangemode": "normal",
    "showexponent": "all",
    "showgrid": False,
    "showline": False,
    "showticklabels": True,
    "tick0": 0,
    "tickangle": "auto",
    "tickcolor": "#444",
    "tickfont": {
      "color": "",
      "family": "",
      "size": 0
    },
    "ticklen": 5,
    "ticks": "",
    "tickwidth": 1,
    "title": "N",
    "titlefont": {
      "color": "",
      "family": "",
      "size": 0
    },
    "type": "linear",
    "zeroline": True,
    "zerolinecolor": "#444",
    "zerolinewidth": 1
  },
  "yaxis": {
    "anchor": "x",
    "autorange": True,
    "autotick": True,
    "domain": [0, 1],
    "dtick": 100000,
    "exponentformat": "B",
    "gridcolor": "#eee",
    "gridwidth": 1,
    "linecolor": "#444",
    "linewidth": 1,
    "mirror": False,
    "nticks": 0,
    "overlaying": False,
    "position": 0,
    "range": [-19861.111111111113, 527361.1111111111],
    "rangemode": "normal",
    "showexponent": "all",
    "showgrid": True,
    "showline": False,
    "showticklabels": True,
    "tick0": 0,
    "tickangle": "auto",
    "tickcolor": "#444",
    "tickfont": {
      "color": "",
      "family": "",
      "size": 0
    },
    "ticklen": 5,
    "ticks": "",
    "tickwidth": 1,
    "title": "Minimum Distribution Time (seconds)",
    "titlefont": {
      "color": "",
      "family": "",
      "size": 0
    },
    "type": "linear",
    "zeroline": True,
    "zerolinecolor": "#444",
    "zerolinewidth": 1
  }
}

data = [data1, data2, data3, data4]
layout = go.Layout(title="CLIENT SERVER VS PEER TO PEER ARCHITECTURE",
xaxis=dict(title='NUMBER OF PEERS (N)'),
yaxis=dict(title='Minimum Distribution Time (seconds)'),
hovermode='closest'
)
fig=go.Figure(data=data,layout=layout)
pyo.plot(fig)
