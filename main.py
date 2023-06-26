import tkinter
import clock

# função responsavel por atualizar as linhas
def update_clock():
    clock_array = clock.clock()
    day = clock.get_day()

    hour = clock_array[0]
    date = clock_array[1]

    # reconfigurando o texto das duas linhas
    line_1.config(text=hour)
    line_1.after(500, update_clock) # atualiza a hora apos 500ms

    line_2.config(text=f"{day} - {date}")
    line_2.after(100000, update_clock) # atualiza a data apos 10000ms

# dicionario contendo algumas cores
colors = {
    'cor1': '#3d3d3d', # preto
    'cor2': '#fafcff', # branco
    'cor3': '#21c25c', # verde
    'cor4': '#eb463b', # vermelho
    'cor5': '#dedcdc', # cinza
    'cor6': '#3080f0', # azul
          }

background = colors['cor1']
font_color = colors['cor3']

# instanciando um objeto Tk()
window = tkinter.Tk()
window.title("Relogio Digital") # definindo titulo
window.geometry("440x190") # definindo o tamanho da janela "width X height"
window.resizable(width=False, height=False) # possibilidade de redefinir o tamanho da janela

window.config(bg=background) # definindo a cor de fundo da janela

# definindo a primeira linha dentro da janela
line_1 = tkinter.Label(window, text="", font=("Times 80"), bg=background, fg=font_color)
line_1.grid(row=0, column=0, sticky="NW", padx=5)

# definindo a segunda linha dentro da janela
line_2 = tkinter.Label(window, text="", font=("Times 20"), bg=background, fg=font_color)
line_2.grid(row=1, column=0, sticky="NW", padx=5)

update_clock() # chamando a função que atualiza o display
window.mainloop() # iniciando app
