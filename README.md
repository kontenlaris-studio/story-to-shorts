# Story-to-Shorts Studio

One topic in — a complete 45–60s Shorts production pack out: hook-first script, scene list with timings, overlays, title + hashtags, and a `script.txt` in the exact format the [Talking-Head Kit](https://github.com/kontenlaris-studio/talking-head-kit) renders.

**Live studio:** https://kontenlaris-studio.github.io/story-to-shorts/

## Offline core

```
python3 studio.py --topic "Why products get views but no sales" \
    --angle mistake --facts facts.txt --out pack/
```

Angles: `mistake` · `history` · `myth` · `numbers` · `story`. Facts are yours (one per line, verifiable); the core guarantees structure: hook ≤ 3s, one idea per sentence, a mid-point turn, a comment-earning close, 110–150 words.

A real sample pack (built from a real store's real numbers) is in `sample-pack/`.

## The chain

Trend Scout finds the topic → **Story-to-Shorts writes it** → Talking-Head Kit films it → ClipSmith cuts it. Each link is a standalone free tool by Kontenlaris Studio; together they are a faceless-content factory with no blank page anywhere in it.

MIT.
