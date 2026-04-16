import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

def plot_tsne_clusters(tsne_emb, labels, output_path):
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x=tsne_emb[:, 0], y=tsne_emb[:, 1], hue=labels, palette='tab10', legend='full')
    plt.title('t-SNE Embeddings with DBSCAN Clusters')
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()

def plot_phase_distribution(phases, output_path):
    plt.figure(figsize=(8, 6))
    sns.countplot(x=phases, order=['A', 'B', 'C', 'Unknown'])
    plt.title('Predicted Phase Distribution')
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()