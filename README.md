# YOLOv9-LicensePlateDetect

## Overview
This project aims to develop a robust license plate detection system using computer vision techniques and deep learning models. The system will be capable of accurately detecting license plates in images or video streams, providing a valuable tool for various applications such as vehicle tracking, parking management, and law enforcement.

## Features

- License Plate Localization: Utilizes state-of-the-art object detection algorithms to precisely locate license plates within images or video frames.
- Character Recognition: Implements optical character recognition (OCR) techniques to extract text from detected license plates. 
- Real-time Processing: Designed for real-time processing, enabling fast and efficient detection of license plates in live video streams. 
- Scalability: Built with scalability in mind, allowing easy integration with existing systems and adaptation to different environments and scenarios.
- Customizable: Provides options for fine-tuning parameters and adapting the system to specific use cases or requirements
- User-friendly Interface: Offers a user-friendly interface for easy interaction and integration into other projects or applications.


## Deployment

To deploy this project copy the Github Repo

```bash
  git clone https://github.com/btwitssayan/YOLOv9-LicensePlateDetect.git
```

## Installation

Install all requirments by running `requirements.txt` file

```bash
  pip install -r requirements.txt
```

## Run Locally

Clone the project

```bash
   git clone https://github.com/btwitssayan/YOLOv9-LicensePlateDetect.git
```

Go to the project directory

```bash
  cd YOLOv9-LicensePlateDetect
```

Install dependencies

```bash
  pip install -r requirements.txt
```

run `main.py`

```bash
  python main.py
```

then run `add_missing_data.py` to get the missing frames

```bash
  python add_missing_data.py
```
then run `visualize.py` to get the video output

```bash
  python visualize.py
```


## Documentation

[Yolov9](https://docs.ultralytics.com/models/yolov9/)

[Bytetrack](https://console.cloud.google.com/vertex-ai/publishers/ifzhang/model-garden/bytetrack-multi-object-tracking?pli=1)

[easyocr](https://pypi.org/project/easyocr/1.1.4/)

## Contributing

Contributions are always welcome!

If you have ideas for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request. Let's collaborate to make this project even better!

## Feedback

If you have any feedback, please reach out to us at sayangolder2004@gmail.com

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

This project is licensed under the MIT License, allowing you to use, modify, and distribute the code for both commercial and non-commercial purposes. See the LICENSE file for more details.
