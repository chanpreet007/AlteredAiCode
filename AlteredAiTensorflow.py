from .AlteredAiDataLoader import AlteredAiDataLoader
from .DataTransformations import DataTransformations

class AlteredAiTensorflow(AlteredAiDataLoader):
    def __init__(self):
        print("AlteredAiTensorflow Loaded Successfully")

    def funTensorflow(self):
        print("This is function from Tensorflow Class")
