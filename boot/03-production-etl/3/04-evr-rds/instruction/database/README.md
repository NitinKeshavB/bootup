# Installation

Follow the steps below to install the DVD Rentals database in your Postgresql instance. 

1. Unzip the `dvdrental.zip` file in this directory 
2. Select an existing server or create a new server 
3. Create a new database within your server, give it any name you wish e.g. `dvd_rental`
4. Select the database 
5. Select `Tools` > `Restore` 

![images-installation/image1.png](images-installation/image1.png)

6. Configure Restore: 
    - Change `Format` to "Directory"
    - Change `Filename` to the dvdrental directory that was created when you performed the unzip (step 1)

![images-installation/image2.png](images-installation/image2.png)

7. Select `Restore`. You should see a success message. 

![images-installation/image3.png](images-installation/image3.png)
