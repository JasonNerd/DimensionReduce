本工程主要讨论关于数据降维的方法与应用, 尤其是Spike神经数据的降维
希望至少弄清楚这些问题:
1. 通常意义下, 有哪些降维算法, 它们的理论基础是怎样的? 它们的应用举例.
2. spike 神经数据的结构是什么? 数据每一部分的含义? 为什么可以将降维算法应用到这些数据上?
3. 将降维算法应用到这些数据上后得到怎样的结果? 如何这些结果的含义?

目前收集到的参考文章及链接如下:
1. [Comparing Open-Source Toolboxes for Processing and Analysis of Spike and Local Field Potentials Data](https://www.frontiersin.org/articles/10.3389/fninf.2019.00057)
该文章从多个方面比较了当前spike神经数据处理工具箱, 例如 FieldTrip 等. 其中, 在神经数据降维这一小节, 文章给出了 FA/GPFA/LDA/PCA/dPCA/pPCA/DCA/TCA 等降维算法, 评估了这些算法在不同工具箱中的可用性, 并提到在应用降维方法时，检查输入数据是否符合模型假设是很重要的：数据是否可以是非平稳的、包含异常值、观测噪声或相关的，记录的活动是否在低维流形中演化，样本量是否足够等。文中提到了一个链接, 该网站给出了几个降维工具箱的简介: https://users.ece.cmu.edu/~byronyu/software.shtml

另外, 主要的参考论文是:
[High-performance brain-to-text communication via handwriting](https://www.nature.com/articles/s41586-021-03506-2)
[Gaussian-Process Factor Analysis for Low-Dimensional Single-Trial Analysis of Neural Population Activity](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2712272/)

其中, 第一篇论文有详细的代码和数据, 第二篇有详细代码.

# 神经数据降维
We consider the problem of extracting smooth, low-dimensional neural trajectories that summarize the activity recorded simultaneously from many neurons on individual experimental trials. Beyond the benefit of visualizing the high-dimensional, noisy spiking activity in a compact form, such trajectories can offer insight into the dynamics of the neural circuitry underlying the recorded activity.








