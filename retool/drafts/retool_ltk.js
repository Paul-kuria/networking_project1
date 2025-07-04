const currentModelJson = {
  "general": {
    "area_calc_unit": "area",
    "detection_process_type": "instance_segmentation",
    "detection_model_architecture": "yolo",
    "download": false
  },
  "yolodetector": {
    "rotate": false,
    "model_weights_path": "./RoseDetectionModel_Enhanced_2025_05_17.pt",
    "detections_number": 1000,
    "conf": 0.4,
    "agnostic_nms": true,
    "iou": 0.2,
    "tta_augment": false,
    "use_sahi": false,
    "sahi_scale": 4,
    "sahi_detections": 40,
    "resize_factor": 2
  },
  "yoloclassifier": {
    "model_weights_path": ""
  },
  "visualization": {
    "rotate": false,
    "show_masks": true,
    "show_boxes": true,
    "show_labels": false,
    "show_conf": false,
    "show_area_calculation": true,
    "line_width": 3
  },
  "yolotraining": {
    "model": "yolo11m",
    "epochs": 200,
    "imgsz": 640,
    "batch": 8,
    "name": "experiment_1",
    "optimizer": "SGD",
    "lr0": 0.001,
    "momentum": 0.9,
    "weight_decay": 0.001,
    "patience": 20,
    "warmup_epochs": 5,
    "augmentation": {
      "hsv_h": 0.01,
      "hsv_s": 0.7,
      "hsv_v": 0.4,
      "flipud": 0.2,
      "fliplr": 0.5,
      "degrees": 5,
      "translate": 0.2,
      "scale": 0.5,
      "shear": 2,
      "perspective": 0.0003,
      "mosaic": 0.5,
      "mixup": 0,
      "copy_paste": 0
    },
    "lrf": 0.01,
    "cos_lr": true,
    "dropout": 0.2,
    "multi_scale": true,
    "auto_train": false,
    "max_runs": 10,
    "max_map": 0.97
  }
}

{{ configSelect.selectedItem.settings }};

// copy of json to avoid mutating the original fetched data directly 
const updatedModelJson = {...currentModelJson};

// override values from input components
updatedModelJson.yolodetector.conf = {{ confidenceLevelInput.value }}

return updatedModelJson
