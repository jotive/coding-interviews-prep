# Coding Interviews Prep

Soluciones a problemas de entrevistas técnicas para roles Senior Backend. Python 3.11+, con tests y análisis de complejidad.

## Filosofía

Cada problema aquí cumple:

1. **Solución pythonic, no la primera que salga.** Trade-offs explícitos entre alternativas.
2. **Tests con `pytest`.** Casos típicos, edge y degenerados.
3. **Análisis O(tiempo) y O(espacio).** En el docstring y en el README de cada problema.
4. **Explicable en inglés.** Cada solución debe ser grabable en ~2 min.

No se optimiza por líneas de código. Se optimiza por **claridad + trade-off justificable**.

## Estructura

```
src/problems/
├── easy/
├── medium/
└── hard/

tests/
```

Cada archivo de solución `pXX_nombre.py` tiene su test `test_pXX_nombre.py`.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install pytest
pytest
```

## Progreso

| # | Problema | Dificultad | Topic | Estado |
|---|---|---|---|---|
| 3 | Second Maximum Element | Easy | Arrays | ✅ |
| 4 | Find Missing Number | Easy | Arrays/Math | ✅ |
| 15 | Balanced Parentheses | Medium | Stack | ✅ |
| 16 | Spiral Matrix Traversal | Medium | Matrix | ✅ |
| 44 | Maximum Subarray Sum | Hard | DP (Kadane) | ✅ |

Banco completo de problemas en notas privadas.

## Autor

[jotive](https://github.com/jotive) — Backend engineer preparando roles Senior / GenAI Architect.
Bitácora técnica: [jotive.dev](https://jotive.dev)
