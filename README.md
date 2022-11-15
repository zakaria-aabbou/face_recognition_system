# face_recognition_system

The objective of this work is to implement a real-time facial recognition and authentication application for WISD Masters students.

During this work, we successfully implemented two facial recognition approaches, one based on the FaceNet method and the other on the VGG16 method in order to compare the results between these two methods. The two implemented approaches are based on the MTCNN model for the detection of faces and their alignments.

The reasons for all these choices were due to articles in the literature which clearly demonstrated the advantage of these models over others.

The FaceNet model performed well when tested against VGGFace, not only was the accuracy of the dataset the greatest, but it was also the closest to the results published by the authors of the network, which adds trust that the experience has been set up correctly. The accuracy of the FaceNet network on the dataset is promising, given the inferior quality and quantity of images used. The author suggests considering the FaceNet network as a starting point for further work on other datasets, whether it is aggregating the data or adjusting the network for better accuracy. The VGGFace network should not be excluded either - the project is still in development and the last result found showed a very big improvement in the accuracy of detecting faces.

This work can be carried out with other methods either with approaches based on Machine Learning or with Deep Learning methods other than those presented in this work in order to improve the detection of the characteristics presented in the human face.
