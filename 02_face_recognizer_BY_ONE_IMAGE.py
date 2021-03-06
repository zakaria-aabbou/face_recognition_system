from scipy.spatial.distance import cosine
import mtcnn , cv2
from keras.models import load_model
from utils import *
from face_alignment_func import align
import matplotlib.pyplot as plt

def recognize(img,
              detector,
              encoder,
              encoding_dict,
              recognition_t=0.5,
              confidence_t=0.99,
              required_size=(160, 160), ):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = detector.detect_faces(img_rgb)
    for res in results:
        if res['confidence'] < confidence_t:
            continue
        l_e = res['keypoints']['left_eye']
        r_e = res['keypoints']['right_eye']
        face = align(img_rgb, l_e, r_e, required_size)
        _, pt_1, pt_2 = get_face(img_rgb, res['box'])
        encode = get_encode(encoder, face, required_size)
        encode = l2_normalizer.transform(encode.reshape(1, -1))[0]
        name = 'unknown'

        distance = float("inf")
        for db_name, db_encode in encoding_dict.items():
            dist = cosine(db_encode, encode)
            if dist < recognition_t and dist < distance:
                name = db_name
                distance = dist
                proba    = (1-dist)*100

        if name == 'unknown':
            cv2.rectangle(img, pt_1, pt_2, (0, 0, 255), 2)
            cv2.putText(img, name, pt_1, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        else:
            cv2.rectangle(img, pt_1, pt_2, (0, 255, 0), 2)
            cv2.putText(img, name + f' {proba:.2f}%', (pt_1[0], pt_1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 3)
    return img

def plot(img):
    plt.figure(figsize=(8, 4))
    plt.imshow(img[:, :, ::-1])
    plt.show()


if __name__ == '__main__':
    encoder_model  = 'data/model/facenet_keras.h5'
    encodings_path = 'data/encodings/encodings.pkl'

    face_detector  = mtcnn.MTCNN()
    face_encoder   = load_model(encoder_model)
    encoding_dict  = load_pickle(encodings_path)

    image = cv2.imread('data/One_image/TEST.jpg')
    frame = recognize(image, face_detector, face_encoder, encoding_dict)
    cv2.imwrite('data/One_image/results.jpg',image)
    print("Image predicted!")
    plot(image)
    #cv2.imshow('camera', image)

