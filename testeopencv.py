import cv2 #Importando a biblioteca OpenCv

print(cv2.__version__) #Comando utilizado para exibir a versão do OpenCV

imagem = cv2.imread('opencv-python.jpg') #Aqui, utilizamos o comando imread para o OpenCV fazer a leitura da imagem e a atribuir em uma variável.
imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) #Estamos utilizando o comando cvtColor para converter a coloração da imagem original para a escala de cinza.
cv2.imshow("Logo", imagem) #Utilizamos este comando para poder exibir a imagem na nossa tela, dentro damos o parâmetro do nome da janela e a variável da imagem a ser exibida.
cv2.imshow("Logo Cinza", imagemcinza) #Utilizamos este comando para poder exibir a imagem na nossa tela, dentro damos o parâmetro do nome da janela e a variável da imagem a ser exibida.
cv2.waitKey() #Comando utilizado para fechar a janela somente ao pressionarmos alguma tecla.
