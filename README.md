# 🤖 Automatizando o DJI Tello com Python
O projeto conta com algoritmos que foram desenvolvidos em Python3 para controlar o drone DJI Tello a partir do computador e alguns processos de automação que utilizam a camera e sensores do aparelho como ferramenta de fornecimento de dados que são processados e aproveitados no software.

## 📸 Projeto 1 - Vigilância
No arquivo [ImageCapture.py](https://github.com/HerculesDraycon/automatizando-tello-com-python/blob/main/control/ImageCapture.py) foi feito um algoritmo que controla o drone através do teclado do computador conectado (e que está executando o código Python) enquanto o drone simultaneamente está transmitindo a imagem capturada em sua câmera pela tela do computador. Ao pressionar a tecla de captura, uma foto é tirada e armazenada automaticamente no diretório de imagem em formato jpg com um título singular (baseado em tempo real) que e evita a sobreescrição de arquivos.

## 📍 Projeto 2 - Trajetória
No arquivo [Mapping.py](https://github.com/HerculesDraycon/automatizando-tello-com-python/blob/main/control/Mapping.py) o algoritmo também controla o drone e desta vez exibe na tela um ponto que representa a localização atual do drone e a partir de seus movimentos o seu trajeto é registrado na tela e os dados sobre sua localização atual são constantemente atualizados de forma simultanea.
O código utiliza parâmetros de performance do drone e alguns cálculos geométricos para garantir boa precisão nos movimentos que são registrados na tela.
