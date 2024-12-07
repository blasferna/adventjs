def fix_packages(packages):
    lopen = -1
    fclose = -1
    i = 0
    for c in packages:
        if c in "(":
            lopen = i
        if c in ")":
            fclose = i
            break
        i += 1
    to_replace = packages[lopen + 1 : fclose]
    packages = packages.replace(f"({to_replace})", to_replace[::-1])
    if "(" in packages:
        return fix_packages(packages)
    else:
        return packages
