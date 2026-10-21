import os
import shutil

print("[*] Preparando estructura para la app web...")
os.makedirs("app/src/main/assets", exist_ok=True)
if os.path.exists("www"):
    shutil.copytree("www", "app/src/main/assets/www", dirs_exist_ok=True)
print("[+] Archivos web copiados con éxito.")

import subprocess

print("[*] Creando archivo MainActivity.java para el WebView...")
os.makedirs("app/src/main/java/com/cineapp/tv", exist_ok=True)

activity_code = """package com.cineapp.tv;
import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebSettings;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        WebView myWebView = new WebView(this);
        WebSettings webSettings = myWebView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webSettings.setDomStorageEnabled(true);
        myWebView.loadUrl("file:///android_asset/www/index.html");
        setContentView(myWebView);
    }
}
"""

with open("app/src/main/java/com/cineapp/tv/MainActivity.java", "w") as f:
    f.write(activity_code)

print("[+] MainActivity.java creado correctamente.")

print("[*] Creando AndroidManifest.xml...")
manifest_content = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.cineapp.tv">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-feature android:name="android.software.leanback" android:required="false" />
    <uses-feature android:name="android.hardware.touchscreen" android:required="false" />

    <application
        android:label="CineApp TV"
        android:icon="@android:drawable/ic_menu_slideshow"
        android:usesCleartextTraffic="true">
        
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:screenOrientation="landscape">
            
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
                <category android:name="android.intent.category.LEANBACK_LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
"""

os.makedirs("app/src/main", exist_ok=True)
with open("app/src/main/AndroidManifest.xml", "w") as f:
    f.write(manifest_content)

print("[+] AndroidManifest.xml creado correctamente.")

print("[*] Creando build.gradle...")
build_gradle = """buildscript {
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:7.4.2'
    }
}

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}

apply plugin: 'com.android.application'

android {
    compileSdkVersion 33
    defaultConfig {
        applicationId "com.cineapp.tv"
        minSdkVersion 21
        targetSdkVersion 33
        versionCode 1
        versionName "1.0"
    }
}
"""

with open("build.gradle", "w") as f:
    f.write(build_gradle)

print("[+] build.gradle creado correctamente.")
