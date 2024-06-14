case $DAY in
  Mon | Fri ) echo ${DAY}day ;;
  Tue | Thu ) echo ${DAY}sday ;;
  Wed ) echo ${DAY}nesday ;;
  S??) echo WEEKEND! ;;
  *) echo "$DAY is not a day I understand."
     echo "April Fool’s Day?" ;;
esac

