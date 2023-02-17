# Deno App on Space

This minimal template is an example of a Space app built with [Deno](https://deno.land).

## Setup

1. If you don't already have a Space account, create one for free [here](https://deta.space/signup).
2. Install the Space CLI and link your Space account to the CLI. Instructions to do that can be found [here](https://deta.space/docs/en/basics/cli).
3. Run the `space new` command inside the root of your project to create a new builder project on Space.

## Project Structure

```text
.
├── static
│   └── index.html
├── main.ts
├── Spacefile
└── Discovery.md
```

- `static`: This directory contains all the static files that your app needs to run.
  
- `main.ts`: This is the entry point of your app. You can write your server logic here.
  
- `Spacefile`: This is the configuration file used by Space to build and deploy your app. To learn more please refer to the [Spacefile](https://deta.space/docs/en/reference/spacefile#whats-the-spacefile) guide.

- `Discovery.md`: This optional file contains information about your app to display on the [Space App Marketplace](https://deta.space/discovery). To learn more please refer to the [Discovery.md](https://deta.space/docs/en/reference/discovery) guide.

## Important

Running `space new` will create a `.space` directory inside your project. This directory contains sensitive information about your app and is used by the Space CLI to push your app to Space. Do not change the name of the directory, include it in any version control software, or add it to repositories.

In this example the Spacefile contains custom commands to compile and run your app. Be sure to update the commands according to your project structure and requirements.

## More Resources

- [Oden - Deno on Space](https://github.com/abdelhai/oden)
