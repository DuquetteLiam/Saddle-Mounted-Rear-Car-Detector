# This file is a modified version of the original detection script found in the picamera2 library at https://github.com/raspberrypi/picamera2/blob/main/examples/imx500/imx500_object_detection_demo.py
# I removed the argument parsing and replaced it with hardcoded values and removed preview functionality because the pi is running in headless mode
import sys
from functools import lru_cache

import cv2

from picamera2 import MappedArray, Picamera2
from picamera2.devices import IMX500
from picamera2.devices.imx500 import NetworkIntrinsics, postprocess_nanodet_detection

last_detections = []

# Constants
MODEL_PATH = "/usr/share/imx500-models/imx500_network_nanodet_plus_416x416_pp.rpk"
THRESHOLD = 0.50
IOU = 0.65
MAX_DETECTIONS = 5
LABELS_PATH = None        # or "/path/to/labels.txt"
PRINT_INTRINSICS = False


class Detection:
    def __init__(self, coords, category, conf, metadata):
        """Create a Detection object, recording the bounding box, category and confidence."""
        self.category = category
        self.conf = conf
        self.box = imx500.convert_inference_coords(coords, metadata, picam2)


def parse_detections(metadata: dict):
    """Parse the output tensor into a number of detected objects, scaled to the ISP output."""
    global last_detections
    bbox_normalization = intrinsics.bbox_normalization
    bbox_order = intrinsics.bbox_order
    threshold = THRESHOLD
    iou = IOU
    max_detections = MAX_DETECTIONS

    np_outputs = imx500.get_outputs(metadata, add_batch=True)
    input_w, input_h = imx500.get_input_size()
    if np_outputs is None:
        return last_detections
    if intrinsics.postprocess == "nanodet":
        boxes, scores, classes = postprocess_nanodet_detection(
            outputs=np_outputs[0], conf=threshold, iou_thres=iou, max_out_dets=max_detections
        )[0]
        from picamera2.devices.imx500.postprocess import scale_boxes

        boxes = scale_boxes(boxes, 1, 1, input_h, input_w, False, False)
    else:
        boxes, scores, classes = np_outputs[0][0], np_outputs[1][0], np_outputs[2][0]
        if bbox_normalization:
            boxes = boxes / input_h

        if bbox_order == "xy":
            boxes = boxes[:, [1, 0, 3, 2]]

    last_detections = [
        Detection(box, category, score, metadata) for box, score, category in zip(boxes, scores, classes) if score > threshold
    ]
    return last_detections


@lru_cache
def get_labels():
    labels = intrinsics.labels

    if intrinsics.ignore_dash_labels:
        labels = [label for label in labels if label and label != "-"]
    return labels

def detect(results):     
        for detection in results:
            class_name = labels[int(detection.category)]
            confidence = detection.conf
            #filter out non-vehicle detections
            if class_name in ["car", "truck", "bus", "motorcycle"]:
                print(f"Detected: {class_name} (confidence: {confidence:.2f})")
                return [class_name, confidence]
            
def capture_result():
    return parse_detections(picam2.capture_metadata())


if __name__ == "__main__":

    # This must be called before instantiation of Picamera2
    imx500 = IMX500(MODEL_PATH)
    intrinsics = imx500.network_intrinsics
    if not intrinsics:
        intrinsics = NetworkIntrinsics()
        intrinsics.task = "object detection"

    elif intrinsics.task != "object detection":
        print("Network is not an object detection task", file=sys.stderr)
        exit()

    # Optional: load a custom labels file if provided
    if LABELS_PATH:
        with open(LABELS_PATH, "r") as f:
            intrinsics.labels = f.read().splitlines()

    # Defaults and sanity
    if intrinsics.labels is None:
        with open("assets/coco_labels.txt", "r") as f:
            intrinsics.labels = f.read().splitlines()
    intrinsics.update_with_defaults()

    if PRINT_INTRINSICS:
        print(intrinsics)
        exit()


    picam2 = Picamera2(imx500.camera_num)
    config = picam2.create_preview_configuration(controls={"FrameRate": intrinsics.inference_rate}, buffer_count=12)

    imx500.show_network_fw_progress_bar()
    picam2.start(config, show_preview=False)

    if intrinsics.preserve_aspect_ratio:
        imx500.set_auto_aspect_ratio()

    last_results = None

    labels = get_labels()
    last_results = parse_detections(picam2.capture_metadata())
    
                   
    

    while True:
        detection = detect(last_results)