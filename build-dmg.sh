#!/bin/bash

# Creates the installer disk image and notarizes it.

arch=$(uname -m)
dmgName="PyQtPopupDemo-${arch}.dmg"

isCreateDmg=$(which -s create-dmg; echo $?)
test $isCreateDmg -eq 0
if [[ $? -ne 0 ]]; then
    echo "ERROR: create-dmg not found"
    exit 1
fi

rm -rf ./dist/PyQtPopupDemo

echo
echo "Enter the name of your Apple Developer ID Application signing identity."
echo "This should start with \"Developer ID Application: ...\""
read -p "Name: " devIDApp

appBundleName="PyQtPopupDemo.app"
test -f "${dmgName}" && rm "${dmgName}"

echo
echo "Enter the profile name of the keychain item where credentials for notarizing"
echo "are stored, e.g. \"Notarize\".  For more info, see:"
echo "https://developer.apple.com/documentation/security/customizing-the-notarization-workflow"
read -p "Profile name: " credProfName

create-dmg \
  --volname "PyQt Popup Demo" \
  --window-size 500 360 \
  --icon-size 96 \
  --icon "${appBundleName}" 100 160 \
  --app-drop-link 350 160 \
  --codesign "${devIDApp}" \
  --notarize "${credProfName}" \
  "${dmgName}" \
  ./dist

echo
echo "Generating SHA-512 checksum of DMG..."

sha512sum $dmgName > ${dmgName}.sha512
cat ${dmgName}.sha512
