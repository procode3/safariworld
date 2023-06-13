# safariworld
![safari world home](home_page.png)

## Introduction
Safari World is a web app that will allow users to book for travels to different destinations within and outside Kenya.  The app will showcase upcoming and past adventures. It will also allow users to have a wallet to enable for lipa pole pole. It will also allow users to book for consultation for a customized adventure as per their need or schedule.  The app will optionally provide an integration with the google calendar API to allow the organizer to plan and organize for trips accordingly. The admin will be able to manage books i.e view monthly earnings, view expenses for every trip, and project sales. 

## Installation in Linux
- Clone the repositiory
- Start the virtual env inside safari directory
<br>```source safari/bin/activate```
- Run pip3 to install the dependencies
<br>```pip3 install -r requirements.txt```
- Run the server in the root directory of the project
<br>```python3 manage.py runserver```
- Visit the local host address on port 8000 on the browser
<br>```localhost:8000/```
- Access the admin site on /admin
- Create a user account and make a booking :)
 

## Usage
- Access /adventures to view available trips
<br> <img src="src/images/adventures.gif" width="800" height="400">
- Click on book now to book a trip after logging in
<br> <img src="src/images/booking.gif" width="800" height="400">
- Sign up on /signup and login on /login


## Related Projects
- [Lets Drift](https://letsdrift.co.ke/)
- [A way to Africa](https://www.awaytoafrica.com/)
- [Hike Maniacs](https://hikemaniak.co.ke/)

## Licensing
[GPL V3.0](https://choosealicense.com/licenses/gpl-3.0/)



# AUTHORS
- [Erick Barasa](https://github.com/procode3)
- [George Wambani](https://github.com/wambani01)
- [Immanuel Kituku](https://github.com/manuel254)
