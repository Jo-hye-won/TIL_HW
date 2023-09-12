vscode 기본설정하기
- ctro + shift + p => json파일
- {
    "editor.tabSize": 2,
    // python
    "[python]": {
        "editor.tabSize": 4
    },

    "terminal.integrated.defaultProfile.windows": "Git Bash",
    "git.openRepositoryInParentFolders": "always",
    "terminal.integrated.enableMultiLinePasteWarning": false,

    // Django
    "files.associations": {
        "**/*.html": "html",
            "**/templates/**/*.html": "django-html",
        "**/templates/**/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },
    "emmet.includeLanguages": {
        "django-html": "html"
    }
}

SQLite = DB 열때 쉽게(??) 하려고 설치 
