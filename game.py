#personagem: parent class
#heroi: controlado pelo usuário
#inimigo: adversário do usuário

import random

class Personagem:
  def __init__(self, name, life, level):
    self.__name = name
    self.__life = life
    self.__level = level

  def get_name(self):
    return self.__name
  
  def get_life(self):
    return self.__life
  
  def get_level(self):
    return self.__level
  
  def exibir_detalhes(self):
    return f"Name: {self.get_name()}\nLife: {self.get_life()}\nLevel: {self.get_level()}"
  
  def receber_ataque(self, dano):
    self.__life -= dano
    if self.__life < 0:
      self.__life = 0
  
  def atacar(self, alvo):
    dano = random.randint(self.get_level() * 2, self.get_level() *4) #baseado no nível
    alvo.receber_ataque(dano)
    print(f"{self.get_name()} atacou {alvo.get_name()} e causou {dano} de dano!")

class Heroi(Personagem):
  def __init__(self, name, life, level, habilidade):
    super().__init__(name, life, level)
    self.__habilidade = habilidade

  def get_habilidade(self):
    return self.__habilidade
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"
  
  def ataque_especial(self, alvo):
    dano = random.randint(self.get_level() * 5, self.get_level() * 8) #dano aumentado
    alvo.receber_ataque(dano)
    print(f"{self.get_name()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_name()} e causou {dano} de dano!")
  
class Inimigo(Personagem):
  def __init__(self, name, life, level, tipo):
    super().__init__(name, life, level)
    self.__tipo = tipo

  def get_tipo(self):
    return self.__tipo  
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"
  

class Game:
  """Classe orquestradora do jogo"""
  def __init__(self) -> None:
    self.heroi = Heroi(name="Hulk", life=150, level=5, habilidade="Super força")
    self.enemy = Inimigo(name="Abominável", life=150, level=5, tipo="Super força")

  def iniciar_batalha(self):
    """Fazer a gestão da batalha em turnos"""
    print("Iniciar batalha")
    while self.heroi.get_life() > 0 and self.enemy.get_life() > 0:
      print("\nDetalhes dos personagens:")
      print(self.heroi.exibir_detalhes())
      print(self.enemy.exibir_detalhes())

      input("Pressione Enter para atacar...")
      escolha = input("Escolha (1- Ataque normal, 2- Ataque especial): ")

      if escolha == "1":
        self.heroi.atacar(self.enemy)
      elif escolha == "2":
        self.heroi.ataque_especial(self.enemy)
      else:
        print("Escolha inválida, tenta novamente!")

      if self.enemy.get_life() > 0:
        self.enemy.atacar(self.heroi)

    if self.heroi.get_life() > 0:
      print("\nParabéns você venceu a batalha")
    else:
      print("\nVocê foi derrotado!")

#Criar instância do jogo e iniciar batalha
jogo = Game()
jogo.iniciar_batalha()
