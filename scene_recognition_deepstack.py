from sound import say
import requests
import time
import cv2

live_frame_count = 1


def scene_recognition(img_path):
    # deepstack --VISION-SCENE True --PORT 80
    image_data = open(img_path, "rb").read()
    # image_data = os.path.join(execution_path, "input_images/crowd.jpg")

    # Send the request and retrieve the response
    response = requests.post("http://localhost:80/v1/vision/scene", files={"image": image_data}).json()
    identified_scene = response['label']


    # set and launch the audio output
    #audio_output = f"environnement: {identified_scene}"
    #say(audio_output, 'fr')
    # print("Label:", response["label"])
    print(response)


def live_scene_recognition():
    global detector, execution_path, live_frame_count
    capture = cv2.VideoCapture(0)
    while True:
        isValid, camera_img = capture.read()
        if isValid:
            cv2.imshow('Camera', camera_img)
            img_path = f"input_images/{live_frame_count}.jpg"  # save each frame

            # save the image for each iteration
            cv2.imwrite(img_path, camera_img)
            live_frame_count += 1

            # analyze the image saved for each iteration
            scene_recognition(img_path)
            time.sleep(3)
        else:
            print('erreur image')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    scene_recognition("input_images/crowd.jpg")
