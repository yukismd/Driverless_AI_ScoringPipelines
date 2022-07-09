## MOJO Java Scoring

***
[Java MOJO Document](https://docs.h2o.ai/driverless-ai/latest-stable/docs/userguide/scoring-mojo-scoring-pipeline.html)  
[Java API Documentに関して（javadoc）](https://docs.h2o.ai/driverless-ai/latest-stable/docs/userguide/mojo2_javadoc.html)  
***

### CSVを与えるバッチスコアリング
ライセンスファイル（license.file）を作成  

#### 予測値のスコアリング
```bash
java -Dai.h2o.mojos.runtime.license.file=license.file -jar mojo2-runtime.jar pipeline.mojo example.csv
```
> MEDV
> 34.316986
> 35.293266
> 36.60863
> :

#### Original Shapleyスコアリング
```bash
java -Dai.h2o.mojos.runtime.license.file=license.file -jar mojo2-runtime.jar --show-contributions-original pipeline.mojo example.csv
```
> contrib_CRIM,contrib_INDUS,contrib_NOX,contrib_RM,contrib_AGE,contrib_TAX,contrib_PTRATIO,contrib_B,contrib_LSTAT,contrib_bias
> 0.43936695792448377,0.10544296012559155,0.8404698378253302,-2.9430116976462344,0.0,1.3195625843047516,1.340921193686255,-1.5585007203253964,12.228996639380586,22.543738252790693
> 0.44369137603857245,0.06317509834025041,0.7974590406465197,-2.331029008333845,0.0,0.19010180109311878,1.5085236016914831,-1.493360871402778,13.570966258976775,22.543738252790693
> 0.5373352566924081,0.16620751192340177,0.7798109589268174,-2.575718598206955,0.0,1.9924226643634202,1.7041594108629208,-1.6132027116367502,13.073878670511533,22.543738252790693
> :
> 
***

### Javaプログラムの作成と実行
Javaファイル([ExecuteDaiMojo.java](ExecuteDaiMojo.java))を作成し、コンパイル
```bash
javac  -cp path/to/mojo2-runtime.jar ExecuteDaiMojo.java
```
実行
```bash
java  -Dai.h2o.mojos.runtime.license.file=$DRIVERLESS_AI_LICENSE_KEY  -cp  .:path/to/mojo2-runtime.jar  ExecuteDaiMojo
```
> MEDV  
> 27.052086

[VS Codeでの開発に関して](./DaiJavaMojo_vscode.pdf)
