rem generate exe file
rem pyinstaller --version-file=versionexe.txt --onefile --console --distpath exe -n bankparser "src\bankparser\bankparsercli.py"
pyinstaller --noupx --onefile --console --distpath exe -n bankparser "src\bankparser\bankparsercli.py" --upx-dir "..\upx" --hidden-import "bankparser.banks.vtb24" --hidden-import "bankparser.banks.admoney" --hidden-import "bankparser.banks.admoney-xml" --hidden-import "bankparser.banks.adshares"
pause