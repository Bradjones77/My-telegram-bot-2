for filepath, content in files.items():
    full_path = os.path.join(project_name, filepath)
    folder = os.path.dirname(full_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
print("All files created.")
