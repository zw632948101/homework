## Mac配置appium
##### 1. 下载xcode，App Store下载xcode直接安装即可
##### 2.下载Android SDK或者Android Studio，测试Android APP需要
###### Android sdk 
* Android SDK下载地址：https://developer.android.com/studio/index.html#downloads
* 解压到任意位置，比如/usr/local/android
* 运行/usr/local/android-sdk-macosx/tools/android，即可启动Android SDK Manager
* <img src="https://upload-images.jianshu.io/upload_images/1338101-3b0b795b40597728.png"></img>
* Accept License。然后Install就可以了。这个过程根据网速不同，可能需要10-20分钟，耐心等待。
*设置Android环境变量
 `export JAVA_HOME=$(/usr/libexec/java_home)
  export ANDROID_HOME=/usr/local/android-sdk-macosx`
 * 终端执行 source ~/.bash_profile 使环境变量生效。
###### Android Studio
* 下载地址：https://developer.android.google.cn/studio/
* 直接安装即可
* 打开Android Studio 点击Configure选择 SDK Manager -> Android SDK -> SDK Tools 勾选同上面一样
* 配置环境变量

`export JAVA_HOME=$(/usr/libexec/java_home)
 ANDROID_HOME=/Users/XXX/Library/Android/sdk
 export ANDROID_HOME`
#### 安装appium
* 下载地址：https://bitbucket.org/appium/appium.app/downloads/
* 点击安装即可
<a href="https://www.jianshu.com/p/0932149baf24">后续步骤参考</a>