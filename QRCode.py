import qrcode
import datetime
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerarQrCode', methods=['POST'])
# Função para gerar o QR code e devolver para o index.html
def gerarQrCode():
    if request.method == 'POST':
        link = request.form['txtLink'] 
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link) # Adicionando o link ao QR Code
        qr.make(fit=True) # 
        nomeArquivo = gerarNome() # Gerando o nome do arquivo com base na data e hora do sistema
        img = qr.make_image(fill_color="black", back_color="white") # Gerando o QR Code
        caminho = 'static/qrcode/'+nomeArquivo+'.png' # variável de definição de caminho para salvar o QR Code gerado
        img.save(caminho)  # Salva a imagem em um arquivo        
        return render_template('index.html', url_img=caminho) # Passa o caminho do arquivo para o template exibir a imagem
    return render_template('index.html')

# Função de gerar e retornar o nome do arquivo com a data e hora do sistema
def gerarNome():
    data = datetime.datetime.now()
    return data.strftime("qrcode%d%m%Y%H%M%S")


if __name__ == '__main__':
    app.run(debug=True)