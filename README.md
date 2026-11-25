# Notes From a Passive-Aggressive Fridge

[![make.fun · u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![rank](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/indraHA01/makefun-u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/rank.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![reward](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/indraHA01/makefun-u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/reward.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)

One funny passive-aggressive note a smart fridge leaves for its owner — an entry for the [make.fun](https://make.fun) bounty "Notes From a Passive-Aggressive Fridge". The fridge counts your door openings, the yogurt is its witness, and it takes sides — against you.

## The entry

> You opened me 14 times today, took nothing, and left the door ajar. The yogurt filed a complaint. I signed it.

110 characters, one line, exactly what the fridge would keep on its door screen.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` is deterministic — no network, no randomness, no clock — and writes the note to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set). It runs the same way twice and produces byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
