@echo off
title Push Electric Vehicle Market Insights to GitHub
echo =======================================================================
echo ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS - GITHUB SYNC
echo Target Repository: https://github.com/sanjanaarathore/ev-market-insights.git
echo Branch: main
echo =======================================================================
echo.

set "PATH=C:\Program Files\Git\cmd;C:\Program Files\Git\ucrt64\bin;C:\Users\Sanjana\AppData\Local\Programs\Git\cmd;%PATH%"

echo Checking Git status...
git status --short
echo.
echo Initiating git push to GitHub...
echo (If prompted, your browser will open to authorize GitHub with 1 click)
echo.

git push -u origin main

echo.
echo =======================================================================
if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Repository pushed to GitHub successfully!
    echo Visit: https://github.com/sanjanaarathore/ev-market-insights
) else (
    echo [NOTICE] Push exited with code %ERRORLEVEL%.
)
echo =======================================================================
echo.
pause
