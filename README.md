# DGM4MICCAI conference website

## Generating the static page

Install astral uv.

Run

```bash
uv run python3 generate.py
```

to generate `index.html` in the root directory.
Make sure to add and commit `index.html` to apply changes to the website.

## Extending the submission deadline

In `config.json`, change `extendedsubmissiondeadline` to the extended deadline.
