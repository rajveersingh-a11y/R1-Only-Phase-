from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from app.config import settings

def apply_pca(scaled_data):
    pca = PCA(n_components=settings.PCA_COMPONENTS)
    pca_features = pca.fit_transform(scaled_data)
    explained_variance = sum(pca.explained_variance_ratio_)
    return pca_features, explained_variance

def apply_tsne(pca_features):
    tsne = TSNE(n_components=2, perplexity=settings.TSNE_PERPLEXITY, 
                max_iter=settings.TSNE_ITER, random_state=42)
    tsne_embeddings = tsne.fit_transform(pca_features)
    return tsne_embeddings