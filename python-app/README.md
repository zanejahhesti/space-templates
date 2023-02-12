# Python App On Space
This is a template to run Python App on Space that uses [FastAPI](https://fastapi.tiangolo.com/) as the web framework.

## Getting Started
To run it on Space, you need to have a Space account. If you don't have one, you can create one for free [here](https://deta.space/signup). Then install the Space CLI and link your Space account to the CLI. You can find the instructions to do that [here](https://deta.space/docs/en/basics/cli). Run command `space new` in the root of your project to create a new app on Space. This will create a `.space` folder in your project. You can then run `space push` to push your app to Space with the following file structure. 

## File Structure
```
.
├── main.py
├── requirements.txt
├── Spacefile
├── Discovery.md
└── .spaceignore
```

- `main.py` - This is the entry point of your app. This file contains the code to run your app. Do not change the name of this file. This file must contain an identifier `app` which is an instance of **asgi** (e.g. FastAPI) or **wsgi** (e.g. Flask).
  
- `requirements.txt` - This file contains the list of dependencies of your app. This file is optional. Add `deta` to this file to avoid issues with the old `deta-python-sdk`.
  
- `Spacefile` - This is the config file for space cli to deploy your app. To know more about this file please refer to [Spacefile](https://deta.space/docs/en/reference/spacefile#whats-the-spacefile) guide.
- `Discovery.md` - This file contains the information about your app to present on the [Space App Marketplace](https://deta.space/discovery).
  
- `.spaceignore` - This file contains the list of files and folders to ignore while deploying your app. This file is optional and follows the same syntax as `.gitignore`.
  
## Important
Do not change the name of the `.space` folder. This folder is used by the Space CLI to push your app on Space. This folder contains sensitive information about your app. Do not share this folder with anyone or push it to any public repository.
