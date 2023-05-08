from selenium import webdriver

def test_title():
    # Configura o driver do navegador
    driver = webdriver.Chrome()
    driver.get("teste.html")

    # Verifica o título da página
    assert driver.title == "Exemplo de Página"

    # Fecha o navegador
    driver.quit()