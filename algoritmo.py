def segunda_oportunidad(refs, n_marcos):
    """Devuelve (pasos, fallos). Cada paso describe el estado tras una referencia."""
    marcos = [None] * n_marcos
    bits = [0] * n_marcos
    puntero = 0
    fallos = 0
    pasos = []

    for pagina in refs:
        victima = None
        if pagina in marcos:
            bits[marcos.index(pagina)] = 1  
            fallo = False
        else:
            fallo = True
            fallos += 1
            while marcos[puntero] is not None and bits[puntero] == 1:
                bits[puntero] = 0
                puntero = (puntero + 1) % n_marcos
            victima = marcos[puntero]
            marcos[puntero] = pagina
            bits[puntero] = 1
            puntero = (puntero + 1) % n_marcos

        pasos.append({
            "ref": pagina,
            "marcos": list(zip(marcos, bits)),
            "puntero": puntero,
            "fallo": fallo,
            "victima": victima,
        })
    return pasos, fallos


def fifo_fallos(refs, n_marcos):
    """FIFO simple, solo para comparar la cantidad de fallos."""
    marcos, fallos = [], 0
    for pagina in refs:
        if pagina not in marcos:
            fallos += 1
            if len(marcos) == n_marcos:
                marcos.pop(0)
            marcos.append(pagina)
    return fallos
