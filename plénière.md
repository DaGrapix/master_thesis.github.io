---
customTheme : "my_theme"
# theme: blood
center: false
slideNumber: true
transition: "fade"
transitionSpeed: fast
controlsTutorial: false
---

<br></br><br></br><br></br>

# Vi-Transformers for Physical Field Prediction
## Anthony Kalaydjian  
<!-- [Safran Tech](https://www.safran-group.com/fr/groupe/innovation/safran-tech) - [EPFL](https://www.epfl.ch/fr/) -->



<div style="display: flex; justify-content: center; align-items: center; gap: 75px;">
    <img src="assets/logos/safran_white.svg" alt="Safran Logo" style="height: 75px;">
    <!-- <img src="assets/logos/epfl.svg" alt="EPFL Logo" style="height: 50px;"> -->
</div>



<div style="position: absolute; bottom: 1em; right: 1em; font-size: 0.9em; color: #666;">
    4 July 2025
</div>

---

## Physics Regression Problem
### Problem statement

<div style="height: 2em;"></div>

<img src="assets/mesh_field_regression_1.svg" style="width: 100%; height: auto;">

---

## Physics Regression Problem
### Problem statement

<div style="height: 2em;"></div>

<img src="assets/mesh_field_regression_2.svg" style="width: 100%; height: auto;">


---

## Physics Regression Problem
### GNNs

<div style="display: flex; justify-content: center;">
<img src="assets/message_passing.svg" style="width: 50%; height: auto;">
</div>

<!-- **Message passing**
<div>
$$
\mathbf{x}_i^{(k)} = \gamma^{(k)} \left( \mathbf{x}_i^{(k-1)}, \bigoplus_{j \in \mathcal{N}(i)} \, \phi^{(k)}\left(\mathbf{x}_i^{(k-1)}, \mathbf{x}_j^{(k-1)},\mathbf{e}_{j,i}\right) \right)
$$
</div> -->

#### **GCN**
<div>
$$
\mathbf{x}_i^{(k)} = \sum_{j \in \mathcal{N}(i) \cup \{ i \}} \frac{1}{\sqrt{\deg(i)} \cdot \sqrt{\deg(j)}} \cdot \left( \mathbf{W}^{\top} \cdot \mathbf{x}_j^{(k-1)} \right) + \mathbf{b},
$$
</div>


---

## Physics Regression Problem
### Receptive field

<div style="height: 2em;"></div>

<table style="margin: auto; text-align: center;">
  <tr>
    <td style="text-align: center; vertical-align: middle;">
      <img src="assets/rnn.svg" style="width: 300px; height: auto; display: block; margin: auto;">
    </td>
    <td style="text-align: center; vertical-align: middle;">
      <img src="assets/cnn.svg" style="width: 300px; height: auto; display: block; margin: auto;">
    </td>
    <td style="text-align: center; vertical-align: middle;">
      <img src="assets/gnn.svg" style="width: 300px; height: auto; display: block; margin: auto;">
    </td>
  </tr>
  <tr>
    <td><b>RNN</b></td>
    <td><b>CNN</b></td>
    <td><b>GNN</b></td>
  </tr>
</table>

---

## Transformers
### Generic architecture

<img src="assets/transformer.svg">

---

## Transformers
### NLP

<img src="assets/transformer_nlp.svg">


---

## Transformers
### ViT

<img src="assets/transformer_vit.svg">


---

## Transformers
### Mesh

<img src="assets/transformer_mesh.svg">


---

## PLAID Benchmark 2/5 -- Evaluation Metrics

<div>
$$
\begin{align*}
\mathrm{RRMSE}_f(\mathbf{f}_{\rm ref}, \mathbf{f}_{\rm pred}) &= \left( \frac{1}{n_\star}\sum_{i=1}^{n_\star} \frac{\frac{1}{N^i}\|\mathbf{f}^i_{\rm ref} - \mathbf{f}^i_{\rm pred}\|_2^2}{\|\mathbf{f}^i_{\rm ref}\|_\infty^2} \right)^{1/2}\\
\mathrm{RRMSE}_s(\mathbf{s}_{\rm ref}, \mathbf{s}_{\rm pred}) &= \left( \frac{1}{n_\star} \sum_{i=1}^{n_\star} \frac{|\mathbf{s}^i_{\rm ref} - \mathbf{s}_{\rm pred}^i|^2}{|\mathbf{s}^i_{\rm ref}|^2} \right)^{1/2}
\end{align*}
$$
$$
\text{score} = \dfrac{1}{\left( N_f + N_s \right)} \left[ \sum_{f} \mathrm{RRMSE}_{f}(\mathbf{f}_{\rm ref}, \mathbf{f}_{\rm pred}) + \sum_{s} \mathrm{RRMSE}_{s}(\mathbf{s}_{\rm ref}, \mathbf{s}_{\rm pred}) \right]
$$
</div>




<!-- <img src="assets/samples.png" alt="Sample Image" style="width: 100%; height: auto;"> -->

---

## Vi-Transformers

<img src="assets/ViT.svg" alt="ViT Diagram" style="width: 100%; height: auto;">

---

### Tokenization 1/2: Padding + Morton registration

<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
<img src="assets/padding_2d.png" alt="2D Grid" style="width: 30%; height: auto;">
</div>

<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
    <img src="assets/morton/2d_grid.png" alt="2D Grid" style="width: 35%; height: auto;">
    <!-- <img src="assets/morton/2d_pointcloud.png" alt="2D Point Cloud" style="width: 35%; height: auto;"> -->
    <img src="assets/morton/patch.png" alt="2D Point Cloud" style="width: 35%; height: auto;">
</div>

---

### Tokenization 2/2: 3d patches
<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
    <iframe src="assets/morton/rotor_patch_0.html" style="width: 1200px; height: 400px; border: none; font-size: 0.01em;"></iframe>
    <iframe src="assets/morton/rotor_patch_1.html" style="width: 1200px; height: 400px; border: none; font-size: 0.01em;"></iframe>
</div>


---


## PLAID Article

<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
<img src="assets/plaid_article.png" width="60%" position="center">
</div>

---



## First Benchmark Results

- Performance equivalent to MGN
- Train time reduced significantly

<br></br>

Other methods:

- MARIO (Neural Fields Representation): Geometry encoding using the SDF
- MMGP: Morphing to a common geometry

---

## Next step

- **Switch on A100 cluster**

<br></br>

### Technical tasks:
* Fix the training environment


<br></br>

### Scientific tasks:
* Morphing
* Decoder
* Conditioning through network modulation

---

### Morphing

<div style="display: flex; justify-content: center; align-items: center; gap: 50px;">
<img src="assets/morphing/patch.png" alt="ViT Diagram" style="width: auto; height: auto;">
<img src="assets/morphing/morphed_patch.png" alt="ViT Diagram" style="width: auto; height: 70%;">
</div>

---

### Decoder

<img src="assets/new_ViT.svg" alt="ViT Diagram" style="width: 100%; height: auto;">

---

### Conditioning by layer modulation

<div style="display: flex; justify-content: center; align-items: center; gap: 75px;">
<img src="assets/DiT.png" alt="ViT Diagram" style="width: 60%; height: auto;">
</div>

---

<br></br><br></br><br></br><br></br>
Thank you for your **attention** !