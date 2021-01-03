#!/bin/sh
# dependency:
# curl to download data
# jq (https://stedolan.github.io/jq/) to parse json data
# usage:
# ./upsCalendar.sh [duration of time, default is 3 days]
# for example, you can use:
# ./upsCalendar.sh "1week"
set -e
start=$(date -I)
end=$(date -d ${1:-"3days"} -I)
echo "Course from $start to $end"
echo "DATE & TIME \t\tInformation\n"
curl -s 'https://edt.univ-tlse3.fr/calendar2/Home/GetCalendarData' --data-raw "start=$start&end=$end&resType=103&calView=month&federationIds%5B%5D=IMAR9CMA&federationIds%5B%5D=IMARACMA&colourScheme=3" | jq '.[] | "\(.start)\t\(.description )" | sub("\r\n\r\n<br />\r\n\r\n";"\n\t\t\t";"g")' -r
