# One-Line Robot Wedding Vows

[![make.fun](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=makefun&utm_medium=referral&utm_campaign=2wht1jqa)
[![Rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/irwan11795/makefun-u-kreutzx-one-line-robot-wedding-vows-a154ba4b/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=makefun&utm_medium=referral&utm_campaign=2wht1jqa)
[![Reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/irwan11795/makefun-u-kreutzx-one-line-robot-wedding-vows-a154ba4b/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=makefun&utm_medium=referral&utm_campaign=2wht1jqa)

One line. One vow. Two robots, forever (or until the next firmware update).

## The Vow

> From this day forward, I promise to share my charger, my backups, and my last 1% of battery — and to love you even when your firmware forgets me.

A wedding vow first, a robot joke second: a real promise ("from this day forward, I promise…"), machine-specific stakes (charger, backups, 1% battery, firmware), and the laugh lands on the last words — the robot who forgets the one it just married.

## Run

```bash
python3 main.py
```

This writes `entry.txt` (UTF-8, no trailing newline) to `MAKEFUN_OUTPUT_DIR` if set, otherwise `/output`, otherwise `output/` in this repo, otherwise a temp directory. The entry is validated before writing: 1–160 characters, exactly one line, not whitespace-only.

## Requirements

- Python 3 (stdlib only, no network)

## License

MIT — see [LICENSE](LICENSE).
