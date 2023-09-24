#!/bin/bash
#This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
PENDING=$(echo $DATA | jq '.[0].pending')
HOSPCUR=$(echo $DATA | jq '.[0].hospitalizedCurrently')
HOSPCUL=$(echo $DATA | jq '.[0].hospitalizedCumulative')
ICUCR=$(echo $DATA | jq '.[0].inIcuCurrently')
ICUCUL=$(echo $DATA | jq '.[0].inIcuCumulative')
DEATH=$(echo $DATA | jq '.[0].death')
TODAY=$(date)

echo "on $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative COVID cases, $PENDING pending COVID cases, $HOSPCUR hospitalized currently, $HOSPCUL hospitalized cumulatively, $ICUCR in ICU currently, $ICUCL in ICU cumulatively and $DEATH deaths."
