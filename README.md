# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/raina027/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/raina027/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in exactly 4,096 bytes of Python: 0x88 board, PeSTO midgame
evaluation, alpha-beta search with quiescence, MVV-LVA move ordering, and
iterative deepening to depth 16 on a fixed 60,000-node budget per move
(~1.4 s/move, deterministic). Perft verified: startpos d3 8,902, d4 197,281;
Kiwipete d3 97,862; pos3 d3 2,812; pos4 d3 9,467.

## Run it

```sh
MAKEFUN_ENV_URL=http://localhost:PORT python3 main.py
```

The engine talks to the make.fun harness over HTTP (`POST /game`, `POST /move`)
and answers every position with a UCI move.
