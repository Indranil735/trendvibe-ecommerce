import glob

jsp_files = glob.glob('src/main/webapp/**/*.jsp', recursive=True)
print(f'Checking {len(jsp_files)} JSP files...')
issues = []
for jsp in jsp_files:
    with open(jsp, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for idx, line in enumerate(lines):
        if '${' in line:
            start = 0
            while True:
                s_idx = line.find('${', start)
                if s_idx == -1: break
                e_idx = line.find('}', s_idx)
                if e_idx == -1: break
                expr = line[s_idx:e_idx+1]
                if '<' in expr or '>' in expr:
                    issues.append(f'{jsp}:{idx+1}: {expr} in line: {line.strip()}')
                start = e_idx + 1

if issues:
    print('Found EL issues:')
    for iss in issues:
        print(iss)
else:
    print('No EL < or > issues found!')
