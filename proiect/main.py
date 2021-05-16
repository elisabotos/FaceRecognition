import cv2
import sys

##### Variabile globale #####
# Introduce imaginea data de utilizator in variabila
imagePath = sys.argv[1]

# Citirea imaginii
image = cv2.imread(imagePath)
# Conversia imaginii in gri
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#############################

##### Functii locale ######
def detectare_fete(gray):
    cascPath = sys.argv[2]
    # Creare haar cascade - algoritm de machine learning de detectie a obiectelor
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Detectarea fetelor din imagine
    face = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )
    return face

def afisare_numar_total_de_fete(faces):
    print("S-au gasit {0} fete!".format(len(faces)))

# Desenare dreptunghi in jurul fetelor + salvarea acestora
def desenare_salvare(faces,image):
    counter = 0
    for (x, y, w, h) in faces:
        counter = counter+1
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 200, 255), 2)
        faces = image[y:y + h, x:x + w]
        cv2.imshow("face-%d" % counter, faces)
        cv2.imwrite('face-%d.jpg' % counter, faces)

    cv2.imshow("Faces found", image)
    cv2.waitKey(0)
###############################

faces = detectare_fete(gray)

def functie1():
    afisare_numar_total_de_fete(faces)

def functie2():
    # Desenare dreptunghi in jurul fetelor + salvarea acestora
    desenare_salvare(faces, image)

if __name__ == '__main__':

    functie1()
    functie2()