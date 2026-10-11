# Prints the Gradle failure as one GitHub annotation so it can be read without the full log.
log = open('build.log', errors='replace').read().splitlines()
keep = []
for i, l in enumerate(log):
    if 'What went wrong' in l:
        keep += log[max(0, i - 2):i + 20]
    elif l.startswith('e: ') or 'error:' in l:
        keep.append(l)
msg = '\n'.join(keep[:70]) or '\n'.join(log[-40:])
msg = msg.replace('%', '%25').replace('\r', '%0D').replace('\n', '%0A')
print('::error title=Gradle::' + msg)
