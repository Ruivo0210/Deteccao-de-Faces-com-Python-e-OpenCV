import cv2

classificador = cv2.CascadeClassifier('cascades/cars.xml') #Aqui, atribuimos uma variável para o classificador XML. Este está treinado para reconhecer rostos.

imagem = cv2.imread('outros/carro1.jpg')
imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetectadas = classificador.detectMultiScale(imagemcinza, scaleFactor=1.1, minNeighbors = 8, minSize=(30,30)) #Este comando serve para fazermos a detecção na imagem baseado naquilo que o classificador é treinado.
print(len(facesDetectadas)) #Exibe a quantidade de itens detectados na imagem
print(facesDetectadas) #Exibe uma matriz de 4 valores identificando os pontos que formam um quadrado demarcando os itens encontrados

for (x,y,l,a) in facesDetectadas:
    print(x,y,l,a)
    cv2.rectangle(imagem, (x,y), (x+l, y+a), (0,0,255),2) #Este comando serve para demarcarmos um triangulo dentro dos itens detectados na imagem e visualizarmos ela. Atribuimos a imagem, as coordenadas do quadrado, a cor dele e a largura.

cv2.imshow("Carros encontrados", imagem)
cv2.waitKey()