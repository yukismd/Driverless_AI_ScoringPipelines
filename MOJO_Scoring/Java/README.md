## NOJO Java Scoring
### Javaプログラムからの実行
Javaファイルのコンパイル
```bash
javac  -cp mojo2-runtime.jar  -J-Xms2g  ExecuteDaiMojo.java
```
実行
```bash
java  -Dai.h2o.mojos.runtime.license.file=$DRIVERLESS_AI_LICENSE_KEY  -cp  .:mojo2-runtime.jar  ExecuteDaiMojo
```
> y
> 2.5617633
