# import requests
# from bs4 import BeautifulSoup
#
# # URL da página que você deseja buscar informações
# url = 'https://www.facebook.com/people/Poker-Brasil/100064546038812/'

# try:
#     # Faz a requisição para a página
#     response = requests.get(url)
#
#     # Verifica se a requisição foi bem-sucedida
#     if response.status_code == 200:
#         # Obtemos o conteúdo da página
#         html_content = response.text
#         print(html_content)
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


# import requests
# import bs4
#
# url = 'https://www.facebook.com/people/Poker-Brasil/100064546038812/'
#
# # Fazer uma solicitação GET para a página do Facebook
# response = requests.get(url)
#
# # Extrair o conteúdo HTML da página
# soup = bs4.BeautifulSoup(response.content, 'html.parser')
# print(soup)
#
# # Encontrar o elemento HTML que contém a imagem
# image_element = soup.find_all('img')[0]
#
# # Extrair o URL da imagem
# image_url = image_element['src']
#
# # Extrair o link da imagem
# link_url = image_url.split('?')[0]
#
# # Imprimir o link da imagem
# print(link_url)



