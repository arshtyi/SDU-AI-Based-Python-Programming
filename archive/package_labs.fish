#!/usr/bin/env fish

set -l script_dir (path resolve (path dirname (status filename)))
set -l project_root (path dirname "$script_dir")
set -l student '202400130242_彭靖轩'

for lab_dir in "$project_root"/lab/*
    test -d "$lab_dir"; or continue

    set -l n (path basename "$lab_dir")
    string match -rq '^[0-9]+$' -- "$n"; or continue

    set -l prefix "lab/$n/"
    set -l files

    for file in (git -C "$project_root" ls-files --cached --others --exclude-standard -z -- "$prefix" | string split0)
        string match -rq '(^|/)solution(/|$)' -- "$file"; and continue

        set -l relative_file (string replace -- "$prefix" '' "$file")
        set -a files "./$relative_file"
    end

    set -l output (string join '' "$script_dir/" "$student" '_lab' "$n" '.zip')
    rm -f "$output"

    pushd "$lab_dir" >/dev/null
    zip -q "$output" $files
    popd >/dev/null

    echo "Created $output"
end
