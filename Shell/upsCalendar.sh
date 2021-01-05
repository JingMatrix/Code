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
		else
			echo -n $(date -d $time +"%a\t%H:%M\t")
			echo "Geometric group theory. (S. Lamy, M. Sablik)"
		fi
	done

