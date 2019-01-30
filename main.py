import time
from pathlib import Path
import cv2
import numpy as np
from fastai.basic_train import load_learner
from fastai.vision.image import open_image

font = cv2.FONT_HERSHEY_SIMPLEX

weights = 'export.pkl'
path = Path(__file__).parent


classes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z', 'del', 'nothing', 'space']

learn = load_learner(path / 'models/', weights)


def detect():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        temp = frame[20:220, 20:220]

        cv2.imwrite('test1.jpg', temp)
        img = open_image(path / 'test1.jpg')
        result = learn.predict(img)
        index = result[1]
        probabilities = result[2]

        cv2.rectangle(frame, (20, 20), (200, 200), (0, 0, 0), 2);
        cv2.putText(frame, str(result[0]) + " " + str(np.around(probabilities[index].numpy(), 3)), (30, 240), font, 1,
                    (0, 0, 0),
                    1,
                    cv2.LINE_AA)

        cv2.imshow('FRAME', frame)
        if cv2.waitKey(1) == ord('q'):
            break
        time.sleep(0.1)

    cap.release()
    cv2.destroyAllWindows()


detect()

