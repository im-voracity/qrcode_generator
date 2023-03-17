# Gerador de QR Code

Este é um gerador de QR Code que pode ser utilizado via terminal. Ele aceita um link como entrada e gera um arquivo PNG com resolução 2000x2000 e um arquivo SVG.

## Requerimentos

- Python 3.x ou superior
- Pillow
- pypng
- qrcode
- typing_extensions
- svgwrite

`pip install requirements.txt`

## Parâmetros
Este script possui um parâmetro obrigatório:

`-l ou --link`: Link para gerar o QR Code

## Como usar

O gerador pode ser utilizado via linha de comando. Basta passar o link como argumento da seguinte maneira:

`python generator.py -l <link>`


Onde `<link>` é o link que você deseja transformar em QR Code.

## Exemplo de uso
Suponha que você queira gerar um QR Code para o link https://www.google.com.

Para isso, execute o seguinte comando no terminal:
`python qrcode_generator.py -l https://www.google.com`

O script irá perguntar o nome do projeto e irá criar uma pasta com esse nome na mesma pasta do script. Dentro dessa pasta, serão gerados dois arquivos contendo o QR Code: um arquivo PNG e um arquivo SVG. O QR Code também será exibido no terminal.

Após a execução do script, a pasta do projeto será aberta automaticamente. Lá você poderá visualizar os QR Codes gerados.

## Autor

Este gerador de QR Code foi desenvolvido [im-voracity](https://github.com/im-voracity). Se você tiver alguma dúvida ou sugestão, não hesite em entrar em contato.

