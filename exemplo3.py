import cv2 #Neste exemplo, queremos identificar faces com base na imagem capturada pela nossa webcam em tempo real.

video = cv2.VideoCapture(0) #Para isso, utilizamos a ferramenta VideoCapture do OpenCV , que consegue acessar a imagem da webcam e atribuir a uma variável. Aqui, definimos a webcam 0, ou seja, a padrão.
classificadorFace = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

while True:
    conectado, frame = video.read() # Definimos um loop para realizar a leitura da imagem da webcam, em seguida definimos a janela de visualização para ela e definimos que a janela feche ao apertarmos a tecla "Q".
    #print(conectado) # Nos exibe se a camera está conectada
    #print(frame) # Nos retorna as informações de leitura da imagem atual

    frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificadorFace.detectMultiScale(frameCinza)
    for (x,y,l,a) in facesDetectadas:
        cv2.rectangle(frame,(x,y),(x+l,y+a),(0,0,255),2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

video.release() #Ao sairmos com a tecla Q, o software para de capturar a imagem.
cv2.destroyAllWindows()