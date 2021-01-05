#!/bin/zsh
# dependency:
# curl to download data
# jq (https://stedolan.github.io/jq/) to parse json data
# usage:
# ./upsCalendar.sh [duration of time, default is 3 days]
# for example, you can use:
# ./upsCalendar.sh "1week"
set -e
startdate=$(date -I)
enddate=$(date -d ${1:-"2days"} -I)
course=(
	"Holomorphic dynamics in dimension one : some advanced topics. (F. Bertheloot and P.Roesch)"
	"Topics in Differential Complex Geometry (E. Legendre)"
	"Hamilton-Jacobi equations for biology (S. Mirrahimi)"
	"Stability analysis of ODE's or PDE's periodic solutions. Theoretical and numerical aspects. (P. Noble)"
	"Learning. (J. M. Loubes, B. Laurent-Bonneau)"
	"Lévy Processes (L. Huang)"
)
zoomlink=(
	# DON'T change the order, it is hard-coded order
	# Complex Geometry Tuesday
	"zoommtg://univ-tlse3-fr.zoom.us/join?action=join&confno=89280020232&pwd=VFlhdFhyUTZZVFdOUnU2UzloTWVldz09"
	# Complex Geometry Friday
	"zoommtg://univ-tlse3-fr.zoom.us/join?action=join&confno=83890569409&pwd=UXRFWjRtZ1duYktCSHJ5Y0tiQ1lHZz09"
	# Reading seminar
	"zoommtg://univ-tlse3-fr.zoom.us/join?action=join&confno=81923444202&pwd=d2lRVU9nYy9jNTM1dUE3VEJpSTJOZz09"
	# Holomorphic dynamics
	"Who knows?"
	# Learning
	"zoommtg://zoom.us/join?action=join&confno=94751387445&pwd=aTFkTVcyeUxCcktRSTZwSDlEVTcxdz09"
)
echo "Course from $startdate to $enddate"
echo "DATE\tTIME\tInformation\n"
curl -s 'https://edt.univ-tlse3.fr/calendar2/Home/GetCalendarData' --data-raw "start=$startdate&end=$enddate&resType=103&calView=month&federationIds%5B%5D=IMAR9CMA&federationIds%5B%5D=IMARACMA&colourScheme=3" | jq -r 'sort_by(.start) | .[] | [.start, .description] | @tsv ' |
	while IFS=$'\t' read -r time description
	do
		b=$(<<< $description | sed 's/.*Course \([0-9]\).*/\1/p' -n)
		if [[ -n $b ]]
		then
			# limit to only courses you follow
			if [[ $b < 4 || $b == 5 ]]
			then
				echo -n $(date -d $time +"%a\t%H:%M\t")
				echo $course[$b]
			fi
			if [[ $zoom == 1 ]]
				# check zoom link
			then
				if [[ $b == 2 || $(date +%a)=='mar.' ]]
				then
					xdg-open $zoomlink[1]
				elif [[ $b == 2 ||  $(date +%a)=='ven.' ]]
				then
					xdg-open $zoomlink[2]
				elif [[ $b == 1 || $(date -I) == $(date -I -d $time) ]]
				then
					# not sure, we don't the link yet
					xdg-open $zoomlink[4] || exit
				elif [[ $b == 5 || $(date -I) == $(date -I -d $time) ]]
				then
					xdg-open $zoomlink[5]
				fi
			fi
		else
			echo -n $(date -d $time +"%a\t%H:%M\t")
			echo "Geometric group theory. (S. Lamy, M. Sablik)"
			if [[ $zoom = 1 && $(date -I) == $(date -I -d $time) ]]
			then
				xdg-open $zoomlink[3]
			fi
		fi
	done

