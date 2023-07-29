import pydf

html_content = '''
<!DOCTYPE html>
<html>
<head>
    <title>Meu PDF Gerado com Python</title>
</head>
<body>
    <h1>Meu PDF Gerado com Python</h1>
    <p>Este e um exemplo de PDF gerado usando Python e a biblioteca pydf.</p>
    <p>Aqui estao algumas vantagens de usar Python:</p>
    <ul>
        <li>Simplicidade</li>
        <li>Facilidade de leitura</li>
        <li>Comunidade ativa</li>
        <li>Ampla variedade de bibliotecas</li>
    </ul>
    <p>Espero que este exemplo tenha sido util!</p>
</body>
</html>
'''

# Gerar o PDF
pdf = pydf.generate_pdf(html_content)

# Salvar o PDF em um arquivo
with open('myPythonPdf.pdf', 'wb') as f:
    f.write(pdf)

print("PDF gerado e salvo com sucesso!")
