import seaborn as sns
import matplotlib.pyplot as plt

def line_plot(out):
    plt.figure(figsize=(6, 4))
    sns.lineplot(x=out["x_axis"], y=out["y_axis"])
    plt.xticks(out["x_axis"])
    plt.xlabel(out['x_axis_name'])
    plt.ylabel(out['y_axis_name'])
    plt.title(out['graph_name'])
    return plt

def bar_plot(out):
    plt.figure(figsize=(6, 4))
    sns.barplot(x=out['x_axis'], y=out['y_axis'])
    plt.xlabel(out['x_axis_name'])
    plt.ylabel(out['y_axis_name'])
    plt.title(out['graph_name'])
    plt.xticks(rotation=45)
    return plt