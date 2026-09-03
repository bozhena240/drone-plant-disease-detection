# Drone-Based Plant Disease Detection

A proof-of-concept computer vision project for detecting agricultural plant diseases using YOLO. 

The model was trained on a dataset of infected plant leaves and achieved an 85.6% mAP. To prepare the model for deployment on lightweight drone hardware (like a Raspberry Pi), the PyTorch weights have been exported to the ONNX format.

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
