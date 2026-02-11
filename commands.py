class AllCommands:
    # basic commands
    BASIC_COMMANDS = {
        "about": "See current version of [bold]refer[/bold] with their respective features",
        "usage": "See the basic [bold]DOCUMENTATION[/bold] about how to use [bold]refer[/bold]",
        "contribute": "Redirects you to [green]refer's official Github repository[/green]",
        "wheredb": "See the path of refer's local DB folder",
        "changedb <path>": "Change refer's local DB folder location [green](Without lossing data)[/green]"

    }

    # packages management commands
    MANAGEMENT_COMMANDS = {
        "addpkg -name \'name\' -path \'path\'": {
            "for": "Add new package / project folder path to your collection",
            "example": "addpkg -name \'clitool\' -path \'C:\\Users\\<name>\\Myprojects\\tool\'"
        },
        "updatepkg -name \'name\' -path \'path\'": {
            "for": "Update existing package / project folder path by reupload it",
            "example": "updatepkg -name \'clitool_modified\' -path \'C:\\Users\\<name>\\Myprojects\\modifyed\'"
        },
        "listpkgs": {
            "for": "See list of all existing packages",
            "example": "listpkgs"
        },
        "listpkg -name \'name\'": {
            "for": "See one specific package path",
            "example": "listpkg -name \'myclitool\'"
        },
        "delpkg -name \'name\'": {
            "for": "Delete & Remove existing package / project folder path from your collection",
            "example": "delpkg -name \'clitool\'"
        },
        "renamepkg -from \'old_name\' -to \'new_name\'": {
            "for": "Rename any existing package / project folder path of your collection",
            "example": "renamepkg -from \'clitool\' -to \'myclitool\'"
        },
    }

    # referral commands
    REFERRAL_FROM_DB = {
        "refer -pkg \'name\'": {
            "for": "Quick share single package with your friends. By doing this Refer use to generate quick one click downloadable link of your package that you want's to refer, by doing this your friend can be able to download that package instantly directly from your system without single any issue",
            "example": "refer -pkg \'guiapp\'"
        },
        "referwith -message \'your message\' -pkgs \'name of packages\'": {
            "for": "Share multiple packages with a single proper message. By doing this it will creates a basic HTML webpage with proper message and downloadable links in structured manner",
            "example": "referwith -message \'This is a GUI apps for xyz.\' -name \'gui_app1 gui_app2 gui_app3\'"
        },
        "referwith -template -message \'your message\' -pkgs \'name of packages\'": {
            "for": "Share multiple packages in available webpage template. After running command refer display all available templates options, you can choose any one of them ",
            "example": "referwith -template -message \'This is the cli tools for xyz.\' -pkgs \'cli_app1 cli_app2 cli_app3\'"
        },
    }
    REFERRAL_FROM_LOCAL = {
        "refer -path \'path\'": {
            "for": "Quick share single package with your friends. By doing this Refer use to generate quick one click downloadable link of your package that you want's to refer, by doing this your friend can be able to download that package instantly directly from your system without single any issue",
            "example": "refer -path \'C:\\Users\\<name>\\Myprojects\\tool\'"
        },
        "referwith -message \'your message\' -paths \"path1\" \"path2\" \"path3\"": {
            "for": "Share multiple packages with a single proper message. By doing this it will creates a basic HTML webpage with proper message and downloadable links in structured manner",
            "example": "referwith -message \'This is a GUI apps for xyz.\' -paths \"C:\\Users\\<name>\\CLITools\\cli_tool1\\\" \"C:\\Users\\<name>\\CLITools\\cli_tool2\\\""
        },
        "referwith -template -message \'your message\' -paths \"path1\" \"path2\" \"path3\"": {
            "for": "Share multiple packages in available webpage template. After running command refer display all available templates options, you can choose any one of them ",
            "example": "referwith -template -message \'This is the cli tools for xyz.\' -paths \"C:\\Users\\<name>\\CLITools\\cli_tool1\\\" \"C:\\Users\\<name>\\CLITools\\cli_tool2\\\""
        },
    }
