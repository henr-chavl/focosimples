# FocoSimples

### Descrição do problema real:
Muitos estudantes, especialmente aqueles que enfrentam dificuldades com neurodivergências (como TDAH) ou falta de hábito, sofrem com a **paralisia de decisão**. Ao se depararem com várias matérias e pouco tempo, perdem mais tempo tentando decidir o que estudar do que realmente estudando, o que gera ansiedade e desmotivação, podendo fazer com que eles acabem nem estudando.

### Proposta da solução:
O **FocoSimples** é uma aplicação de interface de linha de comando (CLI) que aplica o conceito de *Timeblocking* baseado em pesos. O usuário define seu tempo total disponível e o nível de prioridade (ou dificuldade) de cada matéria. O algoritmo calcula automaticamente a distribuição ideal de minutos, entregando um cronograma pronto de estudo para o dia.

### Público-alvo:
* Estudantes com dificuldade de organização de rotina.

### Funcionalidades principais:
* Cálculo proporcional de tempo baseado em pesos de prioridade (1 a 5).
* Interface simplificada via terminal (CLI).
* Tratamento de erros para entradas inválidas.
* Validação automática de código via Integração Contínua (CI).

### Tecnologias utilizadas:
* **Linguagem:** [Python 3.10+](https://www.python.org/)
* **Testes:** [Pytest](https://docs.pytest.org/)
* **Linting/Análise Estática:** [Flake8](https://flake8.pycqa.org/)
* **CI/CD:** GitHub Actions
* **Versionamento:** SemVer (Semantic Versioning)

---

## Como instalar e executar

### Instalação:
Primeiro clone esse repositório;

Depois instale as dependências:
```bash
   pip install -r requirements.txt
```

### Execução:
Execute:
```bash
python focosimples/main.py
```

## Rodar testes e lint

### Testes automatizados:
```bash
python -m pytest tests/test_cronograma.py
```

### Lint:
```bash
flake8 focosimples/ tests/
```

---
# Evidência de funcionamento:
<img width="461" height="236" alt="evidencia-funcionamento" src="https://github.com/user-attachments/assets/f60dfd49-0656-449d-8bb9-1e64e9bcaaec" />

---

## Informações

### Autor:
Henrique Chaves

### Versão:
1.0.0

### Link do repositório:
```bash
https://github.com/henr-chavl/focosimples
```
