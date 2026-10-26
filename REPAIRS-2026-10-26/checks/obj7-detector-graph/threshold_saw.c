#include <stdio.h>
#include <stdlib.h>
/* Exact self-avoiding walk counts from every vertex of an undirected graph. */
static int n, *deg, **nb; static char *on;
static long long walk(int u, int left) {
  if (left == 0) return 1;
  long long t = 0;
  for (int i = 0; i < deg[u]; i++) { int v = nb[u][i]; if (on[v]) continue;
    on[v] = 1; t += walk(v, left - 1); on[v] = 0; }
  return t;
}
int main(int argc, char **argv) {
  int m = atoi(argv[1]);
  if (scanf("%d", &n) != 1) return 1;
  deg = malloc(n * sizeof(int)); nb = malloc(n * sizeof(int *)); on = calloc(n, 1);
  for (int v = 0; v < n; v++) { if (scanf("%d", &deg[v]) != 1) return 1; nb[v] = malloc(deg[v] * sizeof(int));
    for (int i = 0; i < deg[v]; i++) if (scanf("%d", &nb[v][i]) != 1) return 1; }
  long long best = 0;
  for (int v = 0; v < n; v++) { on[v] = 1; long long c = walk(v, m); on[v] = 0; if (c > best) best = c; }
  printf("%d %lld\n", m, best);
  return 0;
}
