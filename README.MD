# OpenStreetMap Web Scraper
[Documentação em Português](#pt-br)

This is a Python script that performs web scraping on OpenStreetMap to obtain information about paths and geographical coordinates.

## Requirements

- Python 3.x
- Python libraries: requests, selenium

## Installation

1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Install the required Python libraries by running the following command:

```
pip install -r requirements.txt
```

3. Download the Chrome driver that matches your browser's version from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure to add the path to the ChromeDriver executable to your PATH.

## Usage

The script will perform the following steps:
- Geocode an address to obtain the IDs of paths on OpenStreetMap.
- Visit the details page of each path to obtain links to geographical coordinates.
- Obtain geographical coordinates for each segment of the path.

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests with improvements or corrections.


# PT-BR

Este é um script Python que realiza web scraping no OpenStreetMap para obter informações sobre caminhos e coordenadas geográficas.

## Requisitos

- Python 3.x
- Bibliotecas Python: requests, selenium

## Instalação

1. Certifique-se de que você possui Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. Instale as bibliotecas Python necessárias executando o seguinte comando:

```
pip install -r requirements.txt
```

3. Baixe o driver do Chrome que corresponda à versão do seu navegador em [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads). Certifique-se de adicionar o caminho para o executável do ChromeDriver ao seu PATH.

## Uso

O script irá realizar as seguintes etapas:
- Geocodificar um endereço para obter os IDs dos caminhos no OpenStreetMap.
- Visitar a página de detalhes de cada caminho para obter os links para coordenadas geográficas.
- Obter coordenadas geográficas para cada trecho do caminho.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar solicitações de pull (pull requests) com melhorias ou correções.

