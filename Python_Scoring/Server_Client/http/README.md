## HTTP Service
[Tornade](https://www.tornadoweb.org/en/stable/)
***



#### Clientからの実行サンプル
- HTTPサーバへのスコアリングのリクエスト実施のサンプル: [Client/run_http_client.ipynb](./Client/run_http_client.ipynb)


#### HTTP Server files (Scoring, MLIにおいてファイル名は共通（中身は異なる）)
Scoringの実行ファイル：[scoring-pipeline](./scoring-pipeline)  
MLIの実行ファイル：[scoring-pipeline-mli](./scoring-pipeline-mli)

- 実行シェルファイル(http_server.pyのコール)- [scoring-pipeline/run_http_server.sh](scoring-pipeline/run_http_server.sh) or [scoring-pipeline-mli/run_http_server.sh](scoring-pipeline-mli/run_http_server.sh)
- サーバプログラム（http_server.py)- [scoring-pipeline/http_server.py](scoring-pipeline/http_server.py) or [scoring-pipeline-mli/http_server.py](scoring-pipeline-mli/http_server.py)
