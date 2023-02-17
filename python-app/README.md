# Python App on Space

This minimal template is an example of a Space app built with Python and [FastAPI](https://fastapi.tiangolo.com).

## Setup

1. If you don't already have a Space account, create one for free [here](https://deta.space/signup).
2. Install the Space CLI and link your Space account to the CLI. Instructions to do that can be found [here](https://deta.space/docs/en/basics/cli).
3. Run the `space new` command inside the root of your project to create a new builder project on Space.

## Project Structure

```tree
.
├── main.py
├── requirements.txt
├── Spacefile
└── Discovery.md
```

- `main.py`: This is the entry point of your app, and it contains the code to run your app. Do not change the name of this file. It must contain an identifier `app` which is an instance of an **ASGI** (e.g. FastAPI) or **WSGI** (e.g. Flask) application.

- `requirements.txt`: This optional file contains your app's dependencies. It is recommended to pin versions of packages (e.g. `deta~=1.1.0`) in order to avoid issues without outdated packages or version conflicts. Read more about version pinning [here](https://medium.com/knerd/best-practices-for-python-dependency-management-cc8d1913db82).

- `Spacefile`: This is the configuration file used by Space to build and deploy your app. To learn more please refer to the [Spacefile](https://deta.space/docs/en/reference/spacefile#whats-the-spacefile) guide.

- `Discovery.md`: This optional file contains information about your app to display on the [Space App Marketplace](https://deta.space/discovery). To learn more please refer to the [Discovery.md](https://deta.space/docs/en/reference/discovery) guide.

## Important

Running `space new` will create a `.space` directory inside your project. This directory contains sensitive information about your app and is used by the Space CLI to push your app to Space. Do not change the name of the directory, include it in any version control software, or add it to repositories.
