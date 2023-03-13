from detector.config import Config
from detector.model import MaskRCNN
from detector.class_names import CLASS_NAMES
import os

class TacoInferenceConfig(Config):
   NAME = "taco_inference"
   GPU_COUNT = 1
   IMAGES_PER_GPU = 1
   DETECTION_MIN_CONFIDENCE = 10
   NUM_CLASSES = len(CLASS_NAMES)

def build_model():
   model =  MaskRCNN(mode="inference",
                config=TacoInferenceConfig(),
                model_dir=os.getcwd())

   model.load_weights(weights_in_path="detector/models/mask_rcnn_taco_0100.h5",
                  weights_out_path="detector/models/mask_rcnn_taco_0100.h5",
                  by_name=True)
   return model
