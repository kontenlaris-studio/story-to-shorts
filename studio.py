#!/usr/bin/env python3
"""studio.py — Story-to-Shorts script-pack assembler (deterministic core).

Given a topic, an angle and your fact lines, it assembles a complete
production pack in the fixed short-form framework: hook (first 3s),
one idea per sentence, mid-point turn, comment-bait close, scene list,
overlay texts, title + hashtags, and a script.txt ready to feed the
Talking-Head Kit pipeline. The hosted app/skill writes the prose; this
core guarantees the structure and the timings.

Usage:
  python3 studio.py --topic "Why products get views but no sales" \
      --angle mistake --facts facts.txt --out pack/
Angles: mistake | history | myth | numbers | story
"""
import argparse, os, sys

HOOKS = {
    "mistake": "Stop. You're making the one mistake that kills {topic_low} — and it's not what you think.",
    "history": "In the beginning, {topic} was completely different. Then one change rewrote everything.",
    "myth": "Everything you believe about {topic} is wrong. Here is the proof.",
    "numbers": "The numbers behind {topic} make no sense — until you see this one.",
    "story": "This is the story of {topic} — and it does not end the way you expect.",
}
TURN = "But here is where it gets interesting."
CLOSE = "Agree or not? Tell me in the comments — and follow for part two."


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", required=True)
    ap.add_argument("--angle", default="mistake", choices=list(HOOKS))
    ap.add_argument("--facts", required=True, help="one fact per line")
    ap.add_argument("--out", default="pack")
    a = ap.parse_args()

    facts = [l.strip() for l in open(a.facts) if l.strip()]
    if not facts:
        print("facts file is empty", file=sys.stderr)
        return 1
    topic_low = a.topic[0].lower() + a.topic[1:]
    hook = HOOKS[a.angle].format(topic=a.topic, topic_low=topic_low)
    mid = max(1, len(facts) // 2)
    body1, body2 = facts[:mid], facts[mid:]
    sentences = [hook] + body1 + [TURN] + body2 + [CLOSE]
    script = " ".join(sentences)
    words = len(script.split())
    secs = round(words / 150 * 60)

    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "script.txt"), "w") as f:
        f.write(script + "\n")
    scenes = {
        hook: "HOOK — big text overlay, face/photo zoom-in",
        TURN: "TURN — pattern interrupt: cut, zoom or angle change",
        CLOSE: "CLOSE — comment prompt on screen",
    }
    with open(os.path.join(a.out, "pack.md"), "w") as f:
        f.write(f"# Story-to-Shorts pack — {a.topic}\n\n")
        f.write(f"Angle: {a.angle} · ~{words} words · ~{secs}s at 150 wpm\n\n")
        f.write("## Script (feed this to the Talking-Head pipeline)\n\n")
        f.write(script + "\n\n## Scene list\n\n")
        t = 0.0
        for s in sentences:
            d = len(s.split()) / 150 * 60
            note = scenes.get(s, "B-roll / supporting visual for this line")
            f.write(f"- [{t:05.1f}s–{t + d:05.1f}s] {note}\n  > {s}\n")
            t += d
        f.write("\n## Title & hashtags\n\n")
        f.write(f"{a.topic} — the part nobody tells you\n")
        tags = " ".join("#" + w for w in
                        ["shorts", "storytime"] +
                        [x.lower().replace(" ", "") for x in
                         a.topic.replace("—", " ").split()[:2]])
        f.write(tags + "\n")
    print(f"OK pack in {a.out}/ (script.txt + pack.md) — {words} words, ~{secs}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
