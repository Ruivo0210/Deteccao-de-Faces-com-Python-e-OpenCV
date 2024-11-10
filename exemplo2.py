import cv2

classificadorFace = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
classificadorOlhos = cv2.CascadeClassifier('cascades/haarcascade_eye.xml') #Neste segundo exemplo, desejamos detectar rostos e olhos na foto. Para isso, adicionamos um segundo classificador para os olhos.

imagem = cv2.imread('pessoas/faceolho.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetectadas = classificadorFace.detectMultiScale(imagemCinza)

for(x,y,l,a) in facesDetectadas:
    imagem = cv2.rectangle(imagem,(x,y),(x+l, y+a),(0,0,2005),2)
    regiao = imagem[y:y + a, x:x + l] #Aqui, definimos a imagem para somente a parte que foi detectada da face
    regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY) #Convertemos a matriz dos olhos para a escala de cinza
    olhosDetectados = classificadorOlhos.detectMultiScale(regiaoCinzaOlho) #E em seguida, utilizamos o classificador para detectar os olhos.
    print(olhosDetectados)
    for(ox, oy, ol, oa) in olhosDetectados: #Agora vamos desenhar os quadrados dos olhos
        cv2.rectangle(regiao,(ox,oy),(ox+ol,oy+oa),(0,0,255),2)

cv2.imshow("Faces e olhos detectados", imagem)
cv2.waitKey()