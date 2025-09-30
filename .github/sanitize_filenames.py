import os, re, subprocess, sys, unicodedata

# Policy: replace spaces with '-', strip trailing dots/spaces, remove <>:"/\|?*,
# block reserved device names (case-insensitive) by suffixing '_'
RESERVED = re.compile(r'^(?i:(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9]))$')
ILLEGAL = re.compile(r'[<>:"/\\|?*]')

def sanitize_component(c: str) -> str:
    c = unicodedata.normalize('NFC', c)
    c = c.replace(' ', '-')
    c = ILLEGAL.sub('', c)
    c = c.rstrip(' .')
    if c == '':
        c = '_'
    if RESERVED.match(c):
        c = c + '_'
    return c

def sanitize_path(p: str) -> str:
    return '/'.join(sanitize_component(pc) for pc in p.split('/'))

# list tracked files
out = subprocess.check_output(['git', 'ls-files', '-z'])
files = [f for f in out.decode('utf-8').split('\x00') if f]

taken = set(files)
taken_lower = {x.lower() for x in taken}
renames = {}

for f in files:
    nf = sanitize_path(f)
    if nf == f:
        continue
    base_nf = nf
    i = 1
    while nf in taken or nf.lower() in taken_lower:
        root, ext = os.path.splitext(base_nf)
        nf = f"{root}-{i}{ext}"
        i += 1
    renames[f] = nf
    taken.add(nf)
    taken_lower.add(nf.lower())

if not renames:
    print("No filenames needed changes.")
    sys.exit(0)

for src, dst in renames.items():
    ddir = os.path.dirname(dst)
    if ddir and not os.path.exists(ddir):
        os.makedirs(ddir, exist_ok=True)
    subprocess.check_call(['git', 'mv', '-k', src, dst])

print("Renamed files:")
for src, dst in renames.items():
    print(f"  {src} -> {dst}")
