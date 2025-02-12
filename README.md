# Aplicação de Previsão do Tempo com Interface Gráfica em Python

Esta é uma aplicação simples de previsão do tempo desenvolvida em Python, que utiliza a API do **OpenWeatherMap** para obter dados meteorológicos em tempo real. A interface gráfica foi criada com a biblioteca **Tkinter**, proporcionando uma experiência amigável e intuitiva para o usuário.

---

## Funcionalidades

### 1. **Busca por Cidade**
   - O usuário pode digitar o nome de uma cidade no campo de entrada.
   - A aplicação faz uma requisição à API do OpenWeatherMap para obter os dados meteorológicos da cidade especificada.

### 2. **Exibição de Dados Meteorológicos**
   - Após a busca, a aplicação exibe as seguintes informações:
     - **Condição climática**: Descrição do clima (ex.: céu limpo, nublado, chuva leve).
     - **Temperatura**: Temperatura atual em graus Celsius.
     - **Humidade**: Porcentagem de humidade no ar.
     - **Velocidade do vento**: Velocidade do vento em metros por segundo.

### 3. **Interface Gráfica Amigável**
   - A interface foi desenvolvida com **Tkinter**, sendo simples e fácil de usar.
   - Contém:
     - Um campo de entrada para o usuário digitar o nome da cidade.
     - Um botão para acionar a busca.
     - Uma área para exibir os resultados da previsão do tempo.

### 4. **Tratamento de Erros**
   - Caso o usuário digite uma cidade inválida ou ocorra algum problema na requisição à API, a aplicação exibe uma mensagem de erro explicativa.

---

## Como Usar

### Pré-requisitos
1. **Python 3.x**: Certifique-se de ter o Python instalado.
2. **Chave de API do OpenWeatherMap**:
   - Crie uma conta no [OpenWeatherMap](https://openweathermap.org/).
   - Obtenha sua chave de API gratuita na seção [API Keys](https://home.openweathermap.org/api_keys).

### Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/Fernando-Psy/previsao_do_tempo.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd previsao_do_tempo
   ```
3. Instale as dependências:
   ```bash
   pip install requests
   ```

### Executando a Aplicação
1. Substitua `sua_chave_api_aqui` no código pela sua chave de API do OpenWeatherMap.
2. Execute o script:
   ```bash
   python previsao_tempo_gui.py
   ```
3. Digite o nome da cidade no campo de entrada e clique em **Buscar Previsão**.

---

## Estrutura do Projeto
```
previsao-tempo-python/
│
├── previsao_tempo_gui.py  # Código principal da aplicação
├── README.md              # Documentação do projeto
└── requirements.txt       # Lista de dependências
```

---

## Melhorias Futuras
- Adicionar ícones para representar as condições climáticas.
- Implementar a previsão do tempo para vários dias.
- Salvar o histórico de consultas em um arquivo.
- Adicionar suporte para geolocalização automática.

---

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** e **pull requests** para sugerir melhorias ou reportar problemas.

---

## Contato
Se tiver dúvidas ou sugestões, entre em contato:
- **Nome**: Fernando Cesar B. Junior
- **E-mail**: fcesarjunior@gmail.com
- **GitHub**: [Fernando-Psy](https://github.com/Fernando-Psy)

 😊
