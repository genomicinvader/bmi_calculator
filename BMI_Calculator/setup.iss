[Setup]
AppName=BMI Calculator
AppVersion=1.0
AppPublisher=Sheikh Md. Mahtabur Rahman
AppPublisherURL=https://github.com/genomicinvader
AppSupportURL=https://github.com/genomicinvader
AppUpdatesURL=https://github.com/genomicinvader/bmi-calculator
AppContact=https://github.com/genomicinvader
AppCopyright=Copyright © 2025 Sheikh Md. Mahtabur Rahman
DefaultDirName={autopf}\BMI Calculator
DefaultGroupName=BMI Calculator
OutputBaseFilename=BMI_Calculator_Setup
OutputDir=installer
Compression=lzma
SolidCompression=yes
SetupIconFile=icon.ico
UninstallDisplayIcon={app}\icon.ico
WizardStyle=modern
LicenseFile=LICENSE.txt

[Files]
Source: "dist\BMICalculator.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "LICENSE.txt"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\BMI Calculator"; Filename: "{app}\BMICalculator.exe"; IconFilename: "{app}\icon.ico"
Name: "{commondesktop}\BMI Calculator"; Filename: "{app}\BMICalculator.exe"; IconFilename: "{app}\icon.ico"
Name: "{group}\Uninstall BMI Calculator"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\BMICalculator.exe"; Description: "Launch BMI Calculator"; Flags: postinstall nowait skipifsilent

[Registry]
; Register publisher URL
Root: HKA; Subkey: "Software\Sheikh Md. Mahtabur Rahman"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Sheikh Md. Mahtabur Rahman\BMI Calculator"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Sheikh Md. Mahtabur Rahman\BMI Calculator"; ValueType: string; ValueName: "PublisherURL"; ValueData: "https://github.com/genomicinvader"

; Register contact protocol
Root: HKA; Subkey: "Software\Classes\genomicinvader"; ValueType: string; ValueData: "URL:GenomicInvader Contact"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\genomicinvader"; ValueType: string; ValueName: "URL Protocol"; ValueData: ""
Root: HKA; Subkey: "Software\Classes\genomicinvader\DefaultIcon"; ValueType: string; ValueData: "{app}\BMICalculator.exe,0"
Root: HKA; Subkey: "Software\Classes\genomicinvader\shell\open\command"; ValueType: string; ValueData: "explorer ""https://github.com/genomicinvader"""

[Code]
procedure InitializeWizard();
begin
  WizardForm.LicenseAcceptedRadio.Checked := True;
end;

procedure CurPageChanged(CurPageID: Integer);
begin
  if CurPageID = wpFinished then
  begin
    WizardForm.FinishedLabel.Caption := 'BMI Calculator has been installed on your computer.' + #13#10 +
      'Developed by Sheikh Md. Mahtabur Rahman' + #13#10 +
      'Contact: +8801711434897 | github.com/genomicinvader';
  end;
end;
