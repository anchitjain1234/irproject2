while true; do
    read -p "Do you wish to run the crawler?" yn
    case $yn in
        [Yy]* ) (cd googleresults/googleresults && ./1.sh); python program.py;break;;
        [Nn]* ) python program.py;exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

