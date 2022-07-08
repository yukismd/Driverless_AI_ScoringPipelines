## MOJO Java Scoring

***
[Document](https://docs.h2o.ai/driverless-ai/latest-stable/docs/userguide/scoring-mojo-scoring-pipeline.html)
***

### Javaプログラムからの実行
Javaファイル([ExecuteDaiMojo.java](ExecuteDaiMojo.java))のコンパイル
```bash
javac  -cp mojo2-runtime.jar  -J-Xms2g  ExecuteDaiMojo.java
```
実行
```bash
java  -Dai.h2o.mojos.runtime.license.file=$DRIVERLESS_AI_LICENSE_KEY  -cp  .:mojo2-runtime.jar  ExecuteDaiMojo
```
> y  
> 2.5617633

[Java API Documentに関して](https://docs.h2o.ai/driverless-ai/latest-stable/docs/userguide/mojo2_javadoc.html)
