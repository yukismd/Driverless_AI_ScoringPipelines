#!/usr/bin/env bash

set -o pipefail
set -ex

#
# This example script demonstrates how to communicate with the Driverless AI Scoring Service via HTTP.
# The protocol used is JSON-RPC 2.0.
#

# ----------------------------------------------------------
# Name   Type      Range                                    
# ----------------------------------------------------------
# x1     float32   [-3.0065999031066895, 2.7874999046325684]
# x2     float32   [-4.136000156402588, 3.256700038909912]  
# x3     float32   [-3.0952999591827393, 3.3822999000549316]
# x4     float32   [-3.42330002784729, 3.0445001125335693]  
# ----------------------------------------------------------

echo "Scoring individual rows..."

curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 1,
  "method": "score",
  "params": {
    "row": {
      "x1": "-2.6043999195098877",
      "x2": "-2.2112998962402344",
      "x3": "-2.627500057220459",
      "x4": "-3.3620998859405518"
    }
  }
}
EOF
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 2,
  "method": "score",
  "params": {
    "row": {
      "x1": "-2.4307000637054443",
      "x2": "-2.7822000980377197",
      "x3": "-2.5227999687194824",
      "x4": "-2.781599998474121"
    }
  }
}
EOF
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 3,
  "method": "score",
  "params": {
    "row": {
      "x1": "-3.0065999031066895",
      "x2": "-2.550600051879883",
      "x3": "-2.7207999229431152",
      "x4": "-3.42330002784729"
    }
  }
}
EOF
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 4,
  "method": "score",
  "params": {
    "row": {
      "x1": "-2.4307000637054443",
      "x2": "-2.2112998962402344",
      "x3": "-2.5227999687194824",
      "x4": "-2.4827001094818115"
    }
  }
}
EOF
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 5,
  "method": "score",
  "params": {
    "row": {
      "x1": "-2.7258999347686768",
      "x2": "-2.7822000980377197",
      "x3": "-2.5227999687194824",
      "x4": "-2.781599998474121"
    }
  }
}
EOF

echo "Scoring multiple rows..."

curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 1,
  "method": "score_batch",
  "params": {
    "rows": [
      {
        "x1": "-2.6043999195098877",
        "x2": "-2.2112998962402344",
        "x3": "-2.627500057220459",
        "x4": "-3.3620998859405518"
      },
      {
        "x1": "-2.4307000637054443",
        "x2": "-2.7822000980377197",
        "x3": "-2.5227999687194824",
        "x4": "-2.781599998474121"
      },
      {
        "x1": "-3.0065999031066895",
        "x2": "-2.550600051879883",
        "x3": "-2.7207999229431152",
        "x4": "-3.42330002784729"
      },
      {
        "x1": "-2.4307000637054443",
        "x2": "-2.2112998962402344",
        "x3": "-2.5227999687194824",
        "x4": "-2.4827001094818115"
      },
      {
        "x1": "-2.7258999347686768",
        "x2": "-2.7822000980377197",
        "x3": "-2.5227999687194824",
        "x4": "-2.781599998474121"
      }
    ]
  }
}
EOF

echo "Get the input columns"
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id":1,
  "method":"get_column_names",
  "params":{}
}
EOF

echo "Get the transformed columns"
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id":1,
  "method":"get_transformed_column_names",
  "params":{}
}
EOF

echo "Get the target labels"
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id":1,
  "method":"get_target_labels",
  "params":{}
}
EOF