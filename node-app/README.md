# NodeJS App On Space
This is a template to run NodeJS App on Space that uses [Express](https://expressjs.com/) as the web framework.

## Getting Started
1. First, you need to have a Space account. If you don't have one, you can create one for free [here](https://deta.space/signup). 
2. Then install the Space CLI and link your Space account to the CLI. You can find the instructions to do that [here](https://deta.space/docs/en/basics/cli). 
3. Run command `space new` inside the root of your project to create a new app on Space. The project structure should look like the following.

## Project Structure
```
.
├── index.js
├── package.json
├── Spacefile
├── Discovery.md
└── .spaceignore
```
- `index.js` is the entry point of your app. It contains the code to start the server.
  
- `package.json` contains the dependencies of your app. 
  
- `Spacefile` - This is the config file for space cli to push your app  in Space. To know more about this file please refer to [Spacefile](https://deta.space/docs/en/reference/spacefile#whats-the-spacefile) guide.

- `Discovery.md` - This file contains the information about your app to present on the [Space App Marketplace](https://deta.space/discovery). To know more about this file please refer to [Discovery.md](https://deta.space/docs/en/reference/discovery) guide.
  
- `.spaceignore` - This file contains the list of files and directories to ignore while deploying your app. This file is optional and follows the same syntax as *.gitignore*.
  
## Important
> Running `space new` will create a **.space** directory inside your project. This contains sensitive information about your app and is used by the Space CLI to push your app on Space. Do not change the name of the directory or push it to any public repository.