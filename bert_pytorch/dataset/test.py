

with open('corpus.small', 'r', encoding='utf-8') as f:
    content = f.read()

    # Step 2: Replace literal escape sequences with actual characters
    content = content.replace('\\t', '\t').replace('\\n', '\n')

    # Step 3: Display the modified content (for debugging)
    print(repr(content))  # This will show the actual special characters (e.g., \t, \n)

    # Step 4: Optionally, count occurrences of tabs and newlines
    tabs = content.count('\t')
    newlines = content.count('\n')

    print(f"Number of tabs: {tabs}")
    print(f"Number of newlines: {newlines}")