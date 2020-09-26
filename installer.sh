echo "INsta Downloader Created by (c)sn.Lionel90, all rights Reserved"                                   
echo "1. Download insta-craken and Install APT Components"
echo "2. Update Repository List"
echo "Choose one option: "
read opcion
convert=false
if [ "$opcion" = 1 ]; then
        echo "****Installing PYTHON 3****"
        sudo apt-get install python3
        echo ""
        echo ""
        echo "****Downloading Instagram Downloader from GitHub repository ****"                                 
        sudo git clone https://github.com/snLionel90/insta-craken.git                                            
        echo ""
        echo ""
        echo "****Installing PIP 3****"
        sudo apt-get install python3-pip -y
        echo ""
        echo ""
        echo "****Updating and install instaloader****"                                                          
        sudo pip3 install instaloader                                                                            
        echo ""
        echo ""
        echo "****Installing TKINTER****"
        sudo apt-get install python3-tk -y
        echo ""
        echo "" 
        echo "Installing Fabric"                                                                                 
        sudo apt-egt install fabric    
        clear
        convert=true


elif [ "$opcion" = 2 ]; then
        echo "Updating repository list"                                                                          
        sudo apt-get update


else
        echo "Failure,script doesn't work properly, closing"                                             
fi

if [ "$convert" = true ]; then
        cp instaDL/instadown.py insta-craken/instaDL                                                             
        chmod u+x insta-craken/instaDL                                                                           
        echo "####################################### END #######################################"               
        echo "Para ejecutar la aplicacion, tan solo tienes que abrir la terminal y escribir instadownloader_linux.py      
        echo "##########################################################################################"
fi

