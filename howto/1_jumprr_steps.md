# JUMP_rr tutorial.
## **Step-by-step tutorial: Using JUMP_rr to answer key biological questions**

<p align="justify">The JUMP_rr interactive [tools](https://github.com/broadinstitute/monorepo/tree/main/libs/jump_rr#quick-data-access) allow you to explore the JUMP dataset of genetic and chemical perturbations and their effects on cell morphology features. The data shown have been aggregated across replicates for each gene and by applying different filters, you can investigate how specific perturbations influence cells, their structures, and the strength of the changes.</p>

In this tutorial, you will learn how to:

**Step 1: Understand the information displayed in the browser.**  
**Step 2: Explore the data to answer the following questions:**

**2.1**. Is my gene in the JUMP dataset?  
**2.2.** Does my gene have a morphological phenotype when overexpressed or knocked down by CRISPR?  
  **2.2.1.** If yes, what are the specific morphological changes or features?  
  **2.2.2.** What other genes look similar or anticorrelated to my gene?

### **Step 1\. Understand the information displayed in the browser.**

When you open one of the interactive tables, such as the CRISPR knock-outs [table](http://broad.io/crispr_feature), you will see an informational section explaining the available columns, and a filtering tool (Figure 1), followed by the data from CRISPR knockouts of all available genes.

<img src="https://zenodo.org/api/records/15243111/files/Figure1.png/content" style="max-width: 100%; height: auto; display: block;">

***Figure 1\.** Information section of the CRISPR Feature Ranking table. The red boxes highlight two key components: the first provides definitions for each column; the second one shows the  tool to filter based on the content values, such as gene name, subcellular compartment or statistical significance associated with each perturbation*

Below you will find the full table (Figure 2), which displays aggregated results across replicates for each perturbation.

<img src="https://zenodo.org/api/records/15243111/files/Figure2.png/content" style="max-width: 100%; height: auto; display: block;">

***Figure 2\.** Each column can be sorted in ascending or descending order by clicking on the header. Sorting is applied to one column at a time and is based on the data type: numerical values are sorted by magnitude, while text is sorted alphabetically. The entries displayed are the 30 most statistically significant features for each gene (Feature Rank), and for each feature, the 30 genes with the most significant values (Gene Rank). A value of 999999 indicates an unassigned entry.*

### **Step 2: Explore the data to answer the following questions:**

#### **2.1. Can I find my gene in the JUMP collection of perturbations?**

The JUMP Hub includes a reference tool to quickly check whether a specific gene is included in the collection of genetic perturbations. From any page on the  [JUMP Hub](https://broad.io/jump), click on the "Available Genes" tab in the sidebar. Here you can type the name gene of interest to search. The number of occurrences in multiple JUMP or JUMP-adjacent morphological profiling datasets will be displayed: “crispr” and “orf” are the JUMP knock-outs and over expression datasets, “A549”, “HeLa\_DMEM” and “HeLa\_HPLM” relate to the [PERISCOPE](https://github.com/broadinstitute/2022_PERISCOPE) dataset. and [Lacoste](https://github.com/carpenter-singh-lab/2024_LacosteHaghighi_Cell_Mislocalization) to a dataset focusing on pathogenic coding variants. This feature is especially useful when you're exploring potential targets or pathways and want to collate data from multiple morphology-based datasets (Figure 3).

<img src="https://zenodo.org/api/records/15243111/files/Figure3.png/content" style="max-width: 100%; height: auto; display: block;">

***Figure 3\.** Overview of the gene reference tool (red box on the left), to quickly check  whether your gene of interest is available in the dataset. You can search using the full name or partial name of a gene in the search window (red box on the right). For each gene, the tool displays how many times it appears in the JUMP dataset under different perturbation types, such as CRISPR (for gene knockout) and ORF (for overexpression), as well as across information related to the PERISCOPE (A549, HeLa\_DMEM and HeLa\_HPLM) and Lacoste datasets.*

#### **2.2. Does my gene of interest produce a morphology phenotype when overexpressed or knocked down by CRISPR?**

To answer this question, we’ll start by exploring the CRISPR knockout dataset to identify genes whose loss affects the phenotype of interest. Then, we’ll use the ORF overexpression dataset to contrast results with gene overexpression. 

***Search for your gene in the CRISPR dataset.***

Let us explore data related to the SLC2A2 gene. This gene encodes **GLUT2**, a glucose transporter primarily expressed in organs such as liver, pancreas and intestine. It plays a key role in glucose sensing and homeostasis. Given its involvement in metabolic processes, changes in SLC2A2 activity or expression could have significant phenotypic consequences that may be captured in image-based profiling data. 

To look for this you can use the Filter Tool, which helps narrow down the dataset based on specific search criteria. When you open the filter tab, a list of all available column names will appear (Figure 4A). In this case, you would select the "Perturbation" column, use the default operator “=”, and enter “SLC2A2” in the search field to display only the rows associated with that gene (Figure 4B).

If you're unsure of the exact name used in the dataset, we recommend make your search case-insensitive by changing the default filter operator from “=” to “like”, and entering a pattern that partially matches a text string, such as “SLC2A%” (Figure 4C).

You can also search for alternative names commonly used in the literature. To do this, select the "Synonyms" column, change the filter operator to “contains” or “like”, and enter an alternative name such as GLUT2, or another known synonym of your compound of interest (Figure 4D).

<img src="https://zenodo.org/api/records/15243111/files/Figure4.png/content" style="max-width: 100%; height: auto; display: block;">

***Figure 4\.** Common usage of filtering options. Panel A shows the full list of columns available for custom filtering, including metadata such as Corrected p-value, Compartment, and others that support more advanced queries beyond gene-level filtering. B and C, illustrate how the number of entries returned depends on the filter type: a broader search using partial names (e.g., “SLC2A%”) yields more entries than an exact match (e.g., “SLC2A2”), which can help identify related genes within the same family. For instance, the GLUT (glucose transporter) family is encoded by different members of the SLC2A gene family (e.g., SLC2A1, SLC2A2, etc.), each representing a distinct transporter rather than isoforms of the same gene. D, highlights the utility of the Synonyms column, which maps alternative gene names used in the literature, especially useful for genes with multiple aliases or legacy names not directly listed under the Perturbation column.*

The table below describes the available logical operators (Table1).

| Operator | Description |
| ----- | ----- |
| \= | Selects results that exactly match the specified value. |
| \!= | Excludes results that exactly match the specified value. |
| contains | Searches for values that include a specific string within the text. |
| ends with | Selects values that end with a specific string. |
| starts with | Selects values that start with a specific string. |
| \> | Selects numeric values greater than the specified value. |
| ≥ | Selects numeric values greater than or equal to the specified value. |
| \< | Selects numeric values less than the specified value. |
| ≤ | Selects numeric values less than or equal to the specified value. |
| like | Searches for patterns that partially match a text string (e.g., “SLC%”). |
| not like | Excludes results that partially match a specific pattern. |
| in | Selects rows where the column value is within a specified list of values. |
| not in | Excludes rows where the column value is within a specified list of values. |
| is blank | Filters rows where the value is an empty string or space — the field exists but has no visible content. |
| is not blank | Filters rows where the field contains visible content (text, numbers, etc.), excluding empty or space-only values. |

***Table 1\.** Filtering operators used to refine values displayed in the dataset. Include or exclude rows based on specific conditions, such as matching exact values, checking for patterns in text, or evaluating numerical comparisons.*

You can combine multiple filters. For instance, to focus on features associated with the SLC2A2 perturbation specifically in the “Cells” and “Nuclei” compartments, select the *Compartment* column, use the “**in”** operator, and enter “Cells, Nuclei” (Figure 5). Similarly, you can filter by other fields, such as perturbation (e.g., a list of genes), experiment type, or cell type. Once the filters are applied, you can copy the filtered table by clicking the JSON hyperlink (Figure 5, red box). To export the content, press Ctrl+A to select all, then Ctrl+C to copy it, and finally paste it into a text editor.

<img src="https://zenodo.org/api/records/15243111/files/Figure5.png/content" style="max-width: 100%; height: auto; display: block;">

***Figure 5\.** Example of combined filters applied to display gene-related data limited to the “Cells” and “Nuclei” compartments. The red box highlights available export options, such as JSON, which can streamline the integration of filtered results into external analysis pipelines or visualization tools.*

After applying the filter for the **SLC2A2** perturbation, we can evaluate whether the perturbation is significantly different to the negative control condition by examining the **Corrected p-value** column. The Corrected p-value represents the statistical significance of how distinctive the overall morphological profile of a perturbation is when compared to the negative control (after false discovery rate correction). In this case, the corrected p-value is **0.00018**  (all rows display the same value in that column, since this value is computed per perturbation, not per feature). This value (p-value\<0.05) indicates a highly significant difference from the control condition, suggesting that overexpressing **SLC2A2** induces a strong and consistent morphological effect (Figure 6).

<img src="https://zenodo.org/api/records/15243111/files/Figure6.png/content" style="max-width: 100%; height: auto; display: block;">

**Figure 6\.**  *The user interface displays the Corrected p-value, which is calculated at the perturbation level. As a result, all rows associated with the SLC2A2 perturbation share the same value (0.00018). When exploring multiple perturbations, sorting by Corrected p-value can help prioritize those with the most statistically significant morphological effects, making it a useful strategy for identifying relevant hits. The rows are sorted in ascending/descending order by clicking the name column header.*

##### **2.2.1. What are the specific morphology changes/features?**

In this section you will be able to identify which features are the most statistically significant within a perturbation. In this filtered view of the SLC2A2 perturbation, all values in the **Feature significance** column are **0.0,** which corresponds to values rounded to five decimal places and  indicates that each listed morphological feature is statistically significant when compared to the control condition (Figure 7). If you'd like more information about the features extracted by CellProfiler, such as how they’re named and calculated, you can check out the [Cellprofiler Handbook](https://cellprofiler-manual.s3.amazonaws.com/CellProfiler-4.0.4/index.html).

<img src="https://zenodo.org/api/records/15243111/files/Figure7.png/content" style="max-width: 100%; height: auto; display: block;">

***Figure 7\.** Top 4 features from the filtered CRISPR dataset for the SLC2A2 perturbation. The rows are sorted in ascending order based on the Feature Significance column (highlighted with a red box). All p-values in this column are displayed as 0.0, which reflects values approximated to five decimal places (i.e., \< 0.00001). Since many features share these low values, we recommend using **Feature Rank** to prioritize features, as it provides their relative importance for each gene.*

***Search for your gene in ORF dataset.***

To explore whether overexpressing SLC2A2 produces a morphological phenotype, we repeated the same filtering process in the ORF overexpression dataset, link [here](http://broad.io/orf_feature). Using the Filter Tool, we selected the Perturbation column, kept the operator as "=", and entered SLC2A2 in the search field. 

After filtering, we examined the **Corrected p-value** column. In this case, the p-value is **0.09482**, which is above the 0.05 threshold, indicating that overexpressing *SLC2A2* does not produce a statistically significant morphological change. This contrasts with the CRISPR knockout dataset, where the loss of *SLC2A2* resulted in a strong and significant phenotypic effect.

However, in the case of SLC2A2, it is still possible to identify individual morphological features that are statistically significant, even if the overall perturbation does not show significant changes compared to the control. In this filtered view, a few features have **Feature Significance** values below 0.05, indicating meaningful differences relative to the control condition (Figure 8).

<img src="https://zenodo.org/api/records/15243111/files/Figure8.png/content" style="max-width: 100%; height: auto; display: block;">

***Figure 8\.** Top four morphological features based on feature significance (per-feature p-values), ranked in increasing order, indicating statistically significant differences compared to the control condition. The Channel and Suffix columns appear empty because these features solely come from an object mask and not a fluorescence image. The rows are sorted in ascending/descending order by clicking the name column header.*

##### **2.2.2. What other genes look similar or anticorrelated to my genes?"**

Before exploring which perturbations produce the most similar or anti-similar (i.e., features that are high in one are lower in the other one), it's important to understand the broader context and potential of image-based gene profiling. 

Morphological profiles can cluster genes into biologically meaningful groups, uncovering known pathways and reveal functional connections, such as a regulatory interaction between pathways (Rohban et al. 2017). This clustering is based on the similarity of high-dimensional morphological features extracted from images after gene overexpression. Comparing these profiles systematically can also identify *anti-correlated* perturbations, such as cases where one perturbation reverses the phenotype of another (Rohban et al., 2022).  This is particularly relevant for therapeutic discovery, as finding antagonistic morphological profiles may highlight candidate compounds or genes that *suppress* an undesired phenotype.

The "matches” table thus quantifies similarity (or anticorrelation) of profiles and is a powerful resource to uncover potential functional relationships between genes, explore unknown gene roles, or even identify suppressors or enhancers within a biological pathway. These insights can help prioritize follow-up experiments and hypothesis generation, especially when analyzing genes or perturbations with poorly characterized functions.

As an initial step, the *SLC2A2* perturbation was analyzed in the CRISPR matches [table](http://broad.io/crispr) , where the Perturbation-Match Similarity scores range from \-1 (strong anti-similarity) to 1 (strong similarity). In this case, *SLC2A2* knockout displays a strong phenotypic effect, and when compared to other perturbations, a wide range of similarity scores is observed, from a maximum of 0.621 (phenotypic similarity) to a minimum of \-0.513 (anticorrelated). 

These similarity relationships can provide insight into genes with potentially related biological functions or pathways. For example, high similarity scores may reflect co-regulated or functionally linked genes, while highly anticorrelated profiles may point to perturbations with opposing phenotypic effects, which could help generate hypotheses about antagonistic regulatory mechanisms or compensatory pathways. The most similar matches may suggest functional relationships (Figure 9, red box) , while the Match Resources column links to external databases where additional biological pathway information can be explored (Figure 9, blue box). 

In contrast, when examining the *SLC2A2* overexpression in the ORF [dataset](http://broad.io/orf), the range of Perturbation-Match Similarity scores is much narrower, spanning approximately from 0.27 to \-0.223. This limited dynamic range may reflect the fact that *SLC2A2* overexpression induces a weaker morphological phenotype compared to its knockout.

Taken together, these comparisons provide a starting point for hypothesis generation and pathway exploration, particularly when integrating multiple types of perturbations.

<img src="https://zenodo.org/api/records/15243111/files/Figure9.png/content" style="max-width: 100%; height: auto; display: block;">

***Figure 9\.** Comparison between the selected perturbation, SLC2A2,  and all other perturbations in the CRISPR dataset, ranked by morphological similarity. The Perturbation-Match Similarity column (red box) indicates how similar or anticorrelated each perturbation is to SLC2A2 (click on column name to sort it). The Match Resources column (blue box) provides external links to databases with additional information about the genes being compared. The merged images of all Cell Painting channels for SLC2A2 and its matched perturbation can be inspected in the "Perturbation example image" and "Match example image" columns, allowing visual assessment of their morphological signatures to facilitate the evaluation of similarities or differences between perturbations.* 

**References:**

Mohammad Hossein Rohban, Shantanu Singh, Xiaoyun Wu, Julia B Berthet, Mark-Anthony Bray, Yashaswi Shrestha, Xaralabos Varelas, Jesse S Boehm, Anne E Carpenter (2017) Systematic morphological profiling of human gene and allele function via Cell Painting eLife 6:e24060

Mohammad H. Rohban, Ashley M. Fuller, Ceryl Tan, Jonathan T. Goldstein, Deepsing Syangtan, Amos Gutnick, Ann DeVine, Madhura P. Nijsure, Megan Rigby, Joshua R. Sacher, Steven M. Corsello, Grace B. Peppler, Marta Bogaczynska, Andrew Boghossian, Gabrielle E. Ciotti, Allison T. Hands, Aroonroj Mekareeya, Minh Doan, Jennifer P. Gale, Rik Derynck, Thomas Turbyville, Joel D. Boerckel, Shantanu Singh, Laura L. Kiessling, Thomas L. Schwarz, Xaralabos Varelas, Florence F. Wagner, Ran Kafri, T.S. Karin Eisinger-Mathason, Anne E. Carpenter (2022) Virtual screening for small-molecule pathway regulators by image-profile matching. *Cell Systems*, 13(9): 724–736.e9.