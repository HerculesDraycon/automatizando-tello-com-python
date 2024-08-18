# Automatizando o DJI Tello com Python
<img src="https://github.com/HerculesDraycon/automatizando-tello-com-python/blob/main/img/tello.jpg" width="717" heigth="358">

O projeto conta com algoritmos que foram desenvolvidos em Python3 para controlar o drone DJI Tello a partir do computador e alguns processos de automação que utilizam a camera e sensores do aparelho como ferramenta de fornecimento de dados que são processados e aproveitados no software.

## 📸 Projeto 1 - Vigilância
No arquivo [ImageCapture.py](https://github.com/HerculesDraycon/automatizando-tello-com-python/blob/main/control/ImageCapture.py) foi feito um algoritmo que controla o drone através do teclado do computador conectado (e que está executando o código Python) enquanto o drone simultaneamente está transmitindo a imagem capturada em sua câmera pela tela do computador. Ao pressionar a tecla de captura, uma foto é tirada e armazenada automaticamente no diretório de imagem em formato jpg com um título singular (baseado em tempo real) que e evita a sobreescrição de arquivos.

## 📍 Projeto 2 - Trajetória
No arquivo [Mapping.py](https://github.com/HerculesDraycon/automatizando-tello-com-python/blob/main/control/Mapping.py) o algoritmo também controla o drone e desta vez exibe na tela um ponto que representa a localização atual do drone e a partir de seus movimentos o seu trajeto é registrado na tela e os dados sobre sua localização atual são constantemente atualizados de forma simultanea.
O código utiliza parâmetros de performance do drone e alguns cálculos geométricos para garantir boa precisão nos movimentos que são registrados na tela.

## 🙋🏻‍♂️ Projeto 3 - Acompanhamento Facial
No arquivo [FaceTracking.py](https://github.com/HerculesDraycon/automatizando-tello-com-python/blob/main/control/FaceTracking.py) está o algoritmo que faz reconhecimento de figuras (nesse projeto especificamente é o rosto humano) e realiza cálculos que calibram o drone para acompanhar uma pessoa enquanto detecta o seu rosto.<br>

Esse projeto conta com o auxílio da famigerada biblioteca OpenCV - Haarcascade. Em seu [arquivo xml](https://github.com/HerculesDraycon/automatizando-tello-com-python/blob/main/resources/haarcascade_frontalface_default.xml) os parâmetros já estão estabelecidos para que quando utilizados no código fonte Python sejam capazes de identificar a parte frontal do rosto.<br>

Enquanto o rosto é detectado, o drone verifica os parâmetros e acompanha os movimentos, se aproximando, afastando e rotacionando quando necessário. O software também conta com instruções para que o drone não realize manobras bruscas ou indesejadas quando perde o alvo da zona de detecção.
