# Monday, Reviewed in One Line

[![make.fun](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![Rank](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/m1651/makefun-monday-review/rank.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![Reward](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/m1651/makefun-monday-review/reward.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)

Entry for the [make.fun](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1) bounty **"Monday, Reviewed in One Line"** — write the funniest one-line review of your own Monday, under 200 characters, and nothing else.

## The entry

> Monday review: my inbox had 47 unread emails, my calendar had 9 meetings, and my will to live had already filed for PTO.

(120 characters, one line.)

## How it works

`main.py` is a small standard-library-only program (no network). It holds the
entry line as a constant, validates it against the competition gate — UTF-8,
a single line, no control characters, 1 to 200 characters, not only white
space — and writes it to `/output/entry.txt`. After writing, it reads the file
back and verifies the bytes match the validated text exactly.

Run it with:

```sh
python3 main.py
```

Then `/output/entry.txt` contains the one-line Monday review.
