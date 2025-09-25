import pygame
from dataclasses import dataclass
from polygon import preencher_poligono_et_aet

@dataclass
class Botao:
    rect: pygame.Rect
    texto: str
    cor_fundo: tuple[int, int, int]
    cor_texto: tuple[int, int, int]

    def __post_init__(self):
        self.fonte: pygame.font.Font = pygame.font.Font(None, 24)
    
    # Desenhar o botão
    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor_fundo, self.rect)
        texto_surface = self.fonte.render(self.texto, True, self.cor_texto)
        texto_rect = texto_surface.get_rect(center=self.rect.center)
        tela.blit(texto_surface, texto_rect)
    
    # Verificar se o botão foi clicado
    def foi_clicado(self, pos_mouse):
        return self.rect.collidepoint(pos_mouse)
    

pygame.init()
pygame.font.init()

# Tamanho da janela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Titulo da janela
pygame.display.set_caption("Polygon Fill - Trabalho de CG")

# Controlar fps
relogio = pygame.time.Clock()

# Cores utilizadas
Preto = (0, 0, 0)
Branco = (255, 255, 255)
Vermelho = (255, 0, 0)
Verde = (0, 255, 0)
Azul = (0, 0, 255)
Cinza = (100,100,100)
#variáveis de controle
espesura_atual = 3
cor_preenchimento_atual = Vermelho

#criando os botões
botao_limpar = Botao(pygame.Rect(10, 10, 100, 40), "Limpar", Cinza, Branco)
botao_preencher = Botao(pygame.Rect(120, 10, 100, 40), "Preencher", (0,150,0), Branco)
botao_cor_vermelha = Botao(pygame.Rect(230, 10, 40, 40), "R", Vermelho, Branco)
botao_cor_verde = Botao(pygame.Rect(280, 10, 40, 40), "G", Verde, Branco)
botao_cor_azul = Botao(pygame.Rect(330, 10, 40, 40), "B", Azul, Branco)
botao_espesura_mais = Botao(pygame.Rect(400, 10, 40, 40), "+", Cinza, Branco)
botao_espesura_menos = Botao(pygame.Rect(450, 10, 40, 40), "-", Cinza, Branco)

botoes = [botao_limpar, botao_preencher, botao_cor_vermelha, botao_cor_verde, botao_cor_azul, botao_espesura_mais, botao_espesura_menos]

vertices = []
# Estado da aplicação
estado_app = 'DESENHANDO'
executando = True

while executando:
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                mouse_pos = evento.pos
                if botao_limpar.foi_clicado(mouse_pos):
                    vertices.clear()
                    estado_app = 'DESENHANDO'
                    # Limpar completamente a tela
                    tela.fill(Preto)
                elif botao_preencher.foi_clicado(mouse_pos):
                    if estado_app == 'PRONTO':
                        preencher_poligono_et_aet(vertices, cor_preenchimento_atual, tela)
                        print(f"Poligono preenchido com a cor {cor_preenchimento_atual}")
                        estado_app = 'PREENCHIDO'
                elif botao_cor_vermelha.foi_clicado(mouse_pos):
                    cor_preenchimento_atual = Vermelho
                elif botao_cor_verde.foi_clicado(mouse_pos):
                    cor_preenchimento_atual = Verde
                elif botao_cor_azul.foi_clicado(mouse_pos):
                    cor_preenchimento_atual = Azul
                elif botao_espesura_mais.foi_clicado(mouse_pos):
                    if espesura_atual < 10:  # Limitar máximo
                        espesura_atual += 1
                        # Redesenhar preenchimento se estiver preenchido
                        if estado_app == 'PREENCHIDO':
                            # Redesenhar apenas o preenchimento (preserva preenchimento)
                            preencher_poligono_et_aet(vertices, cor_preenchimento_atual, tela)
                elif botao_espesura_menos.foi_clicado(mouse_pos):
                    if espesura_atual > 1:
                        espesura_atual -= 1
                        # Redesenhar preenchimento se estiver preenchido
                        if estado_app == 'PREENCHIDO':
                            # Redesenhar apenas o preenchimento (preserva preenchimento)
                            preencher_poligono_et_aet(vertices, cor_preenchimento_atual, tela)
                else:
                    if estado_app == 'DESENHANDO':
                        vertices.append(mouse_pos)
            elif evento.button == 3:
                if estado_app == 'DESENHANDO' and len(vertices) >= 3:
                    estado_app = 'PRONTO'
                    print("Poligono desenhado com sucesso!")

    # Sempre limpar área da UI
    pygame.draw.rect(tela, Preto, (0, 0, LARGURA, 60))

    for botao in botoes:
        botao.desenhar(tela)
    
    fonte_indicador = pygame.font.Font(None, 20)
    texto_espesura = fonte_indicador.render(f"Espessura: {espesura_atual}", True, Branco)
    tela.blit(texto_espesura, (500, 20))
    pygame.draw.rect(tela, cor_preenchimento_atual, (700, 10, 80, 40), 2)

    if len(vertices) >= 2:
        if estado_app == 'DESENHANDO':
            pygame.draw.lines(tela, Branco, False, vertices, espesura_atual)
        else:  # PRONTO ou PREENCHIDO - ambos precisam do contorno
            # Desenhar contorno com espessura atual
            if espesura_atual == 1:
                # Para espessura 1, usar draw.lines para garantir que seja visível
                vertices_fechados = vertices + [vertices[0]]  # Fechar o polígono
                pygame.draw.lines(tela, Branco, True, vertices_fechados, 1)
            else:
                pygame.draw.polygon(tela, Branco, vertices, espesura_atual)
    
    pygame.display.flip()
    relogio.tick(60)
#finalizar
pygame.quit()
