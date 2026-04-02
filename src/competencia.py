def inicializar_estadisticas(rounds):
    stats = {}

    for participante in rounds[0]['scores']:
        stats[participante] = {
            'total': 0,
            'rondas_ganadas': 0,
            'mejor_ronda': 0,
            'puntajes_rondas': []
        }

    return stats


def mostrar_tabla_parcial(stats):
    ranking = sorted(stats.items(), key=lambda x: x[1]['total'], reverse=True)

    print("Tabla de posiciones:")
    for posicion, (participante, datos) in enumerate(ranking, start=1):
        print(f"{posicion}. {participante} - {datos['total']} pts")


def mostrar_tabla_final(stats):
    ranking_final = sorted(stats.items(), key=lambda x: x[1]['total'], reverse=True)

    print("\nTabla de posiciones final:")
    print(f"{'Cocinero':<12} {'Puntaje':<8} {'Ganadas':<8} {'Mejor':<8} {'Promedio':<8}")
    print("-" * 55)

    for participante, datos in ranking_final:
        promedio = datos['total'] / len(datos['puntajes_rondas'])
        print(
            f"{participante:<12} "
            f"{datos['total']:<8} "
            f"{datos['rondas_ganadas']:<8} "
            f"{datos['mejor_ronda']:<8} "
            f"{promedio:<8.1f}"
        )

    print("-" * 55)


def procesar_competencia(rounds):
    stats = inicializar_estadisticas(rounds)

    for numero_ronda, ronda in enumerate(rounds, start=1):
        puntajes_ronda = {}

        for participante, jueces in ronda['scores'].items():
            puntaje = sum(jueces.values())
            puntajes_ronda[participante] = puntaje

            stats[participante]['total'] += puntaje
            stats[participante]['puntajes_rondas'].append(puntaje)

            if puntaje > stats[participante]['mejor_ronda']:
                stats[participante]['mejor_ronda'] = puntaje

        ganador = max(puntajes_ronda, key=puntajes_ronda.get)
        stats[ganador]['rondas_ganadas'] += 1

        print(f"\nRonda {numero_ronda} - {ronda['theme']}:")
        print(f"Ganador: {ganador} ({puntajes_ronda[ganador]} pts)")
        mostrar_tabla_parcial(stats)

    mostrar_tabla_final(stats)