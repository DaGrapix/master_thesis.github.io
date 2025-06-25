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

## Method
### Transformers

<img src="assets/transformer.svg" style="height: 500px;">

<img src="assets/megatron.png" style="height: 500px">

---

## Method
### Attention

<div>
$$
\text{Attention}(Q, K, V) = \text{SoftMax}\left(\dfrac{QK^T}{\sqrt{l}} \right) V
$$

$$
Q \in \mathbb{R}^{m \times l}\newline
K, V \in \mathbb{R}^{n \times l}
$$

**Self-attention:**
$$
\begin{cases}
\begin{align*}
Q &= X W_Q & W_Q \in \mathbb{R}^{d \times l} \newline
K &= X W_K & W_K \in \mathbb{R}^{d \times l} \newline
V &= X W_V & W_L \in \mathbb{R}^{d \times l}
\end{align*}
\end{cases}
$$

$$
X \in \mathbb{R}^{n \times d}
$$
</div>

---

## Method
### Transformers in NLP

<img src="assets/transformer_nlp.svg" style="height: 500px;">

---

## Method
### Transformers in NLP

<img src="assets/transformer_nlp_cls.svg" style="height: 500px;">

---

## Method
### Transformers in CV

<img src="assets/transformer_vit.svg" style="height: 500px;">


---

## Method
### Transformers in Physics Regression

<img src="assets/transformer_mesh.svg" style="height: 500px;">


---

## Method
### Mesh Vision Transformer

<img src="assets/ViT.svg" alt="ViT Diagram" style="width: 100%; height: auto;">

---

## Experiments
### Questions

1. Order of nodes within each patch?
2. Patch consistency across samples? (relative position of patches)
3. Positional encoding?
4. Shape of patches?


---

## Experiments
### Order of nodes within each patch? ❌
#### Morton ordering


---

## Experiments
### Patch regularity?
#### Mesh $\rightarrow$ Image

<img src="assets/physicsimage/features.png" alt="ViT Diagram" style="width: auto; height: 70%;">

<img src="assets/logos/MuscatLogo.svg" style="height: 50px; vertical-align: middle">  Powerful Mesh processing with Muscat


---

## Experiments
### Patch regularity? ✅
#### ViT with 2D patch PE


<img src="assets/physicsimage/vit_pe.png" alt="Unet results" style="width: auto; height: 70%;">
<div style="font-size: 0.8em; font-style: italic; color: #aaa; margin-top: 0.5em;">
ViT with PE
</div>

---

## Experiments
### Positional encoding? ❌
#### ViT without 2D patch PE

<img src="assets/physicsimage/vit_pe_less.png" alt="Unet results" style="width: auto; height: 70%;">
<div style="font-size: 0.8em; font-style: italic; color: #aaa; margin-top: 0.5em;">
ViT without PE
</div>

---

## Experiments
### Patch consistencity across samples?
#### MMVT (Mesh Morphing Vision Transformer)

<img src="assets/encode.svg" alt="ViT Diagram" style="width: 100%; height: auto;">

---

## Experiments
### Patch consistencity across samples?
#### MMVT (Mesh Morphing Vision Transformer)


<img src="assets/decode.svg" alt="ViT Diagram" style="width: 100%; height: auto;">

---

## Results
### PLAID Benchmark -- Evaluation Metrics

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



---

---

<br></br><br></br><br></br><br></br>
Thank you for your **attention** !