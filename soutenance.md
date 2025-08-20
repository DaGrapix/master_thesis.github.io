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


<h1 style="margin-bottom: 0.2em; font-size: 2.3em;">Vi-Transformers for Physics Surrogate Modeling</h1>

## Anthony Kalaydjian  
<!-- [Safran Tech](https://www.safran-group.com/fr/groupe/innovation/safran-tech) - [EPFL](https://www.epfl.ch/fr/) -->



<div style="display: flex; justify-content: center; align-items: center; gap: 75px;">
<img src="assets/logos/epfl.svg" alt="EPFL Logo" style="height: 50px;">
<img src="assets/logos/safran.svg" alt="Safran Logo" style="height: 50px;">
</div>



<div style="position: absolute; bottom: 1em; right: 1em; font-size: 0.9em; color: #666;">
    25 August 2025
</div>

---

## Physics Mesh Regression Problem

<img src="assets/mesh_field_regression_export.svg" style="width: 100%; height: auto;">


---


## Taxonomy of Models for Variable Domain Geometry

<div style="display: flex; gap: 40px; align-items: flex-start; justify-content: center;">
  <div style="flex: 1; padding: 10px; text-align: center;">
    <h3 style="text-align: center;">Shape embedding</h3>
    <div style="font-size:1.1em; color:#444; margin-top:5%; text-align:center">SDF embedding</div>
  <img src="assets/models/mario.svg" alt="Mario SVG" style="width:80%; height:auto; display:inline-block;">
  <div style="font-size:1.1em; color:#444; margin-top:-5%;"></div>
    <div style="font-size:1.1em; color:#444; margin-top:10%; text-align:center">Morphing</div>
  <img src="assets/models/mmgp.svg" alt="MMGP SVG" style="width:80%; height:auto; display:inline-block;">
  </div>
  <div style="flex: 1; padding: 10px; text-align: center;">
    <h3 style="text-align: center;">Relational</h3>
    <div style="font-size:1.1em; color:#444; margin-top:5%; text-align:center;">GNN</div>
  <img src="assets/models/relational.svg" alt="Relational SVG" style="width:60%; height:auto; display:inline-block;">
  </div>
</div>

---

## Transformers

<div style="display: flex; justify-content: center; align-items: initial;">
  <img src="assets/models/transformer.svg" alt="Transformer Architecture" style="width:60%; height:auto; display:inline-block;">
</div>

---

## Self-Attention

### Simple form

<div>
$$
\begin{cases}
    q_n = W_Q x_n\\
    k_n = W_K x_n\\
    v_n = W_V x_n
\end{cases}, \quad
$$
with token $x_n\in \mathbb{R}^l$ and matrices $W_Q, W_K, W_V \in \mathbb{R}^{l \times d}$
</div>

<div style="margin-top:5%">
$$
    \mathrm{SelfAttention}(q_i, (k_n), (v_n)) = \sum_n \alpha_{i, n} v_n,
$$
where $ \alpha_{i, n} = \dfrac{\exp(q_i^T k_n) / \sqrt{d}}{\sum_n \exp(q_i^T k_n) / \sqrt{d}}$
</div>

<br></br>

### Matrix form:
<div>
$$
\mathrm{SelfAttention}(Q, K, V) = \mathrm{SoftMax}\left(\frac{Q K^T}{\sqrt{d}}\right) V,
$$
where $Q = XW_Q, K = XW_K, V = XW_V$
</div>

---

## Transformers in NLP

<div style="display: flex; justify-content: center; align-items: initial;">
  <img src="assets/models/transformer_nlp.svg" alt="Transformer Architecture" style="width:60%; height:auto; display:inline-block;">
</div>

---

## Vision Transformers

<div style="display: flex; justify-content: center;">
  <img src="assets/models/transformer_vit.svg" alt="Transformer Architecture" style="width:60%; height:auto; display:inline-block;">
</div>


---

## Transformer for mesh

<div style="display: flex; justify-content: center;">
  <img src="assets/models/transformer_mesh.svg" alt="Transformer Architecture" style="width:60%; height:auto; display:inline-block;">
</div>


---

## Mesh Vision Transformer

<div style="display: flex; justify-content: center;">
  <img src="assets/models/MVT.svg" alt="MVT" style="height:50vh; width:auto;">
</div>

---

## Patch flattening 1/4

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 30px;">
  <div style="flex: 0 0 45%; display: flex; flex-direction: column; justify-content: flex-start; align-items: center; text-align: center; height: 80vh;">
    <img src="assets/morton/morton.svg" alt="Morton ordering on a regular grid" style="max-height: 100%; width: auto;">
    <div style="font-size: 1em; color: #444; margin-top: 0.5em; margin-bottom: 0;">Morton ordering on a regular 2D grid</div>
  </div>
  <div style="flex: 0 0 45%; display: flex; flex-direction: column; justify-content: flex-start; align-items: center; text-align: center; height: 80vh;">
    <img src="assets/morton/tensile_decomposition.svg" alt="Tensile2D Domain Decomposition" style="max-height: 100%; width: auto;">
    <div style="font-size: 1em; color: #444; margin-top: 0.5em; margin-bottom: 0;"><code>Tensile2D</code> partitioning</div>
  </div>
</div>

---

## Patch flattening 2/4

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 30px;">
  <div style="flex: 0 0 45%; display: flex; flex-direction: column; justify-content: flex-start; align-items: center; text-align: center; height: 80vh;">
    <img src="assets/morton/patch_0.svg" alt="Patch #0" style="max-height: 100%; width: auto;">
    <div style="font-size: 1em; color: #444; margin-top: 0.5em; margin-bottom: 0;">Patch #0</div>
  </div>
  <div style="flex: 0 0 45%; display: flex; flex-direction: column; justify-content: flex-start; align-items: center; text-align: center; height: 80vh;">
    <img src="assets/morton/patch_40.svg" alt="Patch #44" style="max-height: 100%; width: auto;">
    <div style="font-size: 1em; color: #444; margin-top: 0.5em; margin-bottom: 0;">Patch #44</div>
  </div>
</div>

---

## Patch flattening 3/4

<div style="display: flex; flex-direction: column; gap: 30px; align-items: center;">
  <div style="display: flex; justify-content: center; gap: 30px; width: 100%;">
    <div style="flex: 0 0 45%; text-align: center;">
      <iframe src="assets/morton/3d_grid.html" style="width: 500px; height: 350px; border: none;"></iframe>
      <div style="font-size: 1em; color: #444; margin-top: 0.5em;">Morton ordering on a regular 3D grid</div>
    </div>
    <div style="flex: 0 0 45%; text-align: center;">
      <iframe src="assets/morton/rotor37_global_patches_40_60.html" style="width: 500px; height: 350px; border: none;"></iframe>
      <div style="font-size: 1em; color: #444; margin-top: 0.5em;"><code>Rotor37</code> partitioning</div>
    </div>
</div>

---

## Patch flattening 4/4

  <div style="display: flex; justify-content: center; gap: 30px; width: 100%;">
    <div style="flex: 0 0 45%; text-align: center;">
      <iframe src="assets/morton/rotor37_patch_40.html" style="width: 500px; height: 350px; border: none;"></iframe>
      <div style="font-size: 1em; color: #444; margin-top: 0.5em;">Patch #40</div>
    </div>
    <div style="flex: 0 0 45%; text-align: center;">
      <iframe src="assets/morton/rotor37_patch_60.html" style="width: 500px; height: 350px; border: none;"></iframe>
      <div style="font-size: 1em; color: #444; margin-top: 0.5em;">Patch #60</div>
    </div>
  </div>

---

## PLAID Benchmark 1/2

<img src="assets/samples.png" alt="Sample Image" style="width: 100%; height: auto;">

<div style="margin-top: 1.5em; font-size: 1em; color: #444; text-align: center;">
  <strong>PLAID datasets fields visualizations.</strong>
</div>

---


## PLAID Benchmark 2/2



| Dataset                | Mesh (mean nodes) | Inputs         | Outputs            | Splits (train/test)  |
|------------------------|-------------------|----------------|--------------------|----------------------|
| `Tensile2d`            | tri (9,428)       | mesh, 6 scalars| 4 scalars, 6 fields| 500 / 200            |
| `2D_MultiScHypEl`      | tri (5,692)       | mesh, 3 scalars| 1 scalar, 7 fields | 764 / 376            |
| `Rotor37`              | quad (29,773*)    | mesh, 2 scalars| 4 scalars, 3 fields| 1,000 / 200          |
| `2D_profile`           | tri (37,042)      | mesh           | 4 fields           | 300 / 100            |
| `VKI-LS59`             | quad (36,421*)    | mesh, 2 scalars| 6 scalars, 7 fields| 671 / 168            |

<div style="margin-top: 1.5em; font-size: 1em; color: #444; text-align: center;">
  <strong>PLAID datasets characteristics.</strong>
</div>


### Evaluation metrics

<div>
$$
\begin{align*}
\mathrm{RRMSE}_f(\mathbf{f}_{\rm ref}, \mathbf{f}_{\rm pred}) &= \left( \frac{1}{n_\star}\sum_{i=1}^{n_\star} \frac{\frac{1}{N^i}\|\mathbf{f}^i_{\rm ref} - \mathbf{f}^i_{\rm pred}\|_2^2}{\|\mathbf{f}^i_{\rm ref}\|_\infty^2} \right)^{1/2}\\
\mathrm{RRMSE}_s(\mathbf{s}_{\rm ref}, \mathbf{s}_{\rm pred}) &= \left( \frac{1}{n_\star} \sum_{i=1}^{n_\star} \frac{|s^i_{\rm ref} - s_{\rm pred}^i|^2}{|s^i_{\rm ref}|^2} \right)^{1/2}
\end{align*}
$$
$$
\text{total_error} = \dfrac{1}{\left( N_f + N_s \right)} \left[ \sum_{f} \mathrm{RRMSE}_{f}(\mathbf{f}_{\rm ref}, \mathbf{f}_{\rm pred}) + \sum_{s} \mathrm{RRMSE}_{s}(\mathbf{s}_{\rm ref}, \mathbf{s}_{\rm pred}) \right]
$$
</div>



---

## Benchmark results 1/2

| Dataset           | MGN    | MVT       | Augur         | MMGP        | MARIO  |
|-------------------|--------|--------   |--------       |--------     |--------|
| `Tensile2d`       | 0.0673 | 0.0116    | 0.0154        | **0.0026**  | <u>0.0038</u> |
| `2D_MultiScHypEl` | 0.0437 | <u>0.0325</u>    | **0.0232**    | -           | 0.0573 |
| `2D_profile`      | 0.0593 | <u>0.0312</u>  | 0.0425   | 0.0365      | **0.0307** |
| `VKI-LS59`        | 0.0684 | <u>0.0193</u>  | 0.0267   | 0.0312      | **0.0124** |
| `Rotor37`         | 0.0074 | 0.0029    | 0.0033        | **0.0014**  | <u>0.0017</u> |

<div style="margin-top:0.5em; font-size:0.95em; text-align:center; color:#444;">
  <strong>Benchmark total errors.
</div>
<div style="margin-top:0.5em; font-size:0.95em; text-align:center; color:#444;">
  Best on each line is <b>bold</b>, second best is <u>underlined</u>.</strong>
</div>

- **No universal winner**  
- **Shape embedding models (MMGP, MARIO) struggle in varying topology**  
- **MVT >> MGN and consistently strong**

---


## Benchmark results 2/2

<div style="display: flex; flex-direction: column; gap: 30px; align-items: center;">
  <!-- First row: Tensile2D, Multiscale, 2D Profile -->
  <div style="display: flex; justify-content: center; gap: 30px; width: 100%;">
    <div style="flex: 0 0 30%; text-align: center;">
      <img src="assets/benchmarks/tensile2d.svg" alt="Tensile2d"
           style="height: 4cm; max-width: 100%; object-fit: contain;">
      <div style="font-size: 1em; color: #444; margin-top: 0.5em;"><code>Tensile2d</code></div>
    </div>
    <div style="flex: 0 0 30%; text-align: center;">
      <img src="assets/benchmarks/multiscale.svg" alt="2D_MultiScHypEl"
           style="height: 4cm; max-width: 100%; object-fit: contain;">
      <div style="font-size: 1em; color: #444; margin-top: 0.5em;"><code>2D_MultiScHypEl</code></div>
    </div>
    <div style="flex: 0 0 30%; text-align: center;">
      <img src="assets/benchmarks/2d_profile.svg" alt="2D_Profile"
           style="height: 4cm; max-width: 100%; object-fit: contain;">
      <div style="font-size: 1em; color: #444; margin-top: 0.5em;"><code>2D_Profile</code></div>
    </div>
  </div>
  <!-- Second row: Rotor37 and VKIL-S59 -->
  <div style="display: flex; justify-content: center; gap: 30px; width: 100%;">
    <div style="flex: 0 0 45%; text-align: center;">
      <img src="assets/benchmarks/rotor37.svg" alt="Rotor37"
           style="height: 4cm; max-width: 100%; object-fit: contain;">
      <div style="font-size: 1em; color: #444; margin-top: 0.5em;"><code>Rotor37</code></div>
    </div>
    <div style="flex: 0 0 45%; text-align: center;">
      <img src="assets/benchmarks/vkils59.svg" alt="VKIL-S59"
           style="height: 4cm; max-width: 100%; object-fit: contain;">
      <div style="font-size: 1em; color: #444; margin-top: 0.5em;"><code>VKIL-S59</code></div>
    </div>
  </div>
</div>

<div style="margin-top: 1.5em; font-size: 1em; color: #444; text-align: center;">
  <strong>MVT predicted fields visualizations.</strong>
</div>

---

## Total Error vs Patch Size Comparison

<div style="display: flex; flex-direction: column; gap: 30px; align-items: center;">
  <!-- First row: 3 figures -->
  <div style="display: flex; justify-content: center; gap: 30px; width: 100%;">
    <div style="flex: 0 0 30%; text-align: center;">
      <img src="assets/results/2d_multiscale_hyperelasticity_total_error_vs_patch_size.svg" alt="2D_MultiScHypEl" style="height: 4cm; max-width: 100%; object-fit: contain;">
      <div style="font-size: 1em; color: #444; margin-top: 0.5em;"><code>2D_MultiScHypEl</code></div>
    </div>
    <div style="flex: 0 0 30%; text-align: center;">
      <img src="assets/results/2d_profile_total_error_vs_patch_size.svg" alt="2D_profile" style="height: 4cm; max-width: 100%; object-fit: contain;">
      <div style="font-size: 1em; color: #444; margin-top: 0.5em;"><code>2D_profile</code></div>
    </div>
    <div style="flex: 0 0 45%; text-align: center;">
      <img src="assets/results/tensile2d_total_error_vs_patch_size.svg" alt="Tensile2d" style="height: 4cm; max-width: 100%; object-fit: contain;">
      <div style="font-size: 1em; color: #444; margin-top: 0.5em;"><code>Tensile2d</code></div>
    </div>
  </div>
  <!-- Second row: 2 figures -->
  <div style="display: flex; justify-content: center; gap: 30px; width: 100%;">
    <div style="flex: 0 0 45%; text-align: center;">
      <img src="assets/results/rotor37_total_error_vs_patch_size.svg" alt="Rotor37" style="height: 4cm; max-width: 100%; object-fit: contain;">
      <div style="font-size: 1em; color: #444; margin-top: 0.5em;"><code>Rotor37</code></div>
    </div>
    <div style="flex: 0 0 30%; text-align: center;">
      <img src="assets/results/vkils59_total_error_vs_patch_size.svg" alt="VKI-LS59" style="height: 4cm; max-width: 100%; object-fit: contain;">
      <div style="font-size: 1em; color: #444; margin-top: 0.5em;"><code>VKI-LS59</code></div>
    </div>
  </div>
</div>

<div style="margin-top: 1.5em; font-size: 1em; color: #444; text-align: center;">
  <strong>Comparison of total error vs patch size for different datasets.</strong>
</div>

---

## Questions

- Is positional encoding necessary?
- How about the loss of the grid regularity in images?
- Does the cross-sample partitioning consistency matter?
- Is there enough data in the datasets for the transformer to learn?

---

## Mesh-to-image

<div style="display: flex; justify-content: center;">
  <img src="assets/misc/mesh-image.svg" alt="MVT" style="height:50vh; width:auto;">
</div>

- 256 x 256 images

---

## RRMSEs for 2D_MultiScHypEl

| Field, _scalar_         | Vit_pe      | Vit_pe_less | U-Net            |  FNO            | MVT (20)       | 
|-------------------------|-------------|-------------|------------------|---------------- |-------------   |
| **u1**                  | 0.0361      | 0.0355      | 0.0291           |  **0.0115**     | <u>0.0213</u>  |
| **u2**                  | 0.0347      | 0.0353      | 0.0283           |  **0.0117**     | <u>0.0210</u>  |
| **P11**                 | 0.0437      | 0.0439      | **0.0349**       | <u>0.0353</u>   | 0.0397         |  
| **P12**                 | 0.0630      | 0.0623      | **0.0498**       |  <u>0.0513</u>  | 0.0718         |
| **P22**                 | 0.0442      | 0.0444      | **0.0347**       |  <u>0.0359</u>  | 0.0405         |  
| **P21**                 | 0.0626      | 0.0617      | **0.0500**       |  <u>0.0510</u>  | 0.0703         |
| **psi**                 | 0.0367      | 0.0365      | <u>0.0350</u>    |  **0.0329**     | 0.0374         |
| _effective_energy_      | 0.0204      | 0.0217      | 0.0180           | <u>0.0120</u>   | **0.0116**     |      
| **total_error**         | 0.0427      | 0.0426      | <u>0.0350</u>    |  **0.0302**     | 0.0392         |

<div style="margin-top:0.5em; font-size:0.95em; text-align:center; color:#444;">
  <strong>Relative Root Mean Square Errors (RRMSEs) for <code>2D_MultiScHypEl</code>.
</div>
<div style="margin-top:0.5em; font-size:0.95em; text-align:center; color:#444;">
  Best on each line is <b>bold</b>, second best is <u>underlined</u>.</strong>
</div>

---

## MMVT 1/2

<div style="display: flex; justify-content: center;">
  <img src="assets/misc/mmvt.svg" alt="MVT" style="height:50vh; width:auto;">
</div>

---

## MMVT 2/2


<div style="display: flex; gap: 40px; align-items: flex-start; justify-content: center;">
  <div style="flex: 1; min-width: 320px;">
    <table>
      <thead>
        <tr>
          <th>Field, <em>scalar</em></th>
          <th>MMGP</th>
          <th>MVT</th>
          <th>MMVT</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>U1</strong></td><td><strong>0.0015</strong></td><td>0.0086</td><td><u>0.0043</u></td></tr>
        <tr><td><strong>U2</strong></td><td><strong>0.0009</strong></td><td>0.0091</td><td><u>0.0051</u></td></tr>
        <tr><td><strong>sig11</strong></td><td><strong>0.0031</strong></td><td>0.0184</td><td><u>0.0089</u></td></tr>
        <tr><td><strong>sig22</strong></td><td><strong>0.0013</strong></td><td>0.0102</td><td><u>0.0037</u></td></tr>
        <tr><td><strong>sig12</strong></td><td><strong>0.0021</strong></td><td>0.0146</td><td><u>0.0051</u></td></tr>
        <tr><td><em>max_von_mises</em></td><td><strong>0.0050</strong></td><td>0.0090</td><td><u>0.0068</u></td></tr>
        <tr><td><em>max_U2_top</em></td><td><strong>0.0053</strong></td><td>0.0203</td><td><u>0.0073</u></td></tr>
        <tr><td><em>max_sig22_top</em></td><td><strong>0.0017</strong></td><td>0.0021</td><td><u>0.0019</u></td></tr>
        <tr><td><strong>total_error</strong></td><td><strong>0.0026</strong></td><td>0.0116</td><td><u>0.0054</u></td></tr>
      </tbody>
    </table>
    <div style="margin-top:0.5em; font-size:0.95em; text-align:center; color:#444;">
      <strong>RRMSEs for <code>Tensile2d</code>.</strong>
    </div>
    <div style="margin-top:0.5em; font-size:0.95em; text-align:center; color:#444;">
      <strong>Best on each line is <b>bold</b>, 2nd best is <u>underlined</u>.</strong>
    </div>
  </div>
  <div style="flex: 1; min-width: 320px; display: flex; justify-content: center; align-items: center;">
    <img src="assets/results/mvt_mmvt_total_error_vs_patch_size.svg" alt="MVT" style="height:50vh; width:auto;">
  </div>
</div>


---

## Conclusions and future work

- MVT consistently strong results across all benchmarks.
- Much improvement over MGN.
- Regularity improvements (node ordering, morphing).

<br>

- Patch morphing.
- Improved decoder.

---

<br></br><br></br><br></br><br></br>
Thank you for your **attention** !





---

## Appendix
### Morton code

- <span style="color: tomato;"> $x$ : $x_{32}x_{31}...x_1x_0$ </span>
- <span style="color: mediumseagreen;"> $y$ : $y_{32}y_{31}...y_1y_0$ </span>
- morton code : <span style="color: tomato;"><span style="color: mediumseagreen;">$y_{32}$</span>$x_{32}$<span style="color: mediumseagreen;">$y_{31}$</span>$x_{31}$...<span style="color: mediumseagreen;">$y_1$</span>$x_1$<span style="color: mediumseagreen;">$y_0$</span>$x_0$</span>


`0.44s` for `10M` cells. 

---

## Appendix
### UNET

<div style="display: flex; justify-content: center;">
<img src="assets/models/unet.svg" alt="Sample Image">
</div>

---

## Appendix
### PLAID Article

<div style="display: flex; justify-content: center;">
  <img src="assets/plaid_article.png" style="width:80%; height:auto;">
</div>

