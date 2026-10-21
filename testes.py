if __name__ == "__main__":
  # Criando lista com exatamente 10+ instâncias de diferentes tipos (Polimorfismo)
  catalogo = [
      Filme("Inception", "Ficção Científica", 148, "Christopher Nolan"),
      Filme("O Poderoso Chefão", "Drama/Crime", 175, "Francis Ford Coppola"),
      Filme("Interestelar", "Ficção Científica", 169, "Christopher Nolan"),
      Filme("Parasita", "Thriller", 132, "Bong Joon-ho"),
      Filme("Matrix", "Ação/Sci-Fi", 136, "Lana e Lilly Wachowski"),
      Serie("Breaking Bad", "Drama", 5, 12),
      Serie("Stranger Things", "Ficção/Terror", 4, 8),
      Serie("The Office", "Comédia", 9, 22),
      Documentario(
          "Nosso Planeta", "Natureza", 50, "Biodiversidade e Ecossistemas"
      ),
      Documentario("Cosmos", "Ciência", 60, "Astronomia e Origem do Universo"),
      Documentario(
          "O Dilema das Redes",
          "Tecnologia",
          94,
          "Impacto Social das Redes Sociais",
      ),
  ]

  print(
      f"=== CATÁLOGO DE STREAMING (Total de itens: {len(catalogo)}) ===\n"
  )

  for i, conteudo in enumerate(catalogo, 1):
    print(f"Item #{i}:")
    print(f"  Info (__str__): {conteudo}")
    print(f"  Ação (Polimorfismo): {conteudo.reproduzir()}")
    print("-" * 60)