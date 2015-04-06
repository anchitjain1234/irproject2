while true; do
    read -p "Do you want to install Scrapy?" yn
    case $yn in
        [Yy]* ) sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7;echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | sudo tee /etc/apt/sources.list.d/scrapy.list;sudo apt-get update && sudo apt-get install scrapy-0.24 ; break ;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done

while true; do
    read -p "Do you want to install Beautiful Soup?" yn
    case $yn in
        [Yy]* ) sudo apt-get install python-bs4;break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done

while true; do
    read -p "Do you want to install Matplotlib?" yn
    case $yn in
        [Yy]* ) sudo apt-get install python3-matplotlib; exit ;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
