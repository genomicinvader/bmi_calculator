[Setup]
AppName=BMI Calculator
AppVersion=1.0
AppPublisher=HealthTech
DefaultDirName={autopf}\BMI Calculator
DefaultGroupName=BMI Calculator
OutputBaseFilename=BMI_Calculator_Setup
OutputDir=installer
Compression=lzma
SolidCompression=yes
SetupIconFile=icon.ico
UninstallDisplayIcon={app}\icon.ico

[Files]
Source: "dist\BMICalculator.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\BMI Calculator"; Filename: "{app}\BMICalculator.exe"; IconFilename: "{app}\icon.ico"
Name: "{commondesktop}\BMI Calculator"; Filename: "{app}\BMICalculator.exe"; IconFilename: "{app}\icon.ico"

[Run]
Filename: "{app}\BMICalculator.exe"; Description: "Run BMI Calculator"; Flags: postinstall nowait skipifsilent