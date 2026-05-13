class Commands:
    # basic commands
    BASIC_COMMANDS = {
        "about": "See current version of [bold]refer[/bold] with their respective features",
        "usage": "See the basic [bold]DOCUMENTATION[/bold] about how to use [bold]refer[/bold]",
        "contribute": "Redirects you to [green]refer's official Github repository[/green]",
    }
    
    # referral commands
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
