# Steel Surface Defect Detection with YOLOv8

## Overview
A YOLOv8s object detection model that finds and labels six types of steel surface defects in images from the NEU surface defect database.

I built this as a personal project before my 2026 summer internships, to see how computer vision could be used in steel quality inspection. It was trained and evaluated on a small benchmark dataset. It has not been tested on images from a real production line.

## Dataset
| Property | Value |
|----------|-------|
| Source | NEU surface defect database, detection version (NEU-DET), Northeastern University |
| Classes | 6 (crazing, inclusion, patches, pitted_surface, rolled-in_scale, scratches) |
| Total images | 1,800 (300 per class) |
| Split | 70% train / 20% validation / 10% test |

The split was created in Google Colab. The script that created it is not in this repository, so the exact split cannot be reproduced from here. The dataset images are not included in this repository.

## Training
- Model: YOLOv8s, starting from the pretrained `yolov8s.pt` weights
- Epochs: 100 (early stopping patience: 20; training ran all 100 epochs)
- Image size: 640×640, batch size 16
- Framework: Ultralytics 8.4.46, trained on Google Colab
- Script: [`train.py`](train.py), dataset config: [`data.yaml`](data.yaml) (paths point to the Colab environment and need to be changed to run elsewhere)

## Results
These are the validation metrics saved in the training history of the published weights (`best.pt` on Hugging Face, the same file the demo loads). They were recorded during training. They are not a separate re-evaluation.

| Metric (validation split, epoch 98 of 100) | Value |
|--------------------------------------------|-------|
| mAP50 | 0.769 |
| mAP50-95 | 0.436 |
| Precision | 0.742 |
| Recall | 0.715 |

Ultralytics keeps the epoch with the best mAP50-95 as `best.pt`, which here was epoch 98. Over the 100 epochs, validation mAP50 never went above 0.774.

The held-out test split has not been evaluated for these weights, and per-class results for them have not been exported.

**Other files in [`results/`](results/):** `results.txt` (mAP50 0.900) and the PR/F1 curves and confusion matrices come from a different Colab training or evaluation run. They do not match the training history of the published weights, and the run and data split they belong to could not be confirmed. They are kept for reference only and do not describe the demo model.

## Limitations
- Trained only on NEU images, which are small (200×200) grayscale images of steel strip surfaces. Performance on other steel products or on real production images is unknown.
- Only validation metrics recorded during training; no separate test-set evaluation yet.

## Demo
[![Hugging Face Spaces](https://img.shields.io/badge/🤗-Open%20in%20Spaces-blue)](https://huggingface.co/spaces/kirkdokizelli/steel-defect-detection)

Upload a steel surface image and the app shows the model's detections with confidence scores.

## Run Locally
The trained weights (`best.pt`) are not stored in this repository. Download them from the [Hugging Face model page](https://huggingface.co/kirkdokizelli/steel-defect-yolov8/tree/main) and place `best.pt` in the project folder, then:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Next Steps
- Evaluate the published weights on the held-out test split
- Export per-class results and plots for the published weights
- Train and compare on a larger dataset (e.g. Severstal)

## License
No license file has been added to this repository yet. Training and inference use [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics), which is distributed under AGPL-3.0; Ultralytics states that models trained with it are also covered by AGPL-3.0. If you use the NEU dataset, please cite its authors (Kechen Song, Yunhui Yan, Northeastern University).

## Links
- **Demo:** https://huggingface.co/spaces/kirkdokizelli/steel-defect-detection
- **Model weights:** https://huggingface.co/kirkdokizelli/steel-defect-yolov8
- **GitHub:** https://github.com/kirkdokizelli-pixel/steel-defect-detection

---
*Kutay Kaya, Metallurgical and Materials Engineering, Yıldız Technical University*
