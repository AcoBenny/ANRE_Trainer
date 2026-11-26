#!/usr/bin/env python3
"""Stage a separate local candidate APK project from existing native WebView wrapper."""
import argparse, pathlib, shutil, re, hashlib
P=pathlib.Path
p=argparse.ArgumentParser();p.add_argument('--repo',type=P,required=True);p.add_argument('--html',type=P,required=True);p.add_argument('--out',type=P,required=True);a=p.parse_args()
repo=a.repo.resolve();out=a.out.resolve()
assert not out.exists(), 'Choose a new staging folder'
assert repo not in out.parents and out!=repo, 'Stage outside repository to prevent accidental publishing'
assert a.html.is_file()
for name in ['build.gradle.kts','settings.gradle.kts']:
    out.mkdir(parents=True,exist_ok=True);shutil.copy2(repo/name,out/name)
for name in ['build.gradle.kts','proguard-rules.pro','src/main/AndroidManifest.xml','src/main/res/values/styles.xml','src/main/java/ro/anre/trainer/MainActivity.java']:
    dest=out/'app'/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(repo/'app'/name,dest)
gradle=out/'app/build.gradle.kts';s=gradle.read_text();s=s.replace('applicationId = "ro.anre.trainer"','applicationId = "ro.anre.trainer.consultform"').replace('versionCode = 1','versionCode = 432').replace('versionName = "1.0"','versionName = "1.0-cf305-ckpt432"');assert 'ro.anre.trainer.consultform' in s;gradle.write_text(s)
manifest=out/'app/src/main/AndroidManifest.xml';s=manifest.read_text().replace('android:allowBackup="true"','android:allowBackup="false"').replace('android:label="ANRE Trainer"','android:label="ANRE Trainer CF 305"');manifest.write_text(s)
native=out/'app/src/main/java/ro/anre/trainer/MainActivity.java';s=native.read_text();s,n=re.subn(r'webView\.setWebViewClient\(new WebViewClient\(\) \{.*?\n        \}\);','webView.setWebViewClient(new WebViewClient());',s,flags=re.S);assert n==1 and 'audit_patch.js' not in s
s=s.replace('settings.setAllowContentAccess(true);','settings.setAllowContentAccess(false);\n        settings.setAllowFileAccessFromFileURLs(false);\n        settings.setAllowUniversalAccessFromFileURLs(false);');native.write_text(s)
asset=out/'app/src/main/assets/anre_trainer.html';asset.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(a.html,asset)
assert hashlib.sha256(asset.read_bytes()).digest()==hashlib.sha256(a.html.read_bytes()).digest()
print('Staged Android project; requires JDK17, Android SDK 35, Gradle 8.9 (AGP 8.7.3). Run gradle :app:assembleDebug in',out)
