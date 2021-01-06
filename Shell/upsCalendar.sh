#!/bin/zsh
# dependency:
# curl to download data
# jq (https://stedolan.github.io/jq/) to parse json data
# usage:
# ./upsCalendar.sh [duration of time, default is 3 days]
# for example, you can use:
# ./upsCalendar.sh "1week"
# optional you can set startdate manually as environment variable
# set zoom=1 to open zoon link possiblly
set -e
if ! [[ -n $startdate ]]; then
	startdate=$(date -I)
fi
enddate=$(date -d ${startdate}' '${1:-"2days"} -I)
course=(
	"Holomorphic dynamics in dimension one : some advanced topics. (F. Bertheloot and P.Roesch)"
	"Topics in Differential Complex Geometry (E. Legendre)"
	"Hamilton-Jacobi equations for biology (S. Mirrahimi)"
	"Stability analysis of ODE's or PDE's periodic solutions. Theoretical and numerical aspects. (P. Noble)"
	"Learning. (J. M. Loubes, B. Laurent-Bonneau)"
	"Lévy Processes (L. Huang)"
)
seminar=(
	"Geometric group theory. (S. Lamy, M. Sablik)"
	"PDEs and applications. (P. Cantin, G. Faye, S. Le Coz)"
	"Stein method and Applications. (M. Fathi, G. Cebron)"
)
typeset -A zoomlink
zoomlink=(
	# DON'T change the order, it is hard-coded order
	# Complex Geometry Tuesday
	[2mar.]="zoommtg://univ-tlse3-fr.zoom.us/join?action=join&confno=89280020232&pwd=VFlhdFhyUTZZVFdOUnU2UzloTWVldz09"
	# Complex Geometry Friday
	[2ven.]="zoommtg://univ-tlse3-fr.zoom.us/join?action=join&confno=83890569409&pwd=UXRFWjRtZ1duYktCSHJ5Y0tiQ1lHZz09"
	# Reading seminar
	[1seminar]="zoommtg://univ-tlse3-fr.zoom.us/join?action=join&confno=81923444202&pwd=d2lRVU9nYy9jNTM1dUE3VEJpSTJOZz09"
	# Holomorphic dynamics
	[1]="zoommtg://univ-tlse3-fr.zoom.us/join?action=join&confno=81363610874&pwd=T1VnWTl3b0NCK1UyUHNUWXZ6ZEVadz09"
	# Learning
	[5]="zoommtg://zoom.us/join?action=join&confno=94751387445&pwd=aTFkTVcyeUxCcktRSTZwSDlEVTcxdz09"
)
echo "Course from $startdate to $enddate"
echo "DATE\tTIME\tInformation\n"
curl -s 'https://edt.univ-tlse3.fr/calendar2/Home/GetCalendarData' --data-raw "start=$startdate&end=$enddate&resType=103&calView=month&federationIds%5B%5D=IMAR9CMA&federationIds%5B%5D=IMARACMA&colourScheme=3" >/tmp/cour.json | jq -r 'sort_by(.start) | .[] | [.start, .description, .eventCategory] | @tsv' |
	while IFS=$'\t' read -r time description eventCategory; do
		if echo $eventCategory | sed -n '/control/I{q1}'; then
			echo -n '\033[0m'
		else
			echo -n '\033[1;33m'
		fi
		b=$(<<<$description | sed 's/.*Course \([0-9]\).*/\1/p' -n)
		if [[ -n $b ]]; then
			# limit to only courses you follow
			if [[ $b < 4 || $b == 5 ]]; then
				echo -n $(date -d $time +"%a\t%H:%M\t")
				echo $course[$b]
			fi
			if [[ $zoom == 1 && $(date -I) == $(date -I -d $time) ]]; then # check zoom link
				if [[ $b == 2 ]]; then
					tmp1=${b}$(date +%a)
					xdg-open $zoomlink[$tmp1]
				else
					xdg-open $zoomlink[$b]
				fi
			fi
		else
			s=$(<<<$description | sed 's/.*seminar \([0-9]\).*/\1/p' -n)
			if [[ $s == 1 ]]; then
				echo -n $(date -d $time +"%a\t%H:%M\t")
				echo $seminar[$s]
				if [[ $zoom == 1 && $(date -I) == $(date -I -d $time) ]]; then
					tmp2=${s}seminar
					xdg-open $zoomlink[$tmp2]
				fi
			fi
		fi
	done
