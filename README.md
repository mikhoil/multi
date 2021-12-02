# multi
IO-bound
1) синхронная проверка ссылок на 1 потоке:![1.png](IO_bound/1.png) 1564963ms
2) синхронная проверка ссылок с 5 воркерами:![2.png](IO_bound/2.png) 237014ms
3) c 10: ![3.png](IO_bound/3.png) 124689ms
4) с 100: ![4.png](IO_bound/4.png) 25079ms

CPU-bound:
1. генерация монетки на 1 потоке: ![5.png](CPU_bound/5.png) 75519ms
2. на 2 воркерах: ![6.png](CPU_bound/6.png) 10778ms
3. на 4 воркерах: ![7.png](CPU_bound/7.png) 2308ms (у меня 4 ядра)
4. на 5 воркерах: ![8.png](CPU_bound/8.png) 43114ms
5. на 10 воркерах: ![9.png](CPU_bound/9.png) 1477ms
   (время все равно зависит от рандома)