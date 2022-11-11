from deepstack_sdk import ServerConfig, Detection, SceneRecognition

if __name__ == '__main__':
    config = ServerConfig("http://localhost:80")
    detection = Detection(config)
    detec = SceneRecognition(config)

    response = detec.recognizeScene("input_images/crowd.jpg")
    print(response)
    #for obj in response:
    #    print("Name: {}, Confidence: {}, x_min: {}, y_min: {}, x_max: {}, y_max: {}".format(obj.label, obj.confidence,
                                                                            #                obj.x_min, obj.y_min,
                                                                             #               obj.x_max, obj.y_max))
