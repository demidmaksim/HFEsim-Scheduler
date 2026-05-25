import PyInstaller.__main__

PyInstaller.__main__.run(
    [
        "app.py",
        "--onefile",
        "--noconsole",
        "--name=ScheduleCreatorApp V2.1.4",
    ]
)
