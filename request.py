# import requests
# from bs4 import BeautifulSoup
#
# # URL da página que você deseja buscar informações
# url = 'https://www.expressvpn.com/pt/what-is-my-ip?utm_source=windows_app&utm_medium=apps&utm_campaign=ip_address_checker&utm_content=bob_hamburger_ip_address_checker'
#
# try:
#     # Faz a requisição para a página
#     response = requests.get(url)
#
#     # Verifica se a requisição foi bem-sucedida
#     if response.status_code == 200:
#         # Obtemos o conteúdo da página
#         html_content = response.text
#
#         # Criamos o objeto BeautifulSoup para analisar o conteúdo HTML
#         soup = BeautifulSoup(html_content, 'html.parser')
#
#         # Buscamos a tag <span> com a classe "green"
#         span_tag = soup.find('span')
#
#         # Verificamos se encontramos a tag e imprimimos o seu conteúdo
#         if span_tag:
#             print("Informação encontrada:", span_tag.text)
#         else:
#             print("Tag não encontrada.")
#     else:
#         print("Não foi possível acessar a página:", response.status_code)
#
# except Exception as e:
#     print("Erro ao buscar informações da página:", e)
