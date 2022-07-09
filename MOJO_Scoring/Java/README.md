## MOJO Java Scoring

***
[Java MOJO Document](https://docs.h2o.ai/driverless-ai/latest-stable/docs/userguide/scoring-mojo-scoring-pipeline.html)
[Java API Documentに関して（javadoc）](https://docs.h2o.ai/driverless-ai/latest-stable/docs/userguide/mojo2_javadoc.html)
***

### Javaプログラムからの実行
Javaファイル([ExecuteDaiMojo.java](ExecuteDaiMojo.java))のコンパイル
```bash
javac  -cp path/to/mojo2-runtime.jar ExecuteDaiMojo.java
```
実行
```bash
java  -Dai.h2o.mojos.runtime.license.file=$DRIVERLESS_AI_LICENSE_KEY  -cp  .:path/to/mojo2-runtime.jar  ExecuteDaiMojo
```
> MEDV  
> 27.052086

