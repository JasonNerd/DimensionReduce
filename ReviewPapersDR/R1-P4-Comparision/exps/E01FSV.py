# feature sapce visualize with PCA
# ECG200, 96 features
import numpy as np
from matplotlib import pyplot as plt
from ArcReader import get_train_data, get_test_data
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from sklearn.decomposition import PCA, KernelPCA, TruncatedSVD, FastICA, NMF
from sklearn.manifold import Isomap, MDS, LocallyLinearEmbedding, SpectralEmbedding, TSNE
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import warnings
warnings.filterwarnings("ignore")  # 忽略所有警告

X_train, y_train = get_train_data()
X_test, y_test = get_test_data()
ss = StandardScaler()
X_test_normed = ss.fit_transform(X_test)
X_train_normed = ss.fit_transform(X_train)
sn, fn = X_train.shape  # 样本数量, 特征数量
print(sn)
print(fn)

def train_score(Method=None, **params):
    ncs, f1sc, tmu = [], [], []
    if Method is None:
        ncs.append(fn)
        sc, mu = svc_sco(X_train_normed, y_train, X_test_normed, y_test)
        f1sc.append(sc)
        tmu.append(mu)
    else:
        mxn = 100
        rfn = mxn if fn>mxn else fn
        print(f"Iter rounds: {rfn}")
        for nc in range(rfn):
            try:
                sc, mu = dr_train(Method, nc+1, **params)
            except Exception as e:
                # print(e)
                pass
            else:
                ncs.append(nc+1)
                f1sc.append(sc)
                tmu.append(mu)
                if nc%10 == 0:
                    print(f"{str(nc+1).zfill(3)}: {f1sc[nc]:.4f}\t{tmu[nc]*1000:.2f} ms")
    print(len(ncs))
    return np.array(ncs), np.array(f1sc), np.array(tmu)

def dr_train(Method, n_component, **params):
    drm = Method(n_components=n_component, **params)
    X_train_drm = drm.fit_transform(X_train_normed)
    X_test_drm = drm.transform(X_test_normed)
    sc, mu = svc_sco(X_train_drm, y_train, X_test_drm, y_test)
    return sc, mu

def svc_sco(X, y, Xt, yt):
    """训练SVC并返回打分"""
    import time
    t1 = time.time()
    svm_clf = SVC(kernel='rbf')
    cross_val_score(svm_clf, X, y, cv=10)
    svm_clf.fit(X, y)
    y_pred = svm_clf.predict(Xt)
    sc = f1_score(y_pred, yt)
    t2 = time.time()
    return sc, t2-t1

def test_func(method=None, **params):
    org = train_score(method, **params)
    f1sc = org[1].max()
    pcn = org[0][org[1].max()==org[1]][0]
    tmu = org[2].mean()
    if method is None:
        print("Original", end='\t')
    else:
        print(f"{method.__name__}", end='\t')
    print(f"time used:{tmu:.4f}(s)\tscore:{f1sc:.4f}\tpc number:{pcn}")

test_func()
test_func(PCA)
# print(dr_train(PCA, 9))
test_func(KernelPCA, kernel='rbf')
test_func(Isomap, n_neighbors=15)
# test_func(MDS)    # transform
# print(dr_train(MDS, 9))
test_func(LocallyLinearEmbedding, n_neighbors=11)
# test_func(SpectralEmbedding, n_neighbors=14)   # transform
test_func(FastICA, whiten='unit-variance', random_state=3)
# print(dr_train(FastICA, 32, whiten='unit-variance', random_state=2))
test_func(TruncatedSVD)
# print(dr_train(LinearDiscriminantAnalysis, 1))
# print(dr_train(TSNE, 2))    # transform

"""
UserWarning: The number of connected components of the neighbors graph is 2 > 1. Completing the graph to fit Isomap might be slow. 
Increase the number of neighbors to avoid this iclssue.
SparseEfficiencyWarning: Changing the sparsity structure of a csr_matrix is expensive. lil_matrix is more efficient.
Original        time used:0.2940(s)     score:0.7416    pc number:10000
PCA     time used:0.0138(s)     score:0.8125    pc number:19
KernelPCA       time used:0.0137(s)     score:0.8119    pc number:50
Isomap  time used:0.0186(s)     score:0.8000    pc number:38
LocallyLinearEmbedding  time used:0.0157(s)     score:0.8190    pc number:41
SpectralEmbedding       time used:0.0156(s)     score:0.6869    pc number:1
MDS     time used:0.0172(s)     score:0.6667    pc number:15
FastICA time used:0.0139(s)     score:0.8478    pc number:94
TruncatedSVD    time used:0.0135(s)     score:0.8125    pc number:15
"""

"""
001: 0.6735     13.53 ms
011: 0.7959     16.43 ms
021: 0.8000     14.34 ms
031: 0.7872     12.64 ms
041: 0.7835     12.88 ms
051: 0.7500     14.02 ms
061: 0.7755     14.81 ms
071: 0.7755     12.82 ms
081: 0.7755     13.81 ms
091: 0.7500     15.85 ms
100
PCA     time used:0.0139(s)     score:0.8125    pc number:15

(0.7628865979381443, 0.011034488677978516)
"""