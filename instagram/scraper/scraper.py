import csv
from bs4 import BeautifulSoup

# Caminhos dos arquivos
file_path = "../html_post_v1.txt"
output_csv = "../comentarios_extraidos.csv"

try:
    # 1. Abrir e ler o conteúdo do arquivo HTML local
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    # 2. Inicializar o parser do BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Lista para armazenar os dados extraídos antes de salvar
    dados_comentarios = []

    print(f"{'USUÁRIO':<20} | {'COMENTÁRIO'}")
    print("-" * 50)

    # 3. Varre a estrutura procurando elementos que representem os blocos de comentários
    for comment_block in soup.find_all("div", class_="_a9zr"):
        # Extrai o nome de usuário
        user_element = comment_block.find("a", class_="_a3gq") or comment_block.find("h3")
        # Extrai o texto do comentário
        text_element = comment_block.find("span", class_="_aade")
        
        if user_element and text_element:
            username = user_element.text.strip()
            comment_text = text_element.text.strip()
            
            print(f"{username:<20} | {comment_text}")
            
            # Adiciona os dados na lista
            dados_comentarios.append([username, comment_text])

    # 4. NOVA ETAPA: Salvar o resultado em uma planilha CSV
    # O uso de 'utf-8-sig' evita problemas de acentuação e caracteres especiais no Excel
    with open(output_csv, mode="w", newline="", encoding="utf-8-sig") as csv_file:
        # O delimitador ';' força o Excel em português a separar as colunas automaticamente
        writer = csv.writer(csv_file, delimiter=";")
        
        # Grava a linha do cabeçalho
        writer.writerow(["Usuário", "Comentário"])
        
        # Grava todas as linhas de comentários coletadas
        writer.writerows(dados_comentarios)

    print("-" * 50)
    print(f"Sucesso! {len(dados_comentarios)} comentários foram salvos em '{output_csv}'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao processar o arquivo: {e}")