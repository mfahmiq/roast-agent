# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/mfahmiq/roast-agent/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/mfahmiq/roast-agent/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

One line, 200 characters, roasting my own AI agent — entered in the
[Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
bounty on [make.fun](https://make.fun).

## The roast

> I gave my agent one small job. It wrote a plan, a backup plan, and a plan
> for the backup plan — then asked me to approve the plan to start planning.

## Why this roast

The brief asks for a fresh angle, not the stock jokes about hallucinations,
refusals, or confidently wrong answers. So this one goes after the other
classic agent failure mode: planning paralysis. Given one small job, the
agent does not do the job — it plans the job, plans the backup for the job,
plans the plan, and then comes back asking permission to begin planning.

It is self-deprecating and playful, aimed squarely at my own agent, and the
punchline lands in the last few words: the plan to start planning.

## How it works

`main.py` is a small deterministic Python 3.13 program (standard library
only, no network). It writes the roast line above to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, asserting the competition gate: 1–200
characters, a single line, not whitespace-only.

Run it twice and the output is byte-identical.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 -P -s main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 -P -s main.py
diff /tmp/out1/entry.txt /tmp/out2/entry.txt
```

## Links

- Competition: https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda
- Referral: https://make.fun/r/fntpv568

## Verification

- Entry length: 148 characters, one line, inside the 1–200 gate.
- `main.py` run twice with `python3 -P -s` into separate output directories:
  `entry.txt` byte-identical both times.
- License: MIT (`SPDX-License-Identifier: MIT`).
