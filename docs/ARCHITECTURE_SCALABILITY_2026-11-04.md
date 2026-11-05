# tsp-backtracking-lab — Ingeniería, pruebas y escalabilidad realista

**Estado:** plan técnico documentado el 04-11-2026. No constituye resultado experimental ejecutado.

## Evidencia de partida

Material académico y estudio de poda para el TSP, con demostración web; no se verificó solver completo independiente en la raíz.

## Incrementos de ingeniería

Definir estrategia de backtracking con límites inferiores válidos, probar costo óptimo contra la referencia brute-force en matrices pequeñas, contar nodos podados y tiempos.

## Estrategia de escalabilidad

Comparar en familias de instancias simétricas/asimétricas y densidades; demostrar casos donde la poda reduce trabajo y casos adversos donde no.

## Riesgos y condición de aprobación

No afirmar que poda equivale a complejidad polinómica ni que el algoritmo supera siempre al brute-force; preservar coautoría.

## Protocolo de experimentación y calidad

Cada comparativa debe incluir referencia de código/commit, entorno, versiones, semilla cuando corresponda, entrada reproducible, comando de ejecución, datos brutos, repetición y límites. Separar datos de ejemplo de resultados realmente ejecutados. Mantener código histórico y coautoría intactos; publicar evidencias de tests de CI y pruebas manuales en su contexto, sin inventar métricas.

## Referencias consultadas (2026-11-04)

- [AWS Well-Architected — rendimiento y costo](https://docs.aws.amazon.com/wellarchitected/).
- [NIST SSDF — prácticas seguras de software](https://csrc.nist.gov/pubs/sp/800/218/final).
- [Google SRE — medición y objetivos](https://sre.google/workbook/implementing-slos/).

Las referencias son metodológicas; no corroboran los benchmarks particulares de este repositorio.
