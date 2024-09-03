# Impact of Reference Genome Selection on *M. tuberculosis* Clustering Analyses

## Introduction
This project explores the impact of reference genome selection on clustering analysis based on Whole Genome Sequencing (WGS) for tuberculosis (TB) surveillance and epidemiological investigations. The standard reference genome, H37Rv, often used in these analyses, may underestimate the genetic diversity of *M. tuberculosis* isolates from certain lineages. This study aims to evaluate how using lineage-specific reference genomes influences Single Nucleotide Polymorphism (SNP) distances and the resulting epidemiological conclusions. Additionally, it incorporates advanced Deep Learning techniques to enhance the precision of the analyses and utilizes cloud and Docker environments to ensure scalability and reproducibility.

## Research Objectives
- **Evaluate the Impact of Reference Genomes**: Study how different reference genomes affect SNP distances among *M. tuberculosis* isolates from Gambia (Lineages 1 to 6) and Quebec (Lineages 4 and 5).
- **Clustering Analysis and Epidemiology**: Understand how these SNP distances influence the clustering of isolates and the epidemiological conclusions about TB transmission in different contexts.
- **Integration of Deep Learning**: Apply deep learning models, such as Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs), to identify complex patterns in SNP data and predict potential transmission pathways.
- **Cloud and Docker Environments**: Deploy analyses on cloud platforms for better scalability and use Docker to ensure reproducibility of bioinformatics pipelines.

## Methodology

### Data Sets
- **Gambia**: Includes isolates from Lineages 1 to 6, representing a high TB prevalence context.
- **Quebec**: 21 confirmed outbreak isolates of Lineage 4, 21 matched controls, 4 isolates of Lineage 5 (*M. africanum*), and 12 matched controls.

### Sequencing and SNP Typing
- **Sequencing**: Illumina for all Gambia isolates; Illumina and Nanopore for Quebec isolates.
- **SNP Typing and Calling**: Use of Tbprofiler for lineage typing and clockwork/Tbpore for SNP calling.

### Statistical and Clustering Analyses
- **Normality and Variance Tests**: Shapiro-Wilk and Levene tests.
- **Non-Parametric Tests**: Kruskal-Wallis and Wilcoxon tests.
- **Bayesian Modeling**: Estimation of transmission probabilities based on observed SNP distances.

### Deep Learning Approaches
- **Convolutional Neural Networks (CNNs)**: Used for automatic feature extraction from SNP distance matrices, capturing complex patterns of transmission and genomic diversity.
- **Recurrent Neural Networks (RNNs)**: Applied to model temporal or sequential dependencies in epidemiological data, predicting future TB spread.
- **Variational Autoencoders (VAEs) and Generative Adversarial Networks (GANs)**: To generate latent representations of SNP data, facilitating the detection of hidden clusters and emerging lineages.
- **Training and Validation**: Models are trained on GPU compute clusters in the cloud to handle large datasets, with cross-validation and performance evaluation metrics (accuracy, precision, recall, F1-score).

### Cloud and Docker Infrastructure
- **Cloud Deployment**: Utilizing cloud services (AWS, Google Cloud, Azure) to host scalable compute environments necessary for deep learning-intensive analyses.
- **Dockerization of Pipelines**: Creating Docker containers to encapsulate bioinformatics pipelines, ensuring the reproducibility of analyses and facilitating the sharing of complex workflows.

## Expected Results
We anticipate that using deep learning models, combined with lineage-specific reference genomes and synthetic most recent common ancestor (MRCA) genomes, will better capture genomic diversity and reveal higher SNP distances. Deep learning approaches are expected to enhance the detection of complex transmission patterns and provide more accurate predictions about transmission pathways and lineage-specific characteristics. Cloud deployments and Docker usage will improve the scalability and reproducibility of the analyses.

## Conclusion
The results of this study will provide new insights into TB surveillance and outbreak management strategies by integrating advanced deep learning techniques with traditional epidemiological analyses. The use of cloud environments and Docker containers will ensure that the methodologies developed are scalable and reproducible, facilitating their adoption in other research contexts.

## Implications for Public Health
This study could influence public health policies by recommending the adoption of lineage-specific reference genomes and the use of deep learning models to improve molecular clustering analyses. Cloud-based and Dockerized approaches ensure that these methods can be easily scaled and replicated in diverse research environments.

## Author
**Etienne Ntumba Kabongo**

---

