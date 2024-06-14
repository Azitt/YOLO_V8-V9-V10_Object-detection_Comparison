## Overview

This repository contains a study comparing the performance of YOLOv8, YOLOv9, and YOLOv10 on object detection task. The focus is on evaluating the models' performance in terms of accuracy, speed, and model parameters.

## Model Inference Video

![Model Inference](results/output.gif)
![Model Inference](results/output_v8m.gif)

# Comparison results

To compare these models, I used YOLOv8n and YOLOv8m, YOLOv9c, YOLOv10n, and YOLOv10m. The reason for comparing the medium-sized models is that there is only YOLOv9c pretrained weight available, and the size of this model is similar to the medium-sized YOLOv8 and YOLOv10 models. The table below shows the comparison results.

## Objectives

- Compare the accuracy of YOLOv8, YOLOv9, and YOLOv10.
- Evaluate the inference speed and computational requirements of each model.
- Analyze the models' performance on different types of datasets, with a focus on traffic/vehicle detection.

## Repository Structure

- `data/`: Contains the datasets used for training and evaluation.
- `models/`: Contains model configurations and weights for YOLOv8, YOLOv9, and YOLOv10.
- `scripts/`: Python scripts for training, evaluation, and utility functions.
- `results/`: Stores the results of the comparison study.

## Datasets

For comparison and training, I used two datasets from Kaggle:
- [Dataset 1 Name](https://www.kaggle.com/datasets/farzadnekouei/top-view-vehicle-detection-image-dataset)
- [Dataset 2 Name](https://www.kaggle.com/datasets/javiersanchezsoriano/roundabout-aerial-images-for-vehicle-detection/code)


### Prerequisites

- Python 3.8 or higher
- PyTorch
- Other dependencies listed in `requirements.txt`