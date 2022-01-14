# face_recognition_system

L’objectif de ce travail est d’implémenter une application de reconnaissance et
d’authentification faciale en temps réel des étudiants du Master WISD.

Au cours de ce travail, on a réussi à implémenté deux approches de reconnaissance
facial, l’une se base sur la méthode de FaceNet et l’autre sur la méthode de VGG16 afin de
comparer les résultats entre ces deux méthodes. Les deux approches implémentées sont
basées sur le modèle MTCNN pour la détection des visages et leurs alignements.
Les raisons de tous ces choix étaient grâce aux articles dans la littérature qui ont bien
démontré l’avantage de ces modèles par rapport à d’autres.

Le modèle FaceNet a présenté des bons résultats lors des tests par rapport a VGGFace,
Non seulement la précision de l'ensemble de données était la plus grande, mais elle était
également la plus proche des résultats publiés par les auteurs du réseau, ce qui ajoute à la
confiance que l'expérience a été correctement configurée. La précision du réseau FaceNet
sur l’ensemble de données est prometteuse, compte tenu de la qualité inférieure et la
quantité des images utilisés. L'auteur suggère de considérer le réseau FaceNet comme un
point de départ pour d'autres travaux sur d'autres ensemble de données, qu'il s'agisse de
regrouper les données ou d'ajuster le réseau pour obtenir une meilleure précision. Le réseau
VGGFace ne doit pas non plus être exclu - le projet est toujours en développement et le
dernier résultat trouvé a montré une très grande amélioration de la précision pour détecter
les visages.

Ce travail peut être réalisé avec d’autre méthodes soit avec des approches basé sur le
Machine Learning ou bien des méthodes de DeepLearning autre que celles présenté dans ce
travail afin d’amélioré la détection des caractéristiques présenté dans le visage humain, dans
le but d’avoir des résultats plus intéressants
