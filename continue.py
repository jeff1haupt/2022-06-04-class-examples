resident_state = []
nonresdient_state = []
for i in ['IL', 'IN', 'IL', 'OH', 'MI']:
    if i == 'IL':
        resident_state.append(i)
        continue
    nonresdient_state.append(i)

print(resident_state)
print(nonresdient_state)

    