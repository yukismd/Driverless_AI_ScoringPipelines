#!/usr/bin/env bash

set -o pipefail
set -ex

#
# This example script demonstrates how to communicate with the Driverless AI Scoring Service via HTTP.
# The protocol used is JSON-RPC 2.0.
#

# -----------------------
# Name   Type      Range 
# -----------------------
# x1     float64   [0, 0]
# x2     float64   [0, 0]
# x3     float64   [0, 0]
# x4     float64   [0, 0]
# -----------------------

echo "Scoring individual rows..."

curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 1,
  "method": "score_reason_codes",
  "params": {
    "row": {
      "x1": "-2.4871",
      "x2": "-4.136",
      "x3": "-2.7997",
      "x4": "-2.3901"
    }
  }
}
EOF
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 2,
  "method": "score_reason_codes",
  "params": {
    "row": {
      "x1": "-2.6315",
      "x2": "-2.5015",
      "x3": "-2.9812",
      "x4": "-2.7816"
    }
  }
}
EOF
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 3,
  "method": "score_reason_codes",
  "params": {
    "row": {
      "x1": "-2.4492",
      "x2": "-2.5506",
      "x3": "-2.7997",
      "x4": "-3.4233"
    }
  }
}
EOF
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 4,
  "method": "score_reason_codes",
  "params": {
    "row": {
      "x1": "-3.0066",
      "x2": "-2.5015",
      "x3": "-2.5228",
      "x4": "-2.4827"
    }
  }
}
EOF
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 5,
  "method": "score_reason_codes",
  "params": {
    "row": {
      "x1": "-2.4307",
      "x2": "-2.7822",
      "x3": "-2.9812",
      "x4": "-3.3621"
    }
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

echo "Get the Reason Code column names"
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id":1,
  "method":"get_reason_code_column_names",
  "params":{}
}
EOF