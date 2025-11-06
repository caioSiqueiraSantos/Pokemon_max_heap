import random
import os

# ----- Classe Pokemon -----
class Pokemon:
    def __init__(self, nome: str, velocidade: int):
        self.nome = nome
        self.velocidade = int(velocidade)

    def __str__(self):
        return f"{self.nome} (Vel: {self.velocidade})"

# ----- Classe MaxHeap -----
class MaxHeap:
    def __init__(self):
        self.data = []

    def insert(self, pokemon: Pokemon):
        self.data.append(pokemon)
        self._heapify_up(len(self.data) - 1)

    def build_heap(self, pokemons):
        self.data = pokemons[:]
        for i in range(len(self.data) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.data[idx].velocidade > self.data[parent].velocidade:
                self.data[idx], self.data[parent] = self.data[parent], self.data[idx]
                idx = parent
            else:
                break

    def _heapify_down(self, idx):
        n = len(self.data)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx
            if left < n and self.data[left].velocidade > self.data[largest].velocidade:
                largest = left
            if right < n and self.data[right].velocidade > self.data[largest].velocidade:
                largest = right
            if largest != idx:
                self.data[idx], self.data[largest] = self.data[largest], self.data[idx]
                idx = largest
            else:
                break

    def pretty_levels(self):
        if not self.data:
            return "<vazio>"
        s = ""
        level = 0
        count = 0
        n = len(self.data)
        while count < n:
            nodes_this_level = 2 ** level
            level_items = []
            for i in range(nodes_this_level):
                if count >= n:
                    break
                level_items.append(str(self.data[count]))
                count += 1
            s += f"Nível {level}: " + " | ".join(level_items) + "\n"
            level += 1
        return s

    def __str__(self):
        return "[" + ", ".join(str(p) for p in self.data) + "]"

# ----- Lista de pokemons disponíveis -----
disponiveis = [
    Pokemon("Pikachu", 90),
    Pokemon("Charizard", 100),
    Pokemon("Bulbasaur", 45),
    Pokemon("Squirtle", 43),
    Pokemon("Gengar", 110),
    Pokemon("Machamp", 55),
    Pokemon("Alakazam", 120),
    Pokemon("Arcanine", 95),
    Pokemon("Snorlax", 30),
    Pokemon("Dragonite", 80),
    Pokemon("Jolteon", 130),
    Pokemon("Gyarados", 81),
    Pokemon("Eevee", 65),
    Pokemon("Vaporeon", 60),
]

meus_pokemons = []
inimigo_pokemons = []

# ----- Funções utilitárias -----
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_disponiveis():
    print("Pokémons disponíveis:")
    for i, p in enumerate(disponiveis, start=1):
        print(f"{i}. {p}")

def adicionar_pokemon():
    global meus_pokemons
    if len(meus_pokemons) >= 6:
        print("Você já tem 6 pokémons na equipe.")
        return
    mostrar_disponiveis()
    escolhas = input("Digite os números dos pokémons (separados por espaço): ").split()
    for token in escolhas:
        if len(meus_pokemons) >= 6:
            break
        if token.isdigit():
            idx = int(token) - 1
            if 0 <= idx < len(disponiveis):
                p = disponiveis[idx]
                if p not in meus_pokemons:
                    meus_pokemons.append(p)
                    print(f"{p.nome} adicionado!")
                else:
                    print(f"{p.nome} já está na equipe.")
    print(f"Total na equipe: {len(meus_pokemons)}/6")

def mostrar_equipe():
    if not meus_pokemons:
        print("Sua equipe está vazia.")
        return
    print("Sua equipe:")
    for i, p in enumerate(meus_pokemons, start=1):
        print(f"{i}. {p}")

def montar_inimigo():
    restantes = [p for p in disponiveis if p not in meus_pokemons]
    random.shuffle(restantes)
    return restantes[:6]

def executar_turno():
    global meus_pokemons, inimigo_pokemons
    if len(meus_pokemons) != 6:
        print("Você precisa ter 6 pokémons na equipe para batalhar!")
        return

    inimigo_pokemons = montar_inimigo()
    print("\nEquipe inimiga formada:")
    for i, p in enumerate(inimigo_pokemons, 1):
        print(f"{i}. {p}")

    minha_fila = meus_pokemons[:]
    inimiga_fila = inimigo_pokemons[:]

    campo_meu = minha_fila.pop(0)
    campo_inimigo = inimiga_fila.pop(0)

    rodada = 1
    while campo_meu and campo_inimigo:
        print(f"\n--- ROUND {rodada} ---")
        print(f"Seu Pokémon: {campo_meu}")
        print(f"Inimigo: {campo_inimigo}")

        if campo_meu.velocidade > campo_inimigo.velocidade:
            print(f"{campo_meu.nome} vence a rodada!")
            if inimiga_fila:
                campo_inimigo = inimiga_fila.pop(0)
                print(f"Novo inimigo em campo: {campo_inimigo}")
            else:
                print("Você derrotou todos os Pokémons inimigos!")
                break
        elif campo_meu.velocidade < campo_inimigo.velocidade:
            print(f"{campo_inimigo.nome} vence a rodada!")
            if minha_fila:
                campo_meu = minha_fila.pop(0)
                print(f"Novo Pokémon seu em campo: {campo_meu}")
            else:
                print("Todos os seus Pokémons foram derrotados!")
                break
        else:
            print("Empate de velocidade! Desempate por sorteio...")
            if random.choice(["meu", "inimigo"]) == "meu":
                print(f"{campo_meu.nome} venceu o sorteio!")
                if inimiga_fila:
                    campo_inimigo = inimiga_fila.pop(0)
                else:
                    print("Você derrotou todos os Pokémons inimigos!")
                    break
            else:
                print(f"{campo_inimigo.nome} venceu o sorteio!")
                if minha_fila:
                    campo_meu = minha_fila.pop(0)
                else:
                    print("Todos os seus Pokémons foram derrotados!")
                    break

        rodada += 1

    # 🔹 Montar Max-Heap com *todos* que participaram (meus + inimigos)
    todos_participantes = meus_pokemons + inimigo_pokemons
    heap = MaxHeap()
    heap.build_heap(todos_participantes)

    print("\n=== FIM DO TURNO ===")
    print("Heap montado com todos os Pokémons participantes:")
    print(heap)
    print("\nVisualização por níveis:")
    print(heap.pretty_levels())

    # Reinicia equipes
    meus_pokemons = []
    inimigo_pokemons = []

def reiniciar_tudo():
    global meus_pokemons, inimigo_pokemons
    meus_pokemons = []
    inimigo_pokemons = []
    print("Tudo reiniciado!")

def main_loop():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Adicionar Pokémon (escolher 6)")
        print("2 - Mostrar minha equipe")
        print("3 - Executar turno (batalha + montar heap)")
        print("4 - Sair / Reiniciar")
        escolha = input("Escolha uma opção: ").strip()
        clear_screen()
        if escolha == "1":
            adicionar_pokemon()
        elif escolha == "2":
            mostrar_equipe()
        elif escolha == "3":
            executar_turno()
        elif escolha == "4":
            reiniciar_tudo()
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    clear_screen()
    print("=== Batalha Pokémon com Max-Heap ===")
    print("Monte sua equipe (6 pokémons) e execute o turno!")
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\nSaindo do jogo...")
