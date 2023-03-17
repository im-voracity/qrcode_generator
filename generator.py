import qrcode
import argparse
import svgwrite
import os

# Configuração do parser de argumentos
parser = argparse.ArgumentParser(description='Gerador de QR Code')
parser.add_argument('-l', '--link', dest='link', help='Link para gerar o QR Code', required=True)
args = parser.parse_args()

# Perguntar o nome do projeto ao usuário
project_name = input("Insira o nome do projeto: ")

# Criar pasta do projeto e entrar na pasta
project_dir = os.path.join(os.getcwd(), project_name)
if not os.path.exists(project_dir):
    os.makedirs(project_dir)

# Criar arquivo .gitignore se ele não existir
gitignore_path = os.path.join(os.getcwd(), ".gitignore")
if not os.path.exists(gitignore_path):
    with open(gitignore_path, "w") as f:
        f.write("# Arquivos de projeto a serem ignorados\n")

# Adicionar pasta do projeto ao .gitignore se ainda não estiver adicionada
with open(gitignore_path, "r+") as f:
    gitignore_contents = f.read()
    if project_name not in gitignore_contents:
        f.write(f"{project_name}\n")

# Gerar o QR Code
qr = qrcode.QRCode(version=None, box_size=10, border=4)
qr.add_data(args.link)
qr.make(fit=True)

# Salvar imagem em PNG
filename = args.link.split("//")[-1].split("/")[0].split(".")[0] + ".png"
png_file = os.path.join(project_dir, filename)
img = qr.make_image(fill_color="black", back_color="white")
img.save(png_file)

# Salvar imagem em SVG
filename = args.link.split("//")[-1].split("/")[0].split(".")[0] + ".svg"
svg_file = os.path.join(project_dir, filename)  # adicionando esta linha para definir o caminho do arquivo SVG
svg = svgwrite.Drawing(filename=svg_file, size=("2000px", "2000px"))
svg.add(svgwrite.shapes.Rect(insert=(0, 0), size=("2000px", "2000px"), fill="white"))
modules = qr.modules
box_size = 2000 // len(modules)
offset = (2000 - box_size * len(modules)) // 2
for i, row in enumerate(modules):
    for j, module in enumerate(row):
        if module:
            x = j * box_size + offset
            y = i * box_size + offset
            svg.add(svgwrite.shapes.Rect(insert=(x, y), size=(box_size, box_size), fill="black"))
svg.save()

# Mostrar QR Code no terminal
matrix = qr.get_matrix()
terminal_size = 2 * qr.border + len(matrix)  # size including quiet zone
for i in range(terminal_size):
    row = ""
    for j in range(terminal_size):
        if i < qr.border or j < qr.border or i >= terminal_size - qr.border or j >= terminal_size - qr.border:
            row += "  "  # quiet zone
        elif matrix[i - qr.border][j - qr.border]:
            row += "██"  # black module
        else:
            row += "  "  # white module
    print(row)

# Abrir a pasta do projeto
if os.name == 'nt':
    os.startfile(project_dir)
elif os.name == 'posix':

    os.system('open "{}"'.format(project_dir))
else:
    print(f"Não foi possível abrir a pasta automaticamente. A pasta está localizada em: {project_dir}")

# Mostrar mensagem de conclusão
print(f"\nO QR Code acima é apenas ilustrativo, os QR Code funcionais estão na pasta que foi aberta")
print(f"Você pode visualizar os QR Codes funcionais na pasta {project_dir}.")