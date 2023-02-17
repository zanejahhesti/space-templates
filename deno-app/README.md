# Deno App on Space

This minimal template is an example of a Space app built with [Deno](https://deno.land).

## Getting Started

1. First, you need to have a Space account. If you don't have one, you can create one for free [here](https://deta.space/signup).
2. Then install the Space CLI and link your Space account to the CLI. You can find the instructions to do that [here](https://deta.space/docs/en/basics/cli).
3. Run the command `space new` inside the root of your project to create a new app on Space. The project structure should look like the following.

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
