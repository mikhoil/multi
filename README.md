# multi
IO-bound
1) синхронная проверка ссылок на 1 потоке:![1.png](IO_bound/1.png) 1564963ms
2) синхронная проверка ссылок с 5 воркерами:![2.png](IO_bound/2.png) 237014ms
3) c 10: ![3.png](IO_bound/3.png) 124689ms
4) с 100: ![4.png](IO_bound/4.png) 25079ms

CPU-bound:
1. генерация монетки на 1 потоке: ![5.png](CPU_bound/5.png) 75519ms
2. на 5 воркерах