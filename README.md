# Integração Python com API Pública
Integração Python com API Pública
# FIAP - Inteligência artificial e data science

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto
Cap 3 - Colheita de Dados e Insights - Cap 1 - Construindo uma máquina agrícola - Integração Python com API Pública

## Nome do grupo
25

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Guilherme Campos Hermanowski </a>
- <a href="https://www.linkedin.com/company/inova-fusca">Gabriel Viel </a>
- <a href="https://www.linkedin.com/company/inova-fusca"> Matheus Alboredo Soares</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Jonathan Willian Luft </a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">ANDRÉ GODOI CHIOVATO</a>


## 📜 Justificativa do problema e descrição da solução proposta

<br>
Atualmente, o sistema de irrigação desenvolvido funciona de forma autônoma com base em sensores locais, como umidade do solo e presença de nutrientes. No entanto, ele não considera as condições climáticas externas, o que pode levar a decisões ineficientes, como acionar a bomba de irrigação mesmo quando há previsão de chuva. Isso pode resultar em desperdício de água, energia e recursos naturais.

Para resolver esse problema, propõe-se a integração do sistema com uma API meteorológica pública, permitindo o acesso a dados climáticos em tempo real, como temperatura, umidade do ar e previsão de chuva. Com essas informações, o sistema poderá tomar decisões mais inteligentes, como adiar a irrigação quando houver previsão de chuva, tornando-se mais sustentável e eficiente.


## 🔧 Funcionamento
• Importa a biblioteca requests para realizar chamadas HTTP à API de clima.
• Define a função obter_clima(cidade, api_key) para organizar o acesso à API OpenWeatherMap.
• Monta a URL da API com os parâmetros: cidade, chave da API, unidade em Celsius e idioma em português.
• Realiza a requisição com requests.get() e verifica se foi bem-sucedida com raise_for_status().
• Retorna os dados da API em formato JSON (dicionário Python).
• Se ocorrer um erro na requisição, imprime uma mensagem de erro e retorna None.

• Define as variáveis API_KEY e CIDADE para configurar o acesso à API.
• Chama a função obter_clima para obter os dados da cidade especificada.
• Extrai a condição do tempo atual da resposta JSON usando o campo 'weather'[0]['main'].

• 0 é valor padrão do sensor de umidade com a variável (sensor_umidade = 0) 
 para uma integração com o codigo principal (FarmTech Solutions) copie o valor de umidade
 
• Define a lógica para controle da bomba de irrigação:

A bomba será ligada se a umidade for menor que 50%.

E a condição do tempo não for chuva, chuvisco ou tempestade.

• Exibe no console se a bomba será ligada ou desligada com base nessas condições.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
