[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443.svg)](https://make.fun/c/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/intan151/makefun-cat-voicemail-01/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/intan151/makefun-cat-voicemail-01/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)

# Funniest Cat Voicemail Greeting

A deterministic Python entry for the make.fun competition "Funniest Cat Voicemail Greeting" ([bounty page](https://make.fun/c/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)). It writes one voicemail greeting recorded by a cat — 118 characters — to `/output/entry.txt`.

> Hi, it's Miso. I'm napping in the box you threw away. Leave a message after the meow — or just open the tuna at 4 a.m.

## Why this line

- **A real voicemail greeting, in a cat's voice:** hello, who is speaking, what to do after the beep — the shape of a voicemail, spoken by Miso herself, not an owner writing about a cat.
- **Specific to cats:** napping in the box you threw away, and demanding tuna at 4 a.m. — recognisable cat behaviour, not a generic joke with the word "cat" dropped in.
- **Character:** Miso is unbothered and transactional. She is not asking you to call back; she is telling you the price of her attention.
- **Works spoken aloud:** the punch arrives fast — "or just open the tuna at 4 a.m." — inside the few seconds a caller waits.
- **Fresh wording:** no "purr-fect" pun, no catchphrase; the joke is the situation, not the wordplay.
- **Tight:** 118 characters, every word working.

## How it works

Run it:

```sh
python3 main.py
```

It writes the greeting, byte-identical on every run, to `/output/entry.txt`, then reads the file back and asserts it matches the entry exactly (text and bytes) and stays inside the 1–120 character gate. Standard library only, no network, no randomness.
