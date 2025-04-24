---
customTheme : "my_theme"
center: false
slideNumber: true
transition: "None"
transitionSpeed: fast
controlsTutorial: false
---







# Vi-Transformers for Physical Field Prediction
## Anthony Kalaydjian  
<!-- [Safran Tech](https://www.safran-group.com/fr/groupe/innovation/safran-tech) - [EPFL](https://www.epfl.ch/fr/) -->



<div style="display: flex; justify-content: center; align-items: center; gap: 50px;">
    <img src="assets/logos/safran.svg" alt="Safran Logo" style="height: 50px;">
    <img src="assets/logos/epfl.svg" alt="EPFL Logo" style="height: 50px;">
</div>



<div style="position: absolute; bottom: 1em; right: 1em; font-size: 0.9em; color: #666;">
    25 April 2025
</div>

---

## Physics mesh regression problem

---

## PLAID standard



---

## PLAID benchmark (Datasets)

| Dataset                   | Simulation code | Model                                                                         | Nb samples | Volume Zenodo | Volume HF |
|---------------------------|-----------------|-------------------------------------------------------------------------------|------------|---------------|-----------|
| `Tensile2d`               | Z-set           | 2D quasistatic non-linear structural mechanics, small deformations, non-linear constitutive law | 702        | 290 MB        | 1.0 GB    |
| `2D_MultiScHypEl`         | DOLFINx         | 2D quasistatic non-linear structural mechanics, finite elasticity             | 1,140      | 350 MB        | 1.1 GB    |
| `2D_ElPlDynamics`         | OpenRadioss     | 2D dynamic non-linear structural mechanics, non-linear non-local constitutive law | 1,018      | 5.7 GB        | 18 GB     |
| `Rotor37`                 | elsA            | 3D Navier-Stokes (RANS)                                                       | 1,200      | 3.3 GB        | 13 GB     |
| `2D_profile`              | elsA            | 2D Navier-Stokes (RANS)                                                       | 400        | 660 MB        | 2.9 GB    |
| `VKI-LS59`                | BROADCAST       | 2D Navier-Stokes (RANS)                                                       | 839        | 1.9 GB        | 7.4 GB    |
| `AirfRANS original`       | OpenFOAM        | 2D Navier-Stokes (RANS)                                                       | 1,000      | 9.3 GB        | 24 GB     |
| `AirfRANS clipped`        | OpenFOAM        | 2D Navier-Stokes (RANS)                                                       | 1,000      | 9.7 GB        | 26 GB     |
| `AirfRANS remeshed`       | OpenFOAM        | 2D Navier-Stokes (RANS)                                                       | 1,000      | 520 MB        | 2.1 GB    |


---

<h2 style="
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  font-size: 1.5em;
  text-align: center;
  margin: 0;
  padding: 0.5em 0;
  background-color: var(--bg);
  color: var(--fg);
  z-index: 9999;
">
  PLAID benchmark (Problems of interest) 1/2
</h2>


| Dataset                | Mesh (mean nodes) | Inputs         | Outputs            | Splits (train/test)  |
|------------------------|-------------------|----------------|--------------------|----------------------|
| `Tensile2d`            | tri (9,428)       | mesh, 6 scalars| 4 scalars, 6 fields| 500 / 200            |
| `2D_MultiScHypEl`      | tri (5,692)       | mesh, 3 scalars| 1 scalar, 7 fields | 764 / 376            |
| `Rotor37`              | quad (29,773*)    | mesh, 2 scalars| 4 scalars, 3 fields| 1,000 / 200          |
| `2D_profile`           | tri (37,042)      | mesh           | 4 fields           | 300 / 100            |
| `VKI-LS59`             | quad (36,421*)    | mesh, 2 scalars| 6 scalars, 7 fields| 671 / 168            |

---

## PLAID benchmark (Problems of interest) 2/2

<img src="assets/samples.png" alt="Sample Image" style="width: 100%; height: auto;">

---

## PLAID benchmark evaluation metrics


$
\begin{equation}
x = 5
\end{equation}
$

$$
\mathrm{RRMSE}_f(\mathbf{f})
$$


Here’s the reference version: `$ \mathrm{RRMSE}_f(\mathbf{f}_{\rm ref}) $`



$$
\begin{equation}
\mathrm{RRMSE}_f(\mathbf{f}_{\rm ref}, \mathbf{f}_{\rm pred}) = \left( \frac{1}{n_\star}\sum_{i=1}^{n_\star} \frac{\frac{1}{N^i}\|\mathbf{f}^i_{\rm ref} - \mathbf{f}^i_{\rm pred}\|_2^2}{\|\mathbf{f}^i_{\rm ref}\|_\infty^2} \right)^{1/2}
\end{equation}
$$


---

## Vi-Transformers

---

### Padding

<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
<img src="assets/padding_2d.png" alt="2D Grid" style="width: 45%; height: auto;">
</div>

---

### 2D Patch serialization
+ Have a non random ordering of the vertices within a patch
+ Compare patches together


<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
    <img src="assets/morton/2d_grid.png" alt="2D Grid" style="width: 45%; height: auto;">
    <img src="assets/morton/2d_pointcloud.png" alt="2D Point Cloud" style="width: 45%; height: auto;">
</div>

---

#### Morton code

- <span style="color: tomato;"> $x$ : $x_{32}x_{31}...x_1x_0$ </span>
- <span style="color: mediumseagreen;"> $y$ : $y_{32}y_{31}...y_1y_0$ </span>
- morton code : <span style="color: tomato;"><span style="color: mediumseagreen;">$y_{32}$</span>$x_{32}$<span style="color: mediumseagreen;">$y_{31}$</span>$x_{31}$...<span style="color: mediumseagreen;">$y_1$</span>$x_1$<span style="color: mediumseagreen;">$y_0$</span>$x_0$</span>

<pre><code data-trim class="language-python">
    def splitBy2(n: int):
        n = n               & 0x00000000FFFFFFFF
        n = (n | (n << 16)) & 0x0000FFFF0000FFFF
        n = (n | (n << 8))  & 0x00FF00FF00FF00FF
        n = (n | (n << 4))  & 0x0F0F0F0F0F0F0F0F
        n = (n | (n << 2))  & 0x3333333333333333
        n = (n | (n << 1))  & 0x5555555555555555
        return n
</code></pre>

```python
splitBy2(5) #5 = 101
>>> 010001
```

```python
morton(x, y) = splitBy2(x) | splitBy2(y) << 1
```

`0.22s` for `10M` integers 


---

### 3D Patch serialization
<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
    <iframe src="assets/morton/3d_grid.html" style="width: 1200px; height: 400px; border: none; font-size: 0.01em;"></iframe>
    <iframe src="assets/morton/3d_pointcloud.html" style="width: 1200px; height: 400px; border: none; font-size: 0.01em;"></iframe>
    </div>

---

## First benchmark results