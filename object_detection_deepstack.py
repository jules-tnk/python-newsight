from sound import say
import requests
import time
import cv2


def object_recognition(img_path):
    # deepstack --VISION-SCENE True --PORT 80
    image_data = open(img_path, "rb").read()

    # Send the request and retrieve the response
    response = requests.post("http://localhost:80/v1/vision/detection", files={"image": image_data}).json()
    detected_objects = [obj for obj in response["predictions"]]
    for obj in detected_objects:
        print(obj)


if __name__ == '__main__':
    object_recognition("input_images/crowd.jpg")