# Plant Disease Detection Using Deep Learning

This project aims to address the need for early and accurate detection of plant diseases, which significantly impact agricultural productivity and sustainability. Using advanced computer vision and deep learning techniques, we developed a system capable of classifying plant diseases from images with high reliability and scalability.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Preprocessing Techniques](#preprocessing-techniques)
- [Modeling Approaches](#modeling-approaches)
- [Results](#results)
- [Future Enhancements](#future-enhancements)
- [References](#references)

---

## Project Overview

The primary goal of this project is to preprocess plant images and utilize state-of-the-art neural networks for disease classification. We explored custom models and transfer learning (VGG16) to achieve robust and scalable solutions for automated plant disease detection. The system aims to improve agricultural outcomes by enabling prompt intervention.

---

## Dataset

The dataset consists of images representing 38 distinct plant disease categories, including healthy and infected plants. The data was split into training and validation sets, ensuring a balanced distribution across classes.

---

## Preprocessing Techniques

To improve the model's performance, we implemented several image preprocessing techniques:

1. **Image Transformation**: Highlighted infected areas using color-based segmentation and edge detection.
2. **Histogram Equalization**: Enhanced image contrast to make important features more distinguishable.
3. **Shadow Removal**: Reduced shadows to enhance uniformity.
4. **Intrinsic Image Processing**: Separated object colors from illumination for consistent analysis.

While preprocessing improved image quality, it had mixed effects on model accuracy.

---

## Modeling Approaches

We experimented with two main modeling approaches:

1. **Custom Deep Convolutional Neural Network (CNN)**:
   - Five convolutional blocks with progressively increasing filters (32 to 512).
   - Dropout layers to reduce overfitting.
   - Achieved an accuracy of **97.35%**.

2. **VGG16 (Transfer Learning)**:
   - Fine-tuned a pretrained VGG16 model for plant disease classification.
   - Achieved an accuracy of **89.23%**.

---

## Results

- **Custom CNN**: Delivered superior performance with a balanced approach to feature extraction and computational efficiency.
- **VGG16**: Demonstrated moderate accuracy but required more resources for training.

Data augmentation techniques such as flipping, rotating, and brightness adjustment were crucial in enhancing model robustness.

---

## Future Enhancements

1. **Improved Preprocessing**:
   - Advanced segmentation techniques (e.g., semantic segmentation) to isolate plant-specific features.
   - Adaptive histogram equalization for better contrast management.

2. **Object Detection**:
   - Implement YOLO-based object detection to isolate plants and remove background noise.

3. **Scalability**:
   - Expand the system for real-time detection in diverse agricultural settings.

---

## References

1. Bagga, M., & Goyal, S. (2024). *Image-based detection and classification of plant diseases using deep learning*. Urban Agriculture & Regional Food Systems, 9(1), e20053.
2. Eunice, J., et al. (2022). *Deep learning-based leaf disease detection in crops*. Agronomy, 12(10), 2395.
3. Geetharamani, G., & Pandian, A. (2019). *Identification of plant leaf diseases using a nine-layer deep convolutional neural network*. Computers & Electrical Engineering, 76, 323-338.
4. Roy, A. M., & Bhaduri, J. (2021). *A deep learning enabled multi-class plant disease detection model based on computer vision*. AI, 2(3), 413-428.

