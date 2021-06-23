import cx_Freeze
executables = [cx_Freeze.Executable(
    script="testejogo.py", icon="assets/bolinho.ico")]

cx_Freeze.setup(
    name="Saúde bucal",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["assets"]
        }},
    executables=executables
)
