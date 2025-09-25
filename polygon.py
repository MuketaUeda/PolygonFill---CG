from dataclasses import dataclass

@dataclass
class Aresta:
    x: float
    y_max: int
    dx_dy: float

def preencher_poligono_et_aet(vertices, cor_preenchimento_atual, tela):
    # Verificar se é polígono válido
    if len(vertices) < 3:
        return
    
    et = {}
    y_min = min(vertex[1] for vertex in vertices)
    y_max = max(vertex[1] for vertex in vertices)

    # CONSTRUIR ET COMPLETA PRIMEIRO
    n = len(vertices)
    for i in range(n):
        ponto_atual = vertices[i]
        ponto_proximo = vertices[(i + 1) % n]
        
        # Verificar pontos duplicados
        if ponto_atual == ponto_proximo:
            continue

        x1, y1 = ponto_atual
        x2, y2 = ponto_proximo

        # Pular arestas horizontais
        if y1 == y2:
            continue
            
        # Tratar arestas verticais - adicionar à ET como aresta especial
        if x1 == x2:
            # Para arestas verticais, criar aresta com dx_dy = 0
            if y1 < y2:
                y_min_aresta = y1
                y_max_aresta = y2
                x_atual = x1
            else:
                y_min_aresta = y2
                y_max_aresta = y1
                x_atual = x1
            
            # Aresta vertical tem dx_dy = 0
            aresta = Aresta(x_atual, y_max_aresta, 0.0)
            
            if y_min_aresta not in et:
                et[y_min_aresta] = []
            et[y_min_aresta].append(aresta)
            continue

        # Determinar orientação da aresta
        if y1 < y2:
            y_min_aresta = y1
            y_max_aresta = y2
            x_atual = x1
        else:
            y_min_aresta = y2
            y_max_aresta = y1
            x_atual = x2
        
        dx_dy = (x2 - x1) / (y2 - y1)
        aresta = Aresta(x_atual, y_max_aresta, dx_dy)

        if y_min_aresta not in et:
            et[y_min_aresta] = []
        et[y_min_aresta].append(aresta)

    y_atual = y_min
    aet = []
    
    while y_atual <= y_max or aet:
        #Transferir arestas da ET para AET
        if y_atual in et:
            for aresta in et[y_atual]:
                aet.append(aresta)
            del et[y_atual]
        
        #Ordenar AET por coordenada X primeiro
        aet.sort(key=lambda aresta: aresta.x)
        
        #Remover arestas com y_max = y_atual
        aet = [aresta for aresta in aet if aresta.y_max != y_atual]
        
        #Preencher pixels na linha y_atual
        for i in range(0, len(aet), 2):
            if i + 1 < len(aet):
                x_inicio = int(aet[i].x)
                x_fim = int(aet[i + 1].x)

                # Verificar bounds da tela e evitar área dos botões
                if 0 <= y_atual < tela.get_height() and y_atual > 60:
                    for x in range(x_inicio, x_fim + 1):
                        if 0 <= x < tela.get_width():
                            tela.set_at((x, y_atual), cor_preenchimento_atual)
        
        # Se há número ímpar de arestas na AET, tratar a última
        if len(aet) % 2 == 1:
            # Desenhar pixel na última aresta se necessário
            ultima_aresta = aet[-1]
            x_ultima = int(ultima_aresta.x)
            if 0 <= y_atual < tela.get_height() and 0 <= x_ultima < tela.get_width() and y_atual > 60:
                tela.set_at((x_ultima, y_atual), cor_preenchimento_atual)
        
        # Atualizar X das arestas ativas
        for aresta in aet:
            aresta.x += aresta.dx_dy 
        y_atual += 1
