# Create New Programming Assignment

Assignments live in `assignments/<id>/`, and the website reads `config.json` to display them.

## Gather Requirements

If the user has not specified an assignment topic, ask what programming concept it should cover. Read [references/assignment-guide.md](references/assignment-guide.md) for guidance on appropriate scope, difficulty, and starter code.

## Create the Assignment

1. Create `assignments/<kebab-case-id>/README.md` using the [assignment template](../../../templates/assignment-template.md).
2. Add starter code or data files in the assignment directory when they support the learning objective.

## Register the Assignment

Use the bundled scripts instead of editing `config.json` manually.

Register the assignment:

```sh
node .github/skills/new-assignment/scripts/update-config.js <id> "<title>" "<description>"
```

Register each starter or data file:

```sh
node .github/skills/new-assignment/scripts/add-attachment.js <id> "<display-name>" <filename> <type>
```

Common attachment types are `python`, `csv`, `json`, `txt`, and `html`.

## Verify

Confirm the assignment appears in `config.json` and that every created assignment file exists on disk.
