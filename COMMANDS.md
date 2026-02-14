# refer — Command Reference

Here is the lists of all available `refer` commands with short descriptions and examples. Run `usage` in the app for full, richly formatted documentation.

## Basic commands
- `about` — Show project description and version.
	- Example: `about`

- `usage` — Show detailed usage documentation and quick reference.
	- Example: `usage`

- `contribute` — Open the project's GitHub repository in your web browser.
	- Example: `contribute`

- `wheredb` — Show configured `referdb` folder location.
	- Example: `wheredb`

- `changedb <path>` — Move the `referdb` folder to a new location (keeps data when possible).
	- Example: `changedb C:\Users\You\MyReferLocation`

## Management commands (manage packages stored in the local DB)
- `addpkg -name 'name' -path 'path'` — Add a package record (name → path).
	- Example: `addpkg -name 'clitool' -path 'C:\Users\John\Myprojects\tool'`

- `updatepkg -name 'name' -path 'path'` — Update path for an existing package.
	- Example: `updatepkg -name 'clitool' -path 'C:\Users\John\Myprojects\modified'`

- `listpkgs` — List all packages (name and path) stored in `packages.json`.
	- Example: `listpkgs`

- `listpkg -name 'name'` — Show the path for a single package.
	- Example: `listpkg -name 'myclitool'`

- `delpkg -name 'name'` — Delete a package record from the DB.
	- Example: `delpkg -name 'clitool'`

- `renamepkg -from 'old_name' -to 'new_name'` — Rename an existing package entry.
	- Example: `renamepkg -from 'clitool' -to 'clitool_pro'`

## Referral / sharing commands (generate download links or HTML pages)
Commands are provided in two flavors: sharing from the DB (refer by package name) and sharing directly from local paths.

### From DB (refer by package names stored in `packages.json`)
- `refer -pkg 'name'` — Generate a one-click downloadable link for a single DB package.
	- Example: `refer -pkg 'guiapp'`

- `referwith -message 'your message' -pkgs 'pkg1 pkg2 pkg3'` — Create an HTML page listing multiple DB packages with a custom message and download links.
	- Example: `referwith -message 'This is a GUI apps for xyz.' -pkgs 'gui_app1 gui_app2 gui_app3'`

- `referwith -template -message 'your message' -pkgs 'pkg1 pkg2'` — Same as above but choose a template for the generated page.
	- Example: `referwith -template -message 'Collection of tools' -pkgs 'cli_app1 cli_app2'`

### From local paths (share folders without adding to DB)
- `refer -path 'C:\\path\\to\\project'` — Generate a one-click downloadable link for a local folder.
	- Example: `refer -path 'C:\\Users\\John\\Myprojects\\tool'`

- `referwith -message 'your message' -paths "path1" "path2"` — Create an HTML page to share multiple local folders with a message.
	- Example: `referwith -message 'Try these tools' -paths "C:\\Folder1" "C:\\Folder2"`

- `referwith -template -message 'your message' -paths "path1" "path2"` — Use a template for the generated sharing page.
	- Example: `referwith -template -message 'My collection' -paths "C:\\Folder1" "C:\\Folder2"`

## Notes & tips
- The app stores credentials and DB location in `referconfig.yaml`. Run the CLI and follow prompts to create it.
- Use simple package names (no special characters) when adding records to the DB.
- When sharing many packages by name, provide space-separated package names inside the `-pkgs` quoted string.

