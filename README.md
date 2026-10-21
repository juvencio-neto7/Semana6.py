# 🚀 Sistema de Streaming OOP - Sprint 6

Projeto desenvolvido em Python aplicando os principais conceitos de Orientação a Objetos exigidos no desafio da Sprint 6.

## 🛠️ Tecnologias Utilizadas
* **Python 3.10+**
* Módulo `abc` (Abstract Base Classes)

## ✨ Conceitos Aplicados
1. **Classe Abstrata (`ABC`)**: `ConteudoStreaming` define a estrutura padrão que as subclasses devem seguir, impedindo a instanciação direta.
2. **Herança**: As classes `Filme`, `Serie` e `Documentario` herdam atributos e métodos comuns de `ConteudoStreaming`.
3. **Encapsulamento & Propriedades (`@property`)**: Atributos protegidos (como `_titulo` e `_duracao_minutos`) acessados e validados de forma segura via propriedades.
4. **Polimorfismo e `super()`**: Reaproveitamento do construtor da superclasse com `super().__init__()` e sobrescrita do método abstrato `reproduzir()`.
5. **Métodos Especiais**: Implementação de `__init__` para inicialização e `__str__` para exibição formatada dos objetos.

## 📊 Diagrama de Classes
Consulte o diagrama Mermaid na documentação principal para visualizar a hierarquia e o relacionamento entre as classes do sistema.

## 🏃 Como Executar
1. Certifique-se de ter o Python instalado.
2. Salve o código em um arquivo chamado `streaming.py`.
3. Execute o script no terminal:
   ```bash
   python streaming.py




## Diagrama de Classes

```mermaid
classDiagram
    class ConteudoStreaming {
        <<abstract>>
        #str _titulo
        #str _genero
        #int _duracao_minutos
        +titulo()
        +genero()
        +duracao_minutos()
        +reproduzir()*
        +__str__()
    }
    class Filme {
        -str _diretor
        +diretor()
        +reproduzir()
        +__str__()
    }
    class Serie {
        -int _temporadas
        -int _episodios_por_temporada
        +temporadas()
        +reproduzir()
        +__str__()
    }
    class Documentario {
        -str _tema_central
        +tema_central()
        +reproduzir()
        +__str__()
    }
    ConteudoStreaming <|-- Filme
    ConteudoStreaming <|-- Serie
    ConteudoStreaming <|-- Documentario


