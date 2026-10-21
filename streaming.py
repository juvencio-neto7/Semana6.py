from abc import ABC, abstractmethod


# 1. Classe Abstrata base
class ConteudoStreaming(ABC):

  def __init__(self, titulo: str, genero: str, duracao_minutos: int):
    self._titulo = titulo
    self._genero = genero
    self._duracao_minutos = duracao_minutos

  @property
  def titulo(self) -> str:
    return self._titulo

  @property
  def genero(self) -> str:
    return self._genero

  @property
  def duracao_minutos(self) -> int:
    return self._duracao_minutos

  @duracao_minutos.setter
  def duracao_minutos(self, valor: int):
    if valor > 0:
      self._duracao_minutos = valor
    else:
      raise ValueError("A duração em minutos deve ser maior que zero.")

  @abstractmethod
  def reproduzir(self) -> str:
    """Método abstrato que deve ser implementado pelas subclasses (Polimorfismo)."""
    pass

  def __str__(self) -> str:
    return (
        f"[{self.__class__.__name__}] {self._titulo} ({self._genero}) - "
        f"{self._duracao_minutos} min"
    )


# 2. Subclasse Filme
class Filme(ConteudoStreaming):

  def __init__(self, titulo: str, genero: str, duracao_minutos: int, diretor: str):
    super().__init__(titulo, genero, duracao_minutos)  # Uso do super()
    self._diretor = diretor

  @property
  def diretor(self) -> str:
    return self._diretor

  def reproduzir(self) -> str:
    return (
        f"🎬 Reproduzindo o filme '{self.titulo}', dirigido por"
        f" {self._diretor}."
    )

  def __str__(self) -> str:
    base = super().__str__()
    return f"{base} | Diretor: {self._diretor}"


# 3. Subclasse Serie
class Serie(ConteudoStreaming):

  def __init__(
      self,
      titulo: str,
      genero: str,
      temporadas: int,
      episodios_por_temporada: int,
  ):
    # Estimando duração total baseada em média de 45 min por episódio
    duracao_estimada = temporadas * episodios_por_temporada * 45
    super().__init__(titulo, genero, duracao_estimada)
    self._temporadas = temporadas
    self._episodios_por_temporada = episodios_por_temporada

  @property
  def temporadas(self) -> int:
    return self._temporadas

  def reproduzir(self) -> str:
    return (
        f" Reproduzindo série '{self.titulo}' (Total de {self._temporadas}"
        " temporadas)."
    )

  def __str__(self) -> str:
    base = super().__str__()
    return f"{base} | Temporadas: {self._temporadas}"


# 4. Subclasse Documentario
class Documentario(ConteudoStreaming):

  def __init__(
      self,
      titulo: str,
      genero: str,
      duracao_minutos: int,
      tema_central: str,
  ):
    super().__init__(titulo, genero, duracao_minutos)
    self._tema_central = tema_central

  @property
  def tema_central(self) -> str:
    return self._tema_central

  def reproduzir(self) -> str:
    return (
        f"🔬 Exibindo o documentário '{self.titulo}' com foco em"
        f" '{self._tema_central}'."
    )

  def __str__(self) -> str:
    base = super().__str__()
    return f"{base} | Tema: {self._tema_central}"