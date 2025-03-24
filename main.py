try:
    import tkinter as tk
    from tkinter import messagebox
except ModuleNotFoundError:
    print("Erro: O módulo tkinter não está disponível neste ambiente.")
    exit()

# Configuração da janela principal do Tkinter
root = tk.Tk()
root.title("Jogo da Velha")

# Variáveis globais
current_player = "X"
game_over = False
board = [[None] * 3 for _ in range(3)]


# Função para verificar se há um vencedor
def check_winner():
    for row in board:
        if all(row) and row[0]["text"] == row[1]["text"] == row[2]["text"] != "":
            highlight_winner(row)
            return row[0]["text"]

    for col in range(3):
        if all(board[i][col] for i in range(3)) and board[0][col]["text"] == board[1][col]["text"] == board[2][col][
            "text"] != "":
            highlight_winner([board[i][col] for i in range(3)])
            return board[0][col]["text"]

    if all(board[i][i] for i in range(3)) and board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != "":
        highlight_winner([board[i][i] for i in range(3)])
        return board[0][0]["text"]

    if all(board[i][2 - i] for i in range(3)) and board[0][2]["text"] == board[1][1]["text"] == board[2][0][
        "text"] != "":
        highlight_winner([board[i][2 - i] for i in range(3)])
        return board[0][2]["text"]

    return None


# Função para destacar os botões do vencedor
def highlight_winner(buttons):
    for button in buttons:
        button.config(bg="lightgreen")


# Função chamada quando um botão é clicado
def on_click(row, col):
    global current_player, game_over
    if board[row][col] and board[row][col]["text"] == "" and not game_over:
        board[row][col]["text"] = current_player
        winner = check_winner()
        if winner:
            messagebox.showinfo("Fim de Jogo", f"O jogador {winner} venceu!")
            game_over = True
        else:
            if all(board[i][j] and board[i][j]["text"] != "" for i in range(3) for j in range(3)):
                messagebox.showinfo("Fim de Jogo", "Empate!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"


# Função para reiniciar o jogo
def reset_game():
    global current_player, game_over
    current_player = "X"
    game_over = False
    for i in range(3):
        for j in range(3):
            if board[i][j]:
                board[i][j]["text"] = ""
                board[i][j].config(bg="white")


# Criação dos botões do tabuleiro
for i in range(3):
    for j in range(3):
        board[i][j] = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                                command=lambda row=i, col=j: on_click(row, col))
        board[i][j].grid(row=i, column=j)

# Botão para reiniciar o jogo
tk.Button(root, text="Reiniciar", font=("Arial", 14), command=reset_game).grid(row=3, column=0, columnspan=3)

# Inicia o loop principal da interface gráfica
root.mainloop()

