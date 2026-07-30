@echo off
setlocal enabledelayedexpansion

set /p target_folder="Enter folder path (or press Enter for current folder): "
if "!target_folder!"=="" set "target_folder=."

pushd "!target_folder!" 2>nul
if errorlevel 1 exit /b

for %%F in (*) do (
    if "%%~nxF" neq "%~nx0" (
        set "ext=%%~xF"
        if "!ext!"=="" (
            set "folder_name=unknown"
        ) else (
            set "folder_name=!ext:~1!"
        )
        if not exist "!folder_name!\" mkdir "!folder_name!"
        move /y "%%F" "!folder_name!\" >nul
    )
)

popd
