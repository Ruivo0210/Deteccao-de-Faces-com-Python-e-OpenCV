import cv2

classificador = cv2.CascadeClassifier('cascades\cars.xml') 

imagem = cv2.imread('outros/carro3.jpg')
imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetectadas = classificador.detectMultiScale(imagemcinza, scaleFactor=1.01, minNeighbors = 4, minSize=(20,20))
print(len(facesDetectadas))
print(facesDetectadas)

for (x,y,l,a) in facesDetectadas:
    print(x,y,l,a)
    cv2.rectangle(imagem, (x,y), (x+l, y+a), (0,0,255),2)
    if (l >50 or a> 50):
        print ("Fora do padrão")

cv2.imshow("carros encontrados", imagem)
cv2.waitKey()