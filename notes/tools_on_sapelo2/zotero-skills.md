# zotero-skills: read-only trial without a Zotero account (2026-10-12)

What it is: a skill plus a Python client that lets an agent search, add, tag, annotate and merge
items in a Zotero library (local Zotero for reads, the Web API for writes).
I have no Zotero library or key on the cluster, so this was a limited trial.

What I ran:
- Its own test suite: 122 passed in 0.45 s (unit and mocked integration tests; no live library).
- A real read against a public Zotero group (id 2258643) with no key: search returned 5 items,
  4 collections listed; a write (create_note) was refused by Zotero with "An API key is required".
  The client needs a non-empty key to start, so for a key-less public read I had to swap its web
  client by hand.

What I found:
- status() reports web_api "connected" whenever a key string is set. It makes no request. With a
  made-up key it said "connected" and the first real request then failed. It is a check that
  cannot say no.
- get_tags() returned exactly 100 tags. I did not check whether the group has more, so this may be
  the first page only.
Not tested: every write path (add, tag, merge duplicates, attach PDF), which is most of what it is for.
Verdict: installs in a minute and the read path works. Before trusting it with a real library I would
test the write paths on a throwaway library, and not rely on status().
