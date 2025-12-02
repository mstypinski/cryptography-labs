# Dependency management
Before you start, please update system packages database
```
sudo apt update
```

Later, install `uv`
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install python dependencies
```
uv sync
```

Later, start using Python `venv`.

```
source .venv/bin/activate
```

> Please mind once you change the terminal window or close it, the `source` command will need to be rerun.

Lasty, change directory to proper one and work on laboratory.

```
cd labN
```