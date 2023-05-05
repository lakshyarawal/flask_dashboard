# Flask Dashboard

## Technoligies Used
<div align="center">
	<code><img height="50" src="https://user-images.githubusercontent.com/25181517/192158954-f88b5814-d510-4564-b285-dff7d6400dad.png" alt="HTML" title="HTML" /></code>
	<code><img height="50" src="https://user-images.githubusercontent.com/25181517/183423775-2276e25d-d43d-4e58-890b-edbc88e915f7.png" alt="Flask" title="Flask" /></code>
	<code><img height="50" src="https://user-images.githubusercontent.com/25181517/117207330-263ba280-adf4-11eb-9b97-0ac5b40bc3be.png" alt="Docker" title="Docker" /></code>
	<code><img height="50" src="https://user-images.githubusercontent.com/25181517/117447155-6a868a00-af3d-11eb-9cfe-245df15c9f3f.png" alt="JavaScript" title="JavaScript" /></code>
	<code><img height="50" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python" /></code>
	<code><img height="50" src="https://user-images.githubusercontent.com/25181517/117208740-bfb78400-adf5-11eb-97bb-09072b6bedfc.png" alt="PostgreSQL" title="PostgreSQL" /></code>
</div>


## This is a web-based data monitoring flask application. In this project, I built a simple web-based dashboard to visualize real-time process data originating from one of our postgres SQL database.

## The dashboard should allow the user to plot each of these four series (Temperature, pH, Distilled Oxygen, and Pressure) over time.

<img width="1433" alt="Screenshot 2023-05-05 at 3 32 37 AM" src="https://user-images.githubusercontent.com/20071320/236401321-17ff60f6-1102-49a2-8098-1bad7e301b1c.png">

## This allows the user to select the time window. Which is then communicated through app routes to the application and updates the dashboard. It also allows the user to refresh the data without refreshing the page, or auto-refresh the page for the user using a simple button.

<img width="1440" alt="Screenshot 2023-05-05 at 3 33 36 AM" src="https://user-images.githubusercontent.com/20071320/236401341-9f8d8e35-31db-41bc-9316-97097055c79d.png">

## I have also added a "Download as csv" button which allows the user to extract the current graph's information in csv format.

<img width="1440" alt="Screenshot 2023-05-05 at 3 34 30 AM" src="https://user-images.githubusercontent.com/20071320/236401361-7ba4cf7b-4e35-4c0d-bf5a-a1da78a397b3.png">
<img width="1440" alt="Screenshot 2023-05-05 at 3 34 59 AM" src="https://user-images.githubusercontent.com/20071320/236401378-a2b4f75b-4e06-464b-806d-7730b23bb035.png">

## User can filter through between all the varibles through a simple drowpdown. Which updates the graph in realtime.

<img width="1439" alt="Screenshot 2023-05-05 at 3 35 25 AM" src="https://user-images.githubusercontent.com/20071320/236401396-53148edd-8d6d-4772-8863-cf7ec095a290.png">

<img width="1437" alt="Screenshot 2023-05-05 at 3 35 51 AM" src="https://user-images.githubusercontent.com/20071320/236401403-fea8911d-9d39-4f5f-b5e5-db8be66432f1.png">
