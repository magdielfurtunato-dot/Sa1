import json
import os
import sys

ARQUIVO = "produtos.json"

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_dados():
    with open(ARQUIVO, "w") as f:
        json.dump(produtos, f, indent=4)

produtos = carregar_dados()

def getch():
    try:
        import msvcrt
        return msvcrt.getch().decode("utf-8").lower()
    except:
        import termios, tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            return ch.lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def cadastrarproduto():
    nome = input("\033[33mNome do produto: \033[0m")
    preco = float(input("\033[33mPreço $: \033[0m"))
    estoque = input("\033[33mMarca: \033[0m")

    produto = {
        "nome": nome,
        "preco": preco,
        "marca": estoque
    }

    produtos.append(produto)
    salvar_dados() 

    print("\n\033[32mProduto cadastrado!\033[0m")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\n\033[32m=== PRODUTOS ===\033[0m")
    for i, p in enumerate(produtos):
        print(f"\033[31m{i+1} - {p['nome']} | R$ {p['preco']:.2f} | Marca: {p['marca']}")

def remover_produto():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    listar_produtos()

    try:
        indice = int(input("\nNúmero do produto: ")) - 1
        removido = produtos.pop(indice)
        salvar_dados()
        print(f"\033[32mRemovido: {removido['nome']}\033[0m")
    except (ValueError, IndexError):
        print("Opção inválida!")

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def menu_interativo():
    opcoes = [
        "Cadastrar produto ",
        "Pesquisar produto ",
        "Listar produtos ",
        "Remover produto ",
        "\033[31mSair \033[0m"
    ]
    
    posicao = 0

    while True:
        limpar_tela()
        
        print("\n                               ")
        print("     DIRESTRAT MUSIC CENTER  ")
        print("            stock          ")
        print("                               \n\n")
        
        for i, opcao in enumerate(opcoes):
            if i == posicao:
                print(f"\033[42m➜ {opcao}\033[0m")
            else:
                print(f"  {opcao}")
        
        print("\n\033[33mUse W/S para navegar e ENTER para selecionar\033[0m")

        tecla = getch()

        if tecla == "w" and posicao > 0:
            posicao -= 1
        elif tecla == "s" and posicao < len(opcoes) - 1:
            posicao += 1
        elif tecla == "\r":
            return posicao + 1

def pesquisarproduto():
    nome_busca = input("\033[34mNome do produto: \033[0m").lower()
    encontrados = False

    for produto in produtos:
        if nome_busca in produto["nome"].lower():
            print(f"{produto['nome']} - R$ {produto['preco']} | Marca {produto['marca']}")
            encontrados = True

    if not encontrados:
        print("Nenhum produto encontrado.")

while True:
    opcao = menu_interativo()

    limpar_tela()
    
    if opcao == 1:
        cadastrarproduto()
        input("\033[32m[APERTE ENTER PARA CONTINUAR]\033[0m")
    elif opcao == 2:
        pesquisarproduto()
        input("\033[32m[APERTE ENTER PARA CONTINUAR]\033[0m")
    elif opcao == 3:
        listar_produtos()
        input("\033[32m[APERTE ENTER PARA CONTINUAR]\033[0m")
    elif opcao == 4:
        remover_produto()
        input("\033[32m[APERTE ENTER PARA CONTINUAR]\033[0m")
    elif opcao == 5:
        print("Saindo...")
        break