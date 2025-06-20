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
    <img src="assets/logos/safran_white.svg" alt="Safran Logo" style="height: 50px;">
    <img src="assets/logos/epfl.svg" alt="EPFL Logo" style="height: 50px;">
</div>


<div style="position: absolute; bottom: 1em; right: 1em; font-size: 0.9em; color: #666;">
    20 June 2025
</div>

---

## Physics Mesh Regression Problem

<img src="assets/mesh_field_regression_export.svg" style="width: 100%; height: auto;">

---

## Vi-Transformers

<img src="assets/ViT.svg" alt="ViT Diagram" style="width: 100%; height: auto;">

Morphing?

---

### Morphing?

<div style="display: flex; justify-content: center; align-items: center; gap: 50px;">
<img src="assets/morphing/patch.png" alt="ViT Diagram" style="width: auto; height: auto;">
<img src="assets/morphing/morphed_patch.png" alt="ViT Diagram" style="width: auto; height: auto;">
</div>

---

## Regular Images grid

<img src="assets/physicsimage/features.png" alt="ViT Diagram" style="width: auto; height: 70%;">

<img src="assets/logos/MuscatLogo.svg" style="height: 50px; vertical-align: middle">  Powerful Mesh processing with Muscat

---

## Unet 1/2

<div style="display: flex; justify-content: center; align-items: center; gap: 50px;">
<img src="assets/physicsimage/unet_img.svg" alt="Unet results" style="width: auto; height: 70%">
</div>
---

## Unet 2/2

<img src="assets/physicsimage/unet_results.png">
<div style="font-size: 0.8em; font-style: italic; color: #aaa; margin-top: 0.5em;">
Unet
</div>

---

## ViT with 2D patch PE

<img src="assets/physicsimage/vit_pe.png" alt="Unet results" style="width: auto; height: 70%;">
<div style="font-size: 0.8em; font-style: italic; color: #aaa; margin-top: 0.5em;">
ViT with PE
</div>

---

## ViT without 2D patch PE

<img src="assets/physicsimage/vit_pe_less.png" alt="Unet results" style="width: auto; height: 70%;">
<div style="font-size: 0.8em; font-style: italic; color: #aaa; margin-top: 0.5em;">
ViT without PE
</div>

---

## Pre-training MAE ViT 1/2

<div style="justify-content: center; align-items: center; height: 1000px">
<img src="assets/physicsimage/vit_mae_architecture.png" alt="ViT Diagram">
<div style="font-size: 0.8em; font-style: italic; text-align: center; color: #aaa; margin-top: 0.5em;">
He et al., Masked Autoencoders Are Scalable Vision Learners, <a href="https://arxiv.org/abs/2111.06377" target="_blank">arXiv:2111.06377</a>
</div>
</div>

---

## Pre-training MAE ViT 2/2

<img src="assets/physicsimage/features.png" alt="ViT Diagram" style="width: auto; height: 70%;">
<div style="font-size: 0.8em; font-style: italic; color: #aaa; margin-top: 0.5em; margin-bottom: 2em">
Target
</div>


<img src="assets/physicsimage/vit_mae.png" alt="ViT Pretraining" style="width: 100%; height: auto;">
<div style="font-size: 0.8em; font-style: italic; color: #aaa; margin-top: 0.5em;">
Reconstruction
</div>

---

## <img src="assets/logos/MuscatLogo.svg" style="height: 50px; vertical-align: middle"> Encoding

<img src="assets/encode.svg" alt="ViT Diagram" style="width: 100%; height: auto;">

---

## <img src="assets/logos/MuscatLogo.svg" style="height: 50px; vertical-align: middle"> Decoding

<img src="assets/decode.svg" alt="ViT Diagram" style="width: 100%; height: auto;">

---

<br></br><br></br><br></br><br></br>
Thank you for your **attention** !


---

## References

He, K., Chen, X., Xie, S., Li, Y., Dollár, P., & Girshick, R. (2021).  
**Masked Autoencoders Are Scalable Vision Learners**.  
arXiv: [2111.06377](https://arxiv.org/abs/2111.06377)