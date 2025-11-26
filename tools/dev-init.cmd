@echo off
set TEMPLATE=%1
set PROJECT=%2
set DEST=C:\dev-mk\playground\%PROJECT%

if "%TEMPLATE%"=="" (
    echo 사용법: dev-init.cmd 템플릿명 프로젝트명
    exit /b
)

if "%PROJECT%"=="" (
    echo 사용법: dev-init.cmd 템플릿명 프로젝트명
    exit /b
)

if not exist C:\dev-mk\templates\%TEMPLATE% (
    echo ❌ 템플릿이 존재하지 않아요: %TEMPLATE%
    exit /b
)

xcopy /E /I /Y C:\dev-mk\templates\%TEMPLATE% %DEST%
cd %DEST%
code .