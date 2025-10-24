from .simulate import simulate_detailed

def lru(pages, frames, detailed=False):
    """
    Algoritmo LRU (Least Recently Used).
    Reemplaza la página que no se ha usado durante más tiempo.
    
    Args:
        pages: Lista de referencias a páginas.
        frames: Número de frames en memoria.
        detailed: Si True, devuelve dict con metrics y steps detallados.
                  Si False, devuelve solo el conteo de page faults.
    
    Returns:
        int: Número de page faults (si detailed=False)
        dict: {"metrics": {...}, "steps": [...]} (si detailed=True)
    
    Examples:
        >>> lru([1, 2, 3, 1, 2, 4], 3)
        4
        >>> result = lru([1, 2, 3, 1], 2, detailed=True)
        >>> result["metrics"]["faults"]
        3
    """
    result = simulate_detailed("lru", pages, frames)
    if detailed:
        return result
    return result["metrics"]["faults"]
