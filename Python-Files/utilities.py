import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

mpl.rc('font', family='serif', serif='Computer Modern Roman')
mpl.rcParams['text.usetex'] = True

PROPS = {
    'boxprops':{'facecolor':'white', 'edgecolor':'black'},
    'medianprops':{'color':'black'},
    'whiskerprops':{'color':'black'},
    'capprops':{'color':'black'}
}

def line_graph(x, y, x_label, y_label, title, save_dir):
    fig, ax = plt.subplots(figsize=(10,6))
    sns.lineplot(x=x, y=y, marker='o', color='black', ax=ax)
    ax.set_xlabel(x_label, fontsize=14)
    ax.set_ylabel(y_label, fontsize=14)
    ax.set_title(title, fontsize=16)
    ax.grid(True)
    fig.tight_layout()
    fig.savefig(save_dir, dpi=300)
    plt.show()

def boxplot(data, feature, save_dir):
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.boxplot(x=feature,
                data=data,
                showfliers=True,
                linewidth=1,
                ax=ax,
                **PROPS)
    ax.set_title(f'Box plot of {feature}', fontsize=16)
    ax.set_xlabel(feature, fontsize=14)
    ax.set_ylabel('Value', fontsize=14)
    fig.tight_layout()
    fig.savefig(save_dir, dpi=300)
    plt.show()

def scatter(data, feature1, feature2):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=feature1,
                    y=feature2,
                    data=data,
                    alpha=0.5,
                    color='black',
                    s=5,
                    ax=ax)
    ax.set_title(f'Scatter plot of {feature1} vs {feature2}', fontsize=16)
    ax.set_xlabel(feature1, fontsize=14)
    ax.set_ylabel(feature2, fontsize=14)
    plt.show()

def histogram(data, feature, save_dir):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data[feature],
                 bins=30,
                 kde=False,
                 color='white',
                 edgecolor='black',
                 linewidth=1,
                 ax=ax)
    ax.set_title(f'Histogram of {feature}', fontsize=16)
    ax.set_xlabel(feature, fontsize=14)
    ax.set_ylabel('Frequency', fontsize=14)
    fig.tight_layout()
    fig.savefig(save_dir, dpi=300)
    plt.show()

def bar(data, feature, save_dir):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x=feature,
                  data=data,
                  color='white',
                  edgecolor='black',
                  linewidth=1,
                  ax=ax)
    ax.set_title(f'Bar chart of {feature}', fontsize=16)
    ax.set_xlabel(feature, fontsize=14)
    ax.set_ylabel('Count', fontsize=14)
    fig.tight_layout()
    fig.savefig(save_dir, dpi=300)
    plt.show()
